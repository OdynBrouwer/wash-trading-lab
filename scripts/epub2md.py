#!/usr/bin/env python3
"""epub2md.py - converteer EPUB-bestanden naar platte Markdown.

Gebruik:
    python epub2md.py                 # alle *.epub onder de huidige map
    python epub2md.py pad\naar\boek.epub

Schrijft per boek een .md met dezelfde basename, in dezelfde map als de .epub.
Volgt de spine uit het OPF-bestand, dus de leesvolgorde blijft intact.
"""

from __future__ import annotations

import html
import os
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

CONTAINER_NS = "urn:oasis:names:tc:opendocument:xmlns:container"


def _localname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def spine_files(z: zipfile.ZipFile) -> list[str]:
    """Bepaal de leesvolgorde van de content-documenten via container.xml + OPF."""
    opf_path = None
    try:
        cont = ET.fromstring(z.read("META-INF/container.xml"))
        for el in cont.iter():
            if _localname(el.tag) == "rootfile":
                opf_path = el.get("full-path")
                break
    except KeyError:
        pass

    names = z.namelist()
    if not opf_path or opf_path not in names:
        candidates = [n for n in names if n.lower().endswith(".opf")]
        opf_path = candidates[0] if candidates else None
    if not opf_path:
        return sorted(n for n in names if re.search(r"\.x?html?$", n, re.I))

    base = os.path.dirname(opf_path)
    root = ET.fromstring(z.read(opf_path))

    manifest: dict[str, str] = {}
    for el in root.iter():
        if _localname(el.tag) == "item":
            item_id, href = el.get("id"), el.get("href")
            if item_id and href:
                manifest[item_id] = href

    order: list[str] = []
    for el in root.iter():
        if _localname(el.tag) == "itemref":
            href = manifest.get(el.get("idref", ""))
            if href:
                joined = os.path.normpath(os.path.join(base, href)).replace("\\", "/")
                if joined in names:
                    order.append(joined)

    if order:
        return order
    return sorted(n for n in names if re.search(r"\.x?html?$", n, re.I))


def _strip_tags(fragment: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def to_markdown(raw: str) -> str:
    """HTML -> platte Markdown: koppen blijven koppen, lijsten blijven lijsten."""
    raw = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", raw)

    # koppen
    def heading(m: re.Match[str]) -> str:
        level = int(m.group(1))
        text = _strip_tags(m.group(2))
        return f"\n\n{'#' * level} {text}\n\n" if text else "\n\n"

    raw = re.sub(r"(?is)<h([1-6])[^>]*>(.*?)</h\1>", heading, raw)

    raw = re.sub(r"(?is)<li[^>]*>", "\n- ", raw)
    raw = re.sub(r"(?is)<br\s*/?>", "\n", raw)
    raw = re.sub(r"(?is)</(p|div|blockquote|tr|li|h[1-6]|section|article)>", "\n\n", raw)
    raw = re.sub(r"<[^>]+>", "", raw)

    raw = html.unescape(raw).replace("\u00a0", " ").replace("\u3000", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r" *\n *", "\n", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def convert(epub_path: str) -> tuple[str, int, int]:
    out_path = os.path.splitext(epub_path)[0] + ".md"
    with zipfile.ZipFile(epub_path) as z:
        parts: list[str] = []
        files = spine_files(z)
        for name in files:
            try:
                raw = z.read(name).decode("utf-8", "ignore")
            except KeyError:
                continue
            text = to_markdown(raw)
            if text:
                parts.append(text)

    body = "\n\n".join(parts)
    body = re.sub(r"\n{3,}", "\n\n", body)

    title = os.path.splitext(os.path.basename(epub_path))[0]
    header = f"# {title}\n\n> Geconverteerd uit `{os.path.basename(epub_path)}` met epub2md.py\n\n"
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header + body + "\n")

    return out_path, len(files), len(body)


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        targets = argv[1:]
    else:
        targets = []
        for root, _dirs, files in os.walk("."):
            for name in files:
                if name.lower().endswith(".epub"):
                    targets.append(os.path.join(root, name))

    if not targets:
        print("Geen .epub-bestanden gevonden.")
        return 1

    for epub_path in targets:
        try:
            out_path, n_files, n_chars = convert(epub_path)
        except Exception as exc:  # noqa: BLE001 - bewust breed, we melden en gaan door
            print(f"FOUT  {epub_path}: {exc}")
            continue
        print(f"OK    {out_path}  ({n_files} documenten, {n_chars} tekens)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
