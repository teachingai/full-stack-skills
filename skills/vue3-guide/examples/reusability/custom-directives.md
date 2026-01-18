# Custom Directives

## Instructions

This example demonstrates creating custom directives in Vue 3.

### Key Concepts

- Directive definition
- Directive hooks
- Directive arguments and modifiers
- Directive values

### Example: Basic Directive

```vue
<script setup>
const vFocus = {
  mounted: (el) => {
    el.focus()
  }
}
</script>

<template>
  <input v-focus />
</template>
```

### Example: Directive with Hooks

```vue
<script setup>
const vColor = {
  beforeMount(el, binding) {
    el.style.color = binding.value
  },
  updated(el, binding) {
    el.style.color = binding.value
  }
}
</script>

<template>
  <p v-color="'red'">Red text</p>
</template>
```

### Key Points

- Directives provide low-level DOM access
- Use hooks: `beforeMount`, `mounted`, `beforeUpdate`, `updated`, `beforeUnmount`, `unmounted`
- Access binding value, argument, and modifiers
