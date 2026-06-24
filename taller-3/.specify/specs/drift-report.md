<!-- sdd:section:drift-summary -->
# Drift Report

## Summary
- **Feature**: N/A — no feature specification present in scope
- **Analysis Date**: 2026-06-24
- **Mode**: Full Drift Analysis (constrained to `taller-3/`; `taller-2/` ignored per instruction)
- **Scope read**: `taller-3/.specify/`, `taller-3/.github/`, `taller-3/odiseo-backend/`, `taller-3/odiseo-frontend/`
- **Total Findings**: 1 HIGH, 1 LOW, 1 INFO (3 total)
- **Baseline**: Constitution `.specify/memory/constitution.md` (read ✓)

> **Coverage honesty:** Spec↔code drift could **not** be evaluated because no feature
> spec artifacts exist in scope (see DR-001). Constitution compliance was checked by a
> **targeted, mechanically-verifiable sample** of rules (layering, service-locator ban,
> column types, FE stack/structure), **not** an exhaustive line-by-line audit.
<!-- /sdd:section:drift-summary -->

## Findings

### DR-001: No feature specifications present in scope — drift baseline unavailable
- **Severity**: HIGH
- **Category**: Missing Artifacts (no spec baseline to compare against)
- **Code State**: Full Odiseo product code present (`odiseo-backend/`, `odiseo-frontend/`).
  Backend product repo is a nested git repo on branch `feature/OD-4162/taller-2` (HEAD `e13c61f7e`).
- **Spec State**: `taller-3/.specify/specs/` is **empty**. No `spec.md`, `plan.md`,
  `data-model.md`, `tasks.md`, or `test-cases.md` exist anywhere in `taller-3/` (outside
  `.specify/templates/`). The "Saberes Necesarios" artifacts live in `taller-2/`, which is
  out of scope per instruction.
- **Affected Files**: `.specify/specs/` (empty); `.specify/memory/constitution.md` (present)
- **Traces to**: Maintainer Operating Mode 1 steps 2–4 (read spec artifacts → compare spec vs code)
- **Recommendation**: **Clarify intent.** Either (a) a feature spec for taller-3 has not been
  created yet — generate it via the SDD pipeline before drift analysis is meaningful; or
  (b) the specs intended for this analysis live outside taller-3 and the scope constraint
  should be revisited. Until a spec baseline exists, US↔code, data-model, API/event, and
  task traceability cannot be reported.

### DR-002: Frontend `pnpm-lock.yaml` absent from working copy
- **Severity**: LOW
- **Category**: Schema/Config Drift
- **Code State**: `odiseo-frontend/package.json` pins `"packageManager": "pnpm@8.6.2"`,
  but no `pnpm-lock.yaml` (nor `package-lock.json`/`yarn.lock`) is present in the checkout.
- **Spec State**: Constitution §4 (Frontend) mandates **pnpm** as the package manager
  ("No usar npm ni yarn"). A committed lockfile is the mechanism that enforces reproducible installs.
- **Affected Files**: `odiseo-frontend/package.json`, `odiseo-frontend/` (missing `pnpm-lock.yaml`)
- **Traces to**: constitution §4 (Restricciones técnicas → Frontend)
- **Recommendation**: **Clarify intent.** Confirm whether the lockfile is intentionally
  git-ignored or simply absent from this working copy. If absent, restore/commit
  `pnpm-lock.yaml` to satisfy reproducible-install expectations. No code change recommended
  unilaterally (read-only agent).

### DR-003: Legacy `fl_status` still referenced in `app/` (legacy MVC) — tracked debt, not a violation
- **Severity**: INFO
- **Category**: Stale Spec (tracked deprecation, expected)
- **Code State**: `fl_status` appears across legacy `app/` files (Mappers, Exports, Helpers, etc.).
- **Spec State**: Constitution §3 marks `fl_status` as **deprecated** and to be "eliminado
  progresivamente"; §8.4 ("Coexistencia pacífica") and §8.5 explicitly allow legacy `app/`
  code to coexist and forbid refactoring legacy without an explicit ticket.
- **Affected Files**: `app/Exports/Report/*.php`, `app/Helpers/helpers.php`,
  `app/Http/Mappers/V1/**` (and others)
- **Traces to**: constitution §3 (Convenciones → estado booleano) and §8 (Principios 4–5)
- **Recommendation**: **No action.** Consistent with the documented progressive-deprecation
  plan. Surfaced only so it is not mistaken for hidden drift. Verify new `src/` (DDD) code
  uses `is_active`, which the sample confirms.

## Constitution Compliance — Sampled Checks (PASS)

These checks against `.specify/memory/constitution.md` passed within the sampled scope:

| Rule (constitution ref) | Check | Result |
|---|---|---|
| §2 Hexagonal — Dependency Rule / layering | `src/App/Modules/V2/**` has `Domain/Application/Infrastructure` | PASS |
| §2 Hexagonal — CQS read/write interfaces | `*ReadRepositoryInterface` + `*WriteRepositoryInterface` present (e.g. Client) | PASS |
| §2 §5 — No service locator in `src/` | No `App::make(` / `app(` in `src/` | PASS |
| §3 BE — JSONB not `json` | No `->json(` column defs in `database/migrations/` | PASS |
| §2 FE — Modular `src/modules/` | Multiple self-contained modules present | PASS |
| §4 FE — Vue 3 Composition API only | No `new Vue(` / Options-API `data()` in `src/` | PASS |
| §4 FE — pnpm | `packageManager: pnpm@8.6.2` pinned (see DR-002 re: lockfile) | PASS* |
| §4 FE — No jQuery | No `jquery` dependency in `package.json` | PASS |

## Statistics
- Specs in sync: 0 / 0 (no feature specs in scope — see DR-001)
- Constitution violations (hard, within sampled rules): 0
- Constitution config gaps: 1 (DR-002, LOW)
- Tracked legacy debt surfaced: 1 (DR-003, INFO)
- Test coverage gaps: Not assessed (requires a feature/spec scope)
- Undocumented features: Not assessable (no spec baseline)

## Recommended Actions
1. **[P1 / DR-001]** Establish a feature spec baseline in `taller-3/.specify/specs/NNN/`
   (or confirm the correct spec location) before re-running spec↔code drift analysis.
2. **[P2 / DR-002]** Confirm `pnpm-lock.yaml` presence/commit policy for `odiseo-frontend`.
3. **[P3 / DR-003]** No action; continue the documented `fl_status` → `is_active`/`deleted_at`
   deprecation as legacy modules migrate.

---
*Generated by the Tech Context Maintainer (read-only). No source or spec files were modified.
This report is a new artifact. Findings DR-001 and DR-002 are flagged for human decision, not auto-resolved.*
