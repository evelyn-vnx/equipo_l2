## ADDED Requirements

### Requirement: Create saber entry
The system SHALL allow authorized users to create new knowledge entries with name, description, and initial status.

#### Scenario: Successful creation
- **WHEN** an authorized user submits valid saber data (name, description)
- **THEN** the system creates the entry with status "active" and returns the created record

#### Scenario: Missing required name
- **WHEN** a user submits a creation request without a name
- **THEN** the system returns a validation error and does not create the entry

### Requirement: Read saber entry
The system SHALL allow authorized users to retrieve individual knowledge entries by ID.

#### Scenario: Retrieve existing entry
- **WHEN** an authorized user requests a saber by valid ID
- **THEN** the system returns the full entry details including name, description, categories, assigned roles, status, and timestamps

#### Scenario: Entry not found
- **WHEN** a user requests a saber by non-existent ID
- **THEN** the system returns a 404 error

### Requirement: Update saber entry
The system SHALL allow authorized users to modify existing knowledge entries.

#### Scenario: Successful update
- **WHEN** an authorized user submits valid updates to an existing saber
- **THEN** the system updates the entry and returns the modified record

#### Scenario: Update non-existent entry
- **WHEN** a user attempts to update a saber that does not exist
- **THEN** the system returns a 404 error

### Requirement: Delete saber entry
The system SHALL allow authorized users to soft-delete knowledge entries.

#### Scenario: Successful soft delete
- **WHEN** an authorized user deletes an existing saber
- **THEN** the system sets the deleted_at timestamp and the entry is no longer returned in default queries

#### Scenario: Delete non-existent entry
- **WHEN** a user attempts to delete a saber that does not exist
- **THEN** the system returns a 404 error

### Requirement: Toggle saber active status
The system SHALL allow authorized users to activate or deactivate knowledge entries.

#### Scenario: Toggle to inactive
- **WHEN** an authorized user toggles an active saber to inactive
- **THEN** the system updates the is_active flag and returns the updated entry

#### Scenario: Toggle to active
- **WHEN** an authorized user toggles an inactive saber to active
- **THEN** the system updates the is_active flag and returns the updated entry
