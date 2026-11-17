"""Reintentos con límite y espera exponencial para llamadas a una API (cap. 31).

Se demuestra con una función simulada que falla 2 veces con HTTP 503 y luego responde;
no hace llamadas reales a la red.
"""
import time


class ErrorTemporal(Exception):
    """Errores que vale la pena reintentar (429, 502, 503, 504)."""


def con_reintentos(funcion, intentos=4, espera_inicial=0.1, dormir=time.sleep):
    for intento in range(1, intentos + 1):
        try:
            return funcion()
        except ErrorTemporal as error:
            if intento == intentos:
                raise RuntimeError(f"Se agotaron los {intentos} intentos") from error
            espera = espera_inicial * 2 ** (intento - 1)
            print(f"Intento {intento} falló ({error}); reintento en {espera:.2f} s")
            dormir(espera)


def api_simulada(fallos):
    estado = {"llamadas": 0}

    def llamar():
        estado["llamadas"] += 1
        if estado["llamadas"] <= fallos:
            raise ErrorTemporal("HTTP 503")
        return {"status": 200, "llamadas": estado["llamadas"]}

    return llamar


if __name__ == "__main__":
    print("Caso 1:", con_reintentos(api_simulada(fallos=2)))
    try:
        con_reintentos(api_simulada(fallos=10), intentos=3)
    except RuntimeError as error:
        print("Caso 2:", error)
