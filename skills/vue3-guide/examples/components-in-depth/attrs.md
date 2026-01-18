# Fallthrough Attributes

## Instructions

This example demonstrates attribute inheritance and `$attrs` in Vue 3.

### Key Concepts

- Attribute inheritance
- Disabling inheritance
- Accessing `$attrs`
- Multiple root elements

### Example: Attribute Inheritance

```vue
<!-- BaseButton.vue -->
<template>
  <button class="btn">Click me</button>
</template>

<!-- Using the component -->
<template>
  <BaseButton
    type="submit"
    class="large"
    @click="handleClick"
  />
</template>

<!-- Rendered as: -->
<!-- <button type="submit" class="btn large" @click="handleClick">Click me</button> -->
```

### Example: Disabling Inheritance

```vue
<!-- MyComponent.vue -->
<script setup>
defineOptions({
  inheritAttrs: false
})
</script>

<template>
  <div class="wrapper">
    <input v-bind="$attrs" />
  </div>
</template>
```

### Example: Accessing $attrs

```vue
<script setup>
import { useAttrs } from 'vue'

const attrs = useAttrs()
console.log(attrs.class)  // Access attributes
</script>

<template>
  <div>
    <input v-bind="attrs" />
  </div>
</template>
```

### Key Points

- Attributes automatically fall through to root element
- Use `inheritAttrs: false` to disable
- Access `$attrs` to manually control attribute placement
- `$attrs` includes all attributes except props and emits
