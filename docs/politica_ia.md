# Política de uso de IA (capítulo 32)

## Reglas

1. **Declarar** todo código o texto generado con asistencia de IA (encabezado del archivo y descripción del PR).
2. **Prompt verificable**: el prompt queda escrito aquí, con criterios de aceptación que se pueden comprobar con pruebas.
3. **Auditar antes de integrar**: la persona responsable lee el código, busca casos límite y añade pruebas. La IA no fusiona ni aprueba.
4. **Nada sensible en el prompt**: ni datos personales, ni secretos, ni datos reales de clientes.
5. **Responsabilidad humana**: quien fusiona responde por el código, lo haya escrito o no una IA.

## Prompt verificable usado

> Escribe en Python 3, solo con la biblioteca estándar, una función `ticket_por_sede(resumen)` que reciba el diccionario de `generar_resumen()` (claves `total_por_sede` y `operaciones_por_sede`) y devuelva `{sede: total / operaciones}` redondeado a 2 decimales.
>
> Criterios de aceptación: con `data/ventas.csv` debe devolver Lima 203.50, Ica 138.75 y Arequipa 119.00.

## Auditoría

| Paso | Hallazgo |
|---|---|
| Primera propuesta de la IA | `resumen["operaciones_por_sede"][sede]` con acceso directo por clave |
| Caso límite probado | Una sede con total pero sin conteo de operaciones |
| Resultado | `KeyError: 'Cusco'` → **riesgo detectado** (también `ZeroDivisionError` con 0 operaciones) |
| Corrección | `operaciones.get(sede, 0)` y devolver `0.0` si no hay operaciones; `.get()` también para claves de primer nivel |
| Pruebas añadidas | `test_ticket_por_sede_con_datos_reales`, `test_sede_sin_conteo_no_lanza_keyerror`, `test_resumen_vacio` |

Versión auditada: [`src/ia_ticket.py`](../src/ia_ticket.py) · pruebas: [`tests/test_ia_ticket.py`](../tests/test_ia_ticket.py).

## Este repositorio

Gran parte de los archivos de este proyecto se redactaron con asistencia de Claude a partir del cuaderno de prácticas; cada commit lo indica con la línea `Co-Authored-By: Claude`.
