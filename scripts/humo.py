"""Prueba de humo: el total publicado coincide con el CSV.

Uso:
    python scripts/humo.py                      # compara con docs/data/resumen.json
    python scripts/humo.py https://.../         # compara con el sitio publicado
"""
import csv
import json
import sys
import urllib.request
from decimal import Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def total_csv():
    """Total calculado de forma independiente a src/resumen.py."""
    with open(RAIZ / "data" / "ventas.csv", newline="", encoding="utf-8") as f:
        return sum(Decimal(r["cantidad"]) * Decimal(r["precio_unitario"]) for r in csv.DictReader(f))


def resumen_publicado(url=None):
    if url:
        destino = url.rstrip("/") + "/data/resumen.json"
        with urllib.request.urlopen(destino, timeout=30) as respuesta:
            return json.load(respuesta), destino
    ruta = RAIZ / "docs" / "data" / "resumen.json"
    return json.loads(ruta.read_text(encoding="utf-8")), str(ruta.relative_to(RAIZ))


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else None
    esperado = total_csv()
    resumen, origen = resumen_publicado(url)
    publicado = Decimal(str(resumen["total_general"]))
    print(f"CSV: S/ {esperado:.2f} | {origen}: S/ {publicado:.2f}")
    if publicado != esperado:
        print("HUMO: el total publicado NO coincide con el CSV")
        return 1
    print("HUMO: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
