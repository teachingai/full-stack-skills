# API Table of Contents

## API Reference Overview

Cypress API is organized into the following categories:

### Commands

Action, query, and assertion commands:
- `cy.get()` - Get DOM elements
- `cy.click()` - Click elements
- `cy.type()` - Type into inputs
- `cy.visit()` - Visit URLs
- `cy.contains()` - Find elements by text
- `cy.should()` - Make assertions
- And many more...

**See also:** `api/commands.md`

### Cypress API

Global Cypress API:
- `Cypress.config()` - Configuration methods
- `Cypress.Commands` - Custom commands
- `Cypress.env()` - Environment variables
- `Cypress.version` - Cypress version
- `Cypress.platform` - Platform info

**See also:** `api/cypress-api.md`

### Utilities

Cypress utility functions:
- `Cypress._` - Lodash utilities
- `Cypress.Blob` - Blob utilities
- `Cypress.Promise` - Promise utilities
- `Cypress.$` - jQuery reference

**See also:** `api/utilities.md`

### Node Events

Node-level events and tasks:
- `cy.task()` - Run Node tasks
- Plugin events
- File system operations

**See also:** `api/node-events.md`

### Examples

All APIs are demonstrated in the `examples/` directory:
- `examples/e2e-testing/` - E2E testing examples
- `examples/component-testing/` - Component testing examples
