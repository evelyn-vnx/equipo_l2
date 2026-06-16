# SPEC — Gestión de Saberes Necesarios por Tema de Curso

**Versión:** 1.0  
**Fecha:** 2025-06-16  
**Roles involucrados:** Administrador, Didi  
**Estado:** En revisión

---

## Resumen ejecutivo

Se incorpora al módulo de Cursos la gestión completa de Saberes Necesarios (crear, editar, cambiar estado, eliminar), reemplazando la práctica actual de agregarlos dentro del solucionario de cada pregunta y eliminando la galería externa no controlada. Cada saber se identifica con un código único auto-generado `[cod_curso]-[cod_tema][correlativo]`, contiene una imagen SVG obligatoria y tiene nombre único dentro de su tema (hasta 150 caracteres). La imagen se previsualiza adaptándose a la resolución de pantalla del usuario. Preguntas abiertas: (1) ¿Quién define y mantiene el catálogo de temas disponibles? (2) ¿El correlativo se reinicia por tema o es global por curso?

---

## 1. Contexto de negocio (qué y por qué)

**Problema que resuelve:**  
Los docentes actualmente añaden Saberes Necesarios dentro del solucionario de cada pregunta, lo que genera duplicidad de contenido cuando el mismo saber aparece en múltiples preguntas. Como consecuencia, se comenzó a usar una galería externa a Odiseo que produce pérdida de trazabilidad, control de versiones y estandarización.

**Por qué ahora / a quién impacta:**  
La duplicidad activa encarece la creación de contenido (tiempo de carga, coherencia visual) y la galería externa ya existe como workaround, lo que significa que el problema está siendo absorbido por los usuarios. Impacta directamente a Administradores y usuarios Didi que crean y mantienen cursos.

---

## 2. User stories y criterios de aceptación

### US-1 (P1): Acceder a la sección de Saberes Necesarios
Como Administrador o Didi, quiero ver la opción "Saberes Necesarios" dentro del módulo de Cursos, para gestionar los saberes sin salir del sistema.

**AC-1.1** — Dado que el usuario tiene permisos de Administrador o Didi y accede al módulo de Cursos, cuando navega al menú lateral del módulo, entonces aparece la opción "Saberes Necesarios" visible y seleccionable.

**AC-1.2** — Dado que el usuario **no** tiene permisos de Administrador ni Didi, cuando intenta acceder a la ruta de Saberes Necesarios (directa o por menú), entonces el sistema bloquea el acceso y muestra el mensaje: _"No tiene permisos para acceder a esta funcionalidad."_

---

### US-2 (P1): Crear un saber necesario
Como Administrador o Didi, quiero crear un saber necesario con imagen SVG, curso, tema y nombre, para centralizar el contenido reutilizable del curso.

**AC-2.1** — Dado que el usuario está en la lista de Saberes Necesarios, cuando hace clic en "Agregar saber necesario", entonces se abre un modal con los campos: imagen SVG (carga de archivo), Curso, Tema y Nombre.

**AC-2.2** — Dado que el usuario completa todos los campos con datos válidos y hace clic en "Guardar", entonces el sistema registra el saber, genera un código con la estructura `[cod_curso]-[cod_tema][correlativo]` (ej. `03-100001`), y muestra el mensaje: _"Saber necesario creado correctamente. Código: {código generado}"_.

**AC-2.3** — Dado que el usuario intenta guardar sin haber cargado la imagen SVG, o sin seleccionar Curso o Tema, cuando el campo obligatorio está vacío, entonces el botón "Guardar" permanece deshabilitado (no se puede hacer clic).

**AC-2.4** — Dado que el usuario carga un archivo que no es SVG, cuando el sistema detecta el tipo de archivo al seleccionarlo, entonces bloquea la acción y muestra en un modal: _"El archivo debe estar en formato SVG."_

**AC-2.5** — Dado que el usuario ingresó datos en el modal y hace clic en "Cancelar", cuando el modal detecta al menos un campo con contenido, entonces muestra el modal de confirmación: _"¿Desea cancelar? Se perderán los datos ingresados."_

**AC-2.6** — Dado que el usuario intenta guardar un saber cuyo nombre ya existe en el mismo tema del mismo curso, cuando el sistema valida unicidad, entonces bloquea el guardado y muestra un mensaje de error indicando que el nombre ya está en uso en ese tema.

**AC-2.7** — Dado que el usuario ingresa un nombre de saber, cuando escribe más de 150 caracteres, entonces el campo no acepta más caracteres a partir del carácter 151 (truncamiento en input) **o** el sistema muestra un error de validación que impide guardar.

---

### US-3 (P1): Visualizar el listado de saberes necesarios
Como Administrador o Didi, quiero ver la lista de saberes con sus metadatos y aplicar filtros, para encontrar y gestionar rápidamente un saber específico.

