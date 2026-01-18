# Build Options

## Instructions

This example demonstrates build configuration options.

### Key Concepts

- Output directory
- Asset handling
- Minification
- Source maps
- Rollup options

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
    
    // Asset inline limit (4kb default)
    assetsInlineLimit: 4096,
    
    // CSS code splitting
    cssCodeSplit: true,
    
    // Source maps
    sourcemap: false,        // false | 'inline' | true
    sourcemapIgnoreList: false,
    
    // Minification
    minify: 'esbuild',       // 'esbuild' | 'terser' | false
    
    // Terser options (if using terser)
    terserOptions: {
      compress: {
        drop_console: true
      }
    },
    
    // Target browsers
    target: 'es2015',
    
    // Module format
    modulePreload: {
      polyfill: true
    },
    
    // Chunk size warning limit
    chunkSizeWarningLimit: 1000,
    
    // CSS target
    cssTarget: 'chrome80',
    
    // Rollup options
    rollupOptions: {
      input: {
        main: './index.html'
      },
      output: {
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia']
        }
      }
    },
    
    // Report compressed size
    reportCompressedSize: true,
    
    // Watch options (for build --watch)
    watch: null
  }
})
```

### Key Points

- Configure `outDir` for output directory
- Use `manualChunks` for code splitting
- Enable source maps for debugging
- Choose minifier: `esbuild` (faster) or `terser` (more options)
- Optimize asset file names for better caching
