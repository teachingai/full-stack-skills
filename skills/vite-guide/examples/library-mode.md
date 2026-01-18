# Library Mode

## Instructions

This example demonstrates building libraries with Vite.

### Key Concepts

- Library build configuration
- External dependencies
- UMD and ESM formats
- Entry point

### Example: Basic Library Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.js'),
      name: 'MyLib',
      fileName: (format) => `my-lib.${format}.js`,
      formats: ['es', 'umd']
    },
    rollupOptions: {
      external: ['vue'],
      output: {
        globals: {
          vue: 'Vue'
        }
      }
    }
  }
})
```

### Example: TypeScript Library

```typescript
// src/index.ts
export function greet(name: string) {
  return `Hello, ${name}!`
}

export class MyClass {
  constructor(private value: number) {}
  
  getValue() {
    return this.value
  }
}

// vite.config.ts
import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.ts'),
      name: 'MyLib',
      fileName: 'my-lib'
    }
  }
})
```

### Example: Vue Component Library

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.js'),
      name: 'MyComponentLib',
      fileName: 'my-component-lib'
    },
    rollupOptions: {
      external: ['vue'],
      output: {
        globals: {
          vue: 'Vue'
        }
      }
    }
  }
})
```

### Key Points

- Use `build.lib` for library mode
- External dependencies should be listed in `rollupOptions.external`
- Configure `globals` for UMD format
- Entry point exports are the library API
- Supports multiple formats: es, umd, cjs, iife
