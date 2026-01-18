# E2E Testing Basics

## Instructions

This example demonstrates basic E2E testing concepts in Cypress.

### Key Concepts

- Visiting pages
- Selecting elements
- Interacting with elements
- Assertions

### Example: Basic Test

```javascript
// cypress/e2e/example.cy.js
describe('My First Test', () => {
  it('visits the app', () => {
    cy.visit('/')
    cy.contains('Welcome')
  })
})
```

### Example: Selecting Elements

```javascript
// cypress/e2e/login.cy.js
describe('Login', () => {
  it('can login', () => {
    cy.visit('/login')
    cy.get('[data-cy=email]').type('user@example.com')
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=submit]').click()
  })
})
```

### Example: Assertions

```javascript
// cypress/e2e/home.cy.js
describe('Home Page', () => {
  it('displays welcome message', () => {
    cy.visit('/')
    cy.get('h1').should('contain', 'Welcome')
    cy.url().should('include', '/')
  })
})
```

### Example: Chaining Commands

```javascript
// cypress/e2e/navigation.cy.js
describe('Navigation', () => {
  it('navigates to about page', () => {
    cy.visit('/')
    cy.get('[data-cy=about-link]')
      .should('be.visible')
      .click()
    cy.url().should('include', '/about')
  })
})
```

### Key Points

- Use cy.visit() to navigate
- Use cy.get() to select elements
- Commands are automatically retried
- Chain commands for readability
- Use data-cy attributes for selectors
