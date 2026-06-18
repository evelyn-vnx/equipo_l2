## Resumen ejecutivo

Creación del módulo **Saber Necesario** desde cero bajo arquitectura hexagonal DDD en `src/` (backend) y feature module en frontend. Cada saber tiene código auto-generado `[cod_curso]-[cod_tema][correlativo]` (4 dígitos), nombre único por tema-curso (≤150 chars), imagen SVG obligatoria en Google Cloud Storage, y soporta eliminación lógica con estado activo/inactivo. El plan cubre BD (tablas + funciones + permisos), backend (Domain → Application → Infrastructure), frontend (módulo, páginas, diálogos, navegación) y tests (unitarios + integración).

## 1. Enfoque técnico (alto nivel)

- **Base de datos**: Crear tabla `essential_knowledges` con `id` bigint auto-increment, campos `code`, `name` (varchar 150), `course_id` (FK), `topic_id` (FK), `svg_filename` (GCS), `is_active` (boolean), `created_by`, `deleted_at`. Partial unique index `idx_unique_active_course_topic_name` on `(course_id, topic_id, name)` WHERE `deleted_at IS NULL`. Crear funciones de BD `fn_create_essential_knowledge`, `fn_update_essential_knowledge`, `fn_list_essential_knowledge`, `fn_get_essential_knowledge_by_id`. Migración de permisos (`essential_knowledge.listar`, `.crear`, `.actualizar`, `.actualizar_estado`, `.eliminar`) con asignación automática al rol `Super Administrador` de company 1 (Odiseo) vía `Role::SUPER_ADMINISTRADOR` y al rol homólogo de company 2 (Academia Vonex) mediante búsqueda por nombre + `company_id`.
- **Backend**: Módulo DDD completo en `src/App/Modules/V2/Catalog/EssentialKnowledge/` siguiendo la misma estructura del módulo `Area` (constitution §2). Capas: Domain (entidades, repositorios CQS), Application (use cases, DTOs inmutables), Infrastructure (controller, mappers, validators, routes, query builders, providers). Flujo: `Validator → Mapper → Controller → UseCase → Repository`. SVG se sube a GCS mediante `FileStorageInterface` (path `/essential-knowledge/{uuid}.svg`), en BD solo el filename. Código generado en `StoreEssentialKnowledgeUseCase` consultando último correlativo por (course_id, topic_id). Toda operación protegida con middleware `auth:sanctum` y permiso específico según la acción (constitution §2.10, §5). Use case `TransactionalUseCase` para operaciones atómicas (constitution §2.7).
- **Frontend**: Feature module en `src/modules/essential-knowledge/` con página de listado paginado (10 registros), filtros por código/nombre/curso/tema/estado. Diálogos: creación, edición, visualización SVG (responsive), cambio de estado, eliminación. Validación client-side de SVG (MIME `image/svg+xml`, tamaño ≤5 MB). Navegación lateral en módulo Cursos, protegida por CASL (constitution §2.10). Comunicación vía Axios con servicio dedicado.

## 2. Componentes / archivos afectados

### Base de datos — `odiseo-backend/database/migrations/`

**Migraciones de tabla a crear:**
- `database/migrations/tables/table_essential_knowledges/2026_XX_XX_XXXXXX_create_table_essential_knowledges.php` — tabla principal con campos: `id` (bigint, auto-increment), `code` (varchar 20 unique), `name` (varchar 150), `course_id` (FK → courses), `topic_id` (FK → topics), `svg_filename` (varchar 255 nullable), `is_active` (boolean default true), `created_by` (FK → users), `created_at`, `updated_at`, `deleted_at`. Partial unique index `idx_unique_active_course_topic_name` on `(course_id, topic_id, name)` WHERE `deleted_at IS NULL`.
- `database/migrations/tables/table_role_permissions/2026_XX_XX_XXXXXX_add_permissions_essential_knowledges.php` — insertar permisos: `essential_knowledge.listar`, `essential_knowledge.crear`, `essential_knowledge.actualizar`, `essential_knowledge.actualizar_estado`, `essential_knowledge.eliminar`. Asignar a roles Admin y Didi. **Además**, asignar automáticamente al rol `Super Administrador` de company 1 (Odiseo) mediante `Role::SUPER_ADMINISTRADOR->value` y al rol homólogo de company 2 (Academia Vonex) buscando por `name = 'Super Administrador'` y `company_id` obtenido dinámicamente de la tabla `companies`.

