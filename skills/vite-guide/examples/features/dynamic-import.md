# Dynamic Import

## Instructions

This example demonstrates dynamic imports and code splitting in Vite.

### Key Concepts

- Dynamic import syntax
- Code splitting
- Lazy loading
- Route-based splitting

### Example: Basic Dynamic Import

```javascript
// Dynamic import
const module = await import('./module.js')
console.log(module.default)
```

### Example: Route-based Code Splitting

```javascript
// router/index.js
const routes = [
  {
    path: '/',
    component: () => import('./views/Home.vue')
  },
  {
    path: '/about',
    component: () => import('./views/About.vue')
  }
]
```

### Example: Conditional Dynamic Import

```javascript
async function loadComponent(condition) {
  if (condition) {
    const { default: ComponentA } = await import('./ComponentA.vue')
    return ComponentA
  } else {
    const { default: ComponentB } = await import('./ComponentB.vue')
    return ComponentB
  }
}
```

### Example: Dynamic Import with Variables

```javascript
// Use template literals for dynamic paths
const componentName = 'MyComponent'
const component = await import(`./components/${componentName}.vue`)
```

### Example: Preloading

```javascript
// Preload module
const link = document.createElement('link')
link.rel = 'modulepreload'
link.href = '/path/to/module.js'
document.head.appendChild(link)
```

### Key Points

- Dynamic imports create separate chunks
- Use for route-based code splitting
- Supports template literals for dynamic paths
- Modules are loaded on-demand
- Vite automatically handles chunk naming
