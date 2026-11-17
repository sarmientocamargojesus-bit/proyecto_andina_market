# Dependencias (capítulo 26)

## Python

El proyecto usa **solo la biblioteca estándar**: `csv`, `json`, `pathlib`, `unittest`, `decimal`, `urllib`, `hmac`, `hashlib`. No hay `requirements.txt` ni paquetes de terceros, así que la superficie de ataque por dependencias de Python es nula.

## GitHub Actions

| Acción | Uso | Versión |
|---|---|---|
| `actions/checkout` | Descargar el código | `v4` |
| `actions/setup-python` | Preparar Python | `v5` |
| `actions/upload-artifact` | Guardar `resumen.json` | `v4` |
| `actions/configure-pages`, `upload-pages-artifact`, `deploy-pages` | Publicar el sitio | `v5`, `v3`, `v4` |

Dependabot (`.github/dependabot.yml`) revisa estas acciones cada lunes y abre un PR por cada actualización. Cada PR se **evalúa** antes de fusionar: notas de la versión, cambios incompatibles y CI en verde.

## Funciones de seguridad de GitHub (las activas tú)

*Settings → Code security*:

- **Dependabot alerts** y **Dependabot security updates**.
- **Secret scanning** y **Push protection** (gratuitos en repositorios públicos).
- **Private vulnerability reporting** (canal de `SECURITY.md`).
