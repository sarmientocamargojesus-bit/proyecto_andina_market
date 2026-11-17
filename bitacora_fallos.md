# Bitácora de fallos

Registro de incidentes reales del proyecto: qué pasó, cómo se detectó, cómo se resolvió y qué control evita que se repita.

| # | Fecha | Fallo | Detección | Solución | Control añadido |
|---|---|---|---|---|---|
| 1 | 2026-11-17 | `resumen.py` falla si se ejecuta desde `src/` (Issue #2) | Reporte manual | Rutas con `Path(__file__)` | Ejecución desde otra carpeta en la evidencia del cap. 34 |
