# Resolve

## Instructions

This example demonstrates module resolution configuration in Rspack.

### Key Concepts

- Module resolution
- Alias
- Extensions
- Modules directories

### Example: Basic Resolve

```javascript
module.exports = {
  resolve: {
    extensions: ['.js', '.json', '.jsx', '.ts', '.tsx'],
  },
};
```

### Example: Alias

```javascript
const path = require('path');

module.exports = {
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      'components': path.resolve(__dirname, 'src/components'),
    },
  },
};
```

### Example: Modules Directories

```javascript
module.exports = {
  resolve: {
    modules: ['node_modules', 'src'],
  },
};
```

### Example: Resolve Fallback

```javascript
module.exports = {
  resolve: {
    fallback: {
      'crypto': false,
      'stream': false,
      'buffer': false,
    },
  },
};
```

### Example: Condition Names

```javascript
module.exports = {
  resolve: {
    conditionNames: ['import', 'require', 'default'],
  },
};
```

### Example: Main Fields

```javascript
module.exports = {
  resolve: {
    mainFields: ['browser', 'module', 'main'],
  },
};
```

### Key Points

- extensions specifies file extensions to resolve
- alias creates path shortcuts
- modules specifies directories to search
- fallback for Node.js polyfills
- conditionNames for package.json exports
- mainFields for package entry points