**AC-3.1** — Dado que el usuario accede a la sección "Saberes Necesarios", cuando la pantalla carga, entonces se muestra una tabla paginada mostrando 10 registros por defecto, con las columnas: N.° (correlativo, incremental +1), Código, Curso `[código][nombre]`, Tema `[código][nombre]`, Nombre, Fecha Creación, Estado, Acciones (Ver, Editar y Eliminar). El filtro de Estado muestra por defecto "Activo".

**AC-3.2** — Dado que el usuario aplica un filtro por texto (código o nombre), cuando escribe al menos 1 carácter en el buscador, entonces la tabla muestra solo los saberes cuyo código o nombre contiene ese texto (búsqueda no sensible a mayúsculas).

**AC-3.3** — Dado que el usuario filtra por Curso, cuando selecciona un curso de la lista (restringida a los cursos asignados al usuario), entonces la tabla muestra únicamente los saberes pertenecientes a ese curso.

**AC-3.4** — Dado que el usuario filtra por Estado, cuando selecciona "Inactivo", entonces la tabla muestra solo los saberes con ese estado.

---

### US-4 (P1): Ver la imagen de un saber necesario
Como Administrador o Didi, quiero visualizar la imagen SVG de un saber en pantalla completa adaptada a mi resolución, para revisar su contenido sin distorsión.

**AC-4.1** — Dado que el usuario hace clic en la acción "Ver" de un saber, cuando el modal de visualización abre, entonces la imagen SVG se renderiza escalada para ocupar el ancho y alto disponibles del modal sin desbordarse, independientemente de la resolución de pantalla del usuario (responsive dentro del modal).

**AC-4.2** — Dado que la imagen SVG no se puede cargar, cuando el modal intenta renderizarla, entonces muestra el mensaje: _"No se pudo visualizar la imagen del saber necesario."_

---

### US-5 (P1): Editar un saber necesario
Como Administrador o Didi, quiero editar el tema, nombre e imagen SVG de un saber existente, para corregir errores o actualizarlo sin eliminarlo.

**AC-5.1** — Dado que el usuario hace clic en "Editar" sobre un saber, cuando el modal de edición abre, entonces los campos Tema, Nombre e Imagen SVG son editables; los demás datos son de solo lectura.

**AC-5.2** — Dado que el usuario cambia el Tema del saber y guarda, cuando el sistema procesa el cambio, entonces el código del saber se actualiza usando el código del nuevo tema y el correlativo correspondiente, y el código anterior queda reemplazado.

**AC-5.3** — Dado que el usuario guarda los cambios correctamente, cuando el sistema confirma la actualización, entonces muestra el mensaje: _"Saber necesario actualizado correctamente."_

**AC-5.4** — Dado que el usuario elimina la imagen actual sin reemplazarla y hace clic en "Guardar", cuando el sistema valida el campo, entonces bloquea la acción y muestra: _"Debe mantener o cargar una imagen válida en formato SVG."_

**AC-5.5** — Dado que el usuario cambia el nombre del saber por uno que ya existe en el mismo tema, cuando el sistema valida unicidad al guardar, entonces bloquea la acción y muestra un mensaje de error indicando duplicidad de nombre en ese tema.

---

### US-6 (P2): Cambiar el estado de un saber necesario
Como Administrador o Didi, quiero habilitar o inhabilitar un saber, para controlar su disponibilidad sin eliminarlo.

**AC-6.1** — Dado que el usuario hace clic en la acción de cambio de estado, cuando confirma la acción en el modal, entonces el estado del saber cambia entre "Habilitado" e "Inactivo" y se muestra el mensaje: _"El estado del saber necesario ha sido actualizado."_

---

### US-7 (P1): Eliminar un saber necesario
Como Administrador o Didi, quiero eliminar un saber que no esté en uso, para depurar el catálogo sin afectar el contenido activo.

**AC-7.1** — Dado que el usuario intenta eliminar un saber, cuando confirma la eliminación, entonces el saber se elimina de la base de datos y desaparece del listado.

---

### US-8 (P2): Visualizar el uso de un saber en preguntas
Como Administrador o Didi, quiero ver qué preguntas usan un saber específico, para evaluar el impacto antes de editarlo o inhabilitarlo.

**AC-8.1** — Dado que el usuario accede al listado de uso de un saber, cuando existen preguntas asociadas, entonces el sistema muestra la lista de preguntas vinculadas (al menos su identificador o título).

**AC-8.2** — Dado que el usuario accede al listado de uso de un saber, cuando **no** existen preguntas asociadas, entonces el sistema muestra: _"Este saber necesario no está siendo utilizado en ninguna pregunta."_

---

## 3. Requisitos no funcionales (NFR)

