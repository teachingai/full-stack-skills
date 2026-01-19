# Built-in Plugins

## Instructions

This example demonstrates built-in plugins in Rspack.

### Key Concepts

- Available built-in plugins
- Plugin usage
- Plugin options
- Common patterns

### Example: HtmlRspackPlugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.HtmlRspackPlugin({
      template: './index.html',
      filename: 'index.html',
    }),
  ],
};
```

### Example: CopyRspackPlugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.CopyRspackPlugin({
      patterns: [
        { from: 'public', to: 'dist' },
        { from: 'assets', to: 'dist/assets' },
      ],
    }),
  ],
};
```

### Example: DefinePlugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production'),
      'process.env.API_URL': JSON.stringify('https://api.example.com'),
    }),
  ],
};
```

### Example: ProgressPlugin

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

### Example: CssExtractRspackPlugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [rspack.CssExtractRspackPlugin.loader, 'css-loader'],
      },
    ],
  },
  plugins: [
    new rspack.CssExtractRspackPlugin({
      filename: '[name].css',
    }),
  ],
};
```

### Example: CircularDependencyRspackPlugin

```javascript
const rspack = require('@rspack/core');

module.exports = {
  plugins: [
    new rspack.CircularDependencyRspackPlugin({
      exclude: /node_modules/,
      failOnError: true,
    }),
  ],
};
```

### Key Points

- Built-in plugins available from @rspack/core
- HtmlRspackPlugin for HTML generation
- CopyRspackPlugin for copying files
- DefinePlugin for constants
- CssExtractRspackPlugin for CSS extraction
- Many more plugins available
