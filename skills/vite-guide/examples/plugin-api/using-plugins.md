# Using Plugins

## Instructions

This example demonstrates how to use plugins in Vite projects.

### Key Concepts

- Installing plugins
- Configuring plugins
- Plugin options
- Common plugins

### Example: Installing Plugins

```bash
# Install Vue plugin
npm install -D @vitejs/plugin-vue

# Install React plugin
npm install -D @vitejs/plugin-react

# Install other plugins
npm install -D vite-plugin-pwa
npm install -D vite-plugin-eslint
```

### Example: Using Plugins

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [
    vue(),
    visualizer({
      open: true
    })
  ]
})
```

### Example: Plugin with Options

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import legacy from '@vitejs/plugin-legacy'

export default defineConfig({
  plugins: [
    vue(),
    legacy({
      targets: ['defaults', 'not IE 11']
    })
  ]
})
```

### Example: Conditional Plugins

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig(({ mode }) => {
  const plugins = [vue()]
  
  if (mode === 'analyze') {
    plugins.push(visualizer({ open: true }))
  }
  
  return { plugins }
})
```

### Key Points

- Plugins are added to the `plugins` array
- Plugins can have options
- Use conditional logic for mode-specific plugins
- Official plugins: `@vitejs/plugin-vue`, `@vitejs/plugin-react`
- Community plugins available on npm
