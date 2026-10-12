#!/usr/bin/env python3
"""Fetch Google Scholar statistics for the profile and write them as JSON.

Run by .github/workflows/google-scholar.yml; the JSON is pushed to the
`google-scholar-stats` branch and read by assets/js/main.js.
"""
import json
import re
import sys
from datetime import datetime, timezone

from scholarly import scholarly

SCHOLAR_ID = "DqDqY38AAAAJ"


def norm(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())


def main(out):
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    pubs = {}
    for p in author.get("publications", []):
        title = p.get("bib", {}).get("title", "")
        if not title:
            continue
        pubs[norm(title)] = {
            "title": title,
            "citations": p.get("num_citations", 0),
            "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&citation_for_view="
                   + p.get("author_pub_id", ""),
        }
    data = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "citations": author.get("citedby", 0),
        "h_index": author.get("hindex", 0),
        "i10_index": author.get("i10index", 0),
        "publications": pubs,
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"{len(pubs)} publications, {data['citations']} citations")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "gs_data.json")
