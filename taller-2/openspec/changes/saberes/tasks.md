## 1. Backend - Database Migrations

- [ ] 1.1 Create migration for `saberes` table (id, code, name, description, is_active, created_by, updated_by, deleted_by, timestamps)
- [ ] 1.2 Create migration for `saber_categories` table (id, name, description, is_active, timestamps)
- [ ] 1.3 Create migration for `saber_category_pivot` table (saber_id, category_id)
- [ ] 1.4 Create migration for `role_saber` pivot table (role_id, saber_id)
- [ ] 1.5 Create permission migration for saber-necesario.* permissions (listar, crear, actualizar, eliminar, listar-id, actualizar-estado)

## 2. Backend - DDD Module Structure

- [ ] 2.1 Create module directory structure under `Catalog/Saberes/` (Application, Domain, Infrastructure, Tests)
- [ ] 2.2 Create Domain entities (Store, Update, Delete, UpdateIsActive)
- [ ] 2.3 Create Domain DTOs (GetById, GetAll, Filter)
- [ ] 2.4 Create Read/Write repository interfaces
- [ ] 2.5 Create Validator repository interface

## 3. Backend - CRUD Use Cases & Persistence

- [ ] 3.1 Create Request DTOs for all operations
- [ ] 3.2 Create StoreSaberesUseCase with stored procedure integration
- [ ] 3.3 Create GetByIdSaberesUseCase
- [ ] 3.4 Create GetAllSaberesUseCase with pagination
- [ ] 3.5 Create UpdateSaberesUseCase
- [ ] 3.6 Create DeleteSaberesUseCase (soft delete)
- [ ] 3.7 Create UpdateIsActiveSaberesUseCase
- [ ] 3.8 Create Query Builder implementations for read operations
- [ ] 3.9 Create Query Builder implementation for write operations
- [ ] 3.10 Create Query Builder implementation for validation

## 4. Backend - Category & Role Association

- [ ] 4.1 Create use cases for category CRUD (Create, List, Assign, Remove)
- [ ] 4.2 Create use cases for role-saber assignment (Assign, Remove, ListByRole, ListBySaber)
- [ ] 4.3 Create read builders for category and role associations
- [ ] 4.4 Create write builders for category and role associations

## 5. Backend - Search & Filter

- [ ] 5.1 Create FilterSaberesUseCase with keyword, category, role, and status support
- [ ] 5.2 Create ListReadBuilder with dynamic WHERE clause construction
- [ ] 5.3 Implement combined query building for multi-criteria search

## 6. Backend - HTTP Layer

- [ ] 6.1 Create Controllers (SaberesController, SaberesListController)
- [ ] 6.2 Create Request Mappers for all operations
- [ ] 6.3 Create Response formatters
- [ ] 6.4 Create Validators (FormRequest classes) for each operation
- [ ] 6.5 Create Route definitions and index.php
- [ ] 6.6 Create Service Provider with interface-to-implementation bindings
- [ ] 6.7 Register module routes in Bootstrap/Routes.php

## 7. Backend - Tests

- [ ] 7.1 Create Unit tests for Domain entities
- [ ] 7.2 Create Integration tests for all Use Cases
- [ ] 7.3 Run tests and verify all pass

## 8. Frontend - Module Setup & Core Components

- [ ] 8.1 Create frontend module directory `saberes/` under `src/modules/`
- [ ] 8.2 Create SaberesList model (TypeScript interface)
- [ ] 8.3 Create headers enum for VDataTable column configuration
- [ ] 8.4 Create status enum and constants
- [ ] 8.5 Create SaberesService (Axios API calls)

## 9. Frontend - Pages & Dialogs

- [ ] 9.1 Create SaberesPage (main listing with VDataTableServer, search bar, filter controls)
- [ ] 9.2 Create SaberesDialog (create/edit form with name, description, category selection)
- [ ] 9.3 Create SaberesShowDialog (read-only detail view with categories and roles)
- [ ] 9.4 Create route page at `src/pages/odiseo/saberes/index.vue`
- [ ] 9.5 Add navigation item in sidebar for Saberes Necesarios
- [ ] 9.6 Wire up CASL permissions for action-based visibility
