# TransitionGroup

## Instructions

This example demonstrates how to use the `<TransitionGroup>` component for list transitions in Vue 3.

### Key Concepts

- TransitionGroup component
- List transitions
- Enter/leave transitions
- Move transitions
- Transition modes

### Example: Basic TransitionGroup

```vue
<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, text: 'Item 1' },
  { id: 2, text: 'Item 2' },
  { id: 3, text: 'Item 3' }
])

function addItem() {
  items.value.push({ id: Date.now(), text: `Item ${items.value.length + 1}` })
}

function removeItem(item) {
  const index = items.value.indexOf(item)
  if (index > -1) {
    items.value.splice(index, 1)
  }
}
</script>

<template>
  <button @click="addItem">Add Item</button>
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">
      {{ item.text }}
      <button @click="removeItem(item)">Remove</button>
    </li>
  </TransitionGroup>
</template>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.3s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.list-move {
  transition: transform 0.3s ease;
}
</style>
```

### Example: TransitionGroup with Move Transitions

```vue
<template>
  <TransitionGroup name="list" tag="div">
    <div v-for="item in items" :key="item.id" class="item">
      {{ item.text }}
    </div>
  </TransitionGroup>
</template>

<style scoped>
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

.list-leave-active {
  position: absolute;
}
</style>
```

### Key Points

- `<TransitionGroup>` is used for list transitions
- Requires `tag` prop to specify container element
- Each item must have a unique `key`
- Use `move` class for smooth position transitions
- `leave-active` should be positioned absolutely for smooth transitions
