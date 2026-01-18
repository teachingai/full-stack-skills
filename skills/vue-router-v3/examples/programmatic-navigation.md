# Programmatic Navigation

## Instructions

This example demonstrates programmatic navigation using router methods.

### Key Concepts

- router.push()
- router.replace()
- router.go()
- router.back()
- router.forward()
- Navigation with parameters

### Example: Basic Push Navigation

```javascript
// In component methods
methods: {
  goToAbout() {
    this.$router.push('/about')
  }
}
```

### Example: Push with Object

```javascript
methods: {
  goToUser() {
    this.$router.push({
      path: '/user',
      query: { id: '123' }
    })
  },
  
  goToUserByName() {
    this.$router.push({
      name: 'user',
      params: { id: '123' }
    })
  }
}
```

### Example: Replace Navigation

```javascript
methods: {
  replaceToAbout() {
    // Replace current history entry
    this.$router.replace('/about')
  },
  
  replaceWithObject() {
    this.$router.replace({
      name: 'user',
      params: { id: '123' }
    })
  }
}
```

### Example: History Navigation

```javascript
methods: {
  goBack() {
    this.$router.go(-1)  // Go back one step
  },
  
  goForward() {
    this.$router.go(1)  // Go forward one step
  },
  
  goBackMethod() {
    this.$router.back()  // Equivalent to go(-1)
  },
  
  goForwardMethod() {
    this.$router.forward()  // Equivalent to go(1)
  }
}
```

### Example: Navigation with Query

```javascript
methods: {
  navigateWithQuery() {
    this.$router.push({
      path: '/search',
      query: {
        q: 'vue',
        page: 1
      }
    })
    // Results in: /search?q=vue&page=1
  }
}
```

### Example: Navigation with Hash

```javascript
methods: {
  navigateWithHash() {
    this.$router.push({
      path: '/about',
      hash: '#section1'
    })
    // Results in: /about#section1
  }
}
```

### Key Points

- Use `$router.push()` to navigate and add history entry
- Use `$router.replace()` to navigate without adding history
- Use `$router.go(n)` to move n steps in history
- Navigation can use path string or route object
- Query and hash can be included in navigation
