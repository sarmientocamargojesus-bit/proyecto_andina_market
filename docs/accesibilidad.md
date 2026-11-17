# Verificación de accesibilidad del sitio (capítulo 19)

| Control | Dónde | Resultado |
|---|---|---|
| Idioma declarado | `<html lang="es">` en `index.html` y `productos.html` | ✔ |
| Encabezados de tabla con `scope` | `productos.html`: `scope="col"` en columnas, `scope="row"` en cada sede | ✔ |
| Contraste ≥ 4.5:1 | `python scripts/contraste.py` (mínimo 5.93:1) | ✔ |
| Gráfico con alternativa textual | `role="img"` + `aria-label`; los montos también aparecen como texto | ✔ |
| Navegación identificable | `<nav aria-label>` y `aria-current="page"` | ✔ |
| Mensajes de error anunciados | `role="status"` en `#estado` | ✔ |

## Lección 19.5: rutas en un sitio de proyecto

El sitio se publica en `https://sarmientocamargojesus-bit.github.io/proyecto_andina_market/`, es decir, **dentro de una subcarpeta** del dominio.

| Ruta en `app.js` | URL que pide el navegador | Resultado |
|---|---|---|
| `/data/resumen.json` (absoluta) | `https://sarmientocamargojesus-bit.github.io/data/resumen.json` | **404** |
| `data/resumen.json` (relativa) | `https://sarmientocamargojesus-bit.github.io/proyecto_andina_market/data/resumen.json` | 200 |

Por eso `app.js` usa la ruta relativa. La comprobación real con ambas URL queda en `docs/evidencias/registro.md` una vez publicado el sitio.
