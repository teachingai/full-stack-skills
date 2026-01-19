# Commands API

## API Reference

Cypress commands for interacting with your application.

### Action Commands

Commands that perform actions:

#### cy.click()

Click an element.

**Usage:**
```javascript
cy.get('button').click()
cy.get('button').click({ force: true })
```

#### cy.type()

Type into an input.

**Usage:**
```javascript
cy.get('input').type('Hello World')
cy.get('input').type('{enter}')
```

#### cy.select()

Select an option from a select element.

**Usage:**
```javascript
cy.get('select').select('option1')
```

### Query Commands

Commands that query the DOM:

#### cy.get()

Get DOM elements.

**Usage:**
```javascript
cy.get('.my-class')
cy.get('[data-cy=submit]')
cy.get('#my-id')
```

#### cy.contains()

Find elements containing text.

**Usage:**
```javascript
cy.contains('Hello World')
cy.contains('button', 'Submit')
```

#### cy.find()

Find elements within a parent.

**Usage:**
```javascript
cy.get('.parent').find('.child')
```

### Assertion Commands

Commands for making assertions:

#### cy.should()

Make assertions on elements.

**Usage:**
```javascript
cy.get('button').should('be.visible')
cy.get('input').should('have.value', 'test')
cy.url().should('include', '/dashboard')
```

### Navigation Commands

Commands for navigation:

#### cy.visit()

Visit a URL.

**Usage:**
```javascript
cy.visit('/login')
cy.visit('https://example.com')
```

#### cy.go()

Go back or forward in browser history.

**Usage:**
```javascript
cy.go('back')
cy.go('forward')
```

**See also:** `examples/e2e-testing/commands.md`
