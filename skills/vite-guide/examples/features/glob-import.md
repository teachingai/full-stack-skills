# Glob Import

## Instructions

This example demonstrates glob import patterns in Vite.

### Key Concepts

- Glob patterns
- Dynamic imports
- Eager imports
- Multiple patterns

### Example: Basic Glob Import

```javascript
// Import all modules matching pattern
const modules = import.meta.glob('./dir/*.js')

// Access modules
for (const path in modules) {
  modules[path]().then((mod) => {
    console.log(path, mod)
  })
}
```

### Example: Eager Glob Import

```javascript
// Eagerly import all modules
const modules = import.meta.glob('./dir/*.js', { eager: true })

// Direct access (already loaded)
for (const path in modules) {
  console.log(path, modules[path])
}
```

### Example: Named Imports

```javascript
// Import specific exports
const modules = import.meta.glob('./dir/*.js', { 
  import: 'default',
  eager: true
})
```

### Example: Multiple Patterns

```javascript
// Multiple glob patterns
const modules = import.meta.glob([
  './dir/*.js',
  './dir/*.ts',
  '!./dir/exclude.js'  // Exclude pattern
])
```

### Example: Custom Query

```javascript
// With custom query
const modules = import.meta.glob('./dir/*.js', {
  query: { raw: true }
})
```

### Key Points

- Use `import.meta.glob` for pattern matching
- Patterns support `*` and `**` wildcards
- Use `!` prefix to exclude patterns
- `eager: true` loads modules immediately
- Supports custom import queries
