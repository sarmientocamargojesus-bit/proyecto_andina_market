import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

import resumen  # noqa: E402

VENTAS = resumen.leer_ventas(RAIZ / "data" / "ventas.csv")


class PruebasResumen(unittest.TestCase):
    def test_importe_calculado(self):
        fila = {"cantidad": "4", "precio_unitario": "35.00"}
        self.assertEqual(resumen.importe(fila), 140.00)

    def test_total_general(self):
        self.assertEqual(resumen.total_general(VENTAS), 1845.00)

    def test_total_lima(self):
        self.assertEqual(resumen.total_por_sede(VENTAS)["Lima"], 814.00)

    def test_productos_ica(self):
        self.assertEqual(
            resumen.productos_por_sede(VENTAS, "Ica"),
            ["Café orgánico", "Chocolate 70%", "Pallar seco", "Quinua blanca"],
        )

    def test_subtitulo_sedes(self):
        reporte = resumen.reporte_texto(resumen.generar_resumen(VENTAS))
        self.assertIn("Sedes: Lima, Ica, Arequipa", reporte.splitlines()[1])


if __name__ == "__main__":
    unittest.main()
