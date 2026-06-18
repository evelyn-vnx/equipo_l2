## Resumen ejecutivo (≤150 palabras) ← §16.2
La suite de pruebas valida la gestión completa de Saberes Necesarios en el módulo Cursos: creación con imagen SVG obligatoria, edición de imagen, nombre, tema con regeneración automática del código, visualización responsive del SVG, filtros por curso,tema,estado y búsqueda por código o nombre. También cubre cambio de estado (activo/inactivo) y eliminación de saberes, siempre que no estén siendo utilizados en preguntas, en caso contrario, el sistema bloquea la acción y notifica al usuario. Se priorizan las validaciones críticas: formato y peso del SVG, unicidad del nombre por tema-curso, límite de 150 caracteres, control de acceso por rol y consistencia del código auto-generado. Quedan fuera la migración masiva, la edición del contenido SVG y la gestión de cursos y temas.

## Casos de Prueba (Test Cases)

### TC-1 (de AC-1.1, caso feliz): Visualización de la opción Saberes Necesarios
**Datos:** Usuario autenticado con permiso "Listar" sobre Saberes Necesarios (ej. Administrador o Didi).
**Pasos:** Navegar al módulo de Cursos y observar el menú lateral.
**Esperado:** La opción "Saberes Necesarios" aparece visible y seleccionable en el menú lateral del módulo Cursos.

### TC-2 (de AC-1.2, caso de error): Acceso denegado por falta de permisos
**Datos:** Usuario con rol "Docente" sin permisos asignados para Saberes Necesarios.
**Pasos:** Intentar acceder directamente al módulo de Saberes Necesarios.
**Esperado:** El sistema bloquea el acceso y muestra el mensaje: "No tiene permisos para acceder a esta funcionalidad."

### TC-3 (de AC-2.1, caso feliz): Apertura del modal de creación con todos los campos
**Datos:** Usuario Administrador o Didi en el listado de Saberes Necesarios.
**Pasos:** Hacer clic en el botón "Agregar saber necesario" en la parte superior derecha del listado.
**Esperado:** Se abre un modal que muestra: campo para cargar imagen SVG (con botón de selección de archivo), lista desplegable de Cursos, lista desplegable de Temas (filtrados por curso seleccionado), campo de texto para Nombre del saber, botones "Guardar" y "Cancelar".

### TC-4 (de AC-2.2, caso feliz): Registro exitoso con generación de código
**Datos:** Imagen: fracciones_propias.svg (válida, <=5 MB), Curso: Álgebra (cod_curso: 03), Tema: Fracciones (cod_tema: 10), Nombre: "Fracciones propias".
**Pasos:** Completar todos los campos y hacer clic en "Guardar".
**Esperado:** El sistema registra el saber y genera un código automático con la estructura [cod_curso]-[cod_tema][correlativo] (ej. 03-100001). Aparece el mensaje: "Saber necesario creado correctamente. Código: 03-100001". El nuevo saber aparece en el listado con su código generado.

### TC-5 (de AC-2.3, caso de error): Botón Guardar deshabilitado por campos obligatorios vacíos
**Datos:** Modal abierto. Imagen: no cargada. Curso: sin seleccionar. Tema: sin seleccionar. Nombre: vacío.
**Pasos:** Intentar hacer clic en "Guardar" con todos los campos vacíos.
**Esperado:** El botón "Guardar" permanece deshabilitado (no se puede hacer clic).

### TC-6 (de AC-2.3, caso de error): Botón Guardar deshabilitado por falta de imagen
**Datos:** Modal abierto. Curso: Álgebra. Tema: Fracciones. Nombre: "Fracciones propias". Imagen: no cargada.
**Pasos:** Completar Curso, Tema y Nombre. No cargar ninguna imagen. Intentar hacer clic en "Guardar".
**Esperado:** El botón "Guardar" permanece deshabilitado (no se puede hacer clic).

### TC-7 (de AC-2.3, caso de error): Botón Guardar deshabilitado por falta de curso o tema
**Datos:** Modal abierto. Imagen: fracciones_propias.svg cargada. Curso: sin seleccionar. Tema: sin seleccionar. Nombre: "Fracciones propias".
**Pasos:** Cargar la imagen y escribir el nombre. No seleccionar Curso ni Tema. Intentar hacer clic en "Guardar".
**Esperado:** El botón "Guardar" permanece deshabilitado (no se puede hacer clic).

