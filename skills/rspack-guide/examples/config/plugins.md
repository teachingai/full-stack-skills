# Plugins

## Instructions

This example demonstrates plugins configuration in Rspack.

### Key Concepts

- Built-in plugins
- Plugin usage
- Plugin options
- Custom plugins

### Example: HTML Plugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.HtmlRspackPlugin({
      template: './index.html',
    }),
  ],
};
```

### Example: Copy Plugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.CopyRspackPlugin({
      patterns: [
        { from: 'public', to: 'dist' },
      ],
    }),
  ],
};
```

### Example: Define Plugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production'),
    }),
  ],
};
```

### Example: Progress Plugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.ProgressPlugin({
      profile: true,
    }),
  ],
};
```

### Example: Multiple Plugins

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.HtmlRspackPlugin({
      template: './index.html',
    }),
    new rspack.CopyRspackPlugin({
      patterns: [{ from: 'public' }],
    }),
  ],
};
```

### Key Points

- plugins array contains plugin instances
- Built-in plugins available from @rspack/core
- Most Webpack plugins are compatible
- Plugins extend Rspack functionality
- Plugins can have options
