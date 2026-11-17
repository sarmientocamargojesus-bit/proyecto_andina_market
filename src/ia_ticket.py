"""Ticket promedio por sede.

DECLARACIÓN DE USO DE IA: este módulo fue generado con asistencia de IA (Claude) a partir
del prompt documentado en docs/politica_ia.md, y fue auditado y probado por la persona
responsable antes de integrarse (ver la sección "Auditoría" de ese documento).
"""


def ticket_por_sede(resumen):
    """Devuelve {sede: total / operaciones} redondeado a 2 decimales.

    `resumen` es el diccionario de src/resumen.py: generar_resumen().
    Una sede sin operaciones registradas (o ausente del conteo) devuelve 0.0
    en lugar de lanzar KeyError o ZeroDivisionError.
    """
    operaciones = resumen.get("operaciones_por_sede", {})
    tickets = {}
    for sede, total in resumen.get("total_por_sede", {}).items():
        n = operaciones.get(sede, 0)
        tickets[sede] = round(total / n, 2) if n else 0.0
    return tickets
