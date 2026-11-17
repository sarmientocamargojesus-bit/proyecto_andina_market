# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y [versionado semántico](https://semver.org/lang/es/).

## [1.0.0] - 2026-11-17

### Agregado
- Resumen de ventas por sede y total general desde `data/ventas.csv` (12 ventas ficticias).
- Reporte en terminal con título, sedes y origen de los datos (#4, PR #9).
- Filtro de productos por sede.
- Ticket promedio por operación: S/ 153.75 (#5, PR #12).
- Pruebas con `unittest` y workflow de CI con el job `pruebas` (PR #11).
- Plantillas de Issue y PR, `CODEOWNERS` y política de `main` (#8, PR #14).
- Documentación: README, manual, CONTRIBUTING y guías.

### Corregido
- Errata en el encabezado del tablero ("vetnas").
- División entera en el ticket promedio (PR #12).

### Problemas conocidos
- `src/resumen.py` falla si se ejecuta desde `src/` (#2).
