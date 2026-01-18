# Teleport

## Instructions

This example demonstrates the `<Teleport>` component for rendering content to different DOM locations.

### Key Concepts

- Teleport component
- to prop
- Conditional teleporting
- Multiple teleports

### Example: Basic Teleport

```vue
<template>
  <button @click="open = true">Open Modal</button>
  <Teleport to="body">
    <div v-if="open" class="modal">
      <p>Modal content</p>
      <button @click="open = false">Close</button>
    </div>
  </Teleport>
</template>

<script setup>
import { ref } from 'vue'

const open = ref(false)
</script>
```

### Key Points

- Renders content to different DOM location
- Use `to` prop to specify target
- Useful for modals, tooltips, popovers