**Funciones de BD a crear:**
- `database/migrations/functions/fn_create_essential_knowledge/` — `fn_create_essential_knowledge(p_code, p_name, p_course_id, p_topic_id, p_svg_filename, p_created_by)` → inserta y retorna el registro.
- `database/migrations/functions/fn_update_essential_knowledge/` — `fn_update_essential_knowledge(p_id, p_name, p_topic_id, p_svg_filename, p_updated_by)` → actualiza y retorna el registro. Si cambia topic_id, recibe nuevo p_code.
- `database/migrations/functions/fn_list_essential_knowledge/` — `fn_list_essential_knowledge(p_search DEFAULT NULL, p_course_id DEFAULT NULL, p_topic_id DEFAULT NULL, p_status DEFAULT NULL, p_page DEFAULT 1, p_per_page DEFAULT 10)` → retorna paginado con total. Todos los filtros son opcionales.
- `database/migrations/functions/fn_get_essential_knowledge_by_id/` — `fn_get_essential_knowledge_by_id(p_id)` → retorna registro completo incluyendo curso y tema.

### Backend — `odiseo-backend/src/App/Modules/V2/Catalog/EssentialKnowledge/`

Toda la estructura es **nueva** (crear desde cero). Siguiente el patrón del módulo `Area`:

**Domain:**
- `Domain/Entities/StoreEssentialKnowledgeEntity.php` — `code`, `name`, `courseId`, `topicId`, `svgFilename`, `createdBy`
- `Domain/Entities/UpdateEssentialKnowledgeEntity.php` — `id`, `name`, `topicId`, `svgFilename`, `updatedBy`, `?newCode`
- `Domain/Entities/UpdateIsActiveEssentialKnowledgeEntity.php` — `id`, `isActive`, `updatedBy`
- `Domain/Entities/DeleteEssentialKnowledgeEntity.php` — `id`, `deletedBy`
- `Domain/Entities/GetEssentialKnowledgeByIdEntity.php` — retorno con datos + url temporal GCS
- `Domain/Entities/ListEssentialKnowledgeEntity.php` — representación para listado
- `Domain/Entities/Rules/BaseEssentialKnowledgeEntity.php` — validaciones compartidas (nombre ≤150 chars, código formato)
- `Domain/Dtos/ListEssentialKnowledgeDomainDto.php` — DTO de consulta para listado paginado
- `Domain/Repositories/Read/EssentialKnowledgeReadRepositoryInterface.php` — métodos: `getAll(ListDto): DataTableEntity`, `getById(int): ?Entity`, `getLastCodeByCourseAndTopic(int, int): ?string`, `existsByNameInTopic(string, int, int, ?int): bool`
- `Domain/Repositories/Write/EssentialKnowledgeWriteRepositoryInterface.php` — métodos: `store(StoreEntity): StoreEntity`, `update(UpdateEntity): bool`, `updateIsActive(UpdateIsActiveEntity): bool`, `delete(DeleteEntity): bool`, `updateCode(int, string): bool`

