# Guía: publicar una versión (capítulos 18 y 36)

1. Comprueba que `CHANGELOG.md` en `main` tiene la sección de la versión (ej. `## [1.0.0]`).
2. GitHub → **Releases → Draft a new release**.
3. *Choose a tag* → escribe `v1.0.0` → **Create new tag: v1.0.0 on publish**. *Target*: `main`.
4. Título: `Andina Market 360 v1.0.0`. En la descripción pega la sección del CHANGELOG.
5. **Publish release**.
6. En la pestaña **Actions** se ejecuta el workflow *Release*: corre las pruebas y adjunta
   `proyecto_andina_market-v1.0.0.zip` (`git archive`), el `.bundle` verificado y `SHA256SUMS.txt`.

> Desde la web, GitHub crea un tag **ligero**. El tag **anotado** del cuaderno se crea desde tu equipo:
> `git tag -a v1.0.0 -m "Andina Market 360 v1.0.0" && git push origin v1.0.0` y luego se publica la Release eligiendo ese tag.
