# Mode

## Instructions

This example demonstrates mode configuration in Rspack.

### Key Concepts

- Development mode
- Production mode
- None mode
- Mode-specific optimizations

### Example: Development Mode

```javascript
module.exports = {
  mode: 'development',
};
```

### Example: Production Mode

```javascript
module.exports = {
  mode: 'production',
};
```

### Example: Mode with Environment Variable

```javascript
module.exports = {
  mode: process.env.NODE_ENV || 'development',
};
```

### Example: Mode-Specific Configuration

```javascript
const isProduction = process.env.NODE_ENV === 'production';

module.exports = {
  mode: isProduction ? 'production' : 'development',
  optimization: {
    minimize: isProduction,
  },
  devtool: isProduction ? false : 'eval-source-map',
};
```

### Example: None Mode

```javascript
module.exports = {
  mode: 'none',
  // No default optimizations
};
```

### Key Points

- mode: 'development' enables dev optimizations
- mode: 'production' enables prod optimizations
- mode: 'none' disables default optimizations
- Mode affects built-in optimizations
- Can be set via environment variable
