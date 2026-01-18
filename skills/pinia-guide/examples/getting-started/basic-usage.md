# Basic Usage | 基本用法

## Instructions

This example demonstrates basic store usage in Vue components.

### Key Concepts

- Creating a store
- Accessing store in components
- Using state, getters, and actions
- Store reactivity

### Example: Creating a Store

```javascript
// stores/counter.js
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

### Example: Using Store in Component (Composition API)

```vue
<template>
  <div>
    <p>Count: {{ counterStore.count }}</p>
    <p>Double: {{ counterStore.doubleCount }}</p>
    <button @click="counterStore.increment">Increment</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const counterStore = useCounterStore()
</script>
```

### Example: Using Store in Component (Options API)

```vue
<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
import { useCounterStore } from '@/stores/counter'
import { mapState, mapGetters, mapActions } from 'pinia'

export default {
  computed: {
    ...mapState(useCounterStore, ['count']),
    ...mapGetters(useCounterStore, ['doubleCount'])
  },
  methods: {
    ...mapActions(useCounterStore, ['increment'])
  }
}
</script>
```

### Example: Destructuring Store

```vue
<script setup>
import { useCounterStore } from '@/stores/counter'
import { storeToRefs } from 'pinia'

const counterStore = useCounterStore()
// Destructure state and getters (maintains reactivity)
const { count, doubleCount } = storeToRefs(counterStore)
// Actions can be destructured directly
const { increment } = counterStore
</script>
```

### Key Points

- Use `defineStore()` to create stores
- Use `useStore()` to access stores in components
- Stores are reactive
- Use `storeToRefs()` to destructure state and getters
- Actions can be destructured directly
- Works with both Composition API and Options API
