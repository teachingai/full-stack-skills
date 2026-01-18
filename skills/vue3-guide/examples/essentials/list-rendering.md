# List Rendering

## Instructions

This example demonstrates rendering lists using `v-for` directive.

### Key Concepts

- `v-for` for rendering arrays
- `v-for` for rendering objects
- Using `:key` for list items
- `v-for` with ranges
- `v-for` with template

### Example: Basic v-for

```vue
<template>
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item.message }}
    </li>
  </ul>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, message: 'Foo' },
  { id: 2, message: 'Bar' }
])
</script>
```

### Example: v-for with Index

```vue
<template>
  <ul>
    <li v-for="(item, index) in items" :key="item.id">
      {{ index }}: {{ item.message }}
    </li>
  </ul>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, message: 'Foo' },
  { id: 2, message: 'Bar' }
])
</script>
```

### Example: v-for with Object

```vue
<template>
  <ul>
    <li v-for="(value, key, index) in myObject" :key="key">
      {{ index }}. {{ key }}: {{ value }}
    </li>
  </ul>
</template>

<script setup>
import { reactive } from 'vue'

const myObject = reactive({
  title: 'How to do lists in Vue',
  author: 'Jane Doe',
  publishedAt: '2016-04-10'
})
</script>
```

### Example: v-for with Range

```vue
<template>
  <div>
    <span v-for="n in 10" :key="n">{{ n }}</span>
  </div>
</template>
```

### Example: v-for on Template

```vue
<template>
  <ul>
    <template v-for="item in items" :key="item.id">
      <li>{{ item.message }}</li>
      <li class="divider" role="presentation"></li>
    </template>
  </ul>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, message: 'Foo' },
  { id: 2, message: 'Bar' }
])
</script>
```

### Example: v-for with v-if

```vue
<template>
  <!-- v-if has higher priority than v-for -->
  <li v-for="todo in todos" v-if="!todo.isComplete" :key="todo.id">
    {{ todo.text }}
  </li>
  
  <!-- Better: use computed or template wrapper -->
  <template v-for="todo in incompleteTodos" :key="todo.id">
    <li>{{ todo.text }}</li>
  </template>
</template>

<script setup>
import { ref, computed } from 'vue'

const todos = ref([
  { id: 1, text: 'Learn Vue', isComplete: false },
  { id: 2, text: 'Build app', isComplete: true }
])

const incompleteTodos = computed(() => 
  todos.value.filter(todo => !todo.isComplete)
)
</script>
```

### Key Points

- Always use `:key` with `v-for` for proper list updates
- `:key` should be unique and stable
- Use index as key only when list is static
- `v-for` can iterate over arrays, objects, and ranges
- `v-if` has higher priority than `v-for` on the same element
