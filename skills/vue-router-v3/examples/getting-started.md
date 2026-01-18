# Getting Started

## Instructions

This example demonstrates basic Vue Router v3 setup and usage.

### Key Concepts

- Router configuration
- Route definition
- Router-link component
- Router-view component
- Basic navigation

### Example: Basic Router Setup

```javascript
// router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import About from '@/views/About.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
]

const router = new VueRouter({
  routes
})

export default router
```

### Example: Main Application

```javascript
// main.js
import Vue from 'vue'
import App from './App.vue'
import router from './router'

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

### Example: App Component

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
    </nav>
    <router-view />
  </div>
</template>
```

### Example: Route Components

```vue
<!-- views/Home.vue -->
<template>
  <div>
    <h1>Home</h1>
    <p>Welcome to the home page</p>
  </div>
</template>

<!-- views/About.vue -->
<template>
  <div>
    <h1>About</h1>
    <p>This is the about page</p>
  </div>
</template>
```

### Key Points

- Use `Vue.use(VueRouter)` to register the plugin
- Define routes in routes array
- Use `<router-link>` for navigation links
- Use `<router-view>` to display matched component
- Router instance must be passed to Vue instance
