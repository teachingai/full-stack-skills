# State | 状态

## Instructions

This example demonstrates how to define and work with state in Pinia stores.

### Key Concepts

- Defining state
- Accessing state
- Mutating state
- Resetting state
- Replacing state
- State reactivity

### Example: Defining State

```javascript
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    name: 'John',
    age: 30,
    email: 'john@example.com'
  })
})
```

### Example: Accessing State

```vue
<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// Direct access
console.log(userStore.name)

// Or use storeToRefs for destructuring
import { storeToRefs } from 'pinia'
const { name, age } = storeToRefs(userStore)
</script>
```

### Example: Mutating State

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
    setCount(newCount) {
      this.count = newCount
    }
  }
})
```

### Example: Resetting State

```javascript
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    name: '',
    age: 0,
    email: ''
  }),
  actions: {
    reset() {
      this.$reset()
    }
  }
})
```

### Example: Replacing State

```javascript
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    name: '',
    age: 0
  }),
  actions: {
    updateUser(newUser) {
      this.$patch(newUser)
      // Or
      this.$state = { ...this.$state, ...newUser }
    }
  }
})
```

### Example: Using $patch

```javascript
// Patch with object
store.$patch({
  name: 'Jane',
  age: 25
})

// Patch with function
store.$patch((state) => {
  state.items.push({ name: 'shoes', quantity: 1 })
  state.hasChanged = true
})
```

### Example: TypeScript State

```typescript
import { defineStore } from 'pinia'

interface UserState {
  name: string
  age: number
  email: string
}

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    name: '',
    age: 0,
    email: ''
  })
})
```

### Key Points

- State is defined as a function that returns an object
- State is reactive
- Access state via `store.propertyName`
- Mutate state in actions using `this.propertyName`
- Use `$reset()` to reset state to initial values
- Use `$patch()` to update multiple properties
- Use `$state` to replace entire state
- State must be serializable for SSR
