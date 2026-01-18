# Hot Module Replacement (HMR)

## Instructions

This example demonstrates Vite's HMR system and how it works with different file types.

### Key Concepts

- HMR API
- HMR boundaries
- Conditional HMR
- HMR with frameworks

### Example: HMR with Vue

```vue
<!-- Counter.vue -->
<script setup>
import { ref } from 'vue'

const count = ref(0)

// HMR preserves state
console.log('Component loaded')
</script>

<template>
  <button @click="count++">Count: {{ count }}</button>
</template>
```

### Example: HMR API

```javascript
// main.js
if (import.meta.hot) {
  // HMR API available
  import.meta.hot.accept('./counter.js', (newModule) => {
    // Handle update
    console.log('Counter module updated')
  })
  
  // Disconnect
  import.meta.hot.dispose(() => {
    // Cleanup
  })
  
  // Invalidate
  import.meta.hot.invalidate()
}
```

### Example: Conditional HMR

```javascript
// Only accept updates in development
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    if (process.env.NODE_ENV === 'development') {
      // Handle update
    }
  })
}
```

### Key Points

- HMR preserves component state
- CSS updates are instant without page reload
- Vue components support HMR out of the box
- Use `import.meta.hot` API for custom HMR handling
- HMR only works in development mode
