## Resumen ejecutivo (≤150 palabras) ← §16.2
La suite de pruebas valida la gestión completa de Saberes Necesarios en el módulo Cursos: creación con imagen SVG obligatoria, edición de imagen, nombre, tema con regeneración automática del código, visualización responsive del SVG, filtros por curso,tema,estado y búsqueda por código o nombre. También cubre cambio de estado (activo/inactivo) y eliminación de saberes, siempre que no estén siendo utilizados en preguntas, en caso contrario, el sistema bloquea la acción y notifica al usuario. Se priorizan las validaciones críticas: formato y peso del SVG, unicidad del nombre por tema-curso, límite de 150 caracteres, control de acceso por rol y consistencia del código auto-generado. Quedan fuera la migración masiva, la edición del contenido SVG y la gestión de cursos y temas.

## Casos de Prueba (Test Cases)

### TC-1 (de AC-1.1, caso feliz): Visualización de la opción Saberes Necesarios
**Datos:** Usuario Administrador autenticado con permisos en el módulo Cursos.
**Pasos:** Navegar al módulo de Cursos y observar el menú lateral.
**Esperado:** La opción "Saberes Necesarios" aparece visible y seleccionable en el menú lateral del módulo Cursos.

### TC-2 (de AC-1.2, caso de error): Acceso denegado por falta de permisos
**Datos:** Usuario con rol "Docente" sin permisos asignados para Saberes Necesarios.
**Pasos:** Intentar acceder directamente a la URL de Saberes Necesarios.
**Esperado:** El sistema bloquea el acceso y muestra el mensaje: "No tiene permisos para acceder a esta funcionalidad."

### TC-3 (de AC-2.1, caso feliz): Apertura del modal de creación con todos los campos
**Datos:** Usuario Administrador en el listado de Saberes Necesarios.
**Pasos:** Hacer clic en el botón "Agregar saber necesario" en la parte superior derecha del listado.
**Esperado:** Se abre un modal que muestra: campo para cargar imagen SVG (con botón de selección de archivo), lista desplegable de Cursos, lista desplegable de Temas (filtrados por curso seleccionado), campo de texto para Nombre del saber, botones "Guardar" y "Cancelar".

### TC-4 (de AC-2.2, caso feliz): Registro exitoso con generación de código
**Datos:** Imagen: fracciones_propias.svg (válida, < 2 MB), Curso: Matemática (cod_curso: 03), Tema: Álgebra (cod_tema: 10), Nombre: "Fracciones propias".
**Pasos:** Completar todos los campos y hacer clic en "Guardar".
**Esperado:** El sistema registra el saber y genera un código automático con la estructura [cod_curso]-[cod_tema][correlativo] (ej. 03-100001). Aparece el mensaje: "Saber necesario creado correctamente. Código: 03-100001". El nuevo saber aparece en el listado con su código generado.

### TC-5 (de AC-2.3, caso de error): Botón Guardar deshabilitado por campos obligatorios vacíos
**Datos:** Modal abierto. Imagen: no cargada. Curso: sin seleccionar. Tema: sin seleccionar. Nombre: vacío.
**Pasos:** Intentar hacer clic en "Guardar" con todos los campos vacíos.
**Esperado:** El botón "Guardar" permanece deshabilitado (no se puede hacer clic).

### TC-6 (de AC-2.3, caso de error): Botón Guardar deshabilitado por falta de imagen
**Datos:** Modal abierto. Curso: Matemática. Tema: Álgebra. Nombre: "Fracciones propias". Imagen: no cargada.
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
