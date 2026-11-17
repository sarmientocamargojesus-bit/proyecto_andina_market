# Guía: Codespaces (capítulo 30 · opcional, lo haces tú)

`.devcontainer/devcontainer.json` define el entorno: imagen oficial de **Python 3.12** y, al crearse, ejecuta las pruebas y genera el resumen (`postCreateCommand`).

1. *Code → Codespaces → Create codespace on main*.
2. Espera a que termine `postCreateCommand`: en la terminal verás `OK` y el tablero.
3. Para ver el sitio: `python -m http.server 8000 -d docs` → pestaña *Ports* → abrir el puerto 8000.
4. **Al terminar**: *Code → Codespaces → ⋯ → Stop codespace* y luego **Delete**.

> Un Codespace consume horas y almacenamiento de tu cuota gratuita mientras existe (aunque esté detenido ocupa almacenamiento). Elimínalo cuando acabes la práctica.
