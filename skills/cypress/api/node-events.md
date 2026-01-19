# Node Events API

## API Reference

Node-level events and tasks in Cypress.

### cy.task()

Run Node tasks from tests.

**Usage:**
```javascript
// cypress.config.js
module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      on('task', {
        log(message) {
          console.log(message)
          return null
        },
        seedDatabase() {
          // Seed database
          return null
        }
      })
    }
  }
})

// Test
cy.task('log', 'Hello from Node')
cy.task('seedDatabase')
```

### Plugin Events

Register plugin event handlers.

**Usage:**
```javascript
// cypress.config.js
module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      on('before:run', (details) => {
        console.log('Before run')
      })
      
      on('after:run', (results) => {
        console.log('After run')
      })
    }
  }
})
```

### File System Operations

Use cy.task() for file operations.

**Usage:**
```javascript
// cypress.config.js
const fs = require('fs')

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      on('task', {
        readFile(filename) {
          return fs.readFileSync(filename, 'utf8')
        }
      })
    }
  }
})

// Test
cy.task('readFile', 'data.json').then((content) => {
  const data = JSON.parse(content)
  // Use data
})
```

**See also:** `examples/getting-started/configuration-choices.md`
