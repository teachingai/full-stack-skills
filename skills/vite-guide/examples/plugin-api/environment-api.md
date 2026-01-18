# Environment API

## Instructions

This example demonstrates the environment API available to plugins.

### Key Concepts

- import.meta.env
- import.meta.hot
- import.meta.glob
- Client types

### Example: Using import.meta.env

```javascript
// In plugin or code
const apiUrl = import.meta.env.VITE_API_URL
const isDev = import.meta.env.DEV
const isProd = import.meta.env.PROD
const mode = import.meta.env.MODE
const baseUrl = import.meta.env.BASE_URL
```

### Example: HMR API

```javascript
// Hot Module Replacement API
if (import.meta.hot) {
  // Accept updates
  import.meta.hot.accept('./module.js', (newModule) => {
    // Handle update
    console.log('Module updated:', newModule)
  })
  
  // Accept dependencies
  import.meta.hot.accept(['./a.js', './b.js'], (modules) => {
    // Handle multiple updates
  })
  
  // Dispose callback
  import.meta.hot.dispose((data) => {
    // Cleanup
    data.cleanup = true
  })
  
  // Invalidate
  import.meta.hot.invalidate()
  
  // Send custom events
  import.meta.hot.send('custom-event', { data: 'value' })
  
  // Listen to custom events
  import.meta.hot.on('custom-event', (data) => {
    console.log('Received:', data)
  })
}
```

### Example: Glob Import API

```javascript
// Glob import
const modules = import.meta.glob('./dir/*.js')

// Eager glob import
const modules = import.meta.glob('./dir/*.js', { eager: true })

// Glob with options
const modules = import.meta.glob('./dir/*.js', {
  import: 'default',
  eager: true
})
```

### Example: Client Types

```typescript
// vite-env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
  readonly hot?: {
    accept(cb?: (mod: any) => void): void
    accept(dep: string, cb: (mod: any) => void): void
    accept(deps: string[], cb: (mods: any[]) => void): void
    dispose(cb: () => void): void
    invalidate(): void
    send(event: string, data?: any): void
    on(event: string, cb: (data: any) => void): void
  }
  readonly glob: (pattern: string, options?: GlobOptions) => Record<string, () => Promise<any>>
}
```

### Key Points

- `import.meta.env` provides environment variables
- `import.meta.hot` provides HMR API (dev only)
- `import.meta.glob` provides glob import functionality
- Define TypeScript types in `vite-env.d.ts`
- Environment API is available in client code