### TC-8 (de AC-2.4, caso de error): Rechazo de archivo no SVG
**Datos:** Modal abierto. Archivo: diagrama.png (formato PNG).
**Pasos:** Intentar cargar un archivo con extensión .png.
**Esperado:** El sistema bloquea la acción inmediatamente y muestra en un modal: "El archivo debe estar en formato SVG."

### TC-9 (de AC-2.5, caso borde): Cancelación sin datos — cierre directo
**Datos:** Modal abierto. Ningún campo completado.
**Pasos:** Abrir el modal de creación. No ingresar ningún dato. Hacer clic en "Cancelar".
**Esperado:** El modal se cierra directamente, sin mostrar ningún mensaje de confirmación.

### TC-10 (de AC-2.5, caso feliz): Cancelación con datos ingresados
**Datos:** Modal abierto. Imagen: fracciones_propias.svg cargada. Nombre: "Fracciones propias" escrito en el campo.
**Pasos:** Ingresar datos en al menos un campo. Hacer clic en "Cancelar".
**Esperado:** El sistema muestra un modal de confirmación con el mensaje: "¿Desea cancelar? Se perderán los datos ingresados." con opciones "Sí, cancelar" (cierra el modal de creación y descarta todos los datos) y "No, continuar" (cierra el modal de confirmación y regresa al formulario con los datos intactos).

### TC-11 (de AC-2.6, caso de error): Nombre duplicado en mismo tema y curso
**Datos:** Saber existente: curso álgebra (03), tema Fracciones (10), nombre "Fracciones propias". Intento de crear: curso Álgebra (03), tema Fracciones (10), nombre "Fracciones propias".
**Pasos:** Completar el formulario con el mismo nombre que un saber existente en ese tema y curso. Hacer clic en "Guardar".
**Esperado:** El sistema bloquea el guardado y muestra un mensaje de error: "El nombre ya existe en este tema. Por favor, elige otro nombre."

### TC-12 (de AC-2.7, caso borde): Nombre de exactamente 150 caracteres
**Datos:** Nombre: texto de exactamente 150 caracteres.
**Pasos:** Escribir un nombre de exactamente 150 caracteres en el campo. Hacer clic en "Guardar".
**Esperado:** El sistema acepta y guarda el saber correctamente con el nombre completo de 150 caracteres.

### TC-13 (de AC-2.7, caso borde): Nombre superior a 150 caracteres
**Datos:** Nombre: texto de 151 caracteres.
**Pasos:** Intentar escribir o pegar un nombre de 151 caracteres en el campo.
**Esperado:** El campo no acepta más de 150 caracteres (el input trunca en el carácter 150) o el sistema muestra un mensaje de validación: "El nombre no puede exceder los 150 caracteres." y bloquea el guardado.

### TC-14 (de AC-3.1, caso feliz): Visualización de la tabla con todas las columnas
**Datos:** Usuario accede a la sección Saberes Necesarios con al menos 10 saberes registrados.
**Pasos:** Navegar a la sección Saberes Necesarios.
**Esperado:** La pantalla carga en menos de 2 segundos (NFR-1) mostrando una tabla paginada con 10 registros por defecto, ordenados por Fecha Creación del más reciente al más antiguo, con las siguientes columnas: N.° (correlativo 1, 2, 3...), Código (ej. 03-100001), Curso (ej. [03] Álgebra), Tema (ej. [10] Fracciones), Nombre (ej. "Fracciones propias"), Fecha Creación (ej. 16/06/2025), Estado ("Activo" o "Inactivo"), Acciones (iconos: Ver, Editar y Eliminar).

### TC-15 (de AC-3.2, caso feliz): Búsqueda por código
**Datos:** Listado con saberes que incluye uno con código 03-100001.
**Pasos:** Escribir 03-100001 en el campo de búsqueda.
**Esperado:** La tabla muestra únicamente el saber con código 03-100001.

