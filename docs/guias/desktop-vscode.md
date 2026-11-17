# Guía: GitHub Desktop y VS Code (capítulo 11)

Los mismos pasos de la terminal pueden hacerse con una interfaz gráfica. Esta tabla sirve para repetir el capítulo con GitHub Desktop o con la vista *Source Control* de VS Code.

| Acción | Terminal | GitHub Desktop | VS Code |
|---|---|---|---|
| Clonar | `git clone <url>` | *File → Clone repository* | *Command Palette → Git: Clone* |
| Ver cambios | `git status`, `git diff` | Pestaña *Changes* | Vista *Source Control* (Ctrl+Shift+G) |
| Preparar | `git add <archivo>` | Casilla junto al archivo | Botón **+** junto al archivo |
| Confirmar | `git commit -m "..."` | Campo *Summary* + *Commit to main* | Mensaje + ✓ *Commit* |
| Crear rama | `git switch -c <rama>` | *Current branch → New branch* | Barra de estado → nombre de rama → *Create new branch* |
| Cambiar de rama | `git switch <rama>` | *Current branch* | Barra de estado → nombre de rama |
| Fusionar | `git merge <rama>` | *Branch → Merge into current branch* | *Command Palette → Git: Merge Branch* |
| Traer cambios | `git pull` | *Fetch origin → Pull origin* | *Sync Changes* |
| Subir cambios | `git push` | *Push origin* | *Sync Changes* / *Push* |
| Historial | `git log --oneline` | Pestaña *History* | Extensión *Git Graph* o *Timeline* |

## Ejercicio de práctica

1. Clona el repositorio con la herramienta elegida.
2. Edita `bitacora.md` agregando una fila al registro.
3. Haz el commit con el mensaje `docs: registrar práctica con <herramienta>`.
4. Sube el cambio y comprueba en GitHub que aparece en el historial.

> Configura la identidad de ejemplo (`Estudiante` / `estudiante@example.com`) en *File → Options → Git* (Desktop) o con `git config` (VS Code usa la configuración de Git) para no publicar tu correo personal.
