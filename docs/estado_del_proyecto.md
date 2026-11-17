# Estado del proyecto · Andina Market 360

Resumen de lo que ya está hecho en el repositorio y de lo que todavía falta para completar el cuaderno de prácticas (36 capítulos).

**Fecha de corte:** 2026-11-17

| Enlace | URL |
|---|---|
| Repositorio | https://github.com/sarmientocamargojesus-bit/proyecto_andina_market |
| Sitio (GitHub Pages) | https://sarmientocamargojesus-bit.github.io/proyecto_andina_market/ |
| Release v2.0.0 (última) | https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/releases/tag/v2.0.0 |
| Release v1.0.0 | https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/releases/tag/v1.0.0 |
| Registro de las 288 evidencias | [evidencias/registro.md](evidencias/registro.md) |

---

## 1. Resumen

| Aspecto | Estado |
|---|---|
| Capítulos con trabajo en el repositorio | **36 / 36** |
| Issues | #1–#8, #32, #40, #41 → **todos cerrados** |
| Pull Requests propios | #9–#43 fusionados (salvo #21, cerrado a propósito sin fusionar) |
| Pruebas | **12 OK** (9 del resumen + 3 de `ia_ticket`) en Python 3.11 y 3.12 |
| CI (GitHub Actions) | En verde; 8 workflows |
| Sitio en GitHub Pages | **Publicado**; humo después de publicar = OK |
| Releases | **v1.0.0 y v2.0.0 publicadas** con ZIP, bundle y `SHA256SUMS.txt` |
| Cumplimiento | **6/6** controles |
| Escaneo de secretos | 0 hallazgos en todo el historial |
| Resultado verificable | 12 operaciones · Lima S/ 814.00 · Ica S/ 555.00 · Arequipa S/ 476.00 · **Total S/ 1845.00** · ticket S/ 153.75 |

---

## 2. Lo realizado, capítulo por capítulo

Leyenda: ✅ hecho de verdad · 📄 documental (así lo pedía el plan) · ⏳ pendiente (ver sección 3)

### Parte I · Fundamentos y cuenta

| Cap. | Tema | Realizado | Estado |
|---|---|---|---|
| 01 | Introducción | `proyecto.md` (problema, usuarios, 4 preguntas, criterios de éxito) e `inventario.md` | ✅ |
| 02 | Cuenta y perfil | Guía `docs/guias/cuenta.md` y plantilla de README de perfil | 📄 · ⏳ ajustes de cuenta |
| 03 | Interfaz | Guía `docs/guias/exploracion.md` (mapa de pestañas, Hello-World vs Spoon-Knife, Issue `cli/cli#14692`) | 📄 |
| 04 | Crear repositorios | README, `data/`, `src/`, `tests/`, `docs/`, `.github/`, `.gitignore`, licencia MIT | ✅ |
| 05 | Control de versiones | `bitacora.md` (línea base y diagrama de los 3 espacios) y `tabla_cambios.md` | ✅ |

### Parte II · Git local

| Cap. | Tema | Realizado | Estado |
|---|---|---|---|
| 06 | Configuración | Identidad de ejemplo y primer commit `chore: iniciar caso Andina Market` | ✅ |
| 07 | Comandos | Commits separados de docs, datos y pruebas; `diff`, `restore` y parche | ✅ |
| 08 | Ramas | `feature/resumen-sedes`, `fix/encabezado-tablero`, `feature/filtro-productos` (`--no-ff`) | ✅ |
| 09 | Remotos | Primer push, edición remota, `fetch` frente a `pull`, push rechazado resuelto sin `--force` | ✅ |
| 10 | Conflictos | Conflicto de título resuelto, `revert`, `stash`, `reflog` | ✅ |
| 11 | Desktop / VS Code | Procedencia de los datos, pregunta 4 y guía de equivalencias | ✅ · práctica opcional |
| 12 | Markdown | README completo, `docs/manual.md`, `CONTRIBUTING.md`, verificador de enlaces | ✅ |

### Parte III · Colaboración

