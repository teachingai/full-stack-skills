# Component Registration

## Instructions

This example demonstrates global and local component registration in Vue 3.

### Key Concepts

- Global component registration
- Local component registration
- Component naming conventions
- Dynamic components

### Example: Global Registration

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import ComponentA from './components/ComponentA.vue'
import ComponentB from './components/ComponentB.vue'

const app = createApp(App)

// Globally register components
app.component('ComponentA', ComponentA)
app.component('ComponentB', ComponentB)

app.mount('#app')
```

### Example: Local Registration

```vue
<script setup>
import ComponentA from './ComponentA.vue'
import ComponentB from './ComponentB.vue'
</script>

<template>
  <div>
    <ComponentA />
    <ComponentB />
  </div>
</template>
```

### Example: Dynamic Components

```vue
<script setup>
import { ref, shallowRef } from 'vue'
import Home from './Home.vue'
import Posts from './Posts.vue'
import Archive from './Archive.vue'

const currentTab = ref('Home')
const tabs = {
  Home,
  Posts,
  Archive
}
</script>

<template>
  <div class="demo">
    <button
      v-for="(_, tab) in tabs"
      :key="tab"
      :class="['tab-button', { active: currentTab === tab }]"
      @click="currentTab = tab"
    >
      {{ tab }}
    </button>
    <component :is="tabs[currentTab]" class="tab" />
  </div>
</template>
```

### Key Points

- Global registration makes components available everywhere
- Local registration scopes components to specific components
- Use local registration for better tree-shaking
- Dynamic components use `:is` attribute
