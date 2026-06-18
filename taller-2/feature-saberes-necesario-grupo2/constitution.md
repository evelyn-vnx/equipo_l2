# Constitution del SDD — Odiseo

## 1. Objetivo del proyecto

Plataforma para la gestión de preguntas, administración academica y generación automatizada de materiales de balotario y examenes. El backend expone APIs RESTful que el frontend SPA consume. El backend está en migración progresiva de MVC tradicional a arquitectura hexagonal con DDD. El frontend es una SPA modular construida con Vue 3, Vuetify 3, ruteo basado en archivos, control de acceso con CASL y comunicación vía Axios, organizada en módulos autocontenidos dentro de `src/modules/`.

## 2. Reglas arquitectónicas

1. **API versionada** — Toda ruta nueva debe pertenecer a `v2/` bajo la arquitectura DDD. Las rutas `v1/` legacy se mantienen sin cambios hasta su migración.

### Backend
### Arquitectura MVC

1. En `app/`, se maneja los Controllers, Services y repositories. 
2. **CQS** - Se tiene instancia QueryDB con metodos read y readbuilder para solo lectura y metodos write y writeBuilder para escritura.
### Arquitectura hexagonal
1. **Dependency Rule** — En `src/` (DDD), las dependencias apuntan hacia adentro: Infrastructure → Application → Domain. Domain no conoce nada fuera de sí mismo.
2. **CQS (Command-Query Separation)** — Cada módulo DDD debe tener interfaces separadas para lectura (`*ReadRepositoryInterface`) y escritura (`*WriteRepositoryInterface`).
3. **Use Case único** — Cada caso de uso es una clase con una única responsabilidad y un único método público (`__invoke` o `execute`).
4. **DTOs inmutables** — Los Data Transfer Objects de entrada y salida son inmutables, sin lógica de negocio.
5. **Inyección de dependencias por constructor** — Prohibido el uso de `App::make()` o service locator en `src/`. Todo se inyecta vía constructor y se registra en Service Providers.
6. **Transaccionalidad explícita** — Las operaciones que requieren atomicidad se envuelven con `TransactionalUseCase`.

### Frontend
8. **Frontend modular** — Cada funcionalidad se organiza en un módulo autocontenido dentro de `src/modules/` con subdirectorios para componentes, servicios, modelos, diálogos, páginas, enums y composables. Estructura típica: `components/`, `dialogs/`, `services/`, `models/`, `enums/`, `pages/`.
9. **Ruteo basado en archivos** — Las páginas se crean como archivos `.vue` dentro de `src/pages/` siguiendo la estructura de directorios que define la ruta. La configuración de título, sujeto CASL y acción se define mediante `definePage({ meta: { title, subject, action } })`.
10. **CASL para autorización** — Todo control de acceso se realiza mediante `@casl/ability` con sujetos en kebab-case y acciones definidas, declarados en `definePage()` y en la navegación lateral (`src/navigation/vertical/`), no mediante lógica ad-hoc.

## 3. Convenciones de código

### Backend (PHP/Laravel)

| Elemento | Convención |
|---|---|
| Estilo | PSR-12, verificado con Laravel Pint |
| Nombres de tablas | snake_case, plural |
| Primary keys | id bigint incremental |
| Timestamps | TIMESTAMPTZ, con `created_at` y `updated_at` |
| Soft deletes | Para todas las tablas |
| Columnas de estado booleano | `is_active` para desactivación lógica con visibilidad en gestión (registro inactivo visible para reactivación). No usar `fl_status` — está deprecado por ser redundante con `deleted_at`, será eliminado progresivamente |
| Migraciones | Archivos versionados en `database/migrations/` |
| Vistas BD | Prefijo `vw_` |
| Funciones BD | Prefijo `fn_` |
| Triggers BD | Prefijo `trg_` |
| Índices | Prefijo `idx_` |
| JSON en BD | Usar `JSONB`, nunca `json` |
| Restricciones FK | `ON DELETE RESTRICT` por defecto |
| Rutas | Prefijo `v1/` (legacy) o `v2/` (DDD) |
| Respuestas API | Estructura consistente via `ApiResponse` (DDD) o array (legacy) |

### Frontend (Vue/JS)

| Elemento | Convención |
|---|---|
| Estilo | Airbnb (ESLint) + Prettier |
| Componentes Vue | `<script setup>` + Composition API |
| Nombres de archivos `.vue` (generales) | PascalCase |
| Nombres de páginas de módulo | PascalCase, sufijo `.page.vue` |
| Nombres de diálogos modales | PascalCase, sufijo `.dialog.vue` |
| Nombres de servicios | camelCase, sufijo `.service.js` o `.service.ts` |
| Nombres de stores | camelCase, sufijo `.store.js` |
| Nombres de composables | prefijo `use`, camelCase (`useAuth.ts`) |
| Nombres de modelos/TS | camelCase, sufijo `.model.ts` |
| Nombres de archivos de constantes/enums | camelCase, sufijo `.enum.js` o `.header.js` |
| Auto-imports | Usar `unplugin-auto-import` y `unplugin-vue-components` |
| Store | Pinia con Composition API (setup store) |
| Comunicación con API | Axios instance única (`odiseoApi`) con interceptores |
| Lazy loading | `defineAsyncComponent` para diálogos y componentes pesados |
| Comunicación página-diálogo | `provide` / `inject` para recarga de datos al cerrar diálogos |
| Iconos | Remix Icon (`ri-*`) |
| Tablas de datos paginadas | `VDataTableServer` con `AppPagination` para paginación servidor |
| Manejo de errores | SweetAlert2 via `useSwalAlert` composable para toasts y modales; Sentry para tracking |
| CSS | SCSS con Vuetify utility classes |