| Cap. | Tema | Realizado | Estado |
|---|---|---|---|
| 13 | Issues y Projects | Issues #1–#8, etiquetas, plantilla `error_ventas.md`, guía del tablero | ✅ · ⏳ tablero |
| 14 | Pull Requests | PR #9 (revisión y segundo commit, cierra #4), PR #10 (docs), PR #11 (CI) | ✅ |
| 15 | Revisión de código | PR #12: `//` → Actions en rojo → revisión → división real → verde (cierra #5) | ✅ |
| 16 | Código abierto | Guía de fork → rama → PR y ética (PR #13). Sin PR en proyectos ajenos | 📄 |
| 17 | Gobernanza | Plantillas, `CODEOWNERS`, política de `main` (PR #14, cierra #8) | ✅ · ⏳ regla de `main` |
| 18 | Versiones | CHANGELOG 1.0.0, workflow de Release, **Release v1.0.0 publicada** | ✅ |
| 19 | GitHub Pages | Tablero, gráfico, productos, accesibilidad, lección 19.5 (PR #17, cierra #1 y #7). **Sitio publicado** | ✅ |

### Parte IV · Archivos

| Cap. | Tema | Realizado | Estado |
|---|---|---|---|
| 20 | Archivos y paquetes | Tamaños, `dist/` en `.gitignore`, decisión sobre LFS y paquete verificado en una copia limpia (PR #18) | ✅ |

### Parte V · GitHub Actions

| Cap. | Tema | Realizado | Estado |
|---|---|---|---|
| 21 | Introducción | `ci.yml` ampliado y `pr.yml` (PR #19); error de YAML diagnosticado y corregido | ✅ |
| 22 | Integración continua | Pruebas Ica/Arequipa/operaciones (PR #20, cierra #6); fallo controlado en PR #21 | ✅ |
| 23 | Entrega continua | `pages.yml` con `needs: pruebas` y `scripts/humo.py` (PR #22) | ✅ |
| 24 | Automatización avanzada | Workflows manual, programado y reutilizable; matriz 3.11/3.12; artefacto de 7 días (PR #23) | ✅ · ⏳ desactivar el programado |

### Parte VI · Seguridad y gobierno

| Cap. | Tema | Realizado | Estado |
|---|---|---|---|
| 25 | Seguridad | Inventario, `.env.example`, procedimiento ante incidentes, guía de 2FA/SSH (PR #24) | ✅ · ⏳ 2FA |
| 26 | Dependencias | `dependabot.yml`, `SECURITY.md`; PR de Dependabot #26 evaluado y fusionado (PR #25) | ✅ · ⏳ Code security, PR #27–#30 |
| 27 | Auditoría | `cumplimiento.sh` (6/6), auditoría de merges y respaldo con `git bundle` (PR #31) | ✅ |
| 28 | Organizaciones | Diseño ficticio: equipos, roles, transferencia, indicador | 📄 |

### Parte VII · Herramientas avanzadas

| Cap. | Tema | Realizado | Estado |
|---|---|---|---|
| 29 | GitHub CLI | Issue #32 y PR #34 creados por API, workflow disparado por API, guía `gh` | ✅ · práctica con `gh` opcional |
| 30 | Codespaces | `.devcontainer/devcontainer.json` y guía (PR #35) | ✅ · Codespace opcional |
| 31 | API y webhooks | JSON sin token, lectura de campos, reintentos y firma HMAC (secreto ficticio) | ✅ / 📄 |
| 32 | IA | `src/ia_ticket.py` declarado como asistido por IA, 3 pruebas, auditoría de `KeyError`, política de IA (PR #36) | ✅ |
| 33 | Git avanzado | `stash`, `bisect`, `cherry-pick -x`, `rebase -i` (copia local) y hook `pre-commit` (PR #37) | ✅ |
| 34 | Solución de problemas | Bug #2 corregido, push rechazado, HEAD *detached*, CI roja por dato alterado, `bitacora_fallos.md` (PR #38) | ✅ |

### Parte VIII · Proyecto integrador

| Cap. | Tema | Realizado | Estado |
|---|---|---|---|
| 35 | Portafolio | Ficha del caso, diagrama y guion de 3 minutos (PR #39) | 📄 · ⏳ README de perfil |
| 36 | Proyecto final | Issues #40/#41, CHANGELOG 2.0.0 (PR #42), README final, registro de 288 evidencias, verificación en clon limpio (PR #43), **Release v2.0.0 publicada** | ✅ |

---

## 3. Lo que falta por realizar

Todo lo que falta se hace con tu cuenta o en *Settings*: no se puede hacer desde la sesión de Claude.

### Prioridad alta (forma parte de la evaluación)

| # | Tarea | Capítulo | Dónde | Guía |
|---|---|---|---|---|
| 1 | Regla de protección de `main`: exigir PR, check `pruebas`, bloquear *force push*, impedir borrado, **0 aprobaciones** | 17 | *Settings → Rules → Rulesets* | [politica_main.md](politica_main.md) |
| 2 | Activar *Private vulnerability reporting*, *Dependabot alerts*, *Dependabot security updates*, *Secret scanning* y *Push protection* | 26 | *Settings → Code security* | [dependencias.md](dependencias.md) |
| 3 | Crear el tablero **Andina Market 360** (Pendiente / En proceso / Terminado) y agregar los Issues | 13 | Pestaña *Projects* | [guias/projects.md](guias/projects.md) |
| 4 | **PDF de evidencias** (entregable 3 del plan): capturas y enlaces del repositorio real, marcando los capítulos documentales (16, 28 y parte del 31) | 36 | Fuera del repositorio | [evidencias/registro.md](evidencias/registro.md) |

### Prioridad media (cuenta y privacidad)

| # | Tarea | Capítulo | Dónde |
|---|---|---|---|
| 5 | **Keep my email addresses private** y **Block command line pushes that expose my email** | 02 | *Settings → Emails* (de tu cuenta) |
| 6 | Activar **2FA** y guardar los códigos de recuperación en un gestor de contraseñas | 02 / 25 | *Settings → Password and authentication* |
| 7 | Perfil y notificaciones | 02 | *Settings → Public profile / Notifications* |
| 8 | README de perfil en el repositorio `sarmientocamargojesus-bit/sarmientocamargojesus-bit` | 02 / 35 | Copiar [plantilla_readme_perfil.md](plantilla_readme_perfil.md) |

### Mantenimiento del repositorio

| # | Tarea | Dónde |
|---|---|---|
| 9 | Marcar **Automatically delete head branches** | *Settings → General* |
| 10 | Borrar las ramas ya fusionadas, salvo `main` y las de los PR abiertos de Dependabot | Pestaña *Branches* |
| 11 | Evaluar los PR de Dependabot **#27–#30** (Pages y `upload-artifact`) y fusionar solo los que estén en verde | Pestaña *Pull requests* |
| 12 | **Después de entregar**: desactivar el workflow *Programado* | *Actions → Programado → ⋯ → Disable workflow* |

### Opcional (prácticas en tu equipo)

| # | Tarea | Capítulo | Guía |
|---|---|---|---|
| 13 | Repetir un commit con GitHub Desktop o VS Code | 11 | [guias/desktop-vscode.md](guias/desktop-vscode.md) |
| 14 | Clave SSH de laboratorio (no se sube) | 25 | [guias/2fa-ssh.md](guias/2fa-ssh.md) |
| 15 | Instalar `gh` y repetir las operaciones | 29 | [guias/gh-cli.md](guias/gh-cli.md) |
| 16 | Crear un Codespace, probarlo, detenerlo y **eliminarlo** | 30 | [guias/codespaces.md](guias/codespaces.md) |
| 17 | Ensayar el guion de 3 minutos | 35 | [portafolio.md](portafolio.md) |

---

## 4. Observaciones para el informe

| Tema | Detalle |
|---|---|
| Correo visible | El primer commit de edición remota (cap. 09) y los commits de fusión de PR hechos desde GitHub muestran el correo de la cuenta. Activar el correo privado (tarea 5) solo protege lo que se haga desde ese momento. |
| Tag v1.0.0 | Se creó desde la web sobre la versión final de `main` (`c8a8a1d`), no sobre el commit del PR #15 (`75c93f5`). El ZIP de la v1.0.0 contiene el código final. Los tags creados desde la web son **ligeros**, no anotados. |
| Tags y Releases | La sesión de Claude no podía subir tags; las Releases se publicaron desde la web y el workflow `release.yml` adjuntó los paquetes automáticamente. |
| Registro de evidencias | Supone 5 ejemplos y 3 retos por capítulo. Las descripciones resumen lo hecho en el repositorio: compáralas con los nombres exactos del cuaderno. |
| Datos | Las 12 ventas de `data/ventas.csv` se crearon para cuadrar con los totales del plan; no provienen del ZIP del laboratorio. |
| Uso de IA | El trabajo se hizo con asistencia de Claude; cada commit lo indica con `Co-Authored-By` y el cap. 32 lo documenta en [politica_ia.md](politica_ia.md). |
