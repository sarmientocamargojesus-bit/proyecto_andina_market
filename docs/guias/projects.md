# Guía: tablero GitHub Projects "Andina Market 360" (capítulo 13)

Los proyectos de usuario se crean desde tu cuenta (esta parte la haces tú).

## Crear el tablero

1. Pestaña **Projects** del repositorio → **Link a project → New project**.
2. Plantilla **Board**, nombre **Andina Market 360**.
3. Renombra las columnas: **Pendiente**, **En proceso**, **Terminado**.
4. *Add item* → escribe `#` y elige cada Issue de la tabla.

## Tarjetas

| Issue | Título | Etiqueta | Columna inicial |
|---|---|---|---|
| #1 | Gráfico de barras de ventas por sede | mejora | Pendiente |
| #2 | resumen.py falla desde `src/` | bug | Pendiente |
| #3 | Confirmar la licencia | documentación | Terminado |
| #4 | Sedes y origen en el tablero | mejora | En proceso |
| #5 | Ticket promedio | mejora | Pendiente |
| #6 | Pruebas de Ica y Arequipa | mejora | Pendiente |
| #7 | Página de productos | mejora | Pendiente |
| #8 | Proteger `main` | documentación | Pendiente |

Activa en *Workflows* del proyecto la regla **Item closed → Terminado** para que las tarjetas se muevan solas al cerrar el Issue con un PR.
