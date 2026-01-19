# Getters | 计算属性

## Instructions

This example demonstrates how to create and use getters in Pinia stores.

### Key Concepts

- Defining getters
- Accessing other getters
- Passing arguments to getters
- Accessing other stores in getters
- Getters with TypeScript

### Example: Basic Getter

```javascript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  getters: {
    doubleCount: (state) => state.count * 2,
    tripleCount: (state) => state.count * 3
  }
})
```

### Example: Accessing Other Getters

```javascript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  getters: {
    doubleCount: (state) => state.count * 2,
    // Access other getters using 'this'
    quadrupleCount() {
      return this.doubleCount * 2
    }
  }
})
```

### Example: Passing Arguments to Getters

```javascript
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [
      { id: 1, name: 'Apple', price: 1.5 },
      { id: 2, name: 'Banana', price: 2.0 }
    ]
  }),
  getters: {
    // Getter that returns a function
    getItemById: (state) => {
      return (itemId) => state.items.find(item => item.id === itemId)
    },
    // Or using arrow function
    getItemByPrice: (state) => (minPrice) => {
      return state.items.filter(item => item.price >= minPrice)
    }
  }
})
```

### Example: Using Getter with Arguments

```vue
<script setup>
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()

// Call getter with argument
const item = cartStore.getItemById(1)
const expensiveItems = cartStore.getItemByPrice(1.5)
</script>
```

### Example: Accessing Other Stores

```javascript
import { defineStore } from 'pinia'
import { useUserStore } from './user'

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: []
  }),
  getters: {
    // Access another store
    userCartItems() {
      const userStore = useUserStore()
      return this.items.filter(item => item.userId === userStore.userId)
    }
  }
})
```

### Example: TypeScript Getters

```typescript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  getters: {
    doubleCount: (state): number => state.count * 2,
    getCountByMultiplier: (state) => {
      return (multiplier: number): number => state.count * multiplier
    }
  }
})
```

### Example: Getter in Setup Syntax

```javascript
import { defineStore } from 'pinia'
import { computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  
  const doubleCount = computed(() => count.value * 2)
  
  const getCountByMultiplier = computed(() => {
    return (multiplier) => count.value * multiplier
  })
  
  return { count, doubleCount, getCountByMultiplier }
})
```

### Key Points

- Getters are computed properties for stores
- Getters receive state as first parameter
- Access other getters using `this`
- Getters can return functions to accept arguments
- Getters can access other stores
- Getters are cached and only recompute when dependencies change
- Use computed() in setup syntax
