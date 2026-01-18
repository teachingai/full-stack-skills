# Build for Production

## Instructions

This example demonstrates building Vite projects for production.

### Key Concepts

- Production build process
- Build optimization
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
    
    // Rollup options
    rollupOptions: {
      output: {
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia']
        }
      }
    }
  }
})
```

### Key Points

- Production builds use Rollup
- Enable source maps for debugging
- Configure code splitting for optimal chunk sizes
- CSS is automatically extracted and minified
- Assets are optimized and hashed
