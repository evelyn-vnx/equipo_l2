## Context

The Odiseo platform already has an `essential-knowledge` module under `Catalog/EssentialKnowledge` with basic CRUD. The new "Saberes Necesarios" module will be a more comprehensive implementation following DDD/Hexagonal architecture in `src/App/Modules/V2/`, with improved categorization, role association, and search capabilities.

The backend uses Laravel 10 with PostgreSQL (odiseo schema). The frontend uses Vue 3 + Vuetify 3 + Pinia.

## Goals / Non-Goals

**Goals:**
- Full CRUD for knowledge entries with soft delete and status management
- Categorization system (categories, tags, or hierarchical grouping)
- Association of knowledge entries to roles/positions
- Search and filter by category, role, keywords, and status
- Permission-based access control per action

**Non-Goals:**
- Import/export functionality (may be added later)
- Machine learning or auto-suggestions for knowledge entries
- Multi-tenancy isolation (follows existing platform patterns)

## Decisions

- **DDD/Hexagonal architecture** under `Catalog/Saberes/` following the established pattern in the codebase (single-responsibility use cases, repository interfaces, Query Builder persistence)
- **Stored procedures** for write operations (consistent with existing essential-knowledge pattern using `CallerBuilder`)
- **V2 API routes** under `/v2/catalog/saberes/` with Sanctum auth + permission middleware
- **Categorization** using a separate `saber_categories` table with many-to-many relationship
- **Role association** using a pivot table `role_saber` linking saberes to roles
- **Server-side pagination and filtering** via query parameters for search performance
- **Vue 3 Composition API** with `<script setup>` for frontend components, following existing module conventions

## Risks / Trade-offs

- [Scope creep] → Split into separate sub-modules if complexity grows beyond CRUD + categorization
- [Duplication with essential-knowledge] → Keep the new module distinct; existing module remains for backward compatibility
- [Database migration ordering] → Ensure new migration timestamps are sequenced after existing ones
