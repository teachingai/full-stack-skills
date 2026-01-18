# Environment Variables and Modes

## Instructions

This example demonstrates environment variables and modes in Vite.

### Key Concepts

- Environment files
- Mode-specific variables
- Variable prefixes
- TypeScript types

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
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
```

### Key Points

- Variables must be prefixed with `VITE_` to be exposed
- Use `.env.local` for local overrides (gitignored)
- Mode-specific files override base `.env` file
- Access via `import.meta.env`
- Define TypeScript types in `vite-env.d.ts`
