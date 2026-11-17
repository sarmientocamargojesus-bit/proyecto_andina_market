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

### Salida esperada del tablero

```text
Tablero de ventas - Andina Market 360
Sedes: Lima, Ica, Arequipa · Fuente: data/ventas.csv (datos ficticios)

Lima       S/   814.00
Ica        S/   555.00
Arequipa   S/   476.00
Total      S/  1845.00
```

### Lista de verificación antes de un Pull Request

- [ ] `python -m unittest discover -s tests -v` termina en `OK`.
- [ ] El total del tablero es S/ 1845.00.
- [ ] `python scripts/verificar_enlaces.py` informa 0 enlaces rotos.
- [ ] `bash scripts/escaneo_secretos.sh` informa 0 hallazgos.
