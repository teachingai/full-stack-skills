# Configuration File

## Instructions

This example demonstrates Rspack configuration file setup.

### Key Concepts

- Configuration file location
- Configuration file naming
- Supported formats
- Configuration loading

### Example: Configuration File Location

Rspack looks for configuration files in the project root:

```
project/
├── rspack.config.js      # Default
├── rspack.config.ts      # TypeScript
├── rspack.config.cjs     # CommonJS
└── rspack.config.mjs     # ES Modules
```

### Example: Basic Configuration

```javascript
// rspack.config.js
module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
  },
};
```

### Example: TypeScript Configuration

```typescript
// rspack.config.ts
import { defineConfig } from '@rspack/cli';

export default defineConfig({
  entry: './src/index.ts',
  output: {
    filename: 'bundle.js',
  },
});
```

### Example: Custom Configuration Path

```bash
# Specify custom config file
rspack build --config custom.config.js
```

### Example: Multiple Configurations

```javascript
// rspack.config.js
module.exports = [
  {
    name: 'client',
    entry: './src/client.js',
    // ...
  },
  {
    name: 'server',
    entry: './src/server.js',
    // ...
  },
];
```

### Key Points

- Default config file: rspack.config.js
- Supports .js, .ts, .cjs, .mjs formats
- Use defineConfig for TypeScript type hints
- Can specify custom config path with --config
- Supports multiple configurations
