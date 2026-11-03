#!/usr/bin/env python3
"""Controleer alle interne links in de Markdown-bestanden van deze repository.

Elke link wordt opgelost **vanuit de map van het bestand waarin hij staat**, niet
vanuit de root. Dat is het verschil met de versie die hiervoor in dit bestand stond:
die keek alleen naar twee indexbestanden en ging uit van een hardgecodeerd
GitHub-pad van een andere repository.

Externe links (http/https/mailto) worden overgeslagen. Ankers binnen hetzelfde
bestand ook, tenzij je `--anchors` meegeeft.

Gebruik:
    python scripts/check_internal_links.py
    python scripts/check_internal_links.py --anchors
    python scripts/check_internal_links.py --quiet

Exitcode 0 als alles klopt, 1 als er iets stuk is.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

# Mappen die niet bij de documentatie horen.
SKIP_DIRS = {".git", "__pycache__", "sources", "data", "node_modules", ".venv", "venv"}

# Omgezette boeken en papers. Hun interne ankers (#oebps-html-...) zijn door de
# EPUB->Markdown-conversie komen te vervallen: epub2md.py laat de HTML-id's weg.
# Paden controleren we er wel, ankers niet — die zijn niet van ons en niet te
# repareren zonder de conversie te herschrijven.
THIRD_PARTY = ("docs", "bronnen")

# [label](doel) en ![alt](doel); het doel stopt bij de eerste spatie of haakje.
LINK = re.compile(r"!?\[([^\]]*)\]\(([^()\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)
EXTERNAL_SCHEMES = {"http", "https", "mailto", "ftp", "tel", "data"}


def iter_markdown(root: Path):
    """Alle Markdown-bestanden, minus de mappen in SKIP_DIRS."""
    for path in sorted(root.rglob("*.md")):
        parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in parts):
            continue
        yield path


def slugify(text: str) -> str:
    """Benadering van de anker-slug die GitHub maakt. Niet gegarandeerd exact."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


def anchors_of(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return set()
    return {slugify(h) for h in HEADING.findall(text)}


def is_third_party(root: Path, path: Path) -> bool:
    """True voor bestanden onder docs/bronnen/: wel paden checken, geen ankers."""
    return path.relative_to(root).parts[:2] == THIRD_PARTY


def check(root: Path, check_anchors: bool) -> tuple[int, int, list[str]]:
    files = 0
    checked = 0
    failures: list[str] = []

    for md in iter_markdown(root):
        files += 1
        try:
            lines = md.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            failures.append(f"{md.relative_to(root)}: onleesbaar ({exc})")
            continue

        for number, line in enumerate(lines, 1):
            where = f"{md.relative_to(root)}:{number}"
            for match in LINK.finditer(line):
                label, raw = match.groups()
                parts = urlsplit(raw)

                if parts.scheme.lower() in EXTERNAL_SCHEMES:
                    continue

                target = unquote(parts.path)

                if not target:  # alleen een anker binnen hetzelfde bestand
                    if check_anchors and parts.fragment and not is_third_party(root, md):
                        checked += 1
                        if slugify(parts.fragment) not in anchors_of(md):
                            failures.append(
                                f"{where}: [{label}] -> #{parts.fragment} "
                                f"bestaat niet in dit bestand"
                            )
                    continue

                checked += 1
                resolved = (md.parent / target).resolve()

                try:
                    resolved.relative_to(root)
                except ValueError:
                    failures.append(
                        f"{where}: [{label}] -> {target} wijst buiten de repository"
                    )
                    continue

                if not resolved.exists():
                    failures.append(f"{where}: [{label}] -> {target} bestaat niet")
                    continue

                if (check_anchors and parts.fragment
                        and resolved.suffix.lower() == ".md"
                        and not is_third_party(root, resolved)):
                    if slugify(parts.fragment) not in anchors_of(resolved):
                        failures.append(
                            f"{where}: [{label}] -> {target}#{parts.fragment} "
                            f"anker niet gevonden"
                        )

    return files, checked, failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd(),
                        help="repository-root (standaard: huidige map)")
    parser.add_argument("--anchors", action="store_true",
                        help="ook controleren of ankers (#kopje) bestaan (benaderend)")
    parser.add_argument("--quiet", action="store_true", help="alleen fouten tonen")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    if not root.is_dir():
        print(f"Geen map: {root}", file=sys.stderr)
        return 2

    files, checked, failures = check(root, args.anchors)

    if failures:
        print(f"Interne links kapot: {len(failures)} van {checked} gecontroleerd "
              f"in {files} bestanden", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"OK: {checked} interne links in {files} Markdown-bestanden, "
              f"alle doelen bestaan.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