**Application:**
- `Application/Dtos/Requests/StoreEssentialKnowledgeRequestDto.php` — datos de creación (inmutable)
- `Application/Dtos/Requests/UpdateEssentialKnowledgeRequestDto.php` — datos de actualización
- `Application/Dtos/Requests/UpdateIsActiveEssentialKnowledgeRequestDto.php` — datos cambio estado
- `Application/Dtos/Requests/DeleteEssentialKnowledgeRequestDto.php` — id del saber
- `Application/Dtos/Requests/GetByIdEssentialKnowledgeRequestDto.php` — id del saber
- `Application/Dtos/Requests/FilterEssentialKnowledgeRequestDto.php` — parámetros de filtro opcionales (search, course_id, topic_id, status, page, per_page)
- `Application/Dtos/Requests/UploadSvgEssentialKnowledgeRequestDto.php` — datos para subida SVG
- `Application/UseCases/StoreEssentialKnowledgeUseCase.php` — genera código, valida unicidad, persiste (constitution §2.3, §2.7)
- `Application/UseCases/UpdateEssentialKnowledgeUseCase.php` — si cambia topic_id, regenera código, valida unicidad
- `Application/UseCases/UpdateIsActiveEssentialKnowledgeUseCase.php` — cambia is_active
- `Application/UseCases/DeleteEssentialKnowledgeUseCase.php` — soft delete
- `Application/UseCases/GetByIdEssentialKnowledgeUseCase.php` — obtiene + genera URL firmada GCS
- `Application/UseCases/FilterEssentialKnowledgeUseCase.php` — listado paginado con filtros
- `Application/UseCases/UploadSvgEssentialKnowledgeUseCase.php` — sube SVG a GCS, guarda filename

**Infrastructure:**
- `Infrastructure/Http/Controllers/EssentialKnowledgeController.php` — 7 métodos: `index`, `store`, `show`, `update`, `updateIsActive`, `delete`, `uploadSvg`. Patrón: `try/catch` → mapper → use case → response (constitution §2.4)
- `Infrastructure/Http/Validators/` — 7 validators (uno por acción), extienden `FormRequest`, reglas de validación según spec, lanzan `OdiseoValidatorException`
- `Infrastructure/Http/Mappers/` — 7 mappers (uno por acción), método `fromRequest(Validator): RequestDto`
- `Infrastructure/Http/Responses/ListEssentialKnowledgeResponse.php` — formatea respuesta paginada
- `Infrastructure/Http/Responses/GetByIdEssentialKnowledgeResponse.php` — respuesta con URL firmada
- `Infrastructure/Http/Routes/RoutesEssentialKnowledge.php` — 7 rutas REST con middleware `auth:sanctum` y permiso específico: `index` → `essential_knowledge.listar`, `store` → `essential_knowledge.crear`, `show` → `essential_knowledge.listar`, `update` → `essential_knowledge.actualizar`, `updateIsActive` → `essential_knowledge.actualizar_estado`, `delete` → `essential_knowledge.eliminar`, `uploadSvg` → `essential_knowledge.crear`
- `Infrastructure/Http/Routes/index.php` — require de RoutesEssentialKnowledge
- `Infrastructure/Persistences/QueryBuilder/Read/EssentialKnowledgeReadQueryBuilder.php` — implementa read repository (usa `CallerBuilder` para funciones BD y `ConnectionBuilder::read()`)
- `Infrastructure/Persistences/QueryBuilder/Write/EssentialKnowledgeWriteQueryBuilder.php` — implementa write repository (usa `CallerBuilder` para funciones BD y `ConnectionBuilder::write()`)
- `Infrastructure/Providers/EssentialKnowledgeProvider.php` — bindea interfaces a implementaciones via `$this->app->singleton()`
- `Infrastructure/Providers/index.php` — retorna `[EssentialKnowledgeProvider::class]`

**Tests (crear toda la carpeta):**
- `tests/Context/Admin/Catalog/EssentialKnowledge/Builders/` — payload builders y entity builders
- `tests/Context/Admin/Catalog/EssentialKnowledge/Unit/Domain/` — tests de entidades y value objects
- `tests/Context/Admin/Catalog/EssentialKnowledge/Unit/Application/` — tests de use cases (mockeando repositorios)
- `tests/Context/Admin/Catalog/EssentialKnowledge/Feature/Http/` — tests de integración de cada endpoint

