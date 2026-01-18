# Conditional Rendering

## Instructions

This example demonstrates conditional rendering using `v-if`, `v-else-if`, `v-else`, and `v-show`.

### Key Concepts

- `v-if` for conditional rendering
- `v-else-if` and `v-else` for multiple conditions
- `v-show` for toggling visibility
- `v-if` vs `v-show` differences

### Example: v-if / v-else-if / v-else

```vue
<template>
  <div>
    <p v-if="type === 'A'">Type A</p>
    <p v-else-if="type === 'B'">Type B</p>
    <p v-else-if="type === 'C'">Type C</p>
    <p v-else>Not A, B, or C</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const type = ref('A')
</script>
```

### Example: v-if on Template

```vue
<template>
  <template v-if="ok">
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </template>
</template>

<script setup>
import { ref } from 'vue'

const ok = ref(true)
</script>
```

### Example: v-show

```vue
<template>
  <div>
    <h1 v-show="ok">Hello!</h1>
    <p v-show="!ok">Goodbye!</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const ok = ref(true)
</script>
```

### Example: v-if vs v-show

```vue
<template>
  <div>
    <!-- v-if: Conditional rendering, lazy, higher toggle cost -->
    <div v-if="showWithIf">
      <p>This is conditionally rendered</p>
      <p>Only exists in DOM when showWithIf is true</p>
    </div>
    
    <!-- v-show: Always renders, toggles display, higher initial cost -->
    <div v-show="showWithShow">
      <p>This is always in DOM</p>
      <p>Only visibility is toggled</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const showWithIf = ref(true)
const showWithShow = ref(true)
</script>
```

### Key Points

- `v-if` is "lazy" - element is not rendered until condition is true
- `v-show` always renders - only toggles CSS display property
- Use `v-if` for infrequent toggles (lower initial render cost)
- Use `v-show` for frequent toggles (lower toggle cost)
- `v-if` has higher toggle cost, `v-show` has higher initial render cost
