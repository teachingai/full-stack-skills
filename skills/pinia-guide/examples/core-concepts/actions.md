# Actions | 操作

## Instructions

This example demonstrates how to create and use actions in Pinia stores.

### Key Concepts

- Defining actions
- Accessing state and getters in actions
- Accessing other stores
- Async actions
- Action parameters
- Action return values

### Example: Basic Action

```javascript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  actions: {
    increment() {
      this.count++
    },
    decrement() {
      this.count--
    },
    reset() {
      this.count = 0
    }
  }
})
```

### Example: Action with Parameters

```javascript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  actions: {
    incrementBy(amount) {
      this.count += amount
    },
    setCount(newCount) {
      this.count = newCount
    }
  }
})
```

### Example: Accessing Getters in Actions

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
    incrementToDouble() {
      // Access getter using 'this'
      this.count = this.doubleCount
    }
  }
})
```

### Example: Async Actions

```javascript
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    loading: false,
    error: null
  }),
  actions: {
    async fetchUser(userId) {
      this.loading = true
      this.error = null
      try {
        const response = await fetch(`/api/users/${userId}`)
        const user = await response.json()
        this.user = user
      } catch (error) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    }
  }
})
```

### Example: Accessing Other Stores

```javascript
import { defineStore } from 'pinia'
import { useAuthStore } from './auth'

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: []
  }),
  actions: {
    async addItem(item) {
      // Access another store
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        throw new Error('User must be authenticated')
      }
      this.items.push({ ...item, userId: authStore.userId })
    }
  }
})
```

### Example: Action Return Values

```javascript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  actions: {
    increment() {
      this.count++
      return this.count
    },
    async fetchData() {
      const response = await fetch('/api/data')
      const data = await response.json()
      return data
    }
  }
})
```

### Example: Action in Setup Syntax

```javascript
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  
  function increment() {
    count.value++
  }
  
  async function fetchData() {
    const response = await fetch('/api/data')
    const data = await response.json()
    return data
  }
  
  return { count, increment, fetchData }
})
```

### Example: TypeScript Actions

```typescript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  actions: {
    incrementBy(amount: number): void {
      this.count += amount
    },
    async fetchData(): Promise<any> {
      const response = await fetch('/api/data')
      return response.json()
    }
  }
})
```

### Key Points

- Actions are methods for mutating state and performing side effects
- Actions can be synchronous or asynchronous
- Access state and getters using `this`
- Actions can access other stores
- Actions can accept parameters and return values
- Actions are called like regular functions
- Use async/await for asynchronous operations
- Actions can throw errors