### TC-16 (de AC-3.2, caso feliz): Búsqueda por nombre parcial
**Datos:** Listado con saberes que incluye "Fracciones propias" y "Fracciones impropias".
**Pasos:** Escribir fracciones en el campo de búsqueda.
**Esperado:** La tabla muestra ambos saberes: "Fracciones propias" y "Fracciones impropias" (búsqueda no sensible a mayúsculas).

### TC-17 (de AC-3.2, caso borde): Búsqueda con un solo carácter
**Datos:** Listado con varios saberes.
**Pasos:** Escribir a en el campo de búsqueda.
**Esperado:** La tabla muestra todos los saberes cuyo código o nombre contenga la letra "a" (en cualquier posición).

### TC-18 (de AC-3.3, caso feliz): Filtro por curso asignado al usuario
**Datos:** Usuario con cursos Álgebra (03) y Lengua (05) asignados.
**Pasos:** Abrir el filtro de Curso. Seleccionar "Álgebra (03)".
**Esperado:** La lista desplegable muestra solo los cursos Álgebra (03) y Lengua (05). Al seleccionar Álgebra, la tabla muestra únicamente los saberes pertenecientes al curso Álgebra.

### TC-19 (de AC-3.4, caso feliz): Filtro por estado Inactivo
**Datos:** Listado con saberes en estado "Activo" e "Inactivo".
**Pasos:** Abrir el filtro de Estado (que muestra "Activo" por defecto). Seleccionar "Inactivo".
**Esperado:** La tabla muestra únicamente los saberes con estado "Inactivo".

### TC-20 (de AC-4.1, caso feliz): Visualización de imagen SVG en modal
**Datos:** Saber existente con imagen SVG válida.
**Pasos:** Localizar un saber en el listado. Hacer clic en el ícono de "Ver".
**Esperado:** Se abre un modal que muestra la imagen SVG renderizada, escalada para ocupar el ancho y alto disponibles del modal sin desbordarse, adaptándose a la resolución de pantalla del usuario.

### TC-21 (de AC-4.2, caso de error): Error al visualizar imagen SVG
**Datos:** Saber existente con imagen SVG corrupta o no accesible.
**Pasos:** Hacer clic en "Ver" sobre el saber con la imagen dañada.
**Esperado:** El sistema muestra el mensaje: "No se pudo visualizar la imagen del saber necesario."

### TC-22 (de AC-5.1, caso feliz): Apertura del modal de edición
**Datos:** Saber existente en el listado.
**Pasos:** Localizar un saber en el listado. Hacer clic en el ícono de "Editar".
**Esperado:** Se abre un modal de edición mostrando: Campo Curso (solo lectura, no editable), Campo Tema (editable, lista desplegable), Campo Nombre (editable), Imagen SVG actual previsualizada con opción para reemplazar, Botones "Guardar" y "Cancelar".

### TC-23 (de AC-5.2, caso feliz): Actualización automática de código al cambiar tema
**Datos:** Saber existente: código 03-100001, tema Fracciones (cod_tema: 10). Cambio a tema Exponentes (cod_tema: 15).
**Pasos:** Editar el saber y cambiar el tema de "Fracciones" a "Exponentes". Hacer clic en "Guardar".
**Esperado:** El sistema actualiza el código del saber a 03-150001 (manteniendo el mismo correlativo) y el código anterior queda reemplazado. El mensaje de confirmación muestra el nuevo código actualizado.

### TC-24 (de AC-5.3, caso feliz): Confirmación de edición exitosa
**Datos:** Saber existente, cambios válidos realizados (tema, nombre o imagen).
**Pasos:** Realizar cambios válidos en el modal de edición. Hacer clic en "Guardar".
**Esperado:** El sistema actualiza el registro y muestra el mensaje: "Saber necesario actualizado correctamente."

### TC-25 (de AC-5.4, caso de error): Eliminación de imagen sin reemplazo en edición
**Datos:** Saber existente en modo edición con imagen actual cargada.
**Pasos:** Eliminar la imagen actual (sin cargar una nueva). Hacer clic en "Guardar".
**Esperado:** El sistema bloquea la acción y muestra el mensaje: "Debe mantener o cargar una imagen válida en formato SVG."

