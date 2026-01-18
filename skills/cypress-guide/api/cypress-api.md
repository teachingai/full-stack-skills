# Cypress API

## API Reference

Global Cypress API for configuration and utilities.

### Cypress.config()

Get or set configuration values.

**Usage:**
```javascript
// Get config
Cypress.config('baseUrl')

// Set config
Cypress.config('baseUrl', 'https://example.com')
```

### Cypress.env()

Get or set environment variables.

**Usage:**
```javascript
// Get env
Cypress.env('apiUrl')

// Set env
Cypress.env('apiUrl', 'https://api.example.com')
```

### Cypress.Commands

Add custom commands.

**Usage:**
```javascript
Cypress.Commands.add('login', (email, password) => {
  cy.visit('/login')
  cy.get('[data-cy=email]').type(email)
  cy.get('[data-cy=password]').type(password)
  cy.get('[data-cy=submit]').click()
})

// Use custom command
cy.login('user@example.com', 'password123')
```

### Cypress.version

Get Cypress version.

**Usage:**
```javascript
Cypress.version // '13.0.0'
```

### Cypress.platform

Get platform information.

**Usage:**
```javascript
Cypress.platform // 'darwin', 'linux', 'win32'
```

### Cypress.browser

Get browser information.

**Usage:**
```javascript
Cypress.browser.name // 'chrome', 'firefox', 'electron'
Cypress.browser.version // '120.0.0'
```

**See also:** `examples/getting-started/configuration-choices.md`
