# SSR Options

## Instructions

This example demonstrates Server-Side Rendering (SSR) configuration options.

### Key Concepts

- SSR external dependencies
- SSR target
- SSR resolve conditions
- SSR noExternal

### Example: Basic SSR Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  ssr: {
    // Dependencies to externalize (not bundled)
    external: ['vue', 'vue-router'],
    
    // Dependencies to NOT externalize (bundled)
    noExternal: ['some-package'],
    
    // Target environment
    target: 'node',
    
    // Resolve conditions
    resolve: {
      conditions: ['node', 'import']
    }
  }
})
```

### Example: SSR with noExternal

```javascript
export default defineConfig({
  ssr: {
    // Bundle these packages instead of externalizing
    noExternal: [
      'element-plus',
      'some-esm-only-package'
    ]
  }
})
```

### Example: SSR Target Options

```javascript
export default defineConfig({
  ssr: {
    // Target can be 'node' or 'webworker'
    target: 'node',
    
    // Format can be 'esm' or 'cjs'
    format: 'esm'
  }
})
```

### Example: SSR Resolve Conditions

```javascript
export default defineConfig({
  ssr: {
    resolve: {
      // Conditions for package.json exports
      conditions: ['node', 'import', 'default']
    }
  }
})
```

### Key Points

- `ssr.external` lists packages to externalize
- `ssr.noExternal` forces bundling of specific packages
- `ssr.target` sets the target environment
- `ssr.resolve.conditions` controls package resolution
- SSR builds are separate from client builds
