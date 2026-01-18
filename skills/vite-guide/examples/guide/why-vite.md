# Why Vite

## Instructions

This example explains why Vite exists and what problems it solves.

### Key Concepts

- Development server performance
- Production build optimization
- ESM-based development
- HMR improvements

### Example: Development Server Comparison

**Traditional bundler-based dev server:**
- Slow server start (especially for large projects)
- Slow updates (rebundling entire app)
- Linear relationship between app size and dev server start time

**Vite dev server:**
- Instant server start (serves source files directly)
- Fast HMR (only updates changed modules)
- Constant start time regardless of app size

### Example: Production Build

```javascript
// Vite uses Rollup for production builds
// - Optimized code splitting
// - Tree-shaking
// - Asset optimization
// - Modern output formats
```

### Key Points

- Vite uses native ESM in development
- Production builds use Rollup for optimization
- Fast HMR with precise updates
- Framework-agnostic (works with Vue, React, Svelte, etc.)
