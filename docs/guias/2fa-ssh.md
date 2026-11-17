# Guía: 2FA y claves SSH (capítulo 25 · lo haces tú)

> Ningún código, clave ni captura de estos pasos se sube al repositorio.

## Autenticación en dos pasos (2FA)

1. GitHub → foto de perfil → **Settings → Password and authentication**.
2. **Enable two-factor authentication** → elige una app de autenticación (TOTP) o una llave de seguridad / *passkey*.
3. Escanea el código QR con la app e ingresa el código de 6 dígitos.
4. **Descarga los códigos de recuperación** y guárdalos en tu gestor de contraseñas (no en el repositorio, no en el chat, no en capturas).
5. Comprueba en *Sessions* que solo aparecen tus dispositivos.

## Clave SSH de laboratorio

```bash
ssh-keygen -t ed25519 -C "laboratorio-andina"   # usa una frase de paso
cat ~/.ssh/id_ed25519.pub                       # solo la parte PÚBLICA
```

1. *Settings → SSH and GPG keys → New SSH key*, pega la clave **pública** (`.pub`).
2. Prueba: `ssh -T git@github.com` → "Hi <usuario>! You've successfully authenticated".
3. Cambia el remoto si quieres usar SSH: `git remote set-url origin git@github.com:sarmientocamargojesus-bit/proyecto_andina_market.git`.
4. Al terminar el laboratorio, **borra la clave** en GitHub si ya no la usarás.

La clave privada (`id_ed25519`, sin `.pub`) **nunca** se comparte ni se sube.
