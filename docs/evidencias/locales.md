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
