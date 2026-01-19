# Next.js Configuration API

## API Reference

Next.js configuration options in next.config.js.

### Basic Configuration

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Configuration options
}

module.exports = nextConfig
```

### Common Options

#### reactStrictMode

**Type:** `boolean`  
**Default:** `false`

Enable React strict mode.

```javascript
module.exports = {
  reactStrictMode: true,
}
```

#### images

**Type:** `object`

Image optimization configuration.

```javascript
module.exports = {
  images: {
    domains: ['example.com'],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.example.com',
      },
    ],
  },
}
```

#### env

**Type:** `object`

Environment variables exposed to the browser.

```javascript
module.exports = {
  env: {
    CUSTOM_KEY: 'value',
  },
}
```

#### basePath

**Type:** `string`

Base path for the application.

```javascript
module.exports = {
  basePath: '/my-app',
}
```

#### output

**Type:** `string`

Output mode: 'standalone' | 'export'

```javascript
module.exports = {
  output: 'standalone',
}
```

#### experimental

**Type:** `object`

Experimental features.

```javascript
module.exports = {
  experimental: {
    appDir: true,
  },
}
```

**See also:** `examples/getting-started/installation.md`
