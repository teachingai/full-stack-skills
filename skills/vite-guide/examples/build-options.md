# Build Options

## Instructions

This example demonstrates build configuration options and optimizations.

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
    
    // Assets directory (relative to outDir)
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
      // Entry points
      input: {
        main: './index.html',
        admin: './admin.html'
      },
      
      // Output options
      output: {
        // Manual chunks
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          'ui-vendor': ['element-plus']
        },
        
        // Chunk file names
        chunkFileNames: 'js/[name]-[hash].js',
        entryFileNames: 'js/[name]-[hash].js',
        assetFileNames: (assetInfo) => {
          if (assetInfo.name.endsWith('.css')) {
            return 'css/[name]-[hash][extname]'
          }
          return 'assets/[name]-[hash][extname]'
        }
      },
      
      // External dependencies
      external: ['some-big-library']
    },
    
    // Report compressed size
    reportCompressedSize: true,
    
    // Chunking strategy
    chunkSizeWarningLimit: 1000,
    
    // Watch options (for build --watch)
    watch: null
  }
})
```

### Example: Code Splitting Strategy

```javascript
build: {
  rollupOptions: {
    output: {
      manualChunks: (id) => {
        // Split node_modules
        if (id.includes('node_modules')) {
          // Split by package
          if (id.includes('vue')) {
            return 'vue-vendor'
          }
          if (id.includes('element-plus')) {
            return 'ui-vendor'
          }
          // Other vendor code
          return 'vendor'
        }
        
        // Split by directory
        if (id.includes('/src/utils/')) {
          return 'utils'
        }
        if (id.includes('/src/components/')) {
          return 'components'
        }
      }
    }
  }
}
```

### Example: Asset Optimization

```javascript
build: {
  // Inline small assets
  assetsInlineLimit: 4096,
  
  // Copy public assets
  copyPublicDir: true,
  
  rollupOptions: {
    output: {
      // Optimize asset file names
      assetFileNames: (assetInfo) => {
        const info = assetInfo.name.split('.')
        const ext = info[info.length - 1]
        if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(ext)) {
          return `img/[name]-[hash][extname]`
        }
        if (/woff|woff2|eot|ttf|otf/i.test(ext)) {
          return `fonts/[name]-[hash][extname]`
        }
        return `assets/[name]-[hash][extname]`
      }
    }
  }
}
```

### Key Points

- Configure `outDir` for output directory
- Use `manualChunks` for code splitting
- Enable source maps for debugging
- Choose minifier: `esbuild` (faster) or `terser` (more options)
- Optimize asset file names for better caching
