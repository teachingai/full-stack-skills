# HTML

## Instructions

This example demonstrates HTML handling in Vite projects.

### Key Concepts

- HTML as entry point
- HTML transformation
- Asset references in HTML
- HTML preprocessing

### Example: Basic HTML Entry

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vite App</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
```

### Example: HTML with Asset References

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
  <link rel="icon" href="/favicon.ico">
  <link rel="stylesheet" href="/src/styles/main.css">
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
```

### Example: HTML Transformation

```javascript
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: './index.html',
        admin: './admin.html'
      }
    }
  }
})
```

### Example: HTML Preprocessing

```javascript
// Use plugin for HTML preprocessing
import { defineConfig } from 'vite'
import { createHtmlPlugin } from 'vite-plugin-html'

export default defineConfig({
  plugins: [
    createHtmlPlugin({
      inject: {
        data: {
          title: 'My App'
        }
      }
    })
  ]
})
```

### Key Points

- `index.html` is the entry point (not in `src/`)
- Scripts must use `type="module"`
- Asset references are resolved automatically
- HTML can be transformed by plugins
- Multiple HTML files supported for multi-page apps
