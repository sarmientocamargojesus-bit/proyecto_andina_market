"""Resumen de ventas de Andina Market 360 (caso ficticio)."""
import csv
import json
from pathlib import Path

RUTA_VENTAS = "data/ventas.csv"
RUTA_SALIDA = "docs/data/resumen.json"


def leer_ventas(ruta=RUTA_VENTAS):
    with open(ruta, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def importe(fila):
    return round(int(fila["cantidad"]) * float(fila["precio_unitario"]), 2)


def total_por_sede(ventas):
    totales = {}
    for fila in ventas:
        totales[fila["sede"]] = round(totales.get(fila["sede"], 0) + importe(fila), 2)
    return totales


def total_general(ventas):
    return round(sum(importe(fila) for fila in ventas), 2)


def generar_resumen(ventas):
    return {
        "operaciones": len(ventas),
        "total_por_sede": total_por_sede(ventas),
        "total_general": total_general(ventas),
    }


def reporte_texto(resumen):
    lineas = ["Tablero de vetnas - Andina Market 360", ""]
    for sede, total in resumen["total_por_sede"].items():
        lineas.append(f"{sede:<10} S/ {total:>8.2f}")
    lineas.append(f"{'Total':<10} S/ {resumen['total_general']:>8.2f}")
    return "\n".join(lineas)


def main():
    resumen = generar_resumen(leer_ventas())
    Path(RUTA_SALIDA).parent.mkdir(parents=True, exist_ok=True)
    with open(RUTA_SALIDA, "w", encoding="utf-8") as salida:
        json.dump(resumen, salida, ensure_ascii=False, indent=2)
    print(reporte_texto(resumen))


if __name__ == "__main__":
    main()
