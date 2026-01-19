# Defining a Store | 定义 Store

## Instructions

This example demonstrates how to define stores using defineStore() with different syntaxes.

### Key Concepts

- defineStore() function
- Store ID
- Options API syntax
- Setup (Composition API) syntax
- Store naming conventions

### Example: Options API Syntax

```javascript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
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

### Example: Setup (Composition API) Syntax

```javascript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  
  const doubleCount = computed(() => count.value * 2)
  
  function increment() {
    count.value++
  }
  
  return { count, doubleCount, increment }
})
```

### Example: Store with ID as First Argument

```javascript
// Using string ID
export const useCounterStore = defineStore('counter', {
  // ...
})

// Using function that returns ID
export const useCounterStore = defineStore(() => 'counter', {
  // ...
})
```

### Example: TypeScript with Options API

```typescript
import { defineStore } from 'pinia'

interface CounterState {
  count: number
}

export const useCounterStore = defineStore('counter', {
  state: (): CounterState => ({
    count: 0
  }),
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

### Example: TypeScript with Setup Syntax

```typescript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref<number>(0)
  
  const doubleCount = computed(() => count.value * 2)
  
  function increment(): void {
    count.value++
  }
  
  return { count, doubleCount, increment }
})
```

### Key Points

- Use `defineStore()` to create stores
- First argument is the store ID (string or function)
- Second argument is store options (object) or setup function
- Options API syntax: object with state, getters, actions
- Setup syntax: function that returns state, getters, actions
- Store ID must be unique
- Use descriptive store names (e.g., `useUserStore`, `useCartStore`)
