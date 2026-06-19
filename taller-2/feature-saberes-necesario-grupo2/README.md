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
- [x] Cada User Story tiene criterios de aceptación
- [x] Los criterios son medibles
- [x] Se cubren errores
- [x] Se cubren casos borde
- [x] Se consideran NFR relevantes

#### Claridad
- [x] No existen términos ambiguos
- [x] No existen requisitos vagos
- [x] Los valores son específicos
- [x] La redacción es verificable

#### Consistencia
- [x] Terminología consistente
- [x] Nombres consistentes
- [x] No existen contradicciones

#### Testabilidad
- [x] Todos los requisitos son verificables
- [x] Existen criterios observables
- [x] No existen requisitos subjetivos

### Observaciones
- Sin observaciones

### Veredicto
🟢 PASS

## Gate de consistencia

### Coverage Matrix

| Requisito | Plan | Caso de prueba | Estado |
|-----------|------|----------------|--------|
| US-1 / AC-1.1 | plan.md — Trazabilidad (US-1) | TC-1 | ✅ |
| US-1 / AC-1.2 | plan.md — Trazabilidad (US-1) | TC-2 | ✅ |
| US-2 / AC-2.1 | plan.md — Trazabilidad (US-2) | TC-3 | ✅ |
| US-2 / AC-2.2 | plan.md — Trazabilidad (US-2) | TC-4 | ✅ |
| US-2 / AC-2.3 | plan.md — Trazabilidad (US-2) | TC-5, TC-6, TC-7 | ✅ |
| US-2 / AC-2.4 | plan.md — Trazabilidad (US-2) | TC-8 | ✅ |
| US-2 / AC-2.5 | plan.md — Trazabilidad (US-2) | TC-9, TC-10 | ✅ |
| US-2 / AC-2.6 | plan.md — Trazabilidad (US-2) | TC-11 | ✅ |
| US-2 / AC-2.7 | plan.md — Trazabilidad (US-2) | TC-12, TC-13 | ✅ |
| US-2 / AC-2.8 | plan.md — Trazabilidad (US-2) | TC-14 | ✅ |
| US-3 / AC-3.1 | plan.md — Trazabilidad (US-3) | TC-15 | ✅ |
| US-3 / AC-3.2 | plan.md — Trazabilidad (US-3) | TC-16, TC-17, TC-18, TC-21 | ✅ |
| US-3 / AC-3.3 | plan.md — Trazabilidad (US-3) | TC-19, TC-22 | ✅ |
| US-3 / AC-3.4 | plan.md — Trazabilidad (US-3) | TC-20, TC-23 | ✅ |
| US-3 / AC-3.5 | plan.md — Trazabilidad (US-3) | TC-24 | ✅ |
| US-4 / AC-4.1 | plan.md — Trazabilidad (US-4) | TC-25 | ✅ |
| US-4 / AC-4.2 | plan.md — Trazabilidad (US-4) | TC-26 | ✅ |
| US-5 / AC-5.1 | plan.md — Trazabilidad (US-5) | TC-27 | ✅ |
| US-5 / AC-5.2 | plan.md — Trazabilidad (US-5) | TC-28 | ✅ |
| US-5 / AC-5.3 | plan.md — Trazabilidad (US-5) | TC-29 | ✅ |
| US-5 / AC-5.4 | plan.md — Trazabilidad (US-5) | TC-30 | ✅ |
| US-5 / AC-5.5 | plan.md — Trazabilidad (US-5) | TC-31 | ✅ |
| US-6 / AC-6.1 | plan.md — Trazabilidad (US-6) | TC-32, TC-33 | ✅ |
| US-7 / AC-7.1 | plan.md — Trazabilidad (US-7) | TC-34 | ✅ |
| US-7 / AC-7.2 | plan.md — Trazabilidad (US-7) | TC-35 | ✅ |
| US-7 / AC-7.3 | plan.md — Trazabilidad (US-7) | TC-36 | ✅ |

> Nota: Las referencias "plan.md — Trazabilidad (US-X)" apuntan a la sección "Trazabilidad: cada US del spec → dónde se implementa en este plan" dentro de plan.md.

## Evidencias y trazabilidad

- Commit inicial (v0): c8868d30230ebc7f3c829016e0fea6c0b4d3237c
- Refinamientos realizados: ver historial de commits.
- Ajustes posteriores al gate de claridad: Rol "Didi" definido en §5 Assumptions. Término "solucionario" reemplazado por "parámetros de diagramación de cada pregunta" en §1 y §6.
- Ajustes posteriores al gate de consistencia: AC-3.4 y AC-3.5 corregidos en spec.md; TC-37 y TC-38 actualizados en test-cases.md para reflejar que "Todos" muestra activos e inactivos. AC-7.2 (bloqueo por saber en uso) y AC-7.3 (sin permisos) añadidos en spec.md; TC-40 actualizado y TC-44 creado en test-cases.md.

---

Archivos relevantes (local):
- feature-saberes-necesario-grupo2/constitution.md
- feature-saberes-necesario-grupo2/spec.md
- feature-saberes-necesario-grupo2/plan.md
- feature-saberes-necesario-grupo2/test-cases.md

Instrucción siguiente recomendada:
- Completar responsables y asignar revisor(es) para el Gate de claridad.
- Si se desea, generar una matriz detallada que incluya número de línea o sección del spec para cada requisito (opcional).
