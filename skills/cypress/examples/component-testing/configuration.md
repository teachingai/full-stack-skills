# Component Testing Configuration

## Instructions

This example demonstrates component testing configuration in Cypress.

### Key Concepts

- Dev server configuration
- Spec pattern
- Global setup
- Framework configuration

### Example: Basic Configuration

```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  component: {
    devServer: {
      framework: 'vue',
      bundler: 'vite',
    },
    specPattern: 'src/**/*.cy.{js,jsx,ts,tsx}',
  },
})
```

### Example: Vue with Vite

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

### Example: Vue with Webpack

```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  component: {
    devServer: {
      framework: 'vue',
      bundler: 'webpack',
    },
  },
})
```

### Example: Custom Spec Pattern

```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  component: {
    specPattern: 'components/**/*.spec.{js,jsx,ts,tsx}',
  },
})
```

### Example: Global Setup

```javascript
// cypress/support/component.js
import { mount } from 'cypress/vue'
import './commands'

// Global component mount
Cypress.Commands.add('mount', mount)
```

### Key Points

- Configure devServer for framework and bundler
- Customize specPattern for test files
- Use global setup for shared configuration
- Support for Vue, React, Angular, Svelte
- Works with Vite, Webpack, and other bundlers
