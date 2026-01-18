# Multi-page Application

## Instructions

This example demonstrates setting up a multi-page application with Vite.

### Key Concepts

- Multiple HTML entry points
- Shared code
- Page-specific chunks
- Build configuration

### Example: Project Structure

```
my-mpa/
├── index.html             # Main page
├── admin.html             # Admin page
├── package.json
├── vite.config.js
└── src/
    ├── pages/
    │   ├── main/
    │   │   ├── index.js
    │   │   └── App.vue
    │   └── admin/
    │       ├── index.js
    │       └── App.vue
    └── shared/            # Shared code
        ├── components/
        └── utils/
```

### Example: Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        admin: resolve(__dirname, 'admin.html')
      }
    }
  }
})
```

### Key Points

- Multiple HTML files as entry points
- Each page has its own entry script
- Shared code is automatically split
- Configure `build.rollupOptions.input` for multiple entries
