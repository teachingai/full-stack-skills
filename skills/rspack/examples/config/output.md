# Output

## Instructions

This example demonstrates output configuration in Rspack.

### Key Concepts

- Output path
- Output filename
- Public path
- Asset modules
- Clean output

### Example: Basic Output

```javascript
const path = require('path');

module.exports = {
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```

### Example: Output with Template

```javascript
module.exports = {
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js',
    chunkFilename: '[name].chunk.js',
  },
};
```

### Example: Output with Hash

```javascript
module.exports = {
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].chunk.js',
  },
};
```

### Example: Public Path

```javascript
module.exports = {
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
    publicPath: '/assets/',
  },
};
```

### Example: Clean Output

```javascript
const rspack = require('@rspack/core');

module.exports = {
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
    clean: true,  // Clean output directory before build
  },
};
```

### Example: Library Output

```javascript
module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'my-library.js',
    library: {
      name: 'MyLibrary',
      type: 'umd',
    },
  },
};
```

### Key Points

- path specifies output directory
- filename can use templates ([name], [hash], etc.)
- publicPath sets base path for assets
- clean removes old files before build
- library config for library mode
