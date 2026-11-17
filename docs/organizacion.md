# Organización y permisos (capítulo 28 · documental)

> Diseño de una organización **ficticia**. No se crea ninguna organización real ni se transfiere el repositorio: hacerlo cambiaría la URL del proyecto, de GitHub Pages y de los enlaces de evidencia.

## Organización propuesta: `andina-market-360`

| Equipo | Integrantes (roles ficticios) | Responsabilidad | Carpetas (CODEOWNERS) |
|---|---|---|---|
| **Datos** | Analista de datos, encargado de sede | CSV, diccionario y cálculo | `/data/`, `/src/` |
| **Web** | Desarrollador web | Sitio de GitHub Pages | `/docs/*.html`, `/docs/*.css`, `/docs/*.js` |
| **Calidad** | QA / revisor | Pruebas, workflows y reglas | `/tests/`, `/.github/`, `/scripts/` |

## Matriz de roles

| Rol de GitHub | Quién | Puede | No puede |
|---|---|---|---|
| **Owner** (organización) | 1 persona responsable + 1 respaldo | Facturación, miembros, transferir o borrar repos | — |
| **Admin** (repositorio) | Líder de Calidad | Reglas de rama, secretos, Pages | Gestionar la organización |
| **Maintain** | Líderes de Datos y Web | Issues, PR, etiquetas, Releases | Cambiar reglas o secretos |
| **Write** | Integrantes de los equipos | Ramas y PR, fusionar con checks en verde | Saltarse la regla de `main` |
| **Triage** | Encargados de sede | Etiquetar y cerrar Issues | Escribir código |
| **Read** | Gerencia | Ver código, Issues y el sitio | Modificar |

Principio de **mínimo privilegio**: cada persona recibe el rol más bajo que le permite hacer su trabajo; 2FA obligatorio para todos los miembros.

## Lista de verificación para una transferencia (si algún día se hiciera)

- [ ] Crear la organización y exigir 2FA.
- [ ] Crear los equipos Datos, Web y Calidad.
- [ ] *Settings → Transfer ownership* del repositorio (lo hace el Owner actual).
- [ ] Actualizar `CODEOWNERS` de `@sarmientocamargojesus-bit` a `@andina-market-360/datos`, `/web`, `/calidad`.
- [ ] Revisar la regla de `main` (aprobaciones requeridas: 1 cuando haya más de una persona).
- [ ] Actualizar URL de Pages, README y enlaces del registro de evidencias.
- [ ] Rotar secretos de Actions (si existieran).
- [ ] Comprobar que las redirecciones de la URL antigua funcionan.

## Indicador de gobernanza

| Indicador | Fórmula | Meta | Valor actual |
|---|---|---|---|
| PR fusionados con checks en verde | PR verdes / PR fusionados | 100 % | Ver `docs/auditoria.md` |
| Commits directos en `main` desde el cap. 14 | conteo | 0 | Ver `docs/auditoria.md` |
| Controles de cumplimiento | `bash scripts/cumplimiento.sh` | 6/6 | Ver `docs/auditoria.md` |
