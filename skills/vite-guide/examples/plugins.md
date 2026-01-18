# Plugins

## Instructions

This example demonstrates Vite plugins including official plugins and custom plugin development.

### Key Concepts

- Using plugins
- Official Vite plugins
- Community plugins
- Custom plugin development

### Example: Official Plugins

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import react from '@vitejs/plugin-react'
import legacy from '@vitejs/plugin-legacy'

export default defineConfig({
  plugins: [
    vue(),              // Vue support
    // react(),         // React support
    legacy({            // Legacy browser support
      targets: ['defaults', 'not IE 11']
    })
  ]
})
```

### Example: Common Community Plugins

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { visualizer } from 'rollup-plugin-visualizer'
import { VitePWA } from 'vite-plugin-pwa'
import eslint from 'vite-plugin-eslint'

export default defineConfig({
  plugins: [
    vue(),
    eslint(),
    VitePWA({
      registerType: 'autoUpdate'
    }),
    visualizer({
      open: true
    })
  ]
})
```

### Example: Custom Plugin

```javascript
// my-plugin.js
export default function myPlugin() {
  return {
    name: 'my-plugin',
    enforce: 'pre', // 'pre' | 'post'
    // Build hooks
    buildStart() {
      console.log('Build started')
    },
    // Transform hooks
    transform(code, id) {
      if (id.endsWith('.custom')) {
        return {
          code: code.replace(/CUSTOM/g, 'REPLACED'),
          map: null
        }
      }
    },
    // Resolve hooks
    resolveId(id) {
      if (id === 'virtual-module') {
        return id
      }
    },
    load(id) {
      if (id === 'virtual-module') {
        return 'export default "Virtual module content"'
      }
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
function myPlugin(options = {}) {
  const { prefix = 'VITE_' } = options
  
  return {
    name: 'my-plugin',
    configResolved(config) {
      console.log('Config resolved:', config)
    },
    transformIndexHtml(html) {
      return html.replace(
        /<title>(.*?)<\/title>/,
        `<title>${options.title || 'App'}</title>`
      )
    }
  }
}

export default defineConfig({
  plugins: [
    myPlugin({
      title: 'My App',
      prefix: 'APP_'
    })
  ]
})
```

### Key Points

- Plugins are executed in order
- Use `enforce: 'pre'` or `enforce: 'post'` to control execution order
- Plugins can hook into various build stages
- Official plugins: `@vitejs/plugin-vue`, `@vitejs/plugin-react`, `@vitejs/plugin-legacy`
- Community plugins available on npm
