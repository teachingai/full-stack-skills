# Deployment

## Instructions

This example demonstrates deployment strategies for Vite applications.

### Key Concepts

- Static hosting
- Base path configuration
- Environment-specific builds
- Pre-rendering
- SSR deployment

### Example: Static Hosting

```javascript
// vite.config.js
export default defineConfig({
  base: '/my-app/',  // Base public path
  build: {
    outDir: 'dist'
  }
})
```

### Example: GitHub Pages

```javascript
// vite.config.js
export default defineConfig({
  base: process.env.NODE_ENV === 'production' 
    ? '/my-repo/' 
    : '/',
  build: {
    outDir: 'dist'
  }
})

// package.json
{
  "scripts": {
    "build": "vite build",
    "preview": "vite preview",
    "deploy": "npm run build && gh-pages -d dist"
  }
}
```

### Example: Netlify

```toml
# netlify.toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Example: Vercel

```json
// vercel.json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

### Example: Docker

```dockerfile
# Dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Example: Nginx Configuration

```nginx
# nginx.conf
server {
  listen 80;
  server_name example.com;
  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }

  # Cache static assets
  location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
  }
}
```

### Key Points

- Configure `base` path for subdirectory deployment
- Use SPA fallback for client-side routing
- Cache static assets for better performance
- Use environment variables for different deployment targets
- Consider pre-rendering for better SEO
