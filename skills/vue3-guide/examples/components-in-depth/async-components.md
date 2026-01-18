# Async Components

## Instructions

This example demonstrates async component loading and code splitting.

### Key Concepts

- Lazy loading components
- Async component definition
- Loading and error states
- Code splitting

### Example: Basic Async Component

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

const AsyncComponent = defineAsyncComponent(() =>
  import('./HeavyComponent.vue')
)
</script>

<template>
  <AsyncComponent />
</template>
```

### Example: Async Component with Options

```vue
<script setup>
import { defineAsyncComponent } from 'vue'
import LoadingComponent from './LoadingComponent.vue'
import ErrorComponent from './ErrorComponent.vue'

const AsyncComponent = defineAsyncComponent({
  loader: () => import('./HeavyComponent.vue'),
  loadingComponent: LoadingComponent,
  errorComponent: ErrorComponent,
  delay: 200,
  timeout: 3000,
  onError: (error, retry, fail, attempts) => {
    if (attempts <= 3) {
      retry()
    } else {
      fail()
    }
  }
})
</script>

<template>
  <AsyncComponent />
</template>
```

### Example: Async Component in Router

```javascript
// router/index.js
const routes = [
  {
    path: '/',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/about',
    component: () => import('../views/About.vue')
  }
]
```

### Key Points

- Use async components for code splitting
- Components are loaded on demand
- Provide loading and error components for better UX
- Use in routes for lazy loading pages
