# Plugin API Introduction

## Instructions

This example introduces the Vite plugin API and basic concepts.

### Key Concepts

- Plugin structure
- Plugin naming
- Plugin enforce
- Plugin order

### Example: Basic Plugin Structure

```javascript
export default function myPlugin() {
  return {
    name: 'my-plugin',
    enforce: 'pre', // 'pre' | 'post'
    // Plugin hooks here
  }
}
```

### Example: Plugin Naming

```javascript
// Plugin name must be unique
export default function myPlugin() {
  return {
    name: 'vite-plugin-my-plugin', // Recommended format
    // ...
  }
}
```

### Example: Plugin Enforce

```javascript
// Pre plugins run before Vite core plugins
export default function prePlugin() {
  return {
    name: 'pre-plugin',
    enforce: 'pre',
    // Runs first
  }
}

// Post plugins run after Vite core plugins
export default function postPlugin() {
  return {
    name: 'post-plugin',
    enforce: 'post',
    // Runs last
  }
}

// No enforce runs in normal order
export default function normalPlugin() {
  return {
    name: 'normal-plugin',
    // Runs in plugin array order
  }
}
```

### Example: Plugin Order

```javascript
export default defineConfig({
  plugins: [
    prePlugin(),    // Runs first (enforce: 'pre')
    normalPlugin(), // Runs in order
    postPlugin()    // Runs last (enforce: 'post')
  ]
})
```

### Key Points

- Plugin name must be unique
- Use `enforce: 'pre'` for plugins that need to run early
- Use `enforce: 'post'` for plugins that need to run late
- Plugin order matters for plugins without enforce
- Plugin name should follow `vite-plugin-*` convention
