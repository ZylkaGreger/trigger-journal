#!/usr/bin/env python3
"""INDEX.md der Singer-Wissensbasis aus den Episode-Digests neu bauen.

Liest reference/singer-knowledge/episodes/*.md (Titel = erste Zeile,
Themen aus der `themes:`-Zeile) und schreibt reference/singer-knowledge/INDEX.md.
Nach jedem neuen Digest einfach erneut laufen lassen:
  python3 tools/build_index.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "reference" / "singer-knowledge"


def main() -> None:
    eps = sorted((BASE / "episodes").glob("*.md"))
    themes = defaultdict(list)
    all_eps = []
    for p in eps:
        text = p.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip()
        m = re.search(r"^themes:\s*(.+)$", text, re.M)
        tags = [t.strip() for t in m.group(1).split(",")] if m else []
        for t in tags:
            themes[t].append((p.name, title))
        all_eps.append((p.name, title, tags))

    nums = sorted(int(m.group(1)) for f, _, _ in all_eps if (m := re.match(r"e?(\d+)", f)))
    span = f"E{nums[0]}–E{nums[-1]}" if nums else "—"

    out = [
        "# Singer-Wissensbasis — Index",
        "",
        "Destilliert aus den offiziellen Podcast-Transkripten (`reference/transcripts/`).",
        "Pro Folge ein Digest in `episodes/` mit Kernlehre, Beispielen und wörtlich",
        "verifizierten Zitaten. Nur lokal — nie committen.",
        "",
        f"Stand: {len(eps)} Folgen ({span}).",
        "",
        "## Themen",
        "",
    ]
    for t in sorted(themes, key=lambda k: -len(themes[k])):
        out.append(f"### {t} ({len(themes[t])})")
        out.extend(f"- [{title}](episodes/{fname})" for fname, title in themes[t])
        out.append("")
    out += ["## Alle Folgen", ""]
    out.extend(f"- [{title}](episodes/{fname}) — {', '.join(tags)}" for fname, title, tags in all_eps)

    (BASE / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"OK: {len(eps)} Folgen, {len(themes)} Themen → {BASE / 'INDEX.md'}")


if __name__ == "__main__":
    main()
