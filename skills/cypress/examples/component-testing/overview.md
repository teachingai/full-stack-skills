# Component Testing Overview

## Instructions

This example provides an overview of component testing in Cypress.

### Key Concepts

- Component testing
- Framework support
- Mounting components
- Testing in isolation

### Example: What is Component Testing

Component testing allows you to test individual components in isolation, without needing to run the entire application.

**Supported Frameworks**:
- Vue 2 & 3
- React
- Angular
- Svelte

### Example: Vue Component Testing Setup

```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  component: {
    devServer: {
      framework: 'vue',
      bundler: 'vite',
    },
  },
})
```

### Example: React Component Testing Setup

```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  component: {
    devServer: {
      framework: 'create-react-app',
      bundler: 'webpack',
    },
  },
})
```

### Example: Basic Component Test

```javascript
// Button.cy.js
import { mount } from 'cypress/vue'
import Button from './Button.vue'

describe('Button', () => {
  it('renders', () => {
    mount(Button)
    cy.get('button').should('be.visible')
  })
})
```

### Key Points

- Test components in isolation
- Supports multiple frameworks
- Uses cy.mount() to mount components
- Runs in real browser
- Can test user interactions
