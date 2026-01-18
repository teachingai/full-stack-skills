# Creating Plugins

## Instructions

This example demonstrates how to create custom Vite plugins.

### Key Concepts

- Plugin structure
- Plugin options
- Common patterns
- Testing plugins

### Example: Simple Plugin

```javascript
// my-plugin.js
export default function myPlugin() {
  return {
    name: 'my-plugin',
    transform(code, id) {
      // Transform code here
      return code
    }
  }
}

// vite.config.js
import myPlugin from './my-plugin'

export default defineConfig({
  plugins: [myPlugin()]
})
```

### Example: Plugin with Options

```javascript
// my-plugin.js
export default function myPlugin(options = {}) {
  const { prefix = 'VITE_' } = options
  
  return {
    name: 'my-plugin',
    configResolved(config) {
      console.log('Plugin options:', options)
    },
    transformIndexHtml(html) {
      return html.replace(
        /<title>(.*?)<\/title>/,
        `<title>${options.title || 'App'}</title>`
      )
    }
  }
}

// vite.config.js
import myPlugin from './my-plugin'

export default defineConfig({
  plugins: [
    myPlugin({
      title: 'My App',
      prefix: 'APP_'
    })
  ]
})
```

### Example: Virtual Module Plugin

```javascript
export default function virtualModulePlugin() {
  const virtualModuleId = 'virtual:my-module'
  const resolvedVirtualModuleId = '\0' + virtualModuleId
  
  return {
    name: 'virtual-module-plugin',
    resolveId(id) {
      if (id === virtualModuleId) {
        return resolvedVirtualModuleId
      }
    },
    load(id) {
      if (id === resolvedVirtualModuleId) {
        return `export const message = "Hello from virtual module"`
      }
    }
  }
}
```

### Example: Transform Plugin

```javascript
export default function transformPlugin() {
  return {
    name: 'transform-plugin',
    transform(code, id) {
      // Only transform specific files
      if (!id.endsWith('.vue')) {
        return null
      }
      
      // Transform Vue SFC
      return {
        code: code.replace(/console\.log/g, '// console.log'),
        map: null
      }
    }
  }
}
```

### Example: HTML Transform Plugin

```javascript
export default function htmlPlugin() {
  return {
    name: 'html-plugin',
    transformIndexHtml: {
      enforce: 'pre',
      transform(html, ctx) {
        // Transform HTML
        return html.replace(
          '<!-- app -->',
          '<div id="app"></div>'
        )
      }
    }
  }
}
```

### Key Points

- Plugins are functions that return plugin objects
- Use options parameter for configuration
- Implement specific hooks for desired functionality
- Test plugins in isolation before using in projects
- Follow naming convention: `vite-plugin-*`
