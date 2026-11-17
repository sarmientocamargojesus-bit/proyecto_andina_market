# Política de la rama `main` (capítulo 17)

| Regla | Configuración en *Settings → Rules → Rulesets* | Motivo |
|---|---|---|
| Exigir Pull Request | *Require a pull request before merging* | Todo cambio queda revisado y enlazado a un Issue |
| Aprobaciones requeridas | **0** | En un repositorio de una sola persona no puedes aprobar tus propios PR; la revisión se registra como comentario |
| Exigir checks | *Require status checks to pass* → `pruebas` | No se fusiona nada con pruebas en rojo |
| Bloquear *force push* | *Block force pushes* | El historial publicado no se reescribe |
| Impedir borrado | *Restrict deletions* | `main` no puede eliminarse |

## Cómo activarla (lo haces tú)

1. *Settings → Rules → Rulesets → New ruleset → New branch ruleset*.
2. Nombre: `proteger-main`. *Enforcement status*: **Active**.
3. *Target branches → Add target → Include default branch*.
4. Marca: *Restrict deletions*, *Require a pull request before merging* (0 aprobaciones), *Require status checks to pass* (agrega `pruebas`), *Block force pushes*.
5. **Create**.

Responsable de revisión: ver [`.github/CODEOWNERS`](../.github/CODEOWNERS).
