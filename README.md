# Andina Market 360

Resumen de ventas de una cadena **ficticia** de tiendas andinas (Lima, Ica y Arequipa), construido paso a paso con el cuaderno de prácticas Git y GitHub.

Repositorio: https://github.com/sarmientocamargojesus-bit/proyecto_andina_market

## Problema

La gerencia no tiene una vista única de las ventas de sus tres sedes.

## Funcionalidades

- Lee `data/ventas.csv`.
- Calcula el total por sede y el total general.
- Genera `docs/data/resumen.json`.

## Estructura

```
data/   datos ficticios
src/    código Python
tests/  pruebas
docs/   documentación y sitio
.github/ configuración de GitHub
```

## Ejecución

```bash
python src/resumen.py
python -m unittest discover -s tests -v
```

## Sedes

Lima, Ica y Arequipa. Cada sede registra 4 operaciones en el periodo de prueba.
