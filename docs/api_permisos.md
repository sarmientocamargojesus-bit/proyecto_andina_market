# API, webhooks y apps (capítulo 31)

## Scripts locales (sin red ni tokens)

| Script | Qué demuestra |
|---|---|
| `scripts/api/leer_campos.py` | Leer campos de una respuesta JSON de la API (`docs/evidencias/api_issues.json`) |
| `scripts/api/reintentos.py` | Reintentos con límite y espera exponencial ante 503 |
| `scripts/api/webhook_hmac.py` | Verificar `X-Hub-Signature-256` con HMAC-SHA256 y `compare_digest` (secreto **ficticio**) |

**No se registran webhooks ni GitHub Apps reales**: requerirían un servidor público y secretos reales.

## Matriz de permisos de solo lectura

Para un token *fine-grained* o una GitHub App que solo consulte este repositorio:

| Permiso | Nivel | Para qué |
|---|---|---|
| Metadata | Read | Obligatorio: datos básicos del repositorio |
| Contents | Read | Leer `data/ventas.csv` y `docs/data/resumen.json` |
| Issues | Read | Listar Issues |
| Pull requests | Read | Listar PR y su estado |
| Actions | Read | Consultar ejecuciones de workflows |
| Todo lo demás | No access | Mínimo privilegio |

- *Repository access*: **Only select repositories** → `proyecto_andina_market`.
- Caducidad: 30 días o menos.
- El token vive solo en `.env` (ignorado por Git), nunca en el código.
