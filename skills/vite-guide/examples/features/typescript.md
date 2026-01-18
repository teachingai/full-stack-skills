# TypeScript

## Instructions

This example demonstrates TypeScript support in Vite projects.

### Key Concepts

- TypeScript configuration
- Type definitions
- Client types
- Environment variable types

### Example: Basic TypeScript Setup

```bash
# Create TypeScript project
npm create vite@latest my-app -- --template vue-ts
```

### Example: tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "preserve",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src/**/*.ts", "src/**/*.d.ts", "src/**/*.tsx", "src/**/*.vue"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

### Example: Client Types

```typescript
// vite-env.d.ts
/// <reference types="vite/client" />

// Import meta types
interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
```

### Example: Component with TypeScript

```vue
<script setup lang="ts">
import { ref } from 'vue'

interface User {
  id: number
  name: string
  email: string
}

const user = ref<User>({
  id: 1,
  name: 'John',
  email: 'john@example.com'
})
</script>

<template>
  <div>{{ user.name }}</div>
</template>
```

### Example: Vite Config with TypeScript

```typescript
// vite.config.ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  }
})
```

### Key Points

- Vite has built-in TypeScript support
- Use `vite/client` types for import.meta.env
- Configure path aliases in both tsconfig.json and vite.config
- TypeScript files are type-checked but not transformed by Vite
- Use `lang="ts"` in SFC script tags
