# Bitácora de fallos

Registro de incidentes reales del proyecto: qué pasó, cómo se detectó, cómo se resolvió y qué control evita que se repita.

| # | Fecha | Fallo | Detección | Solución | Control añadido |
|---|---|---|---|---|---|
| 1 | 2026-11-17 | `resumen.py` falla si se ejecuta desde `src/` (Issue #2) | Reporte manual | Rutas con `Path(__file__)` | Ejecución desde otra carpeta en la evidencia del cap. 34 |
| 2 | 2026-11-17 | Push rechazado: otra copia subió `bitacora_fallos.md` a la misma rama | `! [rejected] (fetch first)` | `git fetch` + `git merge`, sin `--force` | Regla *Block force pushes* en `main` |
| 3 | 2026-11-17 | Precio de café en Lima alterado (35.00 → 3.50) en `data/ventas.csv` | CI roja: 4 pruebas fallan ([ejecución](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/actions/runs/44169601119)) | `git restore --source=origin/main -- data/ventas.csv` | Las pruebas de totales por sede (cap. 22) lo detectan antes de `main` |
| 4 | 2026-11-17 | Riesgo de página desactualizada: JSON publicado distinto del regenerado | `git diff --stat docs/data/resumen.json` | Regenerar y commitear el JSON | Paso `git diff --exit-code docs/data/resumen.json` en la CI |
| 5 | 2026-11-17 | `git bisect` señaló un commit equivocado | Revisión manual del resultado | `PYTHONDONTWRITEBYTECODE=1` | El hook `pre-commit` lo aplica |
