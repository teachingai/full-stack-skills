# Environment Variables

## Instructions

This example demonstrates environment variables in Vite projects.

### Key Concepts

- Environment variable files
- Variable prefixes
- TypeScript types
- Mode-specific variables

### Example: Environment Files

```
.env                # All environments
.env.local          # All environments (local, gitignored)
.env.development    # Development only
.env.production     # Production only
.env.[mode].local   # Mode-specific local
```

### Example: Using Environment Variables

```javascript
// .env
VITE_API_URL=http://localhost:8080
VITE_APP_TITLE=My App

// In code
console.log(import.meta.env.VITE_API_URL)
console.log(import.meta.env.VITE_APP_TITLE)
console.log(import.meta.env.MODE)        // 'development' or 'production'
console.log(import.meta.env.PROD)        // true in production
console.log(import.meta.env.DEV)         // true in development
console.log(import.meta.env.BASE_URL)    // Base public path
```

### Example: TypeScript Types

```typescript
// vite-env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
  readonly VITE_APP_VERSION: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
```

### Example: Mode-Specific Variables

```bash
# .env.development
VITE_API_URL=http://localhost:8080
VITE_DEBUG=true

# .env.production
VITE_API_URL=https://api.example.com
VITE_DEBUG=false
```

### Example: Loading Variables Programmatically

```javascript
// vite.config.js
import { defineConfig, loadEnv } from 'vite'

export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  
  return {
    define: {
      __APP_VERSION__: JSON.stringify(env.VITE_APP_VERSION)
    }
  }
})
```

### Key Points

- Variables must be prefixed with `VITE_` to be exposed to client
- Use `.env.local` for local overrides (should be gitignored)
- Mode-specific files override base `.env` file
- Access via `import.meta.env`
- Define TypeScript types in `vite-env.d.ts`
