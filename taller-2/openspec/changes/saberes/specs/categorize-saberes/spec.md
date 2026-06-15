## ADDED Requirements

### Requirement: Create category
The system SHALL allow authorized users to create categories for organizing knowledge entries.

#### Scenario: Successful category creation
- **WHEN** an authorized user submits a new category name and optional description
- **THEN** the system creates the category and returns it

### Requirement: Assign category to saber
The system SHALL allow authorized users to associate one or more categories to a knowledge entry.

#### Scenario: Assign single category
- **WHEN** an authorized user assigns a category to a saber entry
- **THEN** the system creates the association and the category appears in the saber's details

#### Scenario: Assign multiple categories
- **WHEN** an authorized user assigns multiple categories to a saber entry
- **THEN** the system creates all associations

### Requirement: Remove category from saber
The system SHALL allow authorized users to remove category associations from knowledge entries.

#### Scenario: Remove category association
- **WHEN** an authorized user removes a category from a saber entry
- **THEN** the system deletes the association

### Requirement: List categories
The system SHALL provide a list of all available categories for selection.

#### Scenario: List all categories
- **WHEN** an authorized user requests the category list
- **THEN** the system returns all categories ordered by name
