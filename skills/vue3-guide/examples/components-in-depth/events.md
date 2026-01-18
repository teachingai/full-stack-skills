# Events

## Instructions

This example demonstrates component events including emitting events and event validation.

### Key Concepts

- Emitting events with `defineEmits()`
- Event arguments
- Event validation
- TypeScript support

### Example: Basic Events

```vue
<!-- ChildComponent.vue -->
<script setup>
defineEmits(['enlarge-text', 'shrink-text'])
</script>

<template>
  <div>
    <button @click="$emit('enlarge-text')">Enlarge</button>
    <button @click="$emit('shrink-text')">Shrink</button>
  </div>
</template>

<!-- ParentComponent.vue -->
<template>
  <ChildComponent
    @enlarge-text="postFontSize += 0.1"
    @shrink-text="postFontSize -= 0.1"
  />
</template>
```

### Example: Events with Arguments

```vue
<!-- ChildComponent.vue -->
<script setup>
const emit = defineEmits(['update', 'delete'])

function handleUpdate() {
  emit('update', { id: 1, value: 'new value' })
}

function handleDelete(id) {
  emit('delete', id)
}
</script>

<template>
  <div>
    <button @click="handleUpdate">Update</button>
    <button @click="handleDelete(1)">Delete</button>
  </div>
</template>

<!-- ParentComponent.vue -->
<template>
  <ChildComponent
    @update="handleUpdate"
    @delete="handleDelete"
  />
</template>

<script setup>
function handleUpdate(data) {
  console.log('Update:', data)
}

function handleDelete(id) {
  console.log('Delete:', id)
}
</script>
```

### Example: Event Validation

```vue
<script setup>
const emit = defineEmits({
  submit: (payload) => {
    if (payload.email && payload.name) {
      return true
    } else {
      console.warn('Invalid submit event payload!')
      return false
    }
  }
})

function submitForm() {
  emit('submit', { email: 'user@example.com', name: 'User' })
}
</script>
```

### Example: TypeScript Events

```vue
<script setup lang="ts">
interface Emits {
  (e: 'update', value: number): void
  (e: 'delete', id: number): void
}

const emit = defineEmits<Emits>()

emit('update', 123)
emit('delete', 456)
</script>
```

### Key Points

- Use `defineEmits()` to define events
- Events flow up (child to parent)
- Event names should use kebab-case
- TypeScript provides type safety for events
