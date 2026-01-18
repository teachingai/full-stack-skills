# Template Refs

## Instructions

This example demonstrates accessing DOM elements and component instances using template refs.

### Key Concepts

- Accessing DOM elements with `ref` attribute
- Accessing component instances
- Refs in `v-for`
- Function refs

### Example: Basic Template Ref

```vue
<template>
  <div>
    <input ref="input" />
    <button @click="focusInput">Focus input</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const input = ref(null)

function focusInput() {
  input.value?.focus()
}

onMounted(() => {
  // Refs are only available after mount
  input.value?.focus()
})
</script>
```

### Example: Ref on Component

```vue
<!-- ChildComponent.vue -->
<script setup>
import { defineExpose, ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}

defineExpose({
  count,
  increment
})
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
  </div>
</template>

<!-- ParentComponent.vue -->
<template>
  <div>
    <ChildComponent ref="child" />
    <button @click="child?.increment()">Increment from parent</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ChildComponent from './ChildComponent.vue'

const child = ref(null)

onMounted(() => {
  console.log(child.value?.count)  // 0
  child.value?.increment()
  console.log(child.value?.count)  // 1
})
</script>
```

### Example: Refs in v-for

```vue
<template>
  <div>
    <ul>
      <li v-for="item in list" :key="item.id" :ref="el => setItemRef(el, item)">
        {{ item.text }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const list = ref([
  { id: 1, text: 'Item 1' },
  { id: 2, text: 'Item 2' },
  { id: 3, text: 'Item 3' }
])

const itemRefs = ref([])

function setItemRef(el, item) {
  if (el) {
    itemRefs.value.push({ el, item })
  }
}
</script>
```

### Example: Function Refs

```vue
<template>
  <div>
    <input :ref="(el) => input = el" />
    <button @click="focusInput">Focus</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

let input = ref(null)

function focusInput() {
  input.value?.focus()
}
</script>
```

### Example: Ref Array

```vue
<template>
  <div>
    <div v-for="item in items" :key="item.id" :ref="setItemRef">
      {{ item.text }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, text: 'Item 1' },
  { id: 2, text: 'Item 2' }
])

const itemRefs = ref([])

function setItemRef(el) {
  if (el) {
    itemRefs.value.push(el)
  }
}
</script>
```

### Key Points

- Use `ref` attribute to get reference to DOM element or component
- Refs are only available after component is mounted
- Use optional chaining (`?.`) when accessing refs
- Use `defineExpose()` to expose properties from child component
- Refs in `v-for` require function refs or ref arrays
