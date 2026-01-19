# Styling Components

## Instructions

This example demonstrates how to handle styling in component tests.

### Key Concepts

- Loading styles
- CSS modules
- Global styles
- Style testing

### Example: Loading Global Styles

```javascript
// Button.cy.js
import { mount } from 'cypress/vue'
import Button from './Button.vue'
import './styles.css' // Load global styles

describe('Button Component', () => {
  it('has correct styles', () => {
    mount(Button)
    cy.get('button').should('have.css', 'background-color', 'rgb(0, 0, 255)')
  })
})
```

### Example: CSS Modules

```javascript
// Button.cy.js
import { mount } from 'cypress/vue'
import Button from './Button.vue'
import styles from './Button.module.css'

describe('Button Component', () => {
  it('applies CSS module classes', () => {
    mount(Button)
    cy.get('button').should('have.class', styles.button)
  })
})
```

### Example: Testing Computed Styles

```javascript
// Card.cy.js
import { mount } from 'cypress/vue'
import Card from './Card.vue'

describe('Card Component', () => {
  it('has correct dimensions', () => {
    mount(Card)
    cy.get('.card').then(($el) => {
      const width = $el.width()
      const height = $el.height()
      expect(width).to.be.greaterThan(0)
      expect(height).to.be.greaterThan(0)
    })
  })
})
```

### Example: Visual Testing

```javascript
// Button.cy.js
import { mount } from 'cypress/vue'
import Button from './Button.vue'

describe('Button Component', () => {
  it('matches visual snapshot', () => {
    mount(Button, {
      props: {
        label: 'Click me'
      }
    })
    cy.get('button').matchImageSnapshot()
  })
})
```

### Key Points

- Import styles in test files
- Test computed styles with cy.should()
- CSS modules are supported
- Global styles can be loaded
- Visual testing with snapshots
