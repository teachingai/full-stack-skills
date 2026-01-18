# Reactivity Fundamentals

## Instructions

This example demonstrates Vue 3's reactivity system using `ref()` and `reactive()`.

### Key Concepts

- Creating reactive state with `ref()`
- Creating reactive objects with `reactive()`
- Accessing reactive values
- Reactive vs non-reactive

### Example: Using ref()

```vue
<script setup>
import { ref } from 'vue'

// Primitive values
const count = ref(0)
const message = ref('Hello Vue 3')

// Objects (ref wraps the object)
const user = ref({
  name: 'Vue',
  age: 3
})

// Access with .value in script
console.log(count.value)      // 0
count.value++
console.log(count.value)       // 1

console.log(user.value.name)   // 'Vue'
user.value.name = 'Vue 3'
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Message: {{ message }}</p>
    <p>User: {{ user.name }} ({{ user.age }})</p>
    <button @click="count++">Increment</button>
  </div>
</template>
```

### Example: Using reactive()

```vue
<script setup>
import { reactive } from 'vue'

const state = reactive({
  count: 0,
  message: 'Hello Vue 3',
  user: {
    name: 'Vue',
    age: 3
  }
})

// Direct access (no .value)
state.count++
state.user.name = 'Vue 3'
</script>

<template>
  <div>
    <p>Count: {{ state.count }}</p>
    <p>Message: {{ state.message }}</p>
    <p>User: {{ state.user.name }} ({{ state.user.age }})</p>
    <button @click="state.count++">Increment</button>
  </div>
</template>
```

### Example: ref() vs reactive()

```vue
<script setup>
import { ref, reactive } from 'vue'

// ref() - can reassign
const count = ref(0)
count.value = 10  // OK

// reactive() - cannot reassign
const state = reactive({ count: 0 })
// state = { count: 10 }  // ❌ This won't work

// ref() with object
const userRef = ref({ name: 'Vue' })
userRef.value.name = 'Vue 3'  // OK
userRef.value = { name: 'Vue 4' }  // OK - can reassign

// reactive() with object
const userReactive = reactive({ name: 'Vue' })
userReactive.name = 'Vue 3'  // OK
// userReactive = { name: 'Vue 4' }  // ❌ Cannot reassign
</script>
```

### Example: Destructuring Reactive Objects

```vue
<script setup>
import { reactive, toRefs } from 'vue'

const state = reactive({
  count: 0,
  name: 'Vue'
})

// ❌ Destructuring loses reactivity
// const { count, name } = state

// ✅ Use toRefs to maintain reactivity
const { count, name } = toRefs(state)

// Now count and name are refs
count.value++
name.value = 'Vue 3'
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Name: {{ name }}</p>
  </div>
</template>
```

### Key Points

- `ref()` creates reactive references for any value type
- `reactive()` creates reactive proxies for objects/arrays
- Use `.value` to access `ref()` values in script
- `reactive()` values are accessed directly
- Both auto-unwrap in templates
- Use `toRefs()` when destructuring reactive objects
