# Dependency Pre-bundling

## Instructions

This example demonstrates dependency pre-bundling configuration in Vite.

### Key Concepts

- Pre-bundling process
- Optimize dependencies
- Include/exclude dependencies
- Force re-bundling

### Example: Basic Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  optimizeDeps: {
    // Dependencies to include
    include: ['vue', 'vue-router', 'pinia'],
    
    // Dependencies to exclude
    exclude: ['some-heavy-library'],
    
    // Force re-bundling
    force: true
  }
})
```

### Example: Custom esbuild Options

```javascript
export default defineConfig({
  optimizeDeps: {
    esbuildOptions: {
      target: 'es2020',
      plugins: [
        // Custom esbuild plugins
      ]
    }
  }
})
```

### Example: Entry Points

```javascript
export default defineConfig({
  optimizeDeps: {
    entries: [
      './src/main.js',
      './src/admin.js'
    ]
  }
})
```

### Example: Excluding from Pre-bundling

```javascript
export default defineConfig({
  optimizeDeps: {
    exclude: [
      'some-big-dependency',
      '@some/package'
    ]
  }
})
```

### Key Points

- Pre-bundling converts CommonJS to ESM
- Cached in `node_modules/.vite`
- Use `include` to force include dependencies
- Use `exclude` to skip pre-bundling
- Use `force: true` to re-bundle
