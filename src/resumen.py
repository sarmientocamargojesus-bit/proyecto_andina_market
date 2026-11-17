"""Resumen de ventas de Andina Market 360 (caso ficticio)."""
import csv
import json
from pathlib import Path

# Rutas relativas al archivo, no al directorio desde el que se ejecuta (Issue #2)
RAIZ = Path(__file__).resolve().parents[1]
RUTA_VENTAS = RAIZ / "data" / "ventas.csv"
RUTA_SALIDA = RAIZ / "docs" / "data" / "resumen.json"


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


def operaciones_por_sede(ventas):
    conteo = {}
    for fila in ventas:
        conteo[fila["sede"]] = conteo.get(fila["sede"], 0) + 1
    return conteo


def productos_por_sede(ventas, sede):
    """Lista ordenada de productos vendidos en una sede (pregunta comercial 3)."""
    return sorted({fila["producto"] for fila in ventas if fila["sede"] == sede})


def total_general(ventas):
    return round(sum(importe(fila) for fila in ventas), 2)


def ticket_promedio(ventas):
    """Importe medio por operación (pregunta comercial 4)."""
    return round(total_general(ventas) / len(ventas), 2)


def generar_resumen(ventas):
    return {
        "operaciones": len(ventas),
        "total_por_sede": total_por_sede(ventas),
        "total_general": total_general(ventas),
        "ticket_promedio": ticket_promedio(ventas),
        "operaciones_por_sede": operaciones_por_sede(ventas),
        "productos_por_sede": {
            sede: productos_por_sede(ventas, sede) for sede in total_por_sede(ventas)
        },
    }


def reporte_texto(resumen):
    sedes = ", ".join(resumen["total_por_sede"])
    lineas = [
        "Tablero de ventas - Andina Market 360",
        f"Sedes: {sedes} · Fuente: data/ventas.csv (datos ficticios)",
        "",
    ]
    for sede, total in resumen["total_por_sede"].items():
        lineas.append(f"{sede:<10} S/ {total:>8.2f}")
    lineas.append(f"{'Total':<10} S/ {resumen['total_general']:>8.2f}")
    lineas.append(f"{'Ticket':<10} S/ {resumen['ticket_promedio']:>8.2f}")
    return "\n".join(lineas)


def main():
    resumen = generar_resumen(leer_ventas())
    RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with open(RUTA_SALIDA, "w", encoding="utf-8") as salida:
        json.dump(resumen, salida, ensure_ascii=False, indent=2)
    print(reporte_texto(resumen))


if __name__ == "__main__":
    main()
