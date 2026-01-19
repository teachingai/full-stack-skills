# Network Requests

## Instructions

This example demonstrates handling network requests in Cypress.

### Key Concepts

- Intercepting requests
- Mocking responses
- Waiting for requests
- Stubbing responses

### Example: Intercepting Requests

```javascript
// Intercept GET request
cy.intercept('GET', '/api/users', { fixture: 'users.json' })

// Intercept POST request
cy.intercept('POST', '/api/login', {
  statusCode: 200,
  body: { success: true }
})
```

### Example: Mocking API Response

```javascript
cy.intercept('GET', '/api/users', {
  statusCode: 200,
  body: [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' }
  ]
}).as('getUsers')

cy.visit('/users')
cy.wait('@getUsers')
```

### Example: Stubbing Network Errors

```javascript
cy.intercept('GET', '/api/users', {
  statusCode: 500,
  body: { error: 'Server error' }
})

cy.visit('/users')
cy.get('[data-cy=error]').should('be.visible')
```

### Example: Waiting for Requests

```javascript
cy.intercept('POST', '/api/login').as('login')

cy.visit('/login')
cy.get('[data-cy=email]').type('user@example.com')
cy.get('[data-cy=password]').type('password123')
cy.get('[data-cy=submit]').click()

cy.wait('@login').then((interception) => {
  expect(interception.request.body).to.include({
    email: 'user@example.com'
  })
})
```

### Example: Using Fixtures

```javascript
// cypress/fixtures/users.json
[
  { "id": 1, "name": "John" },
  { "id": 2, "name": "Jane" }
]

// Test
cy.intercept('GET', '/api/users', { fixture: 'users.json' })
cy.visit('/users')
```

### Key Points

- Use cy.intercept() to mock requests
- Alias requests with .as() for waiting
- Use fixtures for test data
- Can stub errors and delays
- Wait for requests with cy.wait()
