# Shared Options

## Instructions

This example demonstrates shared configuration options that apply to both dev and build.

### Key Concepts

- Root directory
- Base public path
- Mode
- Define replacements
- Plugins
- Public directory

### Example: Basic Shared Options

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  // Root directory (default: process.cwd())
  root: process.cwd(),
  
  // Base public path (default: '/')
  base: '/',
  
  // Mode (default: 'development' for serve, 'production' for build)
  mode: 'development',
  
  // Define global constants
  define: {
    __APP_VERSION__: JSON.stringify('1.0.0'),
    'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV)
  },
  
  // Plugins
  plugins: [vue()],
  
  // Public directory (default: 'public')
  publicDir: 'public',
  
  // Cache directory (default: 'node_modules/.vite')
  cacheDir: 'node_modules/.vite',
  
  // Resolve options
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  
  // CSS options
  css: {
    modules: {
      localsConvention: 'camelCase'
    }
  },
  
  // JSON options
  json: {
    namedExports: true,
    stringify: false
  },
  
  // Log level
  logLevel: 'info',
  
  // Clear screen
  clearScreen: false,
  
  // Environment prefix
  envPrefix: 'VITE_'
})
```

### Example: Conditional Configuration

```javascript
export default defineConfig(({ command, mode }) => {
  const isProduction = mode === 'production'
  
  return {
    base: isProduction ? '/my-app/' : '/',
    define: {
      __DEV__: !isProduction
    }
  }
})
```

### Key Points

- `root` sets the project root directory
- `base` is important for subdirectory deployments
- `mode` can be overridden via CLI
- `define` replaces global constants at build time
- `plugins` array contains all plugins
- `publicDir` files are copied as-is to dist root
