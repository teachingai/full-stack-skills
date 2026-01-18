# Client Types

## Instructions

This example demonstrates client-side types and imports in Vite.

### Key Concepts

- Client-side imports
- Import.meta types
- Environment variable types
- Static asset types

### Example: Import.meta Types

```typescript
// vite-env.d.ts
/// <reference types="vite/client" />

// Import.meta.env types
interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
  readonly MODE: string
  readonly PROD: boolean
  readonly DEV: boolean
  readonly BASE_URL: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
  readonly hot?: {
    accept(cb?: (mod: any) => void): void
    accept(dep: string, cb: (mod: any) => void): void
    accept(deps: string[], cb: (mods: any[]) => void): void
    dispose(cb: () => void): void
    invalidate(): void
  }
}
```

### Example: Static Asset Types

```typescript
// vite-env.d.ts
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare module '*.svg' {
  const content: string
  export default content
}

declare module '*.png' {
  const content: string
  export default content
}

declare module '*.jpg' {
  const content: string
  export default content
}
```

### Example: Using Client Types

```typescript
// main.ts
// Access environment variables with types
const apiUrl: string = import.meta.env.VITE_API_URL
const isDev: boolean = import.meta.env.DEV
const baseUrl: string = import.meta.env.BASE_URL

// HMR API
if (import.meta.hot) {
  import.meta.hot.accept('./module.ts', (newModule) => {
    // Handle update
  })
}
```

### Key Points

- Reference `vite/client` types for import.meta
- Define custom environment variable types
- Declare module types for static assets
- Use TypeScript for type safety
