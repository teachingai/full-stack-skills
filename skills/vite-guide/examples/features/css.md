# CSS Features

## Instructions

This example demonstrates CSS features in Vite including preprocessing, modules, and PostCSS.

### Key Concepts

- CSS preprocessing (Sass, Less, Stylus)
- CSS Modules
- PostCSS
- @import alias and URL rewriting

### Example: CSS Preprocessing

```javascript
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/styles/variables.scss";`
      },
      less: {
        modifyVars: {
          '@primary-color': '#1890ff'
        }
      }
    }
  }
})
```

### Example: Using SCSS

```vue
<style lang="scss">
$primary-color: #42b983;

.button {
  background-color: $primary-color;
  
  &:hover {
    opacity: 0.8;
  }
}
</style>
```

### Example: CSS Modules

```vue
<template>
  <div :class="$style.container">
    <p :class="$style.text">Styled text</p>
  </div>
</template>

<style module>
.container {
  padding: 20px;
}

.text {
  color: #42b983;
}
</style>
```

### Example: CSS Modules with TypeScript

```typescript
// Component.vue
<script setup lang="ts">
import styles from './Component.module.css'

// TypeScript support
const containerClass = styles.container
</script>

<template>
  <div :class="containerClass">Content</div>
</template>
```

### Example: PostCSS Configuration

```javascript
// postcss.config.js
export default {
  plugins: {
    autoprefixer: {},
    tailwindcss: {}
  }
}
```

### Example: Global CSS

```javascript
// main.js
import './styles/global.css'
```

### Key Points

- Vite supports Sass, Less, and Stylus out of the box
- CSS Modules use `module` attribute or `.module.css` extension
- PostCSS is automatically applied
- Use `@import` for global styles in preprocessor options
- CSS is automatically minified in production
