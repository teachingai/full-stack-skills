# Single File Components

## Instructions

This example demonstrates Single File Components (SFC) structure and best practices.

### Key Concepts

- SFC structure
- `<script setup>` syntax
- Scoped styles
- CSS modules

### Example: SFC Structure

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <button @click="count++">Count is: {{ count }}</button>
</template>

<style scoped>
button {
  font-weight: bold;
}
</style>
```

### Key Points

- SFC combines template, script, and styles in one file
- Use `<script setup>` for Composition API
- Scoped styles only apply to component
- CSS modules available with `module` attribute
