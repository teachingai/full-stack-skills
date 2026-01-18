# Preview

## Instructions

This example demonstrates previewing production builds locally.

### Key Concepts

- Preview server
- Preview configuration
- Testing production builds

### Example: Basic Preview

```bash
# Build first
npm run build

# Then preview
npm run preview
```

### Example: Preview Configuration

```javascript
// vite.config.js
export default defineConfig({
  preview: {
    port: 4173,
    host: '0.0.0.0',
    open: true,
    cors: true
  }
})
```

### Example: Preview with Proxy

```javascript
export default defineConfig({
  preview: {
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  }
})
```

### Key Points

- Preview server serves production build
- Default port is 4173
- Configuration similar to dev server
- Use for testing production builds locally
- Supports proxy and HTTPS
