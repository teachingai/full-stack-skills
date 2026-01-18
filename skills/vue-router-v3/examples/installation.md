# Installation

## Instructions

This example demonstrates how to install Vue Router v3 in a Vue 2 project.

### Key Concepts

- npm/yarn installation
- CDN installation
- Vue plugin registration
- Version compatibility

### Example: Install via npm

```bash
npm install vue-router@3
```

### Example: Install via yarn

```bash
yarn add vue-router@3
```

### Example: Install via CDN

```html
<!-- Development version -->
<script src="https://unpkg.com/vue-router@3/dist/vue-router.js"></script>

<!-- Production version -->
<script src="https://unpkg.com/vue-router@3/dist/vue-router.min.js"></script>
```

### Example: Register Vue Router

```javascript
// main.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

// Register Vue Router plugin
Vue.use(VueRouter)

// Create router instance
const router = new VueRouter({
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About }
  ]
})

// Create Vue instance with router
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

### Example: CDN Setup

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/vue@2/dist/vue.js"></script>
  <script src="https://unpkg.com/vue-router@3/dist/vue-router.js"></script>
</head>
<body>
  <div id="app"></div>
  <script>
    Vue.use(VueRouter)
    
    const router = new VueRouter({
      routes: [
        { path: '/', component: { template: '<div>Home</div>' } }
      ]
    })
    
    new Vue({
      router,
      el: '#app',
      template: '<router-view />'
    })
  </script>
</body>
</html>
```

### Key Points

- Vue Router v3 is for Vue 2 applications
- Vue 3 applications should use Vue Router v4
- Must call `Vue.use(VueRouter)` before creating router instance
- Install specific version: `vue-router@3`
- CDN version is available for quick prototyping