### Frontend — `odiseo-frontend/`

**Nuevo módulo `src/modules/essential-knowledge/`:**
- `pages/EssentialKnowledge.page.vue` — página principal con tabla paginada (10 registros), columnas: N.°, Código, Curso [código][nombre], Tema [código][nombre], Nombre, Fecha Creación, Estado, Acciones (Ver/Editar/Eliminar). Filtros opcionales: búsqueda texto (código/nombre), curso (autocomplete restringido por usuario), tema, estado (defecto: Activo). Botón "Agregar saber necesario" y "Limpiar filtros" / "Ver todos". Orden por defecto: Fecha Creación descendente.
- `dialogs/EssentialKnowledge.dialog.vue` — modal crear/editar con campos: Curso (select), Tema (dependiente del curso), Nombre (textarea con contador 150 chars), carga SVG (input file + preview, validación MIME `image/svg+xml` y tamaño ≤5 MB con mensaje AC-2.8). Botón Guardar deshabilitado si faltan campos obligatorios. Confirmación al cancelar si hay datos (AC-2.5).
- `dialogs/EssentialKnowledgeShow.dialog.vue` — modal con datos del saber (Código, Nombre, Curso, Tema) más imagen SVG responsive. Manejo de error "No se pudo visualizar la imagen del saber necesario" (AC-4.2).
- `dialogs/EssentialKnowledgeChangeState.dialog.vue` — confirmación cambio estado. Mensaje: "El estado del saber necesario ha sido actualizado."
- `dialogs/EssentialKnowledgeDelete.dialog.vue` — confirmación eliminación.
- `components/ImageUploader.vue` — componente de carga SVG con validación de tipo MIME (`image/svg+xml`), tamaño ≤5 MB y preview.
- `services/essential-knowledge.service.ts` — métodos CRUD (`list`, `getById`, `store`, `update`, `delete`, `updateIsActive`) + `uploadSvg(file: File)`. Usa `odiseoApi` de Axios.
- `models/EssentialKnowledgeList.model.ts` — interfaz TypeScript para los datos del listado.
- `enums/essential-knowledge.headers.js` — definición de columnas de la tabla.
- `enums/status.enum.js` — enum Activo/Inactivo.
- `routes.ts` (opcional) o registro en el sistema de rutas existente.

**Navegación — `src/navigation/vertical/odiseo/` (archivo existente a modificar):**
- Agregar entrada "Saberes Necesarios" dentro del módulo Cursos, con `subject: 'essential-knowledge'`, `action: 'listar'`, visible solo para usuarios con permiso `essential_knowledge.listar` (constitution §2.10). Ruta `odiseo-cursos-essential-knowledge`.

## 3. Decisiones de arquitectura (mini-ADR) ← §11 (ADRs)

### ADR-1: Arquitectura hexagonal DDD para el módulo
**DECISIÓN:** El módulo se implementa con la misma estructura de capas que `Area`: Domain → Application → Infrastructure, con interfaces de repositorio separadas en Read/Write (CQS).
**POR QUÉ:** Constitution §2 exige Dependency Rule, CQS y Use Case único. Reutilizar el patrón ya establecido en el proyecto reduce riesgo y curva de aprendizaje.
**ALTERNATIVA DESCARTADA:** Implementar en el legacy `app/` con controladores tradicionales Laravel — violaría la estrategia de migración del proyecto (constitution §2.1).

