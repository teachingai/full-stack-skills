# Utilities API

## API Reference

Cypress utility functions and helpers.

### Cypress._

Lodash utilities available in Cypress.

**Usage:**
```javascript
Cypress._.debounce(fn, 300)
Cypress._.throttle(fn, 300)
Cypress._.clone(obj)
```

### Cypress.Blob

Blob utilities for file operations.

**Usage:**
```javascript
Cypress.Blob.base64StringToBlob(base64)
Cypress.Blob.blobToBase64String(blob)
```

### Cypress.Promise

Promise utilities.

**Usage:**
```javascript
Cypress.Promise.all([promise1, promise2])
Cypress.Promise.resolve(value)
```

### Cypress.$

jQuery reference for DOM manipulation.

**Usage:**
```javascript
Cypress.$('button').addClass('active')
Cypress.$('.my-class').hide()
```

### Cypress.moment

Moment.js for date manipulation (if installed).

**Usage:**
```javascript
Cypress.moment().format('YYYY-MM-DD')
```

### Example: Using Utilities

```javascript
// Debounce function
const debouncedFn = Cypress._.debounce(() => {
  console.log('Debounced')
}, 300)

// jQuery manipulation
cy.get('button').then(($btn) => {
  Cypress.$($btn).addClass('active')
})
```

**See also:** `examples/e2e-testing/basics.md`
