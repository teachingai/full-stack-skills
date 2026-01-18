# State Management

## Instructions

This example demonstrates state management with Pinia.

### Key Concepts

- Pinia stores
- State, getters, actions
- Using stores in components

### Example: Store Definition

```javascript
// stores/counter.js
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  getters: {
    doubleCount: (state) => state.count * 2
  },
  actions: {
    increment() {
      this.count++
    }
  }
})
```

### Key Points

- Pinia is the official state management library
- Stores have state, getters, and actions
- Use `storeToRefs` when destructuring to maintain reactivity
