#!/usr/bin/env python3
"""Enrich a famou inventory with arXiv and Crossref metadata.

The output is evidence for parent screening.  It never decides inclusion or
writes landscape Markdown.  arXiv IDs are fetched in serial batches and DOI
lookups are serialized to keep public APIs below their rate limits.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


ATOM = {"a": "http://www.w3.org/2005/Atom"}


def request(url: str, *, retries: int = 4) -> bytes:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "llm-landscape-maintainer/1.0"})
            with urllib.request.urlopen(req, timeout=60) as response:
                return response.read()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            last = exc
            time.sleep(min(5.0, 0.75 * (2**attempt)))
    raise RuntimeError(f"request failed: {url}: {last}")


def arxiv_metadata(ids: list[str], batch_size: int, delay: float) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for start in range(0, len(ids), batch_size):
        batch = ids[start : start + batch_size]
        query = urllib.parse.urlencode({"id_list": ",".join(batch), "max_results": str(len(batch))})
        root = ET.fromstring(request(f"https://export.arxiv.org/api/query?{query}"))
        for entry in root.findall("a:entry", ATOM):
            raw_id = entry.findtext("a:id", default="", namespaces=ATOM)
            match = re.search(r"/(\d{4}\.\d{4,5})(?:v\d+)?$", raw_id)
            if not match:
                continue
            paper_id = match.group(1)
            result[f"arXiv:{paper_id}"] = {
                "title": html.unescape(" ".join((entry.findtext("a:title", default="", namespaces=ATOM) or "").split())),
                "abstract": html.unescape(" ".join((entry.findtext("a:summary", default="", namespaces=ATOM) or "").split())),
                "published": (entry.findtext("a:published", default="", namespaces=ATOM) or "")[:10],
                "source": "arXiv API",
                "url": f"https://arxiv.org/abs/{paper_id}",
            }
        if start + batch_size < len(ids):
            time.sleep(delay)
    return result


def crossref_metadata(dois: list[str], delay: float) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for doi in dois:
        url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='') }"
        try:
            data = json.loads(request(url)).get("message", {})
        except RuntimeError:
            continue
        title = " ".join(str(x) for x in (data.get("title") or [])).strip()
        abstract = re.sub(r"<[^>]+>", " ", str(data.get("abstract") or ""))
        result[f"DOI:{doi.lower()}"] = {
            "title": " ".join(title.split()),
            "abstract": " ".join(html.unescape(abstract).split()),
            "published": ((data.get("published") or data.get("published-print") or {}).get("date-parts") or [[None]])[0][0],
            "source": "Crossref API",
            "url": f"https://doi.org/{doi}",
        }
        time.sleep(delay)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--delay", type=float, default=2.0)
    args = parser.parse_args()
    rows = json.loads(args.inventory.read_text(encoding="utf-8"))
    identifiers = [str(row["identifier"]) for row in rows]
    arxiv_ids = [item.split(":", 1)[1] for item in identifiers if item.startswith("arXiv:")]
    dois = [item.split(":", 1)[1] for item in identifiers if item.startswith("DOI:")]
    metadata = arxiv_metadata(arxiv_ids, args.batch_size, args.delay)
    metadata.update(crossref_metadata(dois, max(0.25, args.delay / 4)))
    for row in rows:
        row["metadata"] = metadata.get(row["identifier"], {})
        row["metadata_found"] = bool(row["metadata"])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"inventory rows: {len(rows)}")
    print(f"metadata matches: {sum(bool(row['metadata']) for row in rows)}")
    print(f"abstracts: {sum(bool(row['metadata'].get('abstract')) for row in rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
