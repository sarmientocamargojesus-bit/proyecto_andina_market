# Guía: GitHub CLI (`gh`) (capítulo 29)

## Instalación y sesión (lo haces tú)

```bash
# Windows: winget install --id GitHub.cli   ·   macOS: brew install gh   ·   Linux: ver cli.github.com
gh auth login            # GitHub.com → HTTPS → Login with a web browser
gh auth status
```

## Equivalencias `gh` ↔ web ↔ API REST

| Operación | `gh` | Web | API REST |
|---|---|---|---|
| Ver el repositorio | `gh repo view sarmientocamargojesus-bit/proyecto_andina_market` | Pestaña *Code* | `GET /repos/{owner}/{repo}` |
| Listar Issues abiertos | `gh issue list` | Pestaña *Issues* | `GET /repos/{owner}/{repo}/issues?state=open` |
| Crear un Issue | `gh issue create --title "..." --body "..." --label documentación` | *Issues → New issue* | `POST /repos/{owner}/{repo}/issues` |
| Ver un Issue | `gh issue view 32` | Abrir el Issue | `GET /repos/{owner}/{repo}/issues/32` |
| Crear un PR | `gh pr create --base main --head docs/gh-cli --fill` | *Pull requests → New* | `POST /repos/{owner}/{repo}/pulls` |
| Estado de los checks | `gh pr checks 33` | Pestaña *Checks* del PR | `GET /repos/{owner}/{repo}/commits/{sha}/check-runs` |
| Fusionar un PR | `gh pr merge 33 --merge` | Botón *Merge pull request* | `PUT /repos/{owner}/{repo}/pulls/33/merge` |
| Ejecutar un workflow manual | `gh workflow run manual.yml -f sede=Ica` | *Actions → Manual → Run workflow* | `POST /repos/{owner}/{repo}/actions/workflows/manual.yml/dispatches` |
| Ver ejecuciones | `gh run list --limit 5` | Pestaña *Actions* | `GET /repos/{owner}/{repo}/actions/runs` |
| Consulta libre | `gh api repos/{owner}/{repo} --jq .default_branch` | — | cualquier endpoint |

## Operaciones reales hechas en este capítulo (vía API REST)

| Operación | Evidencia |
|---|---|
| Consulta del repositorio e Issues | `docs/evidencias/api_issues.json` (cap. 31) |
| Creación de Issue | [#32](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/issues/32) |
| Creación de PR | El PR que agrega esta guía (cierra #32) |
| Disparo de workflow manual | *Actions → Manual* (sede = Ica) |

## Práctica para repetir con tu sesión de `gh`

```bash
gh issue list --label mejora --state all
gh pr list --state merged --limit 5
gh run list --workflow ci.yml --limit 3
gh workflow run manual.yml -f sede=Arequipa && gh run watch
```
