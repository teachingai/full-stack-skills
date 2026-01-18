# Optimize Dependencies

## Instructions

This example demonstrates optimizing dependencies for better performance.

### Key Concepts

- Dependency optimization
- Pre-bundling strategy
- Cache management
- Performance tuning

### Example: Optimize Common Dependencies

```javascript
// vite.config.js
export default defineConfig({
  optimizeDeps: {
    include: [
      'vue',
      'vue-router',
      'pinia',
      'axios',
      'lodash-es'
    ]
  }
})
```

### Example: Exclude Heavy Dependencies

```javascript
export default defineConfig({
  optimizeDeps: {
    exclude: [
      'some-very-large-library',
      '@monaco-editor/react'
    ]
  }
})
```

### Example: Custom Optimization

```javascript
export default defineConfig({
  optimizeDeps: {
    include: ['vue'],
    esbuildOptions: {
      target: 'es2020'
    },
    force: false  // Only re-bundle when needed
  }
})
```

### Example: Multiple Entry Points

```javascript
export default defineConfig({
  optimizeDeps: {
    entries: [
      'src/main.js',
      'src/admin.js',
      'src/mobile.js'
    ]
  }
})
```

### Key Points

- Pre-bundle frequently used dependencies
- Exclude large dependencies that don't need optimization
- Use `force: true` only when needed
- Configure entry points for better detection
- Cache is stored in `node_modules/.vite`
