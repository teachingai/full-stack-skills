# Production Build

## Instructions

This example demonstrates production build configuration and optimization.

### Key Concepts

- Building for production
- Build options
- Code splitting
- Asset optimization

### Example: Basic Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

### Example: Build Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    // Output directory
    outDir: 'dist',
    
    // Assets directory
    assetsDir: 'assets',
    
    // Source maps
    sourcemap: true,
    
    // Minification
    minify: 'esbuild', // 'esbuild' | 'terser' | false
    
    // Target browsers
    target: 'es2015',
    
    // CSS code splitting
    cssCodeSplit: true,
    
    // Chunk size warning limit
    chunkSizeWarningLimit: 1000,
    
    // Rollup options
    rollupOptions: {
      input: {
        main: './index.html'
      },
      output: {
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          'ui-vendor': ['element-plus']
        }
      }
    }
  }
})
```

### Example: Code Splitting

```javascript
build: {
  rollupOptions: {
    output: {
      manualChunks: (id) => {
        if (id.includes('node_modules')) {
          if (id.includes('vue')) {
            return 'vue-vendor'
          }
          if (id.includes('element-plus')) {
            return 'ui-vendor'
          }
          return 'vendor'
        }
      }
    }
  }
}
```

### Example: Build Analysis

```javascript
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [
    visualizer({
      open: true,
      gzipSize: true,
      brotliSize: true,
      filename: 'dist/stats.html'
    })
  ]
})
```

### Key Points

- Production builds use Rollup
- Enable source maps for debugging
- Configure code splitting for optimal chunk sizes
- Use build analysis tools to optimize bundle size
- CSS is automatically extracted and minified
