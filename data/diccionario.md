# Diccionario de datos: `ventas.csv`

| Columna | Tipo | Descripción | Ejemplo |
|---|---|---|---|
| `id` | entero | Identificador único de la venta | `1` |
| `fecha` | fecha ISO (AAAA-MM-DD) | Día de la venta | `2026-03-02` |
| `sede` | texto | Sede: `Lima`, `Ica` o `Arequipa` | `Lima` |
| `producto` | texto | Nombre del producto | `Café orgánico` |
| `cantidad` | entero | Unidades vendidas | `4` |
| `precio_unitario` | decimal (S/) | Precio por unidad en soles | `35.00` |

**Campo calculado:** `importe = cantidad × precio_unitario` (no se guarda en el CSV, lo calcula `src/resumen.py`).

Todos los registros son **ficticios**: no hay clientes, documentos de identidad, teléfonos ni direcciones.

## Procedencia de los datos

Los 12 registros fueron **inventados para el cuaderno de prácticas** (marzo de 2026, 4 por sede). No provienen de ningún sistema real ni de personas reales, por eso pueden publicarse en un repositorio público.
