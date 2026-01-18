# NPM Dependency Resolving

## Instructions

This example demonstrates how Vite resolves and pre-bundles npm dependencies.

### Key Concepts

- Dependency pre-bundling
- ESM and CommonJS compatibility
- Optimized dependencies
- Excluding dependencies

### Example: Dependency Pre-bundling

```javascript
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  optimizeDeps: {
    // Include dependencies to pre-bundle
    include: ['vue', 'vue-router', 'pinia'],
    
    // Exclude dependencies from pre-bundling
    exclude: ['some-big-dependency'],
    
    // Force include (even if already optimized)
    force: true
  }
})
```

### Example: Auto-detected Dependencies

```javascript
// Vite automatically detects dependencies from:
// - package.json dependencies
// - Imports in source code
// - Dynamic imports
```

### Example: Excluding Dependencies

```javascript
// vite.config.js
export default defineConfig({
  optimizeDeps: {
    exclude: [
      'some-heavy-library',
      '@some/package'
    ]
  }
})
```

### Key Points

- Vite pre-bundles dependencies using esbuild
- Pre-bundling converts CommonJS to ESM
- Dependencies are cached in `node_modules/.vite`
- Use `optimizeDeps.include` to force include
- Use `optimizeDeps.exclude` to exclude from pre-bundling
