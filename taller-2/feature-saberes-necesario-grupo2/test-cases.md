## Resumen ejecutivo (≤150 palabras) ← §16.2
La suite de pruebas valida la gestión completa de Saberes Necesarios en el módulo Cursos: creación con imagen SVG obligatoria, edición de imagen, nombre, tema con regeneración automática del código, visualización responsive del SVG, filtros por curso,tema,estado y búsqueda por código o nombre. También cubre cambio de estado (activo/inactivo) y eliminación de saberes, siempre que no estén siendo utilizados en preguntas, en caso contrario, el sistema bloquea la acción y notifica al usuario. Se priorizan las validaciones críticas: formato y peso del SVG, unicidad del nombre por tema-curso, límite de 150 caracteres, control de acceso por rol y consistencia del código auto-generado. Quedan fuera la migración masiva, la edición del contenido SVG y la gestión de cursos y temas.

## Casos de Prueba (Test Cases)

### TC-1 (de AC-1.1, caso feliz): Visualización de la opción Saberes Necesarios
**Datos:** Usuario Administrador o Didi autenticado con permisos en el módulo Cursos.
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
**Datos:** Modal abierto. Curso: Álgebra. Tema: Fracciomes. Nombre: "Fracciones propias". Imagen: no cargada.
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

### TC-9 (de AC-2.5, caso feliz): Cancelación sin datos
**Datos:** Modal abierto. Ningún campo completado.
**Pasos:** Abrir el modal de creación. No ingresar ningún dato. Hacer clic en "Cancelar".
**Esperado:** El modal se cierra directamente, sin mostrar ningún mensaje de confirmación.

### TC-10 (de AC-2.5, caso feliz): Cancelación con datos ingresados
**Datos:** Modal abierto. Imagen: fracciones_propias.svg cargada. Nombre: "Fracciones propias" escrito en el campo.
**Pasos:** Ingresar datos en al menos un campo. Hacer clic en "Cancelar".
**Esperado:** El sistema muestra un modal de confirmación con el mensaje: "¿Desea cancelar? Se perderán los datos ingresados." con opciones "Sí" (cierra el modal y descarta datos) y "No" (regresa al formulario).

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
**Esperado:** La pantalla carga mostrando una tabla paginada con 10 registros por defecto, con las siguientes columnas: N.° (correlativo 1, 2, 3...), Código (ej. 03-100001), Curso (ej. [03] Álgebra), Tema (ej. [10] Fracciones), Nombre (ej. "Fracciones propias"), Fecha Creación (ej. 16/06/2025), Estado ("Activo" o "Inactivo"), Acciones (iconos: Ver, Editar y Eliminar).

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
