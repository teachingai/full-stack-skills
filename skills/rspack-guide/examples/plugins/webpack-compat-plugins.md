# Webpack Compatible Plugins

## Instructions

This example demonstrates Webpack plugin compatibility in Rspack.

### Key Concepts

- Webpack plugin compatibility
- Compatible plugins
- Incompatible plugins
- Migration guide

### Example: Using Webpack Plugins

```javascript
const webpack = require('webpack');

module.exports = {
  plugins: [
    // Most Webpack plugins work directly
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production'),
    }),
  ],
};
```

### Example: Compatible Plugins

**Fully Compatible**:
- html-webpack-plugin → HtmlRspackPlugin
- copy-webpack-plugin → CopyRspackPlugin
- mini-css-extract-plugin → CssExtractRspackPlugin
- webpack.DefinePlugin → rspack.DefinePlugin

### Example: Plugin Compatibility Check

```javascript
// Test if plugin works
const SomeWebpackPlugin = require('some-webpack-plugin');

module.exports = {
  plugins: [
    // Try using Webpack plugin
    new SomeWebpackPlugin({
      // options
    }),
  ],
};
```

### Example: Using Rspack Plugins Instead

```javascript
// Instead of webpack plugin
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    // Use Rspack equivalent
    new rspack.HtmlRspackPlugin({
      template: './index.html',
    }),
  ],
};
```

### Key Points

- 85% of top 50 Webpack plugins work
- Most loaders are compatible
- Use Rspack plugins when available
- Test compatibility for specific plugins
- Check official compatibility list
