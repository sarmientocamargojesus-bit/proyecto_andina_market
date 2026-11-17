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
# Andina Market 360 · Ventas por sede
# Andina Market 360 · Tablero de ventas
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

## CAP31 · Scripts de API, reintentos y firma de webhook

```console
$ python scripts/api/leer_campos.py
Estados: {'closed': 7, 'open': 2}
Etiquetas: {'mejora': 5, 'bug': 1, 'documentación': 3}
Abiertos:
  #2 [Ventas] resumen.py falla si se ejecuta desde la carpeta src/
  #32 Documentar equivalencias de GitHub CLI y la web
$ python scripts/api/reintentos.py
Intento 1 falló (HTTP 503); reintento en 0.10 s
Intento 2 falló (HTTP 503); reintento en 0.20 s
Caso 1: {'status': 200, 'llamadas': 3}
Intento 1 falló (HTTP 503); reintento en 0.10 s
Intento 2 falló (HTTP 503); reintento en 0.20 s
Caso 2: Se agotaron los 3 intentos
$ python scripts/api/webhook_hmac.py
X-Hub-Signature-256: sha256=05e72b3e5a8be59a163c68b5d977ca40aa890d2a3bfb4b474a3433ec598cd773
Firma correcta      -> True
Cuerpo alterado     -> False
Sin cabecera        -> False
## CAP32 · Auditoría de la función asistida por IA

```console
$ python -c "from ia_v0 import ticket_por_sede; ticket_por_sede({\"total_por_sede\": {\"Cusco\": 100.0}, \"operaciones_por_sede\": {}})"
KeyError: 'Cusco'
$ python -m unittest discover -s tests
Ran 12 tests in 0.001s

OK
```

## CAP33 · Git avanzado (copia local de laboratorio, nada se publica)

### stash
```console
$ git stash push -m "nota a medias"
Saved working directory and index state On main: nota a medias
$ git stash list
stash@{0}: On main: nota a medias
$ git stash pop | tail -1
Dropped refs/stash@{0} (c9e68e91e81e4759fa814fdbd9f316d57db54c5c)
```

### bisect: localizar automáticamente el commit que rompe las pruebas
```console
$ git log --oneline -7
50d8bb3 docs: nota de laboratorio 5
3cdef9f docs: nota de laboratorio 4
15425a6 refactor: simplificar importe
6ca85d4 docs: nota de laboratorio 3
10b704a docs: nota de laboratorio 2
fcebb80 docs: nota de laboratorio 1
439db18 Merge pull request #35 from sarmientocamargojesus-bit/feature/api-codespaces
$ export PYTHONDONTWRITEBYTECODE=1   # sin esto, un .pyc en caché puede dar un falso "good" (ver nota)
$ git bisect start HEAD 439db18 | tail -1
[6ca85d47947338228ef2501affece70d2022535a] docs: nota de laboratorio 3
$ git bisect run python3 -m unittest discover -s tests 2>/dev/null | grep -A5 'is the first bad commit' | grep -v '^Date\|^Author\|^$'
15425a6c35b221407842f953b8b843c95677076f is the first bad commit
commit 15425a6c35b221407842f953b8b843c95677076f
    refactor: simplificar importe
