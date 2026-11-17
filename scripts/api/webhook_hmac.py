"""Verifica la firma HMAC-SHA256 de un webhook de GitHub (cap. 31).

El secreto es FICTICIO y solo sirve para la demostración: en un caso real viviría en
una variable de entorno (ver .env.example), nunca en el código.
"""
import hashlib
import hmac
import json

SECRETO_FICTICIO = b"secreto-de-ejemplo-no-real"


def firmar(cuerpo: bytes, secreto: bytes = SECRETO_FICTICIO) -> str:
    return "sha256=" + hmac.new(secreto, cuerpo, hashlib.sha256).hexdigest()


def firma_valida(cuerpo: bytes, cabecera_firma: str, secreto: bytes = SECRETO_FICTICIO) -> bool:
    """Compara en tiempo constante la cabecera X-Hub-Signature-256 con la firma esperada."""
    return hmac.compare_digest(firmar(cuerpo, secreto), cabecera_firma or "")


if __name__ == "__main__":
    cuerpo = json.dumps({"action": "opened", "issue": {"number": 32}}).encode()
    cabecera = firmar(cuerpo)
    print("X-Hub-Signature-256:", cabecera)
    print("Firma correcta      ->", firma_valida(cuerpo, cabecera))
    print("Cuerpo alterado     ->", firma_valida(cuerpo.replace(b"32", b"33"), cabecera))
    print("Sin cabecera        ->", firma_valida(cuerpo, ""))
