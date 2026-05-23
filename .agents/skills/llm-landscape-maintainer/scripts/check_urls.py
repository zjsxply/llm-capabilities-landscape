#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


URL_RE = re.compile(r"https?://[^\s<>\]\)\"']+", re.I)
TRAILING = ".,;:!?)]}'\""
DEFAULT_CACHE_PATH = Path(".tmp/landscape-maintainer/url-check-cache.json")
DEFAULT_CACHE_TTL_DAYS = 30.0


def extract_urls(files: list[Path]) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in URL_RE.finditer(text):
            url = match.group(0).rstrip(TRAILING)
            found.setdefault(url, []).append(str(path))
    return found


def request(url: str, method: str, timeout: float) -> tuple[int | None, str | None, str | None]:
    req = urllib.request.Request(
        url,
        method=method,
        headers={
            "User-Agent": "llm-landscape-url-check/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    try:
        context = ssl.create_default_context()
        with urllib.request.urlopen(req, timeout=timeout, context=context) as response:
            return response.getcode(), response.geturl(), None
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl(), str(exc)
    except Exception as exc:  # noqa: BLE001 - diagnostics script should keep going.
        return None, None, f"{type(exc).__name__}: {exc}"


def check_one(url: str, timeout: float) -> dict[str, Any]:
    status, final_url, error = request(url, "HEAD", timeout)
    method = "HEAD"
    if status is None or status in {400, 403, 405, 406, 429, 500, 501, 502, 503}:
        status, final_url, error = request(url, "GET", timeout)
        method = "GET"
    ok = status is not None and 200 <= status < 400
    blocked = status in {401, 403, 429}
    return {
        "url": url,
        "ok": ok,
        "blocked": blocked,
        "status": status,
        "method": method,
        "final_url": final_url,
        "error": error,
    }


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_now() -> str:
    return utc_now().isoformat(timespec="seconds")


def parse_timestamp(value: Any) -> dt.datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def load_cache(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "entries": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"version": 1, "entries": {}}
    if not isinstance(data, dict):
        return {"version": 1, "entries": {}}
    entries = data.get("entries")
    if not isinstance(entries, dict):
        entries = {}
    return {"version": 1, "entries": entries}


def get_fresh_cached_result(url: str, cache: dict[str, Any], ttl_days: float) -> dict[str, Any] | None:
    if ttl_days < 0:
        return None
    entry = cache.get("entries", {}).get(url)
    if not isinstance(entry, dict):
        return None
    checked_at = parse_timestamp(entry.get("checked_at"))
    result = entry.get("result")
    if checked_at is None or not isinstance(result, dict):
        return None
    age = utc_now() - checked_at
    if age > dt.timedelta(days=ttl_days):
        return None
    cached = dict(result)
    cached["url"] = url
    cached["cache_hit"] = True
    cached["cached_checked_at"] = entry.get("checked_at")
    cached["cache_age_days"] = round(age.total_seconds() / 86400, 3)
    return cached


def cacheable_result(result: dict[str, Any]) -> dict[str, Any]:
    ignored = {"cache_hit", "cached_checked_at", "cache_age_days"}
    return {key: value for key, value in result.items() if key not in ignored}


def update_cache(cache: dict[str, Any], results: list[dict[str, Any]]) -> None:
    entries = cache.setdefault("entries", {})
    if not isinstance(entries, dict):
        entries = {}
        cache["entries"] = entries
    now = iso_now()
    for result in results:
        if result.get("cache_hit"):
            continue
        url = result.get("url")
        if not isinstance(url, str) or not url:
            continue
        entries[url] = {
            "checked_at": now,
            "result": cacheable_result(result),
        }
    cache["updated_at"] = now


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def write_report(path: Path, results: list[dict[str, Any]], sources: dict[str, list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cache_hits = sum(1 for item in results if item.get("cache_hit"))
    network_checks = len(results) - cache_hits
    lines = [
        "# URL Accessibility Report",
        "",
        f"- Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- URLs: {len(results)}",
        f"- Fresh cache hits: {cache_hits}",
        f"- Network checks: {network_checks}",
        f"- OK: {sum(1 for item in results if item['ok'])}",
        f"- Blocked or rate-limited: {sum(1 for item in results if item['blocked'] and not item['ok'])}",
        f"- Failed: {sum(1 for item in results if not item['ok'] and not item['blocked'])}",
        "",
    ]
    for heading, predicate in [
        ("Failures", lambda item: not item["ok"] and not item["blocked"]),
        ("Blocked Or Rate-Limited", lambda item: item["blocked"] and not item["ok"]),
        ("Successful", lambda item: item["ok"]),
    ]:
        lines.extend([f"## {heading}", ""])
        subset = [item for item in results if predicate(item)]
        if not subset:
            lines.append("- None.")
        for item in subset:
            src = ", ".join(sorted(set(sources.get(item["url"], [])))[:5])
            final = f"; final={item['final_url']}" if item.get("final_url") and item["final_url"] != item["url"] else ""
            error = f"; error={item['error']}" if item.get("error") and not item["ok"] else ""
            cache = ""
            if item.get("cache_hit"):
                cache = (
                    f" cached={item.get('cached_checked_at')}"
                    f" age_days={item.get('cache_age_days')}"
                )
            lines.append(
                f"- status={item['status']} method={item['method']}{cache}{final}{error} | "
                f"{item['url']} | {src}"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check HTTP(S) URLs in Markdown/text files with HEAD and GET fallback.")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--out", type=Path, default=Path(".tmp/url_check_report.md"))
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--cache-path", type=Path, default=DEFAULT_CACHE_PATH)
    parser.add_argument("--cache-ttl-days", type=float, default=DEFAULT_CACHE_TTL_DAYS)
    parser.add_argument("--refresh-cache", action="store_true", help="Ignore fresh cache entries and re-check URLs.")
    parser.add_argument("--no-cache", action="store_true", help="Disable reading and writing the URL check cache.")
    parser.add_argument("--fail-on-broken", action="store_true")
    args = parser.parse_args()

    sources = extract_urls(args.files)
    urls = sorted(sources)
    results: list[dict[str, Any]] = []
    cache = {"version": 1, "entries": {}}
    if not args.no_cache:
        cache = load_cache(args.cache_path)

    urls_to_check: list[str] = []
    if args.no_cache or args.refresh_cache:
        urls_to_check = urls
    else:
        for url in urls:
            cached = get_fresh_cached_result(url, cache, args.cache_ttl_days)
            if cached is None:
                urls_to_check.append(url)
            else:
                results.append(cached)

    print(
        f"Checking {len(urls_to_check)} URLs; using {len(results)} fresh cached results",
        flush=True,
    )
    if urls_to_check:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
            futures = {pool.submit(check_one, url, args.timeout): url for url in urls_to_check}
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                results.append(result)
                print(f"{result['status']} {result['method']} {result['url']}", flush=True)

    if not args.no_cache:
        update_cache(cache, results)
        write_json(args.cache_path, cache)

    results.sort(key=lambda item: (item["ok"], item["blocked"], item["url"]))
    write_report(args.out, results, sources)
    if args.json_out:
        write_json(args.json_out, results)
    print(f"Wrote {args.out}", flush=True)
    broken = [item for item in results if not item["ok"] and not item["blocked"]]
    return 1 if args.fail_on_broken and broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
