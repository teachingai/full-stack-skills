# Open the App

## Instructions

This example demonstrates how to open Cypress App and get started.

### Key Concepts

- Installing Cypress
- Opening Cypress App
- Launchpad interface
- Choosing test type

### Example: Installation

```bash
# Using npm
npm install -D cypress

# Using yarn
yarn add -D cypress

# Using pnpm
pnpm add -D cypress
```

### Example: Opening Cypress

```bash
# Open Cypress App (Interactive Mode)
npx cypress open

# Run tests headlessly
npx cypress run
```

### Example: Package.json Scripts

```json
{
  "scripts": {
    "cypress:open": "cypress open",
    "cypress:run": "cypress run",
    "test:e2e": "cypress run --e2e",
    "test:component": "cypress run --component"
  }
}
```

### Example: Launchpad Interface

When you open Cypress, you'll see the Launchpad which helps you:
1. Choose testing type (E2E or Component)
2. Select a browser
3. Create your first test

### Example: First Test

```javascript
// cypress/e2e/example.cy.js
describe('My First Test', () => {
  it('Does not do much!', () => {
    expect(true).to.equal(true)
  })
})
```

### Key Points

- Use `cypress open` for interactive testing
- Use `cypress run` for CI/CD
- Launchpad guides you through setup
- Choose between E2E and Component testing
- Select your preferred browser
