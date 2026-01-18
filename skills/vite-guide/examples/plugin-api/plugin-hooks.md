# Plugin Hooks

## Instructions

This example demonstrates plugin hooks and their usage.

### Key Concepts

- Build hooks
- Transform hooks
- Resolve hooks
- Output generation hooks

### Example: Build Hooks

```javascript
export default function myPlugin() {
  return {
    name: 'my-plugin',
    
    // Called at the start of the build
    buildStart() {
      console.log('Build started')
    },
    
    // Called at the end of the build
    buildEnd(err) {
      if (err) {
        console.error('Build failed:', err)
      } else {
        console.log('Build completed')
      }
    },
    
    // Called when build is aborted
    closeBundle() {
      console.log('Bundle closed')
    }
  }
}
```

### Example: Transform Hooks

```javascript
export default function transformPlugin() {
  return {
    name: 'transform-plugin',
    
    // Transform code
    transform(code, id) {
      if (id.endsWith('.custom')) {
        return {
          code: code.replace(/CUSTOM/g, 'REPLACED'),
          map: null // or provide source map
        }
      }
    },
    
    // Transform index.html
    transformIndexHtml(html) {
      return html.replace(
        '<title>',
        '<title>My App - '
      )
    }
  }
}
```

### Example: Resolve Hooks

```javascript
export default function resolvePlugin() {
  return {
    name: 'resolve-plugin',
    
    // Resolve module IDs
    resolveId(id, importer) {
      if (id === 'virtual-module') {
        return id // Return id to claim it
      }
      return null // Let other plugins handle it
    },
    
    // Load resolved modules
    load(id) {
      if (id === 'virtual-module') {
        return 'export default "Virtual module content"'
      }
    }
  }
}
```

### Example: Config Hooks

```javascript
export default function configPlugin() {
  return {
    name: 'config-plugin',
    
    // Modify config before it's resolved
    config(config) {
      return {
        resolve: {
          alias: {
            '@': '/src'
          }
        }
      }
    },
    
    // Called after config is resolved
    configResolved(resolvedConfig) {
      console.log('Resolved config:', resolvedConfig)
    }
  }
}
```

### Key Points

- Hooks are called at specific stages of the build
- Transform hooks can modify code
- Resolve hooks can handle module resolution
- Config hooks can modify configuration
- Return values control plugin behavior
