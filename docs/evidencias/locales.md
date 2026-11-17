# Evidencias de comandos locales

Salidas reales de los comandos que solo se ejecutan en el equipo local (no dejan rastro en GitHub). Cada bloque indica el identificador del cuaderno.

## CAP07 · git diff, git restore y recuperación con parche

```console
$ git diff --stat
 proyecto.md | 1 +
 1 file changed, 1 insertion(+)
$ git diff > /tmp/cambio.patch   # se guarda el cambio antes de descartarlo
$ git restore proyecto.md
$ git status --short
?? docs/evidencias/
$ git apply --check /tmp/cambio.patch && echo "el parche se puede recuperar"
el parche se puede recuperar
```

Se decidió no recuperar la línea porque era accidental; el parche demuestra que el cambio no se pierde si se guarda antes del `restore`.

## CAP08 · Ramas

```console
$ git branch --merged main
  feature/filtro-productos
  feature/resumen-sedes
  fix/encabezado-tablero
* main
$ git log --oneline --graph -6
*   1eaeae1 Merge branch 'feature/filtro-productos'
|\  
| * 89a230b feat: filtrar productos por sede
|/  
* 38e3159 fix: corregir errata en el encabezado del tablero
* f5a811b feat: agregar reporte por sede con título del tablero
* e6112a1 docs: registrar diff, restore y parche (cap. 07)
* 398f65f test: agregar test_importe_calculado
$ git branch -d feature/resumen-sedes fix/encabezado-tablero feature/filtro-productos
$ git branch
* main
```

## CAP09 · Remotos: fetch frente a pull

El README se editó de forma remota en GitHub (commit `97ff3bd`). Luego, en local:

```console
$ git fetch origin
$ git status -sb   # fetch descarga pero NO cambia los archivos
## main...origin/main [behind 1]
$ git log --oneline main..origin/main
97ff3bd docs: agregar repositorio en GitHub al README (edición remota, cap. 09)
$ git pull --ff-only
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
$ git status -sb
## main...origin/main
```
