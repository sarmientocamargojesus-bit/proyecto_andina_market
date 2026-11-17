# Proyecto Andina Market 360

> Caso **ficticio** del cuaderno de prácticas Git y GitHub (capítulo 01). Ningún dato corresponde a personas o empresas reales.

## Problema

Andina Market es una cadena ficticia de tiendas de productos andinos con tres sedes: **Lima, Ica y Arequipa**. Cada sede registra sus ventas en hojas sueltas y la gerencia no tiene una vista única de cuánto vende cada sede, qué productos se mueven más ni cuál es el valor de una venta típica.

## Usuarios

| Usuario | Qué necesita |
|---|---|
| Gerencia | Ver el total vendido y comparar sedes en una sola página |
| Encargados de sede | Confirmar que sus ventas están bien registradas |
| Equipo de datos | Mantener el cálculo reproducible y con pruebas |

## Necesidad

Un flujo sencillo y verificable: **CSV de ventas → script en Python → resumen JSON → página web**, con historial de cambios en Git y colaboración en GitHub.

## Preguntas comerciales

1. ¿Cuánto vende cada sede y cuánto suma el total?
2. ¿Cuántas operaciones registra cada sede?
3. ¿Qué productos aparecen en las ventas de cada sede?
4. ¿Cuál es el ticket promedio (importe medio por operación)?

## Herramientas

Git · GitHub · Python 3 (solo biblioteca estándar) · `unittest` · CSV/JSON · HTML + CSS + JavaScript sin frameworks · YAML (GitHub Actions).

## Estructura propuesta

| Carpeta | Contenido |
|---|---|
| `data/` | Datos de ventas ficticias y su diccionario |
| `src/` | Código Python que calcula el resumen |
| `tests/` | Pruebas automáticas con `unittest` |
| `docs/` | Documentación y sitio web (GitHub Pages) |
| `.github/` | Plantillas, reglas y workflows de GitHub |

## Criterios de éxito

- El resumen calcula correctamente los totales por sede y el total general.
- Las pruebas pasan en local y en GitHub Actions.
- La página muestra los mismos números que el CSV.
- Todo cambio queda registrado en el historial con mensajes claros.
