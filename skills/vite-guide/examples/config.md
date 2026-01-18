# Configuration

## Instructions

This example demonstrates Vite configuration options and best practices.

### Key Concepts

- Configuration file structure
- Conditional configuration
- Environment-specific configs
- Configuration merging

### Example: Basic Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  // Plugins
  plugins: [vue()],
  
  // Root directory
  root: process.cwd(),
  
  // Public directory
  publicDir: 'public',
  
  // Base public path
  base: '/',
  
  // Development server
  server: {
    host: '0.0.0.0',
    port: 3000,
    open: true,
    cors: true,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  },
  
  // Build options
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: true,
    minify: 'esbuild',
    target: 'es2015',
    cssCodeSplit: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html')
      }
    }
  },
  
  // Resolve options
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
      '~': resolve(__dirname, 'src')
    },
    extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json']
  },
  
  // CSS options
  css: {
    modules: {
      localsConvention: 'camelCase'
    },
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/styles/variables.scss";`
      }
    }
  },
  
  // JSON options
  json: {
    namedExports: true,
    stringify: false
  },
  
  // ESBuild options
  esbuild: {
    target: 'es2015'
  },
  
  // Optimize dependencies
  optimizeDeps: {
    include: ['vue', 'vue-router'],
    exclude: ['some-big-dependency']
  },
  
  // SSR options
  ssr: {
    noExternal: ['some-package']
  }
})
```

### Example: Conditional Configuration

```javascript
import { defineConfig } from 'vite'

export default defineConfig(({ command, mode }) => {
  if (command === 'serve') {
    // Development config
    return {
      server: {
        port: 3000
      }
    }
  } else {
    // Production config
    return {
      build: {
        minify: 'terser',
        sourcemap: false
      }
    }
  }
})
```

### Example: TypeScript Configuration

```typescript
// vite.config.ts
import { defineConfig } from 'vite'
import type { UserConfig } from 'vite'

export default defineConfig({
  // ... config
}) satisfies UserConfig
```

### Key Points

- Use `defineConfig` for better TypeScript support
- Configuration can be conditional based on command and mode
- All options are optional with sensible defaults
- Use path aliases for cleaner imports
- Configure optimizeDeps for better dev server performance
