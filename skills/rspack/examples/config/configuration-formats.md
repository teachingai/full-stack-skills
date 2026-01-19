# Configuration Formats

## Instructions

This example demonstrates different configuration file formats in Rspack.

### Key Concepts

- JavaScript configuration
- TypeScript configuration
- CommonJS vs ES Modules
- Type safety

### Example: JavaScript (CommonJS)

```javascript
// rspack.config.js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```

### Example: JavaScript (ES Modules)

```javascript
// rspack.config.mjs
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```

### Example: TypeScript Configuration

```typescript
// rspack.config.ts
import { defineConfig } from '@rspack/cli';
import path from 'path';

export default defineConfig({
  entry: './src/index.ts',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
});
```

### Example: TypeScript with Type Checking

```typescript
// rspack.config.ts
import type { Configuration } from '@rspack/core';
import { defineConfig } from '@rspack/cli';

const config: Configuration = {
  entry: './src/index.ts',
  output: {
    filename: 'bundle.js',
  },
};

export default defineConfig(config);
```

### Example: JSDoc Type Hints

```javascript
// rspack.config.js
// @ts-check
/**
 * @type {import('@rspack/core').Configuration}
 */
module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
  },
};
```

### Key Points

- Use .js for CommonJS
- Use .mjs for ES Modules
- Use .ts for TypeScript
- Use defineConfig for type hints
- JSDoc provides type checking in .js files
