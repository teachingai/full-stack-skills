# Dependency Injection

## Instructions

This example demonstrates provide/inject for dependency injection in Vue 3.

### Key Concepts

- `provide()` to provide data
- `inject()` to inject data
- Injection with defaults
- Injection keys
- Reactive provide/inject

### Example: Basic Provide/Inject

```vue
<!-- ParentComponent.vue -->
<script setup>
import { provide } from 'vue'
import ChildComponent from './ChildComponent.vue'

const theme = ref('dark')

provide('theme', theme)
</script>

<template>
  <ChildComponent />
</template>

<!-- ChildComponent.vue (any level deep) -->
<script setup>
import { inject } from 'vue'

const theme = inject('theme', 'light')  // 'light' is default
</script>

<template>
  <div :class="theme">
    Theme: {{ theme }}
  </div>
</template>
```

### Example: Reactive Provide/Inject

```vue
<!-- ParentComponent.vue -->
<script setup>
import { provide, ref } from 'vue'

const location = ref('North Pole')

function updateLocation() {
  location.value = 'South Pole'
}

provide('location', {
  location,
  updateLocation
})
</script>

<!-- ChildComponent.vue -->
<script setup>
import { inject } from 'vue'

const { location, updateLocation } = inject('location')
</script>

<template>
  <div>
    <p>Location: {{ location }}</p>
    <button @click="updateLocation">Update Location</button>
  </div>
</template>
```

### Example: Injection Keys

```javascript
// keys.js
export const ThemeSymbol = Symbol()

// ParentComponent.vue
import { provide } from 'vue'
import { ThemeSymbol } from './keys'

provide(ThemeSymbol, 'dark')

// ChildComponent.vue
import { inject } from 'vue'
import { ThemeSymbol } from './keys'

const theme = inject(ThemeSymbol)
```

### Key Points

- `provide()` makes data available to all descendants
- `inject()` retrieves provided data
- Use Symbols for injection keys to avoid conflicts
- Provide reactive values to maintain reactivity
