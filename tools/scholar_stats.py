#!/usr/bin/env python3
"""Fetch Google Scholar statistics for the profile and write them as JSON.

Run by .github/workflows/google-scholar.yml; the JSON is pushed to the
`google-scholar-stats` branch and read by assets/js/main.js.
Standard library only: reads the public profile page directly.
"""
import html
import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone

SCHOLAR_ID = "DqDqY38AAAAJ"
URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en&cstart=0&pagesize=100&sortby=pubdate"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


def norm(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())


def fetch():
    last = None
    for attempt in range(5):
        try:
            req = urllib.request.Request(URL, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as r:
                page = r.read().decode("utf-8", "replace")
            if "gsc_a_tr" in page:
                return page
            last = "unexpected page (captcha?)"
        except Exception as e:  # noqa: BLE001
            last = e
        time.sleep(20 * (attempt + 1))
    raise SystemExit(f"Cannot fetch Google Scholar profile: {last}")


def main(out):
    page = fetch()
    stats = [int(x) for x in re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', page)]
    pubs = {}
    for row in re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, re.S):
        m = re.search(r'href="([^"]*citation_for_view=[^"]*)"[^>]*class="gsc_a_at">(.*?)</a>', row, re.S)
        if not m:
            continue
        title = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        c = re.search(r'class="gsc_a_ac gs_ibl"[^>]*>(\d*)</a>', row)
        pubs[norm(title)] = {
            "title": title,
            "citations": int(c.group(1)) if c and c.group(1) else 0,
            "url": "https://scholar.google.com" + html.unescape(m.group(1)),
        }
    data = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "citations": stats[0] if len(stats) > 0 else 0,
        "h_index": stats[2] if len(stats) > 2 else 0,
        "i10_index": stats[4] if len(stats) > 4 else 0,
        "publications": pubs,
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"{len(pubs)} publications, {data['citations']} citations, h-index {data['h_index']}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "gs_data.json")
