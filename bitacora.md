# Bitácora de trabajo

## Línea base de datos (capítulo 05)

| Dato | Valor |
|---|---|
| Registros en `data/ventas.csv` | 12 |
| Sedes | Lima, Ica, Arequipa (4 operaciones cada una) |
| Total Lima | S/ 814.00 |
| Total Ica | S/ 555.00 |
| Total Arequipa | S/ 476.00 |
| **Total general** | **S/ 1845.00** |

## Los tres espacios de Git

```mermaid
flowchart LR
    A[Directorio de trabajo] -- git add --> B[Área de preparación]
    B -- git commit --> C[Repositorio local]
    C -- git restore --> A
    C -- git push --> D[(GitHub)]
```

| Espacio | Qué contiene | Comando para ver su estado |
|---|---|---|
| Directorio de trabajo | Archivos que se editan | `git status` |
| Área de preparación (*staging*) | Cambios elegidos para el próximo commit | `git diff --staged` |
| Repositorio | Historial de commits | `git log --oneline` |

## Registro

| Fecha | Capítulo | Acción |
|---|---|---|
| 2026-11-17 | 05 | Línea base registrada |
| 2026-11-17 | 09 | Primer push y edición remota del README |
| 2026-11-17 | 09 | Push rechazado resuelto con fetch + merge |
| 2026-11-17 | 10 | Conflicto de título resuelto; revert de sede Cusco; stash y reflog |
| 2026-11-17 | 12 | README completo, manual, CONTRIBUTING y verificación de enlaces |
| 2026-11-17 | 13 | Issues #1–#8, etiquetas, plantilla y guía de Projects |
| 2026-11-17 | 14–16 | PR #9, #10, #11 y #12 (rojo→verde); guía de código abierto |
| 2026-11-17 | 17–19 | Gobernanza, CHANGELOG, workflow de Release y sitio de Pages |
| 2026-11-17 | 20–23 | Paquetes fuera del historial; CI ampliado y pr.yml; pruebas Ica/Arequipa; fallo controlado en PR #21; Pages con needs y humo |
| 2026-11-17 | 24–28 | Workflows avanzados; seguridad; dependabot; cumplimiento 6/6; auditoría; organización documental |
| 2026-11-17 | 29–31 | Issue y PR por API, guía gh; devcontainer; scripts de API, reintentos y HMAC |
| 2026-11-17 | 32–33 | Función asistida por IA auditada; stash, bisect, cherry-pick -x, rebase -i local y hook pre-commit |