$ git bisect reset 2>&1 | head -1
Previous HEAD position was 15425a6 refactor: simplificar importe
```

> **Nota:** en el primer intento `bisect` señaló un commit equivocado. `*` y `+` tienen el mismo tamaño y bisect cambia de commit en el mismo segundo, así que Python reutilizó el `.pyc` en caché (se invalida por fecha y tamaño). Con `PYTHONDONTWRITEBYTECODE=1` (o `python -B`) el resultado es correcto.

### revert del commit encontrado
```console
$ git revert --no-edit 15425a6 | head -1
[main 4a10e11] Revert "refactor: simplificar importe"
$ python3 -m unittest discover -s tests 2>&1 | tail -1
OK
```

### cherry-pick -x: llevar una corrección puntual a otra rama
```console
$ git cherry-pick -x 6bf94e9 | head -1
[main d9a89c4] docs: aclarar fórmula del importe
$ git log -1 --format=%B | grep 'cherry picked'
(cherry picked from commit 6bf94e922edf1f544e2a984c99a43c08ed558170)
```

### rebase -i (solo en esta copia local): unir las notas 1 a 3
```console
$ git log --oneline -9 | head -8
d9a89c4 docs: aclarar fórmula del importe
4a10e11 Revert "refactor: simplificar importe"
50d8bb3 docs: nota de laboratorio 5
3cdef9f docs: nota de laboratorio 4
15425a6 refactor: simplificar importe
6ca85d4 docs: nota de laboratorio 3
10b704a docs: nota de laboratorio 2
fcebb80 docs: nota de laboratorio 1
$ git rebase -i 439db18   # en el editor: "fixup" para las notas 2 y 3
$ git log --oneline -7
f33fdd7 docs: aclarar fórmula del importe
968d57d Revert "refactor: simplificar importe"
f452c97 docs: nota de laboratorio 5
f9c988a docs: nota de laboratorio 4
cc9314e refactor: simplificar importe
5333ec0 docs: nota de laboratorio 1
439db18 Merge pull request #35 from sarmientocamargojesus-bit/feature/api-codespaces
$ python3 -m unittest discover -s tests 2>&1 | tail -1
OK
```

El `rebase -i` reescribe commits: se usa **solo** en ramas locales que nadie más tiene. En `main` publicado está prohibido (regla *Block force pushes*).

### Hook `pre-commit` de pruebas
```console
$ cp scripts/hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
$ git commit -am "fix: cambio que rompe el importe"
pre-commit: las pruebas fallan; commit cancelado.
Ejecuta: python -m unittest discover -s tests -v
(código de salida: 1)
$ git commit -am "docs: nota válida"
pre-commit: pruebas OK
```
## CAP34 · Solución de problemas

### Bug #2: ejecutar desde `src/`
```console
$ cd src && python resumen.py   # antes
FileNotFoundError: [Errno 2] No such file or directory: 'data/ventas.csv'
$ cd src && python resumen.py   # después de usar Path(__file__)
Total      S/  1845.00
Ticket     S/   153.75
$ cd /tmp && python <repo>/src/resumen.py | tail -1
Ticket     S/   153.75
```

### Push rechazado → fetch + merge (sin `--force`)
```console
$ git push
 ! [rejected]        fix/ruta-resumen -> fix/ruta-resumen (fetch first)
hint: Updates were rejected because the remote contains work that you do not
$ git fetch origin && git merge --no-edit origin/fix/ruta-resumen
 1 file changed, 7 insertions(+)
 create mode 100644 bitacora_fallos.md
$ git push
   1cc3ac3..4fc8e94  fix/ruta-resumen -> fix/ruta-resumen
```

### HEAD *detached*
```console
$ git checkout HEAD~2
You are in 'detached HEAD' state. You can look around, make experimental
Turn off this advice by setting config variable advice.detachedHead to false
HEAD is now at 968d57d Revert "refactor: simplificar importe"
$ git status | head -1
HEAD detached at 968d57d
$ git commit -am "docs: commit hecho sin rama"   # queda "colgando"
$ git switch -c rescate   # se le da una rama antes de salir para no perderlo
Switched to a new branch 'rescate'
$ git log --oneline -1
a9cd92b docs: commit hecho sin rama
```

### Página desactualizada frente al JSON regenerado
```console
$ # con el precio alterado en data/ventas.csv (fila 1), se regenera el resumen
$ python src/resumen.py && git diff --stat docs/data/resumen.json
docs/data/resumen.json | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

El JSON que publica la página ya no coincide con los datos: si `git diff` muestra cambios, el sitio está desactualizado: se regenera el JSON, se hace commit y el workflow de Pages lo publica. Para que no vuelva a ocurrir, la CI ahora ejecuta `git diff --exit-code docs/data/resumen.json` después de generar el resumen.

### CI en rojo por un dato alterado
```console
$ git log --oneline -1 -- data/ventas.csv
3777bd7 data: actualizar precio de café en Lima
$ git diff HEAD~1 -- data/ventas.csv | grep "^[-+]1,"
-1,2026-03-02,Lima,Café orgánico,4,35.00
+1,2026-03-02,Lima,Café orgánico,4,3.50
# CI: Ran 12 tests … FAILED (failures=4) — ejecución 44169601119
$ git restore --source=origin/main -- data/ventas.csv
$ python -m unittest discover -s tests 2>&1 | tail -1
OK
```
