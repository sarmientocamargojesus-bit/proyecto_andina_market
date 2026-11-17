# Auditoría y cumplimiento (capítulo 27)

## Reglas vigentes

| Regla | Dónde está definida |
|---|---|
| Todo cambio en `main` entra por Pull Request con el check `pruebas` en verde | [politica_main.md](politica_main.md) |
| Títulos de PR con formato `tipo: descripción` | [CONTRIBUTING.md](../CONTRIBUTING.md), verificado por `.github/workflows/pr.yml` |
| Revisión por el responsable de cada área | [.github/CODEOWNERS](../.github/CODEOWNERS) |
| Sin datos personales ni secretos | [seguridad.md](seguridad.md), `scripts/escaneo_secretos.sh` |
| Reporte privado de vulnerabilidades | [SECURITY.md](../SECURITY.md) |

## Auditoría de merges en `main`

Generada con `git log --first-parent --merges main`:

| Commit | Pull Request |
|---|---|
| `bc0c05c` | [#25](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/25) · `docs/dependencias` |
| `a238ebb` | [#24](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/24) · `docs/seguridad` |
| `ea5a0c5` | [#23](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/23) · `ci/automatizacion-avanzada` |
| `616576d` | [#22](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/22) · `ci/entrega-continua` |
| `4e2630c` | [#20](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/20) · `test/sedes-ica-arequipa` |
| `b95b495` | [#19](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/19) · `ci/workflows-base` |
| `84ec6a2` | [#18](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/18) · `chore/archivos-paquetes` |
| `7b5669e` | [#17](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/17) · `feature/pages-tablero` |
| `bbd98c6` | [#16](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/16) · `ci/adjuntos-release` |
| `75c93f5` | [#15](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/15) · `feature/release-v1` |
| `f1d5c79` | [#14](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/14) · `docs/gobernanza` |
| `3037663` | [#13](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/13) · `docs/open-source` |
| `5f25c40` | [#12](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/12) · `feature/ticket-promedio` |
| `5a9036b` | [#11](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/11) · `ci/pruebas-actions` |
| `1ee2771` | [#10](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/10) · `docs/manual-verificacion` |
| `5e54e67` | [#9](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/9) · `feature/ficha-sedes` |

- PR cerrados **sin** fusionar: [#21](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/21) (refactor con error detectado por CI).
- Commits directos en `main` desde el capítulo 14 (después de fusionar el PR #9): **0**.

## Respaldo con `git bundle`

```console
$ git bundle create andina.bundle main
$ git bundle verify andina.bundle
The bundle uses this hash algorithm: sha1
$ git clone andina.bundle desde-bundle -b main && cd desde-bundle
$ python -m unittest discover -s tests
OK
```

El bundle **no** se guarda en el repositorio (`*.bundle` está en `.gitignore`); se adjunta a cada Release mediante `.github/workflows/release.yml`.

## Controles de cumplimiento

```console
$ bash scripts/cumplimiento.sh
✔ C1 Licencia MIT presente
✔ C2 Gobernanza: SECURITY.md, CODEOWNERS y plantilla de PR
✔ C3 .env ignorado y fuera del índice
✔ C4 Historial sin secretos
✔ C5 Pruebas unitarias en verde
✔ C6 Humo: JSON publicado = CSV
Cumplimiento: 6/6 controles
```
