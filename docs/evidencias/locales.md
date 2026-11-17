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

### Push rechazado y resuelto sin `--force`

Otro clon (`clon2`) subió un commit a la bitácora mientras aquí se trabajaba en las evidencias:

```console
$ git push origin main
 ! [rejected]        main -> main (fetch first)
hint: Updates were rejected because the remote contains work that you do not
$ git pull --no-rebase --no-edit   # fetch + merge, sin reescribir historial
 bitacora.md | 1 +
 1 file changed, 1 insertion(+)
$ git push origin main
   26438a3..f00c9e4  main -> main
```

## CAP10 · Conflicto, revert, stash y reflog

```console
$ git merge prueba/alternativa-a   # avance rápido
$ git merge prueba/alternativa-b
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
$ head -5 README.md
<<<<<<< HEAD
# Andina Market 360 · Tablero de ventas
=======
# Andina Market 360 · Ventas por sede
>>>>>>> prueba/alternativa-b
$ # se combinan ambas ideas en un solo título
$ head -1 README.md
# Andina Market 360 · Tablero de ventas por sede
Deleted branch prueba/alternativa-a (was 6cd6478).
Deleted branch prueba/alternativa-b (was 5246ad0).
$ git revert --no-edit HEAD   # Cusco no es una sede del caso
[main f68c89c] Revert "docs: agregar sede Cusco por error"
$ git stash push -m "idea gráfico"
Saved working directory and index state On main: idea gráfico
$ git stash list
stash@{0}: On main: idea gráfico
$ git stash drop   # la idea se registrará como Issue en el cap. 13
Dropped refs/stash@{0} (38815155132ee83b3734cc660c2c6e827c4b9510)
$ git reflog -6
f68c89c HEAD@{0}: reset: moving to HEAD
f68c89c HEAD@{1}: revert: Revert "docs: agregar sede Cusco por error"
1ff6eb4 HEAD@{2}: commit: docs: agregar sede Cusco por error
7f4b74a HEAD@{3}: commit (merge): docs: resolver conflicto de título entre alternativas A y B
6cd6478 HEAD@{4}: merge prueba/alternativa-a: Fast-forward
13f664d HEAD@{5}: checkout: moving from prueba/alternativa-b to main
```

## CAP19 · Prueba local del sitio en una subcarpeta (como GitHub Pages)

```console
$ python -m http.server  # sirviendo docs/ en /proyecto_andina_market/
$ node prueba_sitio.js   # Chromium headless (Playwright)
total: S/ 1845.00 | ticket: S/ 153.75 | Ica: S/ 555.00 | estado: ""
filas productos: 3
absoluta /data/resumen.json -> 404 | relativa data/resumen.json -> 200
$ python scripts/contraste.py
texto / fondo                14.76:1
texto suave / fondo           6.46:1
marca / fondo                 7.73:1
texto suave / tarjeta         5.93:1
texto / tarjeta              13.56:1
mensaje de error / fondo      8.15:1
Mínimo: 5.93:1 (requerido ≥ 4.5:1)
```

## CAP20 · Paquete verificado en una copia limpia

```console
$ git archive --format=zip -o dist/paquete.zip HEAD
$ unzip dist/paquete.zip -d /tmp/limpio && cd /tmp/limpio/proyecto_andina_market-main
$ ls -a | head
. .. .github .gitignore CHANGELOG.md CONTRIBUTING.md 
$ python -m unittest discover -s tests
Ran 6 tests in 0.000s

OK
$ python src/resumen.py | tail -2
Total      S/  1845.00
Ticket     S/   153.75
```
