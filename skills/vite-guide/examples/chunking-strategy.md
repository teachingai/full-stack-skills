# Chunking Strategy

## Instructions

This example demonstrates code splitting and chunking strategies in Vite.

### Key Concepts

- Manual chunks
- Automatic chunking
- Vendor splitting
- Route-based splitting

### Example: Manual Chunks

```javascript
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          'ui-vendor': ['element-plus'],
          'utils': ['./src/utils']
        }
      }
    }
  }
})
```

### Example: Function-based Chunking

```javascript
build: {
  rollupOptions: {
    output: {
      manualChunks: (id) => {
        // Split node_modules
        if (id.includes('node_modules')) {
          // Split by package
          if (id.includes('vue')) {
            return 'vue-vendor'
          }
          if (id.includes('element-plus')) {
            return 'ui-vendor'
          }
          // Other vendor
          return 'vendor'
        }
        
        // Split by directory
        if (id.includes('/src/utils/')) {
          return 'utils'
        }
        if (id.includes('/src/components/')) {
          return 'components'
        }
      }
    }
  }
}
```

### Example: Route-based Chunking

```javascript
// Automatic route-based splitting with dynamic imports
const routes = [
  {
    path: '/',
    component: () => import('./views/Home.vue')  // Creates separate chunk
  },
  {
    path: '/about',
    component: () => import('./views/About.vue')  // Creates separate chunk
  }
]
```

### Key Points

- Use `manualChunks` for custom chunking
- Split vendor code from application code
- Route-based splitting happens automatically with dynamic imports
- Balance chunk size for optimal loading
