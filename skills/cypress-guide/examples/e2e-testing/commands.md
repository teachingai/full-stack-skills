# Common Commands

## Instructions

This example demonstrates common Cypress commands for E2E testing.

### Key Concepts

- Action commands
- Query commands
- Assertion commands
- Command chaining

### Example: Action Commands

```javascript
// Click
cy.get('button').click()

// Type
cy.get('input').type('Hello World')

// Select
cy.get('select').select('option1')

// Check/Uncheck
cy.get('checkbox').check()
cy.get('checkbox').uncheck()

// Clear
cy.get('input').clear()
```

### Example: Query Commands

```javascript
// Get element
cy.get('.my-class')

// Find within element
cy.get('.parent').find('.child')

// Contains text
cy.contains('Hello World')

// Get by data attribute
cy.get('[data-cy=submit]')
```

### Example: Assertion Commands

```javascript
// Should assertions
cy.get('button').should('be.visible')
cy.get('input').should('have.value', 'test')
cy.url().should('include', '/dashboard')

// Expect assertions
cy.get('h1').then(($el) => {
  expect($el.text()).to.equal('Welcome')
})
```

### Example: Navigation Commands

```javascript
// Visit URL
cy.visit('/login')

// Go back/forward
cy.go('back')
cy.go('forward')

// Reload
cy.reload()
```

### Example: Command Chaining

```javascript
cy.get('[data-cy=form]')
  .find('[data-cy=email]')
  .type('user@example.com')
  .should('have.value', 'user@example.com')
```

### Key Points

- Commands are automatically retried
- Commands are asynchronous but read synchronously
- Chain commands for better readability
- Use data-cy attributes for stable selectors
- Commands wait for elements automatically