- **NFR-1 — Rendimiento:** La carga inicial del listado de Saberes Necesarios debe completarse en menos de 2 segundos.
- **NFR-2 — Formato de imagen:** Solo se aceptan archivos `.svg`. El sistema debe validar el tipo MIME (`image/svg+xml`) y la extensión en el lado servidor, no solo en el cliente.
- **NFR-3 — Unicidad del código:** El código generado `[cod_curso]-[cod_tema][correlativo]` debe ser único en la base de datos; la generación debe ser atómica para evitar colisiones en inserciones concurrentes.
- **NFR-4 — Longitud de nombre:** El campo Nombre del saber acepta un máximo de 150 caracteres. La validación debe ejecutarse tanto en el front-end (contador visible) como en el back-end.
- **NFR-5 — Control de acceso:** El acceso a la sección y todas sus operaciones deben verificarse por rol en el back-end; la validación solo en el front-end no es suficiente.
- **NFR-6 — Trazabilidad:** Cada creación, edición, cambio de estado y eliminación debe quedar registrada en el log de auditoría del sistema con usuario, timestamp y acción realizada.

---

## 4. Casos límite

- **Nombre en el límite exacto (150 caracteres):** El sistema debe guardar correctamente un nombre de exactamente 150 caracteres; el error solo aplica desde el carácter 151.
- **Nombre idéntico en distinto tema:** `"Fracciones propias"` en Tema A y `"Fracciones propias"` en Tema B del mismo curso son válidos y no deben generar conflicto.
- **Nombre idéntico en distinto curso:** Permitido sin restricción.
- **SVG malformado o con scripts embebidos:** El sistema debe rechazar SVGs con código malicioso.
- **Correlativo al llegar a 4 dígitos (9999):** Si el correlativo supera 4 dígitos, el sistema no debe permitir el registro o actualización del saber, y notificar al usuario con el mensaje "No se pudo guardar el saber.".
- **Carga simultánea del mismo nombre en el mismo tema:** Dos usuarios crean en paralelo el mismo nombre en el mismo tema; la restricción de unicidad debe resolverse a nivel de base de datos (constraint único), no solo de lógica de aplicación.
- **Imagen SVG de gran tamaño (> 5 MB):** Definir límite máximo de peso del archivo SVG aceptado; sin límite el servidor podría sobrecargarse.

---

## 5. Assumptions

- Asumimos que la lista de Cursos y Temas ya existe y es mantenida por otro módulo del sistema; si es falso, se requiere incorporar la gestión de temas en este mismo alcance.
- Asumimos que el correlativo del código es numérico, secuencial y con formato de 4 dígitos con ceros a la izquierda (ej. `0001`); si es falso, el formato del código puede diferir de los ejemplos documentados.
- Asumimos que "Didi" es un rol con los mismos permisos operativos que "Administrador" dentro de esta funcionalidad; si es falso, se deben especificar las restricciones diferenciales del rol Didi.
- Asumimos que los Cursos disponibles en el filtro están restringidos a los asignados al usuario autenticado; si es falso, usuarios con acceso amplio verán cursos que no les corresponden.
- Asumimos que la previsualización SVG se renderiza directamente en el navegador sin conversión intermedia a raster; si es falso, se requiere un servicio de conversión o sanitización adicional.

---

## 6. Aclaraciones (máx 3)

1. **Tamaño máximo del archivo SVG:** ¿Existe un límite de peso (en KB o MB) para los archivos SVG que se pueden cargar? Sin este límite definido no es posible implementar la validación de tamaño en front y back-end.

2. **Sanitización de SVG:** ¿El equipo de seguridad ya tiene un pipeline de sanitización para SVGs (eliminación de `<script>`, `<foreignObject>`, event handlers)? Si no, esto debe ser un NFR adicional antes de habilitar la carga de SVG en producción.

---

## 7. Scope

**DENTRO:**
- Nueva sección "Saberes Necesarios" dentro del módulo de Cursos.
- CRUD completo: Crear, leer (listado + detalle), editar (tema, nombre, imagen), cambiar estado (activo/inactivo), eliminar (solo si no está en uso).
- Generación automática de código único con estructura `[cod_curso]-[cod_tema][correlativo]`.
- Validación de unicidad de nombre a nivel de tema-curso.
- Límite de 150 caracteres en el nombre del saber.
- Carga y previsualización de imagen SVG adaptada al tamaño de pantalla del usuario.
- Actualización automática del código al cambiar de tema.
- Filtros por código/nombre, curso (restringido al usuario), tema y estado.
- Control de acceso por rol (Administrador y Didi).
- Mensajes de confirmación y error definidos en los criterios de aceptación.

**FUERA (explícito):**
- Gestión del catálogo de Cursos o Temas (son entidades preexistentes).
- Asociación directa saber-pregunta desde esta pantalla (solo visualización de uso).
- Migración automática de saberes actualmente en solucionarios de preguntas hacia la nueva galería.
- Exportación o importación masiva de saberes (bulk upload/download).
- Versionado o historial de cambios del saber (más allá del log de auditoría).
- Edición del contenido SVG dentro del sistema (el sistema solo almacena y muestra el archivo).