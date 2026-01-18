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

### Example: Worker Import

```javascript
// Import Web Worker
import MyWorker from './worker.js?worker'

const worker = new MyWorker()
```

### Example: Shared Worker

```javascript
// Import Shared Worker
import SharedWorker from './shared-worker.js?sharedworker'

const sharedWorker = new SharedWorker()
```

### Example: Asset Inlining

```javascript
// Inline small assets (smaller than 4kb by default)
import smallIcon from './small-icon.png?inline'
```

### Example: Dynamic Asset Import

```javascript
function getImageUrl(name) {
  return new URL(`./assets/${name}.png`, import.meta.url).href
}

const imageUrl = getImageUrl('logo')
```

### Key Points

- Imported assets are processed and get hashed filenames
- Public directory files are copied as-is to dist root
- Use `?url` to get explicit URL
- Use `?raw` to import as raw string
- Use `?worker` for Web Workers
- Small assets (< 4kb) are inlined by default
