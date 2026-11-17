# Proyecto final (capítulo 36)

## Alcance → evidencia

| Alcance comprometido | Evidencia |
|---|---|
| Resumen por sede y total general desde el CSV | `src/resumen.py` · [PR #9](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/9) |
| Ticket promedio (153.75) | [PR #12](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/12) (rojo → verde) · [Issue #5](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/issues/5) |
| Ticket por sede asistido por IA y auditado | [PR #36](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/36) · [política de IA](politica_ia.md) |
| 12 pruebas automáticas | `tests/` · [CI](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/actions/workflows/ci.yml) |
| Sitio web accesible con gráfico y productos | [PR #17](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/17) · [accesibilidad](accesibilidad.md) |
| Publicación continua solo con pruebas en verde | [pages.yml](../.github/workflows/pages.yml) · [PR #22](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/22) |
| Colaboración con Issues y PR revisados | [Issues](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/issues?q=) · [auditoría de merges](auditoria.md) |
| Gobernanza de `main` | [política](politica_main.md) · [CODEOWNERS](../.github/CODEOWNERS) |
| Seguridad y dependencias | [SECURITY.md](../SECURITY.md) · [Dependabot PR #26](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/26) |
| Cumplimiento 6/6 y respaldo con bundle | [auditoria.md](auditoria.md) |
| Errores detectados antes de `main` | [PR #21](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/21) (cerrado sin fusionar) · [bitácora de fallos](../bitacora_fallos.md) |
| Bug real corregido | [Issue #2](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/issues/2) · [PR #38](https://github.com/sarmientocamargojesus-bit/proyecto_andina_market/pull/38) |
| Versiones 1.0.0 y 2.0.0 | [CHANGELOG](../CHANGELOG.md) · [guía de Release](guias/release.md) |
| Registro de las 288 evidencias | [registro.md](evidencias/registro.md) |

## Ruta completa en verde (clon limpio)

VERIFICACION_PENDIENTE

## Autoevaluación

| Criterio | Nivel alcanzado | Justificación |
|---|---|---|
| Historial claro y por capítulos | Logrado | Mensajes `tipo: descripción`; 0 commits directos en `main` desde el cap. 14 |
| Colaboración real (Issues, PR, revisión) | Logrado | 11 Issues, más de 30 PR, revisiones con cambios pedidos y atendidos |
| Pruebas y CI | Logrado | 12 pruebas; matriz 3.11/3.12; rojos reales detectados (PR #12, #21, #38) |
| Publicación (Pages) | Logrado tras activar Pages | Workflow listo; requiere *Settings → Pages → Source: GitHub Actions* |
| Seguridad y cumplimiento | Logrado | Escaneo de secretos, Dependabot, SECURITY.md, 6/6 controles |
| Versiones y Releases | Parcial → Logrado al publicar | CHANGELOG 1.0.0 y 2.0.0 listos; los tags y las Releases los publica la persona responsable |
| Documentación | Logrado | README, manual, 9 guías, portafolio y registro de evidencias |
| Uso responsable de IA | Logrado | Declaración, prompt verificable, auditoría y pruebas |

> Ajusta los niveles a la rúbrica oficial del curso si usa otra escala.
