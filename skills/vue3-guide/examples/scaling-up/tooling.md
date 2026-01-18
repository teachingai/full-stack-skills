# Tooling

## Instructions

This example demonstrates Vue 3 tooling setup including build tools, IDE support, and development tools.

### Key Concepts

- Build tools (Vite, Vue CLI, webpack)
- IDE support
- Browser DevTools
- TypeScript support
- ESLint and Prettier

### Example: Vite Setup

```bash
# Create Vue 3 project with Vite
npm create vue@latest my-project

# Or with TypeScript
npm create vue@latest my-project -- --typescript
```

### Example: Vite Configuration

```javascript
// vite.config.js
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

### Example: TypeScript Configuration

```json
// tsconfig.json
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
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src/**/*.ts", "src/**/*.d.ts", "src/**/*.tsx", "src/**/*.vue"]
}
```

### Example: ESLint Configuration

```javascript
// .eslintrc.cjs
module.exports = {
  root: true,
  env: {
    node: true,
    'vue/setup-compiler-macros': true
  },
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended'
  ],
  parserOptions: {
    ecmaVersion: 2020
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off'
  }
}
```

### Example: Vue DevTools

```javascript
// Install Vue DevTools browser extension
// Chrome: https://chrome.google.com/webstore
// Firefox: https://addons.mozilla.org

// Or use standalone app
npm install -g @vue/devtools
```

### Key Points

- Vite is the recommended build tool for Vue 3
- TypeScript support is built-in
- Vue DevTools provides debugging capabilities
- ESLint helps maintain code quality
- IDE extensions provide better development experience
