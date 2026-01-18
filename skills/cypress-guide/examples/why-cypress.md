# Why Cypress

## Instructions

This example explains why to use Cypress and its key benefits.

### Key Concepts

- Why Cypress
- Key benefits
- E2E and Component testing
- Comparison with other tools

### Example: Why Use Cypress

Cypress is a next-generation front-end testing tool built for the modern web. It enables you to write tests that can run both in the browser (E2E) and in isolation (Component Testing).

**Key Benefits**:
- **Time Travel**: See exactly what happened at each step
- **Real-time Reloads**: See commands execute in real time
- **Automatic Waiting**: No need for manual waits or sleeps
- **Debugging**: Powerful debugging tools built-in
- **Screenshots & Videos**: Automatic screenshots and video recording

### Example: E2E Testing

```javascript
// Test entire user workflows
describe('User Login', () => {
  it('should login successfully', () => {
    cy.visit('/login')
    cy.get('[data-cy=email]').type('user@example.com')
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=submit]').click()
    cy.url().should('include', '/dashboard')
  })
})
```

### Example: Component Testing

```javascript
// Test Vue components in isolation
import { mount } from 'cypress/vue'
import Button from './Button.vue'

describe('Button Component', () => {
  it('renders correctly', () => {
    mount(Button, {
      props: {
        label: 'Click me'
      }
    })
    cy.get('button').should('contain', 'Click me')
  })
})
```

### Example: Real Browser Testing

```javascript
// Tests run in a real browser
// No need to mock DOM APIs
cy.visit('https://example.com')
cy.get('h1').should('be.visible')
```

### Key Points

- Cypress runs in a real browser
- Supports both E2E and Component testing
- Automatic waiting and retries
- Time-travel debugging
- Great developer experience
- Excellent documentation
