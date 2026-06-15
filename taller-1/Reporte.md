# REPORTE

##  Pregunta #1 - ¿Por qué el orden importa y no solo el tamaño?

El agente prioriza de arriba hacia abajo porque así hace la lectura del archivo. Si el archivo se encuentra organizado por importancia ayuda a evitar que el agente actúe con contexto incompleto o ambiguo.

##  Pregunta #2 - ¿Por qué generar output cuesta más que leer input?

El input se procesa de manera paralela, mientras que el output se genera de manera secuencial, token a token. Tener el archivo agents.md detallado es menos costoso.

## Pregunta #3 - El agente lleva 3 intentos fallidos. ¿Qué haces y por qué?

Sería revisar el historial para averiguar el motivo o razón de la falla, puede ser por que alguna instrucción es ambigua o se contradice líneas abajo, también puede ser porque no tiene el contexto necesario, etc. Es importante no volver a enviarlo lo mismo porque ahí nosotros estaríamos cometiendo un error sin sentido, lo que haría podría ser hacer más pequeña la instrucción o petición, dividirlo en tareas pequeñas y así también por partes se podrá ver en qué falla con más exactitud, esto es algo común que se suele hacer de manera cotidiana y creo que sería una buena manera de actuar.