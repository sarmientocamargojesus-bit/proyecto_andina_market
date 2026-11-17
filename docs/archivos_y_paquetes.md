# Archivos, tamaños y paquetes (capítulo 20)

## Tamaño de los archivos versionados

| Archivo | Bytes |
|---|---:|
| `docs/evidencias/locales.md` | 3805 |
| `src/resumen.py` | 2123 |
| `docs/guias/contribuir-open-source.md` | 2076 |
| `proyecto.md` | 1943 |
| `docs/guias/desktop-vscode.md` | 1789 |
| `docs/manual.md` | 1535 |
| `bitacora.md` | 1424 |
| `README.md` | 1375 |
| `.github/workflows/release.yml` | 1357 |
| `tabla_cambios.md` | 1195 |

Tamaño del repositorio (`git count-objects -vH`): 0 bytes.

Ningún archivo supera los 50 MB que GitHub advierte ni los 100 MB que bloquea.

## ¿Hace falta Git LFS?

**No.** Git LFS sirve para binarios grandes que cambian (videos, modelos, datasets de cientos de MB). Este proyecto solo versiona texto pequeño (CSV, Python, HTML), que Git comprime y compara bien. Activar LFS añadiría una dependencia y consumiría la cuota de almacenamiento LFS sin beneficio.

Si algún día se agregara un archivo grande:

```bash
git lfs install
git lfs track "*.parquet"
git add .gitattributes
```

## Paquete de distribución

El ZIP se genera **desde un tag** con `git archive` (solo archivos versionados, sin `.git` ni temporales):

```bash
git archive --format=zip --prefix=proyecto_andina_market-v1.0.0/ -o dist/proyecto_andina_market-v1.0.0.zip v1.0.0
```

- `dist/`, `*.zip` y `*.bundle` están en `.gitignore`: el paquete **no se guarda como commit**.
- Se publica solo como **adjunto de una Release** (workflow `release.yml`).
- Verificación en una copia limpia: ver `docs/evidencias/locales.md` (CAP20).
