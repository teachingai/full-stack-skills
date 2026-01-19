# Configuration Choices

## Instructions

This example demonstrates configuration choices in Cypress.

### Key Concepts

- E2E vs Component Testing
- Configuration file
- Testing types
- Framework detection

### Example: E2E Testing

```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    baseUrl: 'http://localhost:3000',
    specPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
  },
})
```

### Example: Component Testing

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

### Example: Both E2E and Component Testing

```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    // E2E config
  },
  component: {
    // Component config
  },
})
```

### Example: TypeScript Configuration

```typescript
// cypress.config.ts
import { defineConfig } from 'cypress'

export default defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
})
```

### Key Points

- E2E tests run against a running app
- Component tests run components in isolation
- Can use both in same project
- Framework auto-detection for component testing
- Configure via cypress.config.js/ts
