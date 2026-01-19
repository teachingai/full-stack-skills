# Quick Start

## Instructions

This example demonstrates how to quickly get started with Rspack.

### Key Concepts

- Installation
- Project setup
- Basic configuration
- Running Rspack

### Example: Installation

```bash
# Using npm
npm install -D @rspack/core @rspack/cli

# Using yarn
yarn add -D @rspack/core @rspack/cli

# Using pnpm
pnpm add -D @rspack/core @rspack/cli
```

### Example: Basic Configuration

```javascript
// rspack.config.js
const path = require('path');
const rspack = require('@rspack/core');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  plugins: [
    new rspack.HtmlRspackPlugin({
      template: './index.html',
    }),
  ],
};
```

### Example: Package.json Scripts

```json
{
  "scripts": {
    "dev": "rspack serve",
    "build": "rspack build"
  }
}
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

### Example: Using Rsbuild (Recommended)

```bash
# Create new project with Rsbuild
npm create rsbuild@latest my-app

# Or with specific template
npm create rsbuild@latest my-app -- --template react
```

### Key Points

- Install @rspack/core and @rspack/cli
- Create rspack.config.js for configuration
- Use rspack serve for development
- Use rspack build for production
- Consider using Rsbuild for easier setup
