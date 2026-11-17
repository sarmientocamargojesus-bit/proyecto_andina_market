# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y [versionado semántico](https://semver.org/lang/es/).

## [2.0.0] - 2026-11-17

### Agregado
- Sitio en GitHub Pages: tarjetas, gráfico de barras por sede y página de productos accesible (#1, #7, PR #17).
- `operaciones_por_sede` y `productos_por_sede` en `resumen.json`.
- Pruebas de Ica, Arequipa y operaciones por sede: 9 pruebas del resumen (#6, PR #20).
- `src/ia_ticket.py`: ticket promedio por sede, asistido por IA y auditado, con 3 pruebas (PR #36). Total: **12 pruebas**.
- Workflows: `pr.yml`, `pages.yml` (`needs: pruebas` + humo), `release.yml`, `manual.yml`, `programado.yml`, `reutilizable.yml`, `usa-reutilizable.yml`; matriz Python 3.11/3.12 y artefacto de 7 días (PR #19, #22, #23).
- Scripts: `humo.py`, `cumplimiento.sh` (6 controles), `contraste.py`, `verificar_enlaces.py`, scripts de API y hook `pre-commit`.
- `.devcontainer/` para Codespaces (PR #35).
- Documentación: seguridad, dependencias, auditoría, organización, política de IA, portafolio, guías y `bitacora_fallos.md`.

### Cambiado
- `actions/checkout` v4 → v7, evaluado en el PR de Dependabot #26.
- La CI verifica enlaces, cumplimiento y que `resumen.json` esté al día.

### Corregido
- `src/resumen.py` ya funciona desde cualquier carpeta gracias a `Path(__file__)` (#2, PR #38).

### Seguridad
- `SECURITY.md` con reporte privado, `dependabot.yml`, `.env.example` y procedimiento ante incidentes (PR #24, #25).

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
- `src/resumen.py` falla si se ejecuta desde `src/` (#2, corregido en 2.0.0).
