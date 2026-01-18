# Creating an Application

## Instructions

This example demonstrates how to create a Vue 3 application using different methods.

### Key Concepts

- Creating an app instance with `createApp()`
- Mounting the app to the DOM
- Application configuration
- Global properties and components

### Example: Basic App Creation

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

app.mount('#app')
```

### Example: App with Configuration

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

// Configure global properties
app.config.globalProperties.$http = axios
app.config.globalProperties.$message = 'Hello Vue 3'

// Register global components
app.component('MyComponent', MyComponent)

// Use plugins
app.use(router)
app.use(pinia)

app.mount('#app')
```

### Example: Multiple App Instances

```javascript
// Create multiple independent apps
const app1 = createApp(App1)
app1.mount('#app1')

const app2 = createApp(App2)
app2.mount('#app2')
```

### Example: App with Root Component

```vue
<!-- App.vue -->
<script setup>
import { ref } from 'vue'

const message = ref('Hello Vue 3!')
</script>

<template>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>
</template>
```

### Key Points

- Use `createApp()` to create an app instance
- Call `mount()` to mount the app to a DOM element
- Configure the app before mounting
- Each app instance is independent