### ADR-2: Código auto-generado con formato `[cod_curso]-[cod_tema][correlativo]`
**DECISIÓN:** El código se genera en `StoreEssentialKnowledgeUseCase` consultando el último correlativo por (course_id, topic_id). Formato fijo de 4 dígitos con ceros a la izquierda. Si cambia de tema al editar, se regenera.
**POR QUÉ:** El formato debe reflejar curso y tema de origen, y ser único dentro del tema. La generación en UseCase permite atomicidad controlada con transacción (constitution §2.7).
**ALTERNATIVA DESCARTADA:** Secuencia auto-incremental global en BD — perdería la semántica curso-tema. Secuencia por curso (sin tema) — no reflejaría el tema de origen.

### ADR-3: SVG almacenado en GCS, filename en BD
**DECISIÓN:** El SVG se sube a Google Cloud Storage en `/essential-knowledge/{uuid}.svg`. En BD solo el filename. La URL se genera firmada y temporal al consultar.
**POR QUÉ:** Constitution §4 exige GCS para almacenamiento de archivos. Consistente con el flujo agreement del módulo Area. GCS maneja escalabilidad y caché.
**ALTERNATIVA DESCARTADA:** SVG como BLOB en BD (impacta rendimiento y backup). Base64 en columna text (infla la fila). Almacenamiento local en disco (no escala horizontalmente).

### ADR-4: Validación de unicidad en BD + aplicación (solo activos)
**DECISIÓN:** Partial unique index `idx_unique_active_course_topic_name` on `(course_id, topic_id, name)` WHERE `deleted_at IS NULL` + validación en el UseCase antes de insertar/actualizar. Un soft-delete no bloquea la re-creación del mismo nombre.
**POR QUÉ:** El spec §4 exige resolver concurrencia a nivel BD. Al ser soft delete, un registro eliminado no debería impedir crear uno nuevo con el mismo nombre. La validación en aplicación da mejor experiencia de usuario (mensaje inmediato sin esperar error BD).
**ALTERNATIVA DESCARTADA:** Constraint unique global `(course_id, topic_id, name)` — un soft-delete bloquearía permanentemente ese nombre, violando el principio de menor sorpresa.

### ADR-5: Sanitización de SVG obligatoria
**DECISIÓN:** Todo SVG subido se sanitiza (eliminar `<script>`, `<foreignObject>`, event handlers `on*`) antes de almacenarse en GCS.
**POR QUÉ:** Los SVGs pueden contener scripts maliciosos (XSS). El spec NFR-7 lo exige explícitamente. Constitution §5 exige protección contra XSS.
**ALTERNATIVA DESCARTADA:** Confiar en validación client-side (bypasseable). Desactivar SVG rendering en frontend (pérdida de funcionalidad).

### ADR-6: `deleted_at` para soft delete, `is_active` para visibilidad en gestión
**DECISIÓN:** `deleted_at` para soft delete (registro invisible en toda la plataforma). `is_active` para desactivación lógica donde el registro sigue visible en el módulo de gestión (pero no seleccionable). El listado por defecto muestra activos e inactivos (excepto eliminados); el filtro de estado opera sobre `is_active`.
**POR QUÉ:** `fl_status` era redundante con `deleted_at` — ambos cumplían el mismo rol de soft delete. Se reemplaza por `is_active` con semántica distinta: un registro inactivo (`is_active = false`) sigue siendo visible para que el usuario pueda reactivarlo; uno eliminado (`deleted_at` not null) desaparece por completo. Constitution §3 exige soft delete.
**ALTERNATIVA DESCARTADA:** Usar solo `deleted_at` (un registro inactivo desaparecería, impidiendo reactivación). Usar `fl_status` legacy (redundante con `deleted_at`, confundía ambos conceptos).

### ADR-7: Correlativo máximo 4 dígitos (9999)
**DECISIÓN:** Si al generar el correlativo se supera 9999, el sistema rechaza la operación con mensaje claro.
**POR QUÉ:** El spec §4 (caso límite) lo exige. Mantiene la consistencia del formato documentado.
**ALTERNATIVA DESCARTADA:** Permitir 5+ dígitos (rompe formato). Reiniciar correlativo (pérdida de trazabilidad).

