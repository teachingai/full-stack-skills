# Static Assets

## Instructions

This example demonstrates how to handle static assets in Vite projects.

### Key Concepts

- Importing static assets
- Public directory
- Asset URL handling
- Explicit URL imports
- Raw imports

### Example: Importing Images

```vue
<script setup>
import logo from './assets/logo.png'
import icon from './assets/icon.svg'
</script>

<template>
  <img :src="logo" alt="Logo" />
  <img :src="icon" alt="Icon" />
</template>
```

### Example: Public Directory

```html
<!-- Files in public/ are served at root -->
<img src="/logo.png" alt="Logo" />
<link rel="icon" href="/favicon.ico" />
```

### Example: Explicit URL Import

```javascript
// Get explicit URL
import logoUrl from './logo.png?url'

console.log(logoUrl) // /assets/logo.abc123.png
```

### Example: Raw Import

```javascript
// Import as raw string
import logoRaw from './logo.svg?raw'

console.log(logoRaw) // Raw SVG content as string
```

### Key Points

- Imported assets are processed and get hashed filenames
- Public directory files are copied as-is to dist root
- Use `?url` to get explicit URL
- Use `?raw` to import as raw string
- Small assets (< 4kb) are inlined by default
