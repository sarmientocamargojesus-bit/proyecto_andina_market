# Andina Market 360 · Tablero de ventas por sede

Resumen de ventas de una cadena **ficticia** de tiendas andinas, construido paso a paso con el cuaderno de prácticas Git y GitHub.

Repositorio: https://github.com/sarmientocamargojesus-bit/proyecto_andina_market

## Objetivo

Dar a la gerencia una vista única y verificable de las ventas de las sedes **Lima, Ica y Arequipa**, con un flujo reproducible: CSV → Python → JSON → página web.

## Requisitos

- Python 3.11 o superior (solo biblioteca estándar, sin dependencias externas).
- Git 2.30 o superior.

## Datos

| Archivo | Descripción |
|---|---|
| [`data/ventas.csv`](data/ventas.csv) | 12 ventas ficticias, 4 por sede |
| [`data/diccionario.md`](data/diccionario.md) | Columnas, tipos y procedencia |

## Indicadores

| Indicador | Valor esperado |
|---|---|
| Operaciones | 12 |
| Total Lima | S/ 814.00 |
| Total Ica | S/ 555.00 |
| Total Arequipa | S/ 476.00 |
| **Total general** | **S/ 1845.00** |

## Inicio rápido

```bash
git clone https://github.com/sarmientocamargojesus-bit/proyecto_andina_market.git
cd proyecto_andina_market
python src/resumen.py
python -m unittest discover -s tests -v
```

Más detalles en el [manual](docs/manual.md). Para colaborar, lee [CONTRIBUTING.md](CONTRIBUTING.md).

## Licencia

[MIT](LICENSE). Los datos son ficticios y no representan a ninguna empresa real.
