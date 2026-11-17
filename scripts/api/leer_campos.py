"""Lee campos de una respuesta JSON de la API de GitHub guardada en disco (cap. 31)."""
import json
import sys
from collections import Counter
from pathlib import Path

RUTA = Path(__file__).resolve().parents[2] / "docs" / "evidencias" / "api_issues.json"


def resumen_issues(datos):
    issues = datos["issues"]
    estados = Counter(i["state"] for i in issues)
    etiquetas = Counter(e for i in issues for e in i.get("labels", []))
    abiertos = [f"#{i['number']} {i['title']}" for i in issues if i["state"] == "open"]
    return estados, etiquetas, abiertos


if __name__ == "__main__":
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else RUTA
    estados, etiquetas, abiertos = resumen_issues(json.loads(ruta.read_text(encoding="utf-8")))
    print("Estados:", dict(estados))
    print("Etiquetas:", dict(etiquetas))
    print("Abiertos:", *abiertos, sep="\n  ")
