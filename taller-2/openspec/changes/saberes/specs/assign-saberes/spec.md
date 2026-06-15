## ADDED Requirements

### Requirement: Assign saber to role
The system SHALL allow authorized users to associate a knowledge entry with a role or position.

#### Scenario: Successful role assignment
- **WHEN** an authorized user assigns a saber to a specific role
- **THEN** the system creates the role-saber association

#### Scenario: Duplicate assignment
- **WHEN** an authorized user attempts to assign the same saber to the same role twice
- **THEN** the system ignores the duplicate and returns success

### Requirement: Remove saber from role
The system SHALL allow authorized users to remove a saber-role association.

#### Scenario: Remove assignment
- **WHEN** an authorized user removes a saber from a role
- **THEN** the system deletes the association

### Requirement: List saberes by role
The system SHALL return all knowledge entries assigned to a given role.

#### Scenario: Query by role ID
- **WHEN** an authorized user queries saberes by role ID
- **THEN** the system returns all saberes assigned to that role with their details

### Requirement: List roles by saber
The system SHALL return all roles assigned to a given knowledge entry.

#### Scenario: Query by saber ID
- **WHEN** an authorized user queries roles by saber ID
- **THEN** the system returns all roles associated with that saber entry
