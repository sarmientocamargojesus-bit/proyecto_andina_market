# Cómo contribuir

1. Abre o elige un **Issue** que describa el cambio.
2. Crea una rama desde `main` con un prefijo: `feature/…`, `fix/…` o `docs/…`.
3. Haz commits pequeños con el formato `tipo: descripción` (`docs`, `feat`, `fix`, `test`, `data`, `ci`, `chore`).
4. Ejecuta las pruebas antes de subir: `python -m unittest discover -s tests -v`.
5. Abre un **Pull Request** hacia `main`, completa la plantilla y enlaza el Issue (`Closes #N`).
6. Espera la revisión y que GitHub Actions esté en verde antes de fusionar.

## Reglas de datos

- Solo datos **ficticios**. Nunca subas datos de clientes, documentos de identidad, teléfonos ni direcciones.
- Nunca subas secretos (tokens, contraseñas, claves, archivos `.env`). Ejecuta `bash scripts/escaneo_secretos.sh` antes de cada push.
