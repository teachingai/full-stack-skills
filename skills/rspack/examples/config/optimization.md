# Optimization

## Instructions

This example demonstrates optimization configuration in Rspack.

### Key Concepts

- Code splitting
- Minification
- Tree shaking
- Chunk optimization

### Example: Basic Optimization

```javascript
module.exports = {
  optimization: {
    minimize: true,
  },
};
```

### Example: Code Splitting

```javascript
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
      },
    },
  },
};
```

### Example: Minification Options

```javascript
module.exports = {
  optimization: {
    minimize: true,
    minimizer: [
      new rspack.SwcJsMinimizerRspackPlugin({
        compress: {
          drop_console: true,
        },
      }),
    ],
  },
};
```

### Example: Tree Shaking

```javascript
module.exports = {
  optimization: {
    usedExports: true,
    sideEffects: false,
  },
};
```

### Example: Runtime Chunk

```javascript
module.exports = {
  optimization: {
    runtimeChunk: 'single',
  },
};
```

### Example: Module IDs

```javascript
module.exports = {
  optimization: {
    moduleIds: 'deterministic',
    chunkIds: 'deterministic',
  },
};
```

### Key Points

- minimize enables minification
- splitChunks configures code splitting
- usedExports enables tree shaking
- runtimeChunk extracts runtime code
- deterministic IDs for better caching
