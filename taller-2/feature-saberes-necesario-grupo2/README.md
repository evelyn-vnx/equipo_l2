# Gestión de Saberes Necesarios por Tema de Curso

## Equipo
- Integrantes: 
    - Evelyn Noealia Pachas Arratia [Product]
    - Rony Martín Quispe Quispe [Tech]
    - Andi Abraham Cuyotupa Casachagua [QA]

## Resumen ejecutivo
Pequeña feature para centralizar y gestionar "Saberes Necesarios" por curso y tema: CRUD (crear/editar/activar/inactivar/eliminar), código auto-generado, imagen SVG obligatoria y previsualización responsive. Artefactos entregados en este repositorio: constitution.md, spec.md, plan.md y test-cases.md. Ver sección de artefactos para su propósito y responsables.

## Artefactos
- constitution.md
  - propósito: Define objetivos del SDD, reglas arquitectónicas, convenciones de código, restricciones técnicas, seguridad, testing y definición de done del proyecto (ver constitution.md).
  - responsables: Evelyn Noealia Pachas Arratia, Rony Martín Quispe Quispe, Andi Abraham Cuyotupa Casachagua

- spec.md
  - propósito: Documenta el alcance funcional y no funcional de la feature, user stories, criterios de aceptación, casos límite y assumptions (ver SPEC — Gestión de Saberes Necesarios por Tema de Curso).
  - responsable: Evelyn Noealia Pachas Arratia

- plan.md
  - propósito: Plan de implementación técnico (DB, backend DDD, frontend, rutas, providers, tests y ADRs). Incluye mapeo trazabilidad US → componentes planificados.
  - responsable: Rony Martín Quispe Quispe

- test-cases.md
  - propósito: Casos de prueba manuales/automatizables que verifican criterios de aceptación documentados en spec.md.
  - responsable: Andi Abraham Cuyotupa Casachagua

## Flujo SDD aplicado

Constitution
↓
Spec
↓
Plan
↓
Test Design

(Los artefactos concretos se encuentran en la carpeta: feature-saberes-necesario-grupo2/)

## Gate de claridad

### Revisor
#### Equipo L4

### Checklist

#### Completitud
- [ ] Cada User Story tiene criterios de aceptación
- [ ] Los criterios son medibles
- [ ] Se cubren errores
- [ ] Se cubren casos borde
- [ ] Se consideran NFR relevantes

#### Claridad
- [ ] No existen términos ambiguos
- [ ] No existen requisitos vagos
- [ ] Los valores son específicos
- [ ] La redacción es verificable

#### Consistencia
- [ ] Terminología consistente
- [ ] Nombres consistentes
- [ ] No existen contradicciones

#### Testabilidad
- [ ] Todos los requisitos son verificables
- [ ] Existen criterios observables
- [ ] No existen requisitos subjetivos

### Observaciones
[PENDIENTE]

### Veredicto
🟢 PASS | 🟡 PASS CON OBSERVACIONES | 🔴 FAIL
(Marcar resultado final tras la revisión)

## Gate de consistencia

### Coverage Matrix

