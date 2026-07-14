#!/usr/bin/env python3
"""Offizielle Michael-Singer-Podcast-Transkripte von Sounds True lokal sammeln.

Nur für den privaten Gebrauch. Die Transkripte landen in reference/transcripts/
(gitignoriert — sie gehören nie ins Repo, auch nicht ins private).

Aufruf (aus dem Repo-Wurzelverzeichnis oder von überall):
  python3 tools/fetch_transcripts.py            # neueste 2 Archiv-Seiten (~10 Folgen)
  python3 tools/fetch_transcripts.py --pages 5  # neueste 5 Archiv-Seiten
  python3 tools/fetch_transcripts.py --all      # komplettes Archiv (~36 Seiten, dauert)

Bereits gespeicherte Folgen werden übersprungen. Folgen ohne fertiges Transkript
("Transcript coming soon") werden gemeldet und beim nächsten Lauf erneut versucht.
"""

from __future__ import annotations

import argparse
import html as htmllib
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://www.soundstrue.com/a/resources"
ARCHIVE = f"{BASE}/category/michael-singer-podcast/"
OUT_DIR = Path(__file__).resolve().parent.parent / "reference" / "transcripts"
UA = {"User-Agent": "Mozilla/5.0 (private transcript archiver for personal study)"}
DELAY_SECONDS = 1.5


def get(url: str) -> str | None:
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def episode_slugs(pages: int | None) -> list[str]:
    """Slugs von den Archiv-Seiten, neueste zuerst."""
    slugs: list[str] = []
    page = 1
    while pages is None or page <= pages:
        url = ARCHIVE if page == 1 else f"{ARCHIVE}page/{page}/"
        html = get(url)
        if html is None:
            break
        found = re.findall(r'href="https://www\.soundstrue\.com/a/resources/podcast/([^"/]+)/?"', html)
        new = [s for s in dict.fromkeys(found) if s not in slugs]
        if not new:
            break
        slugs.extend(new)
        page += 1
        time.sleep(DELAY_SECONDS)
    return slugs


def extract_transcript(html: str) -> tuple[str, str] | None:
    """(Titel, Transkript-Text) aus einer Transkript-Seite, oder None."""
    m = re.search(r"<title>([^<]+?)\s*\|\s*Sounds True</title>", html)
    title = htmllib.unescape(m.group(1).strip()) if m else "Unbekannte Folge"

    paras = re.findall(r"<p[^>]*>(.*?)</p>", html, re.S)
    lines: list[str] = []
    for p in paras:
        text = htmllib.unescape(re.sub(r"<[^>]+>", " ", p))
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) < 60:  # Navigation, Footer, Bildunterschriften
            continue
        if "©" in text or "All rights reserved" in text:
            continue
        lines.append(text)
    if len(lines) < 5:  # kein fertiges Transkript auf der Seite
        return None
    return title, "\n\n".join(lines)


def fetch_one(slug: str) -> str:
    """Eine Folge holen. Rückgabe: 'saved' | 'exists' | 'pending'."""
    out = OUT_DIR / f"{slug}.md"
    if out.exists():
        return "exists"
    html = get(f"{BASE}/transcript/{slug}")
    if html is None:
        return "pending"
    result = extract_transcript(html)
    if result is None:
        return "pending"
    title, text = result
    out.write_text(
        f"# {title}\n\n"
        f"Quelle: {BASE}/transcript/{slug} (offizielles Sounds-True-Transkript)\n"
        f"Nur für den privaten Gebrauch — nicht weitergeben, nicht committen.\n\n"
        f"---\n\n{text}\n",
        encoding="utf-8",
    )
    return "saved"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", type=int, default=2, help="Anzahl Archiv-Seiten (à ~5 Folgen), neueste zuerst")
    ap.add_argument("--all", action="store_true", help="komplettes Archiv durchgehen")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    slugs = episode_slugs(None if args.all else args.pages)
    if not slugs:
        sys.exit("Keine Folgen im Archiv gefunden — hat sich die Seitenstruktur geändert?")

    saved, pending = [], []
    for slug in slugs:
        status = fetch_one(slug)
        if status == "saved":
            saved.append(slug)
            print(f"  ✓ {slug}")
            time.sleep(DELAY_SECONDS)
        elif status == "pending":
            pending.append(slug)
            print(f"  … {slug} (Transkript noch nicht veröffentlicht)")
            time.sleep(DELAY_SECONDS)

    total = len(list(OUT_DIR.glob("*.md")))
    print(f"\n{len(saved)} neu gespeichert, {len(pending)} noch ausstehend, {total} Transkripte insgesamt in {OUT_DIR}")


if __name__ == "__main__":
    main()
