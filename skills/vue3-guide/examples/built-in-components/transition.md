# Transition

## Instructions

This example demonstrates the `<Transition>` component for element transitions.

### Key Concepts

- Transition component
- Transition classes
- Transition hooks
- Named transitions

### Example: Basic Transition

```vue
<template>
  <button @click="show = !show">Toggle</button>
  <Transition>
    <p v-if="show">Hello</p>
  </Transition>
</template>

<script setup>
import { ref } from 'vue'

const show = ref(true)
</script>

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
```

### Key Points

- `<Transition>` wraps single element
- CSS classes: `v-enter-from`, `v-enter-active`, `v-enter-to`, `v-leave-from`, `v-leave-active`, `v-leave-to`
- Use with `v-if`, `v-show`, or dynamic components