## 4. Riesgos y dependencias

- **Dependencia crítica**: El catálogo de Cursos y Temas debe preexistir (Assumption spec §5). Si no existe, el alcance debe ampliarse.
- **Concurrencia en creación**: Dos usuarios crean el mismo nombre en el mismo tema simultáneamente. Mitigado por ADR-4 (partial unique index en BD).
- **SVG malicioso (XSS)**: Scripts embebidos en SVG. Mitigado por ADR-5 (sanitización obligatoria).
- **Correlativo agotado (>9999)**: El tema alcanzó el máximo de saberes. Mitigado por ADR-8 (validación + mensaje). Plan de contingencia: evaluar expansión a 5 dígitos.
- **Google Cloud Storage**: Timeout o fallo de autenticación. Mitigado con reintentos, timeout configurable y logging.
- **Cursos no asignados al usuario**: El filtro de curso debe restringirse a los cursos del usuario autenticado. Si no se implementa correctamente, usuarios ven cursos no autorizados.
- **SVG de gran tamaño (>5 MB)**: El límite de 5 MB está definido por AC-2.8. Validar también en servidor para evitar rechazo luego de la subida a GCS.

## 5. Trazabilidad: cada US del spec → dónde se implementa en este plan

- **US-1 (Acceder a sección Saberes Necesarios)** → Navegación lateral (`src/navigation/vertical/odiseo/`) con entrada "Saberes Necesarios" protegida por CASL (`subject: 'essential-knowledge'`, `action: 'listar'`). Ruta de página (`src/pages/odiseo/cursos/essential-knowledge/index.vue`). Backend: ruta `GET api/v2/catalog/essential-knowledge` con middleware `permission:essential_knowledge.listar`.
- **US-2 (Crear un saber necesario)** → `EssentialKnowledge.dialog.vue` (modal creación), `StoreEssentialKnowledgeUseCase` (generación código + validación unicidad), `StoreEssentialKnowledgeRequestValidator` (validación SVG obligatorio, nombre ≤150 chars, curso-tema existentes), `UploadSvgEssentialKnowledgeUseCase` (subida SVG a GCS y sanitización).
- **US-3 (Visualizar listado con filtros)** → `EssentialKnowledge.page.vue` (tabla paginada 10 registros, columnas del spec AC-3.1, orden por defecto Fecha Creación DESC, botón "Limpiar filtros" AC-3.5), `FilterEssentialKnowledgeUseCase` (filtros opcionales: código/nombre, curso, tema, estado), `FilterEssentialKnowledgeRequestValidator`, `fn_list_essential_knowledge` (BD paginada).
- **US-4 (Ver imagen SVG del saber)** → `EssentialKnowledgeShow.dialog.vue` (datos del saber + imagen SVG responsive, manejo de error AC-4.2), `GetByIdEssentialKnowledgeUseCase` (retorna URL firmada de GCS + metadatos), `GetByIdEssentialKnowledgeResponse`.
- **US-5 (Editar un saber necesario)** → `EssentialKnowledge.dialog.vue` (modo edición, campos editables: tema, nombre, imagen), `UpdateEssentialKnowledgeUseCase` (regenera código si cambia tema, valida unicidad), `UpdateEssentialKnowledgeRequestValidator`.
- **US-6 (Cambiar estado activo/inactivo)** → `EssentialKnowledgeChangeState.dialog.vue` (confirmación), `UpdateIsActiveEssentialKnowledgeUseCase`, `UpdateIsActiveEssentialKnowledgeValidator`, `fn_update_essential_knowledge` (BD actualiza is_active). Ruta protegida con permiso `essential_knowledge.actualizar_estado`.
- **US-7 (Eliminar un saber necesario)** → `EssentialKnowledgeDelete.dialog.vue` (confirmación), `DeleteEssentialKnowledgeUseCase` (soft delete), `DeleteEssentialKnowledgeRequestValidator`.

