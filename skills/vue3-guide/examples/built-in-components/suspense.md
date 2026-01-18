# Suspense

## Instructions

This example demonstrates how to use the `<Suspense>` component for handling async dependencies in Vue 3.

### Key Concepts

- Suspense component
- Async components
- Fallback content
- Error handling
- Nested suspense

### Example: Basic Suspense

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

const AsyncComponent = defineAsyncComponent(() => import('./AsyncComponent.vue'))
</script>

<template>
  <Suspense>
    <template #default>
      <AsyncComponent />
    </template>
    <template #fallback>
      <div>Loading...</div>
    </template>
  </Suspense>
</template>
```

### Example: Suspense with Async Setup

```vue
<!-- AsyncComponent.vue -->
<script setup>
const data = await fetch('/api/data').then(r => r.json())
</script>

<template>
  <div>{{ data.message }}</div>
</template>
```

### Example: Suspense with Error Handling

```vue
<script setup>
import { onErrorCaptured } from 'vue'
import { defineAsyncComponent } from 'vue'

const AsyncComponent = defineAsyncComponent(() => import('./AsyncComponent.vue'))

const error = ref(null)

onErrorCaptured((err) => {
  error.value = err
  return false
})
</script>

<template>
  <div v-if="error">Error: {{ error.message }}</div>
  <Suspense v-else>
    <template #default>
      <AsyncComponent />
    </template>
    <template #fallback>
      <div>Loading...</div>
    </template>
  </Suspense>
</template>
```

### Example: Nested Suspense

```vue
<template>
  <Suspense>
    <template #default>
      <ParentComponent />
    </template>
    <template #fallback>
      <div>Loading parent...</div>
    </template>
  </Suspense>
</template>

<!-- ParentComponent.vue -->
<template>
  <Suspense>
    <template #default>
      <ChildComponent />
    </template>
    <template #fallback>
      <div>Loading child...</div>
    </template>
  </Suspense>
</template>
```

### Key Points

- `<Suspense>` handles async component loading
- Requires async component or async setup
- `#default` slot contains async content
- `#fallback` slot shows loading state
- Use `onErrorCaptured` for error handling
