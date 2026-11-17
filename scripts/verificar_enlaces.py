"""Verifica que los enlaces relativos de los archivos Markdown apunten a archivos existentes."""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ENLACE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")


def enlaces_rotos():
    rotos = []
    for md in RAIZ.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for destino in ENLACE.findall(md.read_text(encoding="utf-8")):
            if destino.startswith(("http://", "https://", "mailto:")):
                continue
            if not (md.parent / destino).exists():
                rotos.append(f"{md.relative_to(RAIZ)} -> {destino}")
    return rotos


if __name__ == "__main__":
    rotos = enlaces_rotos()
    for r in rotos:
        print("ROTO:", r)
    print(f"Enlaces relativos rotos: {len(rotos)}")
    sys.exit(1 if rotos else 0)
