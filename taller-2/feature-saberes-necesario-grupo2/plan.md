## Resumen ejecutivo
Se implementará CRUD del recurso Saber necesario bajo la arquitectura hexagonal y estar relacionado al tema y curso, ya que un tema puede tener varios saberes.
Se debe guardar el nombre, tema, curso y nombre del archivo svg alojado en google cloud.
Al registrar y actualizar  validará la exitencia del curso y tema. Asi como si ese tema pertenece al curso indicado. Validará su unicidad medianto comparación normalizada del nombre original.
La consulta de listado será paginada y permitirá filtros opcionales por curso, tema, nombre, codigo y estado activo, inactivo o ambos. Considerará registros no eliminados. La lista debe retornar el codigo, nombre, nombre de curso, nombre de tema, fecha de creacion, estado y el id del saber, y el total de registros para calcular la cantidad de paginas.
La api para obtener un saber debe recibir el id y validar si existe y no está eliminado. Debe retornar el codigo, id del saber, nombre del curso, id del curso, nombre de tema, id de tema, nombre del saber, url de la imagen alojado en google cloud (link temporal)
Si al editar un saber, cambia de tema. Se debe regenerar un codigo nuevo y validarlo.
## 1. Enfoque técnico (alto nivel)
Base de datos:

Backend:
Implementación en arquitectura hexagonal con los estandares y flujos ya existentes del modulo Area, las apis agreement que ya maneja el flujo de carga y guardado de archivos. Establecer un path para google cloud de los saberes y guardar en la BD solo nombre del archivo cargado.
Routes -> Validator -> Controller -> Mapper -> UseCase -> Repository

Frontend:

## 2. Componentes / archivos afectados
Base de datos:

Backend: 
Dominio: 
    - StoreEssentialKnowledge, UpdateEssentialKnowledge, UpdateStateEssentialKnowledge, DeleteEssentialKnowledge
    - Value Objects relacionados si se cree necesario.
    - Reglas de validacion de dominio como la longitud maxima de caracteres
    - Contrato Repository
Aplication
    - CreateEssentialKnowledgeUsecase
    - UpdateEssentialKnowledgeUsecase
    - DeleteEssentialKnowledgeUseCase
    - GetEssentialKnowledgeUsecase
    - ListEssentialKnowledgeUsecase
    - Dtos de entrada y salida entre capas
    - Mappers
    - Validators de request
Infraestructura
    - Enrutamiento
    - Creacion de tablas
    - Controller
    - Implementación Repository
Testing
    - Tests unitarios de los entities y value objects.
    - Tests de integración de los usecases.

Frontend:

## 3. Decisiones de arquitectura (mini-ADR) ← §11 (ADRs)
DECISIÓN: El nombre del saber solo se validará en backend.
POR QUÉ: Para evitar error critico en la base de datos.
ALTERNATIVA DESCARTADA: Hacer unique el campo nombre en la tabla de la base de datos, para evitar errores criticos

DECISIÓN: Eliminación logica del saber necesario
POR QUÉ: Para mantener integridad de la informaciónm
ALTERNATIVA DESCARTADA: Hacer una eliminación fisica de los registros en la tabla. Porque dañaria la integridad de la información
## 4. Riesgos y dependencias
Saberes con el mismo nombre dentro de un mismo tema.
Error al momento de subir el archivo a google cloud.
## 5. Trazabilidad:
Crear un saber:
    Implementación: UseCase, Validator, Mappers, Dtos, Queries, Repository
Actualizar un saber:
    Implementación:  Usecase, Validator, Mappers, dto, queries, repository
Lista de saberes:
    Implementación: UseCase, Validator, Mappers, dto, queries paginados, repository
Eliminar Saber:
    - Implementación: UseCase, Validator, Mappers, Dtos, queries, repository
Consulta de un saber:
    Implementación: UseCase, Mappers, dto, queries, repository
Validar Saber:
    - Reglas de dominio y validaciones a nivel aplicación.