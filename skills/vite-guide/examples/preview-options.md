# Preview Options

## Instructions

This example demonstrates preview server configuration options.

### Key Concepts

- Preview server
- Preview configuration
- HTTPS in preview
- CORS in preview

### Example: Basic Preview Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  preview: {
    port: 4173,
    host: '0.0.0.0',
    open: true,
    cors: true
  }
})
```

### Example: Preview with HTTPS

```javascript
import fs from 'fs'

export default defineConfig({
  preview: {
    https: {
      key: fs.readFileSync('path/to/key.pem'),
      cert: fs.readFileSync('path/to/cert.pem')
    }
  }
})
```

### Example: Preview Proxy

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

### Example: Running Preview

```bash
# Build first
npm run build

# Then preview
npm run preview

# Or with custom port
npm run preview -- --port 5000
```

### Key Points

- Preview server serves production build
- Configuration similar to dev server
- Use for testing production builds locally
- Supports proxy and HTTPS
- Default port is 4173