### TC-26 (de AC-5.5, caso de error): Nombre duplicado en edición dentro del mismo tema
**Datos:** Saber editado: "Fracciones propias" (tema Fracciones). Otro saber existente en el mismo tema con nombre "Fracciones propias".
**Pasos:** Editar el nombre y cambiarlo a "Fracciones propias" (coincidiendo con otro saber existente en el tema). Hacer clic en "Guardar".
**Esperado:** El sistema bloquea la acción y muestra un mensaje de error: "El nombre ya existe en este tema. Por favor, elige otro nombre."

### TC-27 (de AC-6.1, caso feliz): Cambio de estado Activo a Inactivo
**Datos:** Saber existente con estado "Activo".
**Pasos:** Hacer clic en el botón de cambio de estado del saber. Confirmar la acción en el modal.
**Esperado:** El estado cambia de "Activo" a "Inactivo". Se muestra el mensaje: "El estado del saber necesario ha sido actualizado." y en la tabla refleja el nuevo estado.

### TC-28 (de AC-7.1, caso feliz): Eliminación de saber no utilizado
**Datos:** Saber existente que no está asociado a ninguna pregunta.
**Pasos:** Hacer clic en el ícono de "Eliminar" sobre el saber. Confirmar la eliminación en el modal de confirmación.
**Esperado:** El saber se elimina de la base de datos y desaparece del listado.

### TC-29 (caso borde): Correlativo de código al llegar a 9999
**Datos:** Intento de crear un nuevo saber cuando el correlativo actual del tema ya está en 9999.
**Pasos:** Intentar crear un nuevo saber en un tema cuyo correlativo ha alcanzado 9999. Hacer clic en "Guardar".
**Esperado:** El sistema no permite el registro y muestra el mensaje: "No se pudo guardar el saber." (el límite de correlativos ha sido alcanzado).

### TC-30 (caso borde): SVG malicioso con scripts embebidos
**Datos:** Archivo SVG que contiene código `<script>alert('xss')</script>` embebido en el markup.
**Pasos:** Intentar cargar el SVG malicioso en el modal de creación de un saber.
**Esperado:** El sistema sanitiza el SVG, eliminando los elementos `<script>` y cualquier event handler (`onload`, `onclick`, etc.) antes de almacenarlo. La imagen se guarda sin código ejecutable. El SVG malicioso no se rechaza sino que se limpia (NFR-7).

### TC-31 (de AC-2.8, caso de error): Imagen SVG de gran tamaño (> 5 MB)
**Datos:** Archivo SVG de 6 MB.
**Pasos:** Intentar cargar un SVG superior a 5 MB en el modal de creación o edición.
**Esperado:** El sistema bloquea la carga y muestra el mensaje: "El archivo SVG supera el límite de 5 MB. Por favor, comprima la imagen o use un archivo de menor tamaño."

### TC-32 (caso feliz): Filtro de Cursos restringido al usuario
**Datos:** Usuario con 2 cursos asignados.
**Pasos:** Abrir el filtro de Cursos en el listado.
**Esperado:** El filtro muestra solo los 2 cursos asignados al usuario autenticado. El usuario no puede ver ni seleccionar cursos que no le pertenecen.

### TC-33 (caso feliz): Filtro de Temas dinámico por curso seleccionado
**Datos:** Curso Álgebra con temas: Fracciones, Exponentes, Logaritmos. Curso Lengua con temas: Gramática, Redacción.
**Pasos:** Seleccionar "Álgebra" en el filtro de Cursos.
**Esperado:** El filtro de Temas muestra solo: Fracciones, Exponentes, Logaritmos. Los temas de Lengua no aparecen.

### TC-34 (caso feliz): Estado filtro por defecto "Activo"
**Datos:** Usuario accede a la sección Saberes Necesarios.
**Pasos:** Ingresar a la sección.
**Esperado:** El filtro de Estado muestra por defecto "Activo" y la tabla carga mostrando solo los saberes con estado "Activo".

### TC-35 (de AC-3.2, caso feliz): Limpieza del campo de búsqueda
**Datos:** Listado filtrado por una búsqueda activa (ej. "fracciones").
**Pasos:** Borrar completamente el texto del campo de búsqueda.
**Esperado:** La tabla muestra todos los saberes disponibles, aplicando el filtro de Estado por defecto ("Activo") y el ordenamiento por defecto por Fecha Creación del más reciente al más antiguo.

