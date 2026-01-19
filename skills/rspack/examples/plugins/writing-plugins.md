# Writing Plugins

## Instructions

This example demonstrates how to write custom plugins for Rspack.

### Key Concepts

- Plugin structure
- Compiler hooks
- Compilation hooks
- Plugin API

### Example: Basic Plugin

```javascript
class MyPlugin {
  apply(compiler) {
    compiler.hooks.done.tap('MyPlugin', (stats) => {
      console.log('Build completed!');
    });
  }
}

module.exports = {
  plugins: [new MyPlugin()],
};
```

### Example: Plugin with Options

```javascript
class MyPlugin {
  constructor(options) {
    this.options = options;
  }

  apply(compiler) {
    compiler.hooks.emit.tap('MyPlugin', (compilation) => {
      console.log('Options:', this.options);
    });
  }
}

module.exports = {
  plugins: [
    new MyPlugin({
      message: 'Hello from plugin',
    }),
  ],
};
```

### Example: TypeScript Plugin

```typescript
import type { Compiler } from '@rspack/core';

class MyPlugin {
  apply(compiler: Compiler) {
    compiler.hooks.done.tap('MyPlugin', (stats) => {
      console.log('Build completed!');
    });
  }
}

export default MyPlugin;
```

### Example: Using Compiler Hooks

```javascript
class MyPlugin {
  apply(compiler) {
    compiler.hooks.beforeRun.tap('MyPlugin', () => {
      console.log('Before run');
    });

    compiler.hooks.run.tap('MyPlugin', () => {
      console.log('Run');
    });

    compiler.hooks.done.tap('MyPlugin', (stats) => {
      console.log('Done');
    });
  }
}
```

### Example: Using Compilation Hooks

```javascript
class MyPlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap('MyPlugin', (compilation) => {
      compilation.hooks.optimizeChunks.tap('MyPlugin', () => {
        console.log('Optimizing chunks');
      });
    });
  }
}
```

### Key Points

- Plugins are classes with apply method
- apply receives compiler instance
- Use compiler.hooks to tap into lifecycle
- Can access compilation via compilation hook
- TypeScript support available
