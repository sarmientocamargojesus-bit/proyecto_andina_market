import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

import ia_ticket  # noqa: E402
import resumen  # noqa: E402


class PruebasIaTicket(unittest.TestCase):
    def test_ticket_por_sede_con_datos_reales(self):
        datos = resumen.generar_resumen(resumen.leer_ventas(RAIZ / "data" / "ventas.csv"))
        self.assertEqual(
            ia_ticket.ticket_por_sede(datos),
            {"Lima": 203.50, "Ica": 138.75, "Arequipa": 119.00},
        )

    def test_sede_sin_conteo_no_lanza_keyerror(self):
        datos = {"total_por_sede": {"Cusco": 100.0}, "operaciones_por_sede": {}}
        self.assertEqual(ia_ticket.ticket_por_sede(datos), {"Cusco": 0.0})

    def test_resumen_vacio(self):
        self.assertEqual(ia_ticket.ticket_por_sede({}), {})


if __name__ == "__main__":
    unittest.main()
