# Routing

## Instructions

This example demonstrates routing setup with Vue Router.

### Key Concepts

- Vue Router setup
- Route configuration
- Navigation
- Route guards

### Example: Router Setup

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  { path: '/', component: Home }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

### Key Points

- Use Vue Router for client-side routing
- Configure routes with path and component
- Use `router-link` and `router-view` components
- Navigation guards for route protection