### TC-36 (de AC-3.3, caso feliz): Filtro de Curso — opción "Todos"
**Datos:** Usuario con cursos Álgebra (03) y Lengua (05) asignados. Saberes existentes en ambos cursos.
**Pasos:** Abrir el filtro de Curso y seleccionar "Todos".
**Esperado:** La tabla muestra los saberes de todos los cursos asignados al usuario, aplicando el filtro de Estado por defecto ("Activo") y el ordenamiento por defecto por Fecha Creación del más reciente al más antiguo.

### TC-37 (de AC-3.4, caso feliz): Filtro de Estado — opción "Todos"
**Datos:** Listado con saberes en estado "Activo" e "Inactivo".
**Pasos:** Abrir el filtro de Estado y seleccionar "Todos".
**Esperado:** La tabla aplica el filtro por defecto de Estado "Activo" (no muestra todos), ordenados por Fecha Creación del más reciente al más antiguo.

### TC-38 (de AC-3.5, caso feliz): Limpiar todos los filtros
**Datos:** Listado con múltiples filtros aplicados (búsqueda por nombre, curso seleccionado, estado "Inactivo").
**Pasos:** Hacer clic en el botón "Limpiar filtro" o "Ver todos".
**Esperado:** La tabla muestra todos los saberes disponibles con el filtro de Estado por defecto "Activo" y ordenados por Fecha Creación del más reciente al más antiguo, independientemente de los filtros previamente aplicados.

### TC-39 (de AC-6.1, caso feliz): Cambio de estado Inactivo a Activo
**Datos:** Saber existente con estado "Inactivo".
**Pasos:** Hacer clic en el botón de cambio de estado del saber. Confirmar la acción en el modal de confirmación.
**Esperado:** El estado cambia de "Inactivo" a "Activo". Se muestra el mensaje: "El estado del saber necesario ha sido actualizado." y en la tabla refleja el nuevo estado.

### TC-40 (de AC-7.1, caso de error): Eliminación bloqueada por saber en uso
**Datos:** Saber existente que está asociado a una o más preguntas activas.
**Pasos:** Hacer clic en el ícono de "Eliminar" sobre el saber. Confirmar la eliminación en el modal de confirmación.
**Esperado:** El sistema bloquea la eliminación y muestra un mensaje de error: "No se puede eliminar el saber porque está siendo utilizado en preguntas." El saber permanece en el listado.

### TC-41 (caso borde): Nombre idéntico en distinto tema del mismo curso
**Datos:** Saber existente: curso Álgebra (03), tema Fracciones (10), nombre "Fracciones propias". Nuevo intento: curso Álgebra (03), tema Exponentes (15), nombre "Fracciones propias".
**Pasos:** Crear un nuevo saber con el mismo nombre pero en un tema diferente del mismo curso.
**Esperado:** El sistema permite la creación sin conflicto de unicidad. Ambos saberes coexisten con el mismo nombre en temas distintos.

### TC-42 (caso borde): Nombre idéntico en distinto curso
**Datos:** Saber existente: curso Álgebra (03), tema Fracciones (10), nombre "Fracciones propias". Nuevo intento: curso Lengua (05), tema Gramática (01), nombre "Fracciones propias".
**Pasos:** Crear un nuevo saber con el mismo nombre en un curso diferente.
**Esperado:** El sistema permite la creación sin conflicto de unicidad. Ambos saberes coexisten con el mismo nombre en cursos distintos.

### TC-43 (caso borde): Carga simultánea del mismo nombre en el mismo tema
**Datos:** Dos usuarios (A y B) intentan crear simultáneamente un saber con curso Álgebra (03), tema Fracciones (10), nombre "Fracciones propias".
**Pasos:** Ambos usuarios completan el formulario y hacen clic en "Guardar" al mismo tiempo.
**Esperado:** Solo una de las dos operaciones tiene éxito. La segunda operación es rechazada a nivel de base de datos (restricción de unicidad) y el sistema muestra un mensaje de error indicando que el nombre ya existe en ese tema.