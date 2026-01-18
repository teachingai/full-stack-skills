# Navigation Guards

## Instructions

This example demonstrates navigation guards in Vue Router v3.

### Key Concepts

- Global guards
- Per-route guards
- Component guards
- Guard execution order
- Navigation control

### Example: Global Before Guard

```javascript
// router/index.js
const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  // Check authentication
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated()) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})
```

### Example: Global Resolve Guard

```javascript
router.beforeResolve((to, from, next) => {
  // Called after beforeRouteEnter and beforeRouteUpdate
  // Useful for data fetching
  next()
})
```

### Example: Global After Hook

```javascript
router.afterEach((to, from) => {
  // Called after navigation is confirmed
  // No next() function, cannot affect navigation
  // Useful for analytics, page tracking
  console.log('Navigated to:', to.path)
})
```

### Example: Per-Route Guard

```javascript
// router/index.js
const routes = [
  {
    path: '/admin',
    component: Admin,
    beforeEnter: (to, from, next) => {
      if (isAdmin()) {
        next()
      } else {
        next('/')
      }
    }
  }
]
```

### Example: Component Guards

```vue
<script>
export default {
  beforeRouteEnter(to, from, next) {
    // Called before component is created
    // Cannot access this
    // Can call next(vm => {}) to access component instance
    next(vm => {
      vm.loadData()
    })
  },
  
  beforeRouteUpdate(to, from, next) {
    // Called when route changes but component is reused
    // Can access this
    this.userId = to.params.id
    next()
  },
  
  beforeRouteLeave(to, from, next) {
    // Called when leaving the route
    // Can access this
    if (this.hasUnsavedChanges) {
      if (confirm('Leave without saving?')) {
        next()
      } else {
        next(false)
      }
    } else {
      next()
    }
  }
}
</script>
```

### Example: Navigation Control

```javascript
router.beforeEach((to, from, next) => {
  // Allow navigation
  next()
  
  // Cancel navigation
  next(false)
  
  // Redirect
  next('/login')
  
  // Redirect with object
  next({
    path: '/login',
    query: { redirect: to.fullPath }
  })
  
  // Error
  next(new Error('Navigation error'))
})
```

### Key Points

- Global guards: beforeEach, beforeResolve, afterEach
- Per-route guard: beforeEnter
- Component guards: beforeRouteEnter, beforeRouteUpdate, beforeRouteLeave
- Guards are executed in specific order
- Use next() to control navigation flow
