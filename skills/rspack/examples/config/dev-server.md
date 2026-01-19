# Development Server

## Instructions

This example demonstrates development server configuration in Rspack.

### Key Concepts

- Dev server setup
- Hot Module Replacement
- Proxy configuration
- Server options

### Example: Basic Dev Server

```javascript
module.exports = {
  devServer: {
    port: 3000,
    open: true,
  },
};
```

### Example: Dev Server with HMR

```javascript
module.exports = {
  devServer: {
    hot: true,
    liveReload: true,
  },
};
```

### Example: Proxy Configuration

```javascript
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
    },
  },
};
```

### Example: Static Files

```javascript
module.exports = {
  devServer: {
    static: {
      directory: path.join(__dirname, 'public'),
    },
  },
};
```

### Example: Headers

```javascript
module.exports = {
  devServer: {
    headers: {
      'X-Custom-Header': 'value',
    },
  },
};
```

### Example: HTTPS

```javascript
module.exports = {
  devServer: {
    https: true,
  },
};
```

### Key Points

- devServer configures development server
- hot enables Hot Module Replacement
- proxy forwards requests to backend
- static serves static files
- headers sets response headers
- https enables HTTPS
