# TypeScript | 类型支持

## Instructions

This example demonstrates how to use Pinia with TypeScript for type safety.

### Key Concepts

- TypeScript store definitions
- Typed state
- Typed getters
- Typed actions
- Type inference
- Store types

### Example: Typed Store (Options API)

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
  }),
  getters: {
    isAdult: (state): boolean => state.age >= 18,
    fullInfo: (state): string => `${state.name} (${state.email})`
  },
  actions: {
    updateName(name: string): void {
      this.name = name
    },
    async fetchUser(id: number): Promise<void> {
      const response = await fetch(`/api/users/${id}`)
      const user = await response.json()
      this.name = user.name
      this.age = user.age
      this.email = user.email
    }
  }
})
```

### Example: Typed Store (Setup Syntax)

```typescript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

interface User {
  name: string
  age: number
  email: string
}

export const useUserStore = defineStore('user', () => {
  const user = ref<User | null>(null)
  const loading = ref<boolean>(false)
  
  const isAdult = computed((): boolean => {
    return user.value ? user.value.age >= 18 : false
  })
  
  const fullInfo = computed((): string => {
    if (!user.value) return ''
    return `${user.value.name} (${user.value.email})`
  })
  
  async function fetchUser(id: number): Promise<void> {
    loading.value = true
    try {
      const response = await fetch(`/api/users/${id}`)
      user.value = await response.json()
    } finally {
      loading.value = false
    }
  }
  
  return {
    user,
    loading,
    isAdult,
    fullInfo,
    fetchUser
  }
})
```

### Example: Using Typed Store

```vue
<script setup lang="ts">
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// TypeScript knows the types
userStore.updateName('John') // ✅
// userStore.updateName(123) // ❌ Type error

const isAdult = userStore.isAdult // boolean
const fullInfo = userStore.fullInfo // string
</script>
```

### Key Points

- Define interfaces for state types
- Type getters with return types
- Type actions with parameters and return types
- TypeScript infers types from store definitions
- Use type annotations for better type safety
- Setup syntax also supports full TypeScript typing