| Requisito | Plan | Caso de prueba | Estado |
|------------|--------|----------------|---------|
| US-1 | plan.md — Trazabilidad (US-1) | test-cases.md: TC-1, TC-2 | ✅ |
| AC-1.1 | plan.md — Trazabilidad (US-1) | test-cases.md: TC-1 | ✅ |
| AC-1.2 | plan.md — Trazabilidad (US-1) | test-cases.md: TC-2 | ✅ |
| US-2 | plan.md — Trazabilidad (US-2) | test-cases.md: TC-3..TC-13 | ✅ |
| AC-2.1 | plan.md — Trazabilidad (US-2) | test-cases.md: TC-3 | ✅ |
| AC-2.2 | plan.md — Trazabilidad (US-2) | test-cases.md: TC-4 | ✅ |
| AC-2.3 | plan.md — Trazabilidad (US-2) | test-cases.md: TC-5, TC-6, TC-7 | ✅ |
| AC-2.4 | plan.md — Trazabilidad (US-2) | test-cases.md: TC-8 | ✅ |
| AC-2.5 | plan.md — Trazabilidad (US-2) | test-cases.md: TC-9, TC-10 | ✅ |
| AC-2.6 | plan.md — Trazabilidad (US-2) | test-cases.md: TC-11 | ✅ |
| AC-2.7 | plan.md — Trazabilidad (US-2) | test-cases.md: TC-12, TC-13 | ✅ |
| AC-2.8 | plan.md — Trazabilidad (US-2) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| US-3 | plan.md — Trazabilidad (US-3) | test-cases.md: TC-14..TC-16 | ✅ |
| AC-3.1 | plan.md — Trazabilidad (US-3) | test-cases.md: TC-14 | ✅ |
| AC-3.2 | plan.md — Trazabilidad (US-3) | test-cases.md: TC-15, TC-16 | ✅ |
| AC-3.3 | plan.md — Trazabilidad (US-3) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-3.4 | plan.md — Trazabilidad (US-3) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-3.5 | plan.md — Trazabilidad (US-3) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| US-4 | plan.md — Trazabilidad (US-4) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-4.1 | plan.md — Trazabilidad (US-4) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-4.2 | plan.md — Trazabilidad (US-4) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| US-5 | plan.md — Trazabilidad (US-5) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-5.1 | plan.md — Trazabilidad (US-5) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-5.2 | plan.md — Trazabilidad (US-5) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-5.3 | plan.md — Trazabilidad (US-5) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-5.4 | plan.md — Trazabilidad (US-5) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-5.5 | plan.md — Trazabilidad (US-5) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| US-6 | plan.md — Trazabilidad (US-6) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-6.1 | plan.md — Trazabilidad (US-6) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| US-7 | plan.md — Trazabilidad (US-7) | test-cases.md: [PENDIENTE] | [PENDIENTE] |
| AC-7.1 | plan.md — Trazabilidad (US-7) | test-cases.md: [PENDIENTE] | [PENDIENTE] |

> Nota: Las referencias "plan.md — Trazabilidad (US-X)" apuntan a la sección "Trazabilidad: cada US del spec → dónde se implementa en este plan" dentro de plan.md.

### Hallazgos

#### Huecos detectados
- Falta de casos de prueba documentados en test-cases.md para: AC-2.8, AC-3.3, AC-3.4, AC-3.5, AC-4.*, AC-5.*, AC-6.*, AC-7.* → marcar como [PENDIENTE] en matriz.
- Responsables por artefacto no especificados (constitution.md, spec.md, plan.md, test-cases.md).

#### Scope creep detectado
- Elementos detallados en plan.md (funciones y migraciones de BD, ADRs y providers) sin un requisito funcional único que los justifique explícitamente en spec.md (necesita verificación de alcance).

### Veredicto
🟢 PASS | 🟡 PASS CON OBSERVACIONES | 🔴 FAIL
[PENDIENTE] — completar tras resolución de huecos y asignación de responsables.

## Estado final de revisión

| Gate | Estado |
|--------|--------|
| Claridad | [PENDIENTE] |
| Consistencia | [PENDIENTE] |

## Evidencias y trazabilidad

- Commit inicial (v0): [PENDIENTE — colocar SHA]
- Refinamientos realizados: ver historial de commits y notas de reunión (si aplica) [POR COMPLETAR]
- Ajustes posteriores al gate de claridad: [PENDIENTE]
- Ajustes posteriores al gate de consistencia: [PENDIENTE]

---

Archivos relevantes (local):
- feature-saberes-necesario-grupo2/constitution.md
- feature-saberes-necesario-grupo2/spec.md
- feature-saberes-necesario-grupo2/plan.md
- feature-saberes-necesario-grupo2/test-cases.md

Instrucción siguiente recomendada:
- Completar responsables y asignar revisor(es) para el Gate de claridad.
- Añadir/actualizar casos de prueba faltantes en test-cases.md (marcados arriba).
- Ejecutar la checklist y actualizar los veredictos y la coverage matrix con evidencia de commits/PRs.
