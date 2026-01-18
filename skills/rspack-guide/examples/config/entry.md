# Entry

## Instructions

This example demonstrates entry point configuration in Rspack.

### Key Concepts

- Single entry
- Multiple entries
- Entry object
- Dynamic entries

### Example: Single Entry (String)

```javascript
module.exports = {
  entry: './src/index.js',
};
```

### Example: Single Entry (Array)

```javascript
module.exports = {
  entry: ['./src/index.js', './src/polyfills.js'],
};
```

### Example: Multiple Entries (Object)

```javascript
module.exports = {
  entry: {
    main: './src/index.js',
    vendor: './src/vendor.js',
  },
};
```

### Example: Multiple Entries with Path

```javascript
module.exports = {
  entry: {
    app: './src/app.js',
    admin: './src/admin.js',
  },
  output: {
    filename: '[name].bundle.js',
  },
};
```

### Example: Dynamic Entry

```javascript
module.exports = {
  entry: () => {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({
          main: './src/index.js',
        });
      }, 1000);
    });
  },
};
```

### Example: Entry with Dependencies

```javascript
module.exports = {
  entry: {
    main: {
      import: './src/index.js',
      dependOn: 'shared',
    },
    shared: 'lodash',
  },
};
```

### Key Points

- Entry can be string, array, object, or function
- Multiple entries create multiple bundles
- Use [name] in output.filename for named entries
- Can specify dependencies between entries
- Dynamic entries support async loading
