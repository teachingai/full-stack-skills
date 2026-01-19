# Vue Component Testing Examples

## Instructions

This example demonstrates Vue component testing with Cypress.

### Key Concepts

- Mounting Vue components
- Passing props
- Testing events
- Testing slots
- Testing user interactions

### Example: Basic Component Mount

```javascript
// Button.cy.js
import { mount } from 'cypress/vue'
import Button from './Button.vue'

describe('Button Component', () => {
  it('renders', () => {
    mount(Button)
    cy.get('button').should('be.visible')
  })
})
```

### Example: Mounting with Props

```javascript
// Button.cy.js
import { mount } from 'cypress/vue'
import Button from './Button.vue'

describe('Button Component', () => {
  it('displays label prop', () => {
    mount(Button, {
      props: {
        label: 'Click me'
      }
    })
    cy.get('button').should('contain', 'Click me')
  })
})
```

### Example: Testing Events

```javascript
// Button.cy.js
import { mount } from 'cypress/vue'
import Button from './Button.vue'

describe('Button Component', () => {
  it('emits click event', () => {
    mount(Button, {
      props: {
        label: 'Click me'
      }
    })
    cy.get('button').click()
    // Assert event was emitted
  })
})
```

### Example: Testing Slots

```javascript
// Card.cy.js
import { mount } from 'cypress/vue'
import Card from './Card.vue'

describe('Card Component', () => {
  it('renders slot content', () => {
    mount(Card, {
      slots: {
        default: 'Card content'
      }
    })
    cy.get('.card').should('contain', 'Card content')
  })
})
```

### Example: Testing User Interactions

```javascript
// Form.cy.js
import { mount } from 'cypress/vue'
import Form from './Form.vue'

describe('Form Component', () => {
  it('handles form submission', () => {
    mount(Form)
    cy.get('[data-cy=email]').type('user@example.com')
    cy.get('[data-cy=submit]').click()
    cy.get('[data-cy=success]').should('be.visible')
  })
})
```

### Key Points

- Use cy.mount() to mount Vue components
- Pass props via mount options
- Test events and user interactions
- Support for slots
- Real browser environment
