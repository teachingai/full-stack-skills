# Props

## Instructions

This example demonstrates component props including validation, types, and best practices.

### Key Concepts

- Defining props
- Prop validation
- Prop types
- Required and default values
- TypeScript support

### Example: Basic Props

```vue
<script setup>
defineProps(['title', 'likes'])
</script>

<template>
  <div>
    <h3>{{ title }}</h3>
    <span>{{ likes }}</span>
  </div>
</template>
```

### Example: Props with Types

```vue
<script setup>
defineProps({
  title: String,
  likes: Number,
  isPublished: Boolean,
  commentIds: Array,
  author: Object,
  callback: Function,
  contactsPromise: Promise
})
</script>
```

### Example: Props with Validation

```vue
<script setup>
defineProps({
  // Basic type check
  propA: Number,
  
  // Multiple types
  propB: [String, Number],
  
  // Required
  propC: {
    type: String,
    required: true
  },
  
  // Default value
  propD: {
    type: Number,
    default: 100
  },
  
  // Default function
  propE: {
    type: Object,
    default: () => ({ message: 'hello' })
  },
  
  // Custom validator
  propF: {
    validator: (value) => {
      return ['success', 'warning', 'danger'].includes(value)
    }
  }
})
</script>
```

### Example: TypeScript Props

```vue
<script setup lang="ts">
interface Props {
  title: string
  likes?: number
}

const props = withDefaults(defineProps<Props>(), {
  likes: 0
})
</script>
```

### Key Points

- Props are read-only in child components
- Use prop validation for better error messages
- Always use object syntax for default values
- TypeScript provides compile-time type checking
