# Server Options

## Instructions

This example demonstrates development server configuration options.

### Key Concepts

- Server host and port
- HTTPS configuration
- Proxy configuration
- CORS settings
- Open browser

### Example: Basic Server Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    host: '0.0.0.0',        // Listen on all addresses
    port: 3000,             // Port number
    strictPort: false,      // Try next port if occupied
    open: true,             // Open browser automatically
    cors: true,             // Enable CORS
    https: false            // Enable HTTPS
  }
})
```

### Example: HTTPS Configuration

```javascript
import fs from 'fs'

export default defineConfig({
  server: {
    https: {
      key: fs.readFileSync('path/to/key.pem'),
      cert: fs.readFileSync('path/to/cert.pem')
    }
  }
})
```

### Example: Proxy Configuration

```javascript
export default defineConfig({
  server: {
    proxy: {
      // String shorthand
      '/api': 'http://localhost:8080',
      
      // Object configuration
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
        configure: (proxy, options) => {
          proxy.on('error', (err, req, res) => {
            console.log('proxy error', err)
          })
        }
      }
    }
  }
})
```

### Key Points

- Use `host: '0.0.0.0'` to access from network
- Configure proxy for API requests in development
- HTTPS requires certificate files
- WebSocket proxying requires `ws: true`
- Use `rewrite` to modify proxy paths
