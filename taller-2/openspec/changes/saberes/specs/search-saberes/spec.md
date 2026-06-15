## ADDED Requirements

### Requirement: Search saberes by keyword
The system SHALL allow authorized users to search knowledge entries by keyword matching name and description.

#### Scenario: Search with matching keyword
- **WHEN** an authorized user searches with a keyword that matches one or more saber names or descriptions
- **THEN** the system returns matching entries with pagination metadata

#### Scenario: Search with no matches
- **WHEN** an authorized user searches with a keyword that matches no entries
- **THEN** the system returns an empty paginated result set

### Requirement: Filter saberes by category
The system SHALL filter knowledge entries by category ID.

#### Scenario: Filter by single category
- **WHEN** an authorized user filters saberes by a category ID
- **THEN** the system returns saberes belonging to that category

#### Scenario: Filter by multiple categories
- **WHEN** an authorized user filters saberes by multiple category IDs
- **THEN** the system returns saberes belonging to any of the specified categories

### Requirement: Filter saberes by role
The system SHALL filter knowledge entries by assigned role ID.

#### Scenario: Filter by role
- **WHEN** an authorized user filters saberes by a role ID
- **THEN** the system returns saberes assigned to that role

### Requirement: Filter saberes by status
The system SHALL filter knowledge entries by active/inactive status.

#### Scenario: Filter active only
- **WHEN** an authorized user filters with status "active"
- **THEN** the system returns only active saberes

#### Scenario: Filter inactive only
- **WHEN** an authorized user filters with status "inactive"
- **THEN** the system returns only inactive saberes

### Requirement: Combined search and filters
The system SHALL support combining keyword search with category, role, and status filters.

#### Scenario: Combined query
- **WHEN** an authorized user searches with keywords and applies category and status filters simultaneously
- **THEN** the system returns entries matching all criteria

### Requirement: Paginated results
The system SHALL return paginated results for search and list operations.

#### Scenario: Default pagination
- **WHEN** an authorized user requests a list or search without pagination parameters
- **THEN** the system returns the first page with default page size

#### Scenario: Custom pagination
- **WHEN** an authorized user specifies page number and page size
- **THEN** the system returns the requested page with the specified number of entries
