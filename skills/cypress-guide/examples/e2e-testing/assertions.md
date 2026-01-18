# Assertions

## Instructions

This example demonstrates assertions in Cypress.

### Key Concepts

- Should assertions
- Expect assertions
- Implicit assertions
- Explicit assertions

### Example: Should Assertions

```javascript
// Visibility
cy.get('button').should('be.visible')
cy.get('input').should('not.be.visible')

// Text content
cy.get('h1').should('contain', 'Welcome')
cy.get('p').should('have.text', 'Hello World')

// Attributes
cy.get('input').should('have.attr', 'type', 'text')
cy.get('a').should('have.attr', 'href', '/about')

// CSS
cy.get('button').should('have.css', 'background-color', 'rgb(0, 0, 255)')
```

### Example: Expect Assertions

```javascript
cy.get('h1').then(($el) => {
  expect($el.text()).to.equal('Welcome')
  expect($el).to.be.visible
})

cy.get('input').then(($input) => {
  expect($input.val()).to.include('@')
})
```

### Example: Multiple Assertions

```javascript
cy.get('form')
  .should('be.visible')
  .and('have.class', 'login-form')
  .find('input')
  .should('have.length', 2)
```

### Example: Custom Assertions

```javascript
cy.get('button').should(($button) => {
  expect($button).to.have.length(1)
  expect($button[0].innerText).to.equal('Submit')
})
```

### Key Points

- Use should() for implicit assertions
- Use expect() for explicit assertions
- Chain assertions with .and()
- Assertions automatically retry
- Can assert on multiple properties
