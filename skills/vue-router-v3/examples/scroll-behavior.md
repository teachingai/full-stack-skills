# Scroll Behavior

## Instructions

This example demonstrates custom scroll behavior in Vue Router v3.

### Key Concepts

- Scroll behavior function
- Scroll position restoration
- Smooth scrolling
- Scroll to element

### Example: Basic Scroll Behavior

```javascript
// router/index.js
const router = new VueRouter({
  routes: [...],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
})
```

### Example: Smooth Scrolling

```javascript
const router = new VueRouter({
  routes: [...],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve({ x: 0, y: 0 })
        }, 500)
      })
    }
  }
})
```

### Example: Scroll to Element

```javascript
const router = new VueRouter({
  routes: [...],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        selector: to.hash,
        offset: { x: 0, y: 100 }
      }
    }
    if (savedPosition) {
      return savedPosition
    }
    return { x: 0, y: 0 }
  }
})
```

### Example: Scroll to Element with Delay

```javascript
const router = new VueRouter({
  routes: [...],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve({
            selector: to.hash,
            offset: { x: 0, y: 100 }
          })
        }, 300)
      })
    }
    if (savedPosition) {
      return savedPosition
    }
    return { x: 0, y: 0 }
  }
})
```

### Key Points

- scrollBehavior function controls scroll position
- savedPosition is available when using browser back/forward
- Can return position object or Promise
- Can scroll to element using selector
- Use offset for fine-tuning scroll position
