# Module

## Instructions

This example demonstrates module configuration in Rspack.

### Key Concepts

- Module rules
- Loaders
- Parser options
- Generator options

### Example: Basic Module Rules

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        use: ['babel-loader'],
      },
    ],
  },
};
```

### Example: Multiple Loaders

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
};
```

### Example: Loader with Options

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: [
          {
            loader: 'ts-loader',
            options: {
              transpileOnly: true,
            },
          },
        ],
      },
    ],
  },
};
```

### Example: Exclude Files

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
    ],
  },
};
```

### Example: Asset Modules

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
      {
        test: /\.svg$/i,
        type: 'asset/inline',
      },
    ],
  },
};
```

### Example: TypeScript with Rspack

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: [
          {
            loader: 'builtin:swc-loader',
            options: {
              jsc: {
                parser: {
                  syntax: 'typescript',
                },
              },
            },
          },
        ],
        type: 'javascript/auto',
      },
    ],
  },
};
```

### Key Points

- rules array defines module processing rules
- test matches file patterns
- use specifies loaders
- exclude/include filter files
- type: 'asset' for asset modules
- Built-in SWC loader for TypeScript