## 4. Restricciones técnicas

### Backend
- **PHP 8.1+** obligatorio. No usar features de PHP 8.2+ hasta que se actualice el requirement.
- **Laravel 10** — No actualizar a Laravel 11 sin aprobación explícita.
- **PostgreSQL 16** con réplicas: `pgsql_master` (escritura), `pgsql_stand_by` (lectura). El helper `QueryDB` valida el tipo de operación.
- **Redis** para colas (Horizon), caché y sesiones.
- **Google Cloud Storage** para almacenamiento de archivos (PDFs, imágenes).
- No se permite agregar dependencias sin evaluar su impacto en rendimiento y mantenibilidad.

### Frontend
- **Vue 3.4+** con Composition API. Prohibido Vue 2 u Options API en código nuevo.
- **Vite 5** para build. No usar Webpack.
- **Vuetify 3** como framework UI. No introducir otro framework de componentes.
- **pnpm** como gestor de paquetes. No usar npm ni yarn.
- **Node.js 18+** requerido para desarrollo.
- No usar librerías jQuery o jQuery-based.

### Base de datos
- Una sola base de datos con schema `odiseo`.
- Las migraciones se ejecutan en orden secuencial, sin alterar migraciones ya aplicadas.
- Las operaciones pesadas (generación de PDF, migración de fórmulas matemáticas, etc.) se ejecutan como Jobs en cola Redis, nunca en el request HTTP.

## 5. Requisitos de seguridad

1. **Autenticación** — JWT (`tymon/jwt-auth`) para rutas v1, Laravel Sanctum para rutas v2. Prohibido el uso de auth basada en sesiones.
2. **RBAC granular** — Todo endpoint debe tener verificación de permiso via middleware `permission:xxx` o CASL checks en frontend.
3. **reCAPTCHA** — Activado en login para entornos que no sean local.
4. **CORS** — Lista blanca configurada por entorno en `config/cors.php`. No permitir orígenes comodín en producción.
5. **Validación de entrada** — Toda entrada de usuario debe validarse con Form Requests (legacy) o Validators (DDD) antes de llegar al caso de uso.
6. **Protección contra XSS** — Usar DOMPurify para contenido HTML generado por usuarios. No renderizar HTML sin sanitizar.
7. **Secretos** — Nunca hardcodear API keys, tokens o passwords. Todo via `.env` o variables de entorno.
8. **HTTPS** — Obligatorio en producción. Las cookies de autenticación deben tener flag `Secure`.
9. **Sentry** — Error tracking activo en backend y frontend. No enviar datos sensibles (passwords, tokens) en los eventos.

## 6. Requisitos de testing

| Tipo | Framework | Cobertura mínima | Ubicación |
|---|---|---|---|
| Unit tests (backend) | Pest PHP | 70% | `tests/Unit/` |
| Feature tests (backend) | Pest PHP | 80% en nuevos módulos | `tests/Feature/` |
| Static analysis (backend) | PHPStan + Larastan | Nivel 6 | Análisis en CI |
| Code style (backend) | Laravel Pint | — | `./vendor/bin/pint` |

### Reglas de testing
- Todo nuevo caso de uso (Use Case) debe tener su test correspondiente.
- Los tests de feature deben usar `DatabaseTransactions` para no contaminar la BD.
- Los builders de tests deben usar el patrón Builder (`tests/Builders/`).
- No escribir tests que dependan de datos existentes en la BD (siempre crear los datos necesarios).
- Los mocks deben usar Mockery (backend) o MSW (frontend).

## 7. Definición de Done

Una tarea o historia se considera **Done** cuando cumple **todas** las siguientes condiciones:

1. **Código implementado** — El código cumple con las reglas arquitectónicas y convenciones del proyecto.
2. **Code review** — Aprobado por al menos un par. Sin bloquers.
3. **Tests** — Tests unitarios y/o de feature escritos y pasando.
4. **Static analysis** — PHPStan pasa sin errores (nivel 6). ESLint sin errores.
5. **Sin regresiones** — La suite de tests completa (backend + frontend) pasa.
7. **Sin vulnerabilidades** — No se introducen secretos, dependencias vulnerables o malas prácticas de seguridad.
8. **Integración continua** — Pipeline de CI/CD pasa exitosamente.
9. **Prueba funcional** — La funcionalidad fue probada manualmente en un entorno similar a producción.

## 8. Principios de desarrollo

1. **Principio de menor sorpresa** — El código debe comportarse como se espera. Nombres claros, efectos secundarios explícitos.
2. **Falla rápido** — Validar entradas al inicio. No propagar datos inválidos a través de capas.
3. **Código legible sobre código ingenioso** — Preferir claridad a brevedad. El código se lee muchas más veces de las que se escribe.
4. **Coexistencia pacífica** — El código legacy (`app/`) y el nuevo (`src/`) pueden convivir. No refactorizar legacy sin un ticket explícito. No acoplar módulos DDD al código legacy.
5. **Migración por módulo** — La migración de v1 a v2 se hace un módulo/bounded context a la vez. No se mezclan migraciones.
6. **Responsabilidad única** — Una clase, una preocupación. Un método, una responsabilidad.
8. **Rendimiento consciente** — Las consultas N+1, la carga innecesaria de datos y los procesos síncronos pesados deben identificarse y evitarse en revisiones de código.
9. **Consistencia > Perfectibilidad** — Seguir las convenciones existentes aunque no sean las ideales. La consistencia del código base es más valiosa que una mejora aislada.
10. **Automación primero** — Toda verificación repetible (estilo, tipos, tests) debe estar automatizada en el pipeline de CI.
