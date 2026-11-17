# Manual de uso

## 1. Instalación

1. Instala Python 3.11 o superior y Git.
2. Clona el repositorio:
   ```bash
   git clone https://github.com/sarmientocamargojesus-bit/proyecto_andina_market.git
   cd proyecto_andina_market
   ```
3. No hay dependencias que instalar: el proyecto usa solo la biblioteca estándar.

## 2. Indicadores (KPI)

| KPI | Fórmula | Fuente |
|---|---|---|
| Importe de una venta | `cantidad × precio_unitario` | `src/resumen.py: importe()` |
| Total por sede | Suma de importes de la sede | `total_por_sede()` |
| Total general | Suma de todos los importes | `total_general()` |
| Operaciones | Número de filas del CSV | `generar_resumen()` |

## 3. Ejecución

Desde la **raíz** del repositorio:

```bash
python src/resumen.py
```

Genera `docs/data/resumen.json` e imprime el tablero en la terminal.

## 4. Verificación

```bash
python -m unittest discover -s tests -v
```

Todas las pruebas deben terminar en `OK`. El total general debe ser **S/ 1845.00**.
