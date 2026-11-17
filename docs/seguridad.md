# Seguridad y autenticación (capítulo 25)

## Inventario de elementos sensibles

| Elemento | ¿Existe en el proyecto? | Dónde vive | Protección |
|---|---|---|---|
| Token personal de GitHub (PAT) | Opcional (scripts del cap. 31) | Solo en `.env` local | `.env` en `.gitignore`; caducidad ≤ 30 días; permisos de solo lectura |
| `GITHUB_TOKEN` de Actions | Sí | Lo genera GitHub en cada ejecución | `permissions:` mínimos en cada workflow |
| Secreto de webhook | Solo ficticio (cap. 31) | Constante de prueba en el script | Nunca un secreto real en el código |
| Claves SSH | En el equipo de la persona | `~/.ssh/` | Nunca dentro del repositorio; frase de paso |
| Códigos de recuperación 2FA | En la cuenta de la persona | Gestor de contraseñas | Nunca en el repositorio ni en capturas |
| Datos personales | **No** | — | Solo datos ficticios (`data/diccionario.md`) |

## Controles en el repositorio

- `.gitignore` bloquea `.env`; `.env.example` documenta las variables **sin valores**.
- `scripts/escaneo_secretos.sh` revisa todo el historial antes de cada push.
- *Secret scanning* y *Push protection* de GitHub (capítulo 26).

## Procedimiento ante un incidente (secreto expuesto)

1. **Revocar primero**: invalidar el token o la clave en el servicio de origen (*Settings → Developer settings → Tokens* en GitHub). Un secreto publicado se considera comprometido aunque se borre después.
2. **Generar uno nuevo** y guardarlo solo en `.env` o en *Settings → Secrets and variables → Actions*.
3. **Revisar el uso**: *Settings → Security log* de la cuenta y registros del servicio.
4. **Limpiar el repositorio**: eliminar el secreto del código en un commit nuevo. Reescribir el historial solo si es imprescindible y coordinado con el equipo.
5. **Registrar** el incidente en `bitacora_fallos.md` (qué pasó, cuándo, cómo se resolvió, qué control se añade).

## Fuga simulada (cap. 25.5) — solo documental

El ejercicio de "subir un token falso y ver cómo lo detecta GitHub" **no se reproduce en este repositorio público**: aun siendo falso, un patrón de token publicado activa alertas reales y queda en el historial. Se practica en un repositorio privado de laboratorio y aquí solo se documenta el procedimiento anterior.
