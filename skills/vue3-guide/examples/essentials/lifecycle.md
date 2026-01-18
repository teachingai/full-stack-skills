# Lifecycle

## Instructions

This example demonstrates component lifecycle hooks in Vue 3 Composition API.

### Key Concepts

- Lifecycle hooks in Composition API
- Lifecycle stages
- When to use each hook
- Cleanup in lifecycle hooks

### Example: All Lifecycle Hooks

```vue
<script setup>
import {
  onBeforeMount,
  onMounted,
  onBeforeUpdate,
  onUpdated,
  onBeforeUnmount,
  onUnmounted
} from 'vue'

onBeforeMount(() => {
  console.log('Before mount - component is about to be mounted')
})

onMounted(() => {
  console.log('Mounted - component is mounted to DOM')
  // Good for: API calls, DOM manipulation, setting up subscriptions
})

onBeforeUpdate(() => {
  console.log('Before update - component is about to update')
})

onUpdated(() => {
  console.log('Updated - component has been updated')
  // Good for: DOM updates after state change
})

onBeforeUnmount(() => {
  console.log('Before unmount - component is about to be unmounted')
  // Good for: cleanup before unmount
})

onUnmounted(() => {
  console.log('Unmounted - component has been unmounted')
  // Good for: cleanup (timers, subscriptions, event listeners)
})
</script>

<template>
  <div>Lifecycle Example</div>
</template>
```

### Example: Lifecycle with API Calls

```vue
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const data = ref(null)
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    const response = await fetch('/api/data')
    data.value = await response.json()
  } catch (error) {
    console.error('Failed to fetch data:', error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else>{{ data }}</div>
  </div>
</template>
```

### Example: Lifecycle with Cleanup

```vue
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const count = ref(0)
let timer = null

onMounted(() => {
  timer = setInterval(() => {
    count.value++
  }, 1000)
})

onUnmounted(() => {
  if (timer) {
    clearInterval(timer)
  }
})
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
  </div>
</template>
```

### Example: Lifecycle with Event Listeners

```vue
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const x = ref(0)
const y = ref(0)

function updateMousePosition(event) {
  x.value = event.pageX
  y.value = event.pageY
}

onMounted(() => {
  window.addEventListener('mousemove', updateMousePosition)
})

onUnmounted(() => {
  window.removeEventListener('mousemove', updateMousePosition)
})
</script>

<template>
  <div>
    <p>Mouse position: {{ x }}, {{ y }}</p>
  </div>
</template>
```

### Lifecycle Diagram

```
setup() / beforeCreate
  ↓
created
  ↓
onBeforeMount / beforeMount
  ↓
onMounted / mounted
  ↓
onBeforeUpdate / beforeUpdate (when data changes)
  ↓
onUpdated / updated
  ↓
onBeforeUnmount / beforeUnmount
  ↓
onUnmounted / unmounted
```

### Key Points

- Use `onMounted` for initialization that needs DOM access
- Use `onUnmounted` for cleanup (timers, subscriptions, event listeners)
- Lifecycle hooks are registered during `setup()`
- Hooks are called in order
- Always clean up side effects in `onUnmounted`
