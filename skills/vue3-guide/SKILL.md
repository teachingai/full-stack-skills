---
name: vue3-guide
description: Vue 3.x 完整开发指南，基于官方文档（https://cn.vuejs.org/guide/introduction），涵盖声明式渲染、响应式系统、组合式 API、单文件组件、模板语法、组件开发、路由管理、状态管理等核心概念和最佳实践。适用于使用 Vue 3 开发前端应用的场景。
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create Vue 3 applications or components
- Learn Vue 3 core concepts (declarative rendering, reactivity, Composition API)
- Build single-file components (SFC) with Vue 3
- Implement component communication (props, emits, provide/inject)
- Set up routing with Vue Router
- Manage application state with Pinia or Vuex
- Use TypeScript with Vue 3
- Optimize Vue 3 application performance
- Understand the differences between Composition API and Options API
- Create reusable composables (composition functions)
- Work with Vue 3 template syntax (directives, bindings, event handling)
- Set up Vue 3 projects with Vite or other build tools
- Implement lifecycle hooks in Vue 3
- Handle forms and user input with v-model
- Create dynamic and conditional rendering
- Work with lists and rendering (v-for)
- Implement transitions and animations
- Use Vue 3 with UI component libraries (Element Plus, Ant Design Vue, etc.)

## How to use this skill

This skill is organized to match the Vue 3 official documentation structure (https://cn.vuejs.org/guide/introduction.html). When working with Vue 3:

1. **Identify the topic** from the user's request:
   - Creating an application/创建一个应用 → `examples/essentials/creating-an-app.md`
   - Template syntax/模板语法 → `examples/essentials/template-syntax.md`
   - Reactivity fundamentals/响应式基础 → `examples/essentials/reactivity-fundamentals.md`
   - Computed properties/计算属性 → `examples/essentials/computed-properties.md`
   - Class and style bindings/类与样式绑定 → `examples/essentials/class-and-style-bindings.md`
   - Conditional rendering/条件渲染 → `examples/essentials/conditional-rendering.md`
   - List rendering/列表渲染 → `examples/essentials/list-rendering.md`
   - Event handling/事件处理 → `examples/essentials/event-handling.md`
   - Form input binding/表单输入绑定 → `examples/essentials/form-input-binding.md`
   - Watchers/侦听器 → `examples/essentials/watchers.md`
   - Template refs/模板引用 → `examples/essentials/template-refs.md`
   - Component basics/组件基础 → `examples/essentials/component-basics.md`
   - Lifecycle/生命周期 → `examples/essentials/lifecycle.md`
   - Component registration/注册 → `examples/components-in-depth/registration.md`
   - Props → `examples/components-in-depth/props.md`
   - Events/事件 → `examples/components-in-depth/events.md`
   - Component v-model → `examples/components-in-depth/component-v-model.md`
   - Fallthrough attributes/透传 Attributes → `examples/components-in-depth/attrs.md`
   - Slots/插槽 → `examples/components-in-depth/slots.md`
   - Dependency injection/依赖注入 → `examples/components-in-depth/dependency-injection.md`
   - Async components/异步组件 → `examples/components-in-depth/async-components.md`
   - Composables/组合式函数 → `examples/reusability/composables.md`
   - Custom directives/自定义指令 → `examples/reusability/custom-directives.md`
   - Plugins/插件 → `examples/reusability/plugins.md`
   - Transition → `examples/built-in-components/transition.md`
   - KeepAlive → `examples/built-in-components/keepalive.md`
   - Teleport → `examples/built-in-components/teleport.md`
   - Single File Components/单文件组件 → `examples/scaling-up/single-file-components.md`
   - Routing/路由 → `examples/scaling-up/routing.md`
   - State management/状态管理 → `examples/scaling-up/state-management.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Essentials (基础)**:
   - `examples/essentials/creating-an-app.md` - Creating a Vue application with `createApp()`
   - `examples/essentials/template-syntax.md` - Template syntax, interpolation, and expressions
   - `examples/essentials/reactivity-fundamentals.md` - `ref()` and `reactive()` for reactive state
   - `examples/essentials/computed-properties.md` - Computed properties with `computed()`
   - `examples/essentials/class-and-style-bindings.md` - Dynamic class and style bindings
   - `examples/essentials/conditional-rendering.md` - `v-if`, `v-else-if`, `v-else`, and `v-show`
   - `examples/essentials/list-rendering.md` - `v-for` directive for rendering lists
   - `examples/essentials/event-handling.md` - Event handling with `v-on` and event modifiers
   - `examples/essentials/form-input-binding.md` - Two-way binding with `v-model` for form inputs
   - `examples/essentials/watchers.md` - `watch()` and `watchEffect()` for side effects
   - `examples/essentials/template-refs.md` - Accessing DOM elements and component instances
   - `examples/essentials/component-basics.md` - Component basics, props, events, and slots
   - `examples/essentials/lifecycle.md` - Component lifecycle hooks

   **Components In Depth (深入组件)**:
   - `examples/components-in-depth/registration.md` - Global and local component registration
   - `examples/components-in-depth/props.md` - Props definition, validation, and TypeScript support
   - `examples/components-in-depth/events.md` - Emitting events and event validation
   - `examples/components-in-depth/component-v-model.md` - Using `v-model` with custom components
   - `examples/components-in-depth/attrs.md` - Fallthrough attributes and `$attrs`
   - `examples/components-in-depth/slots.md` - Default, named, and scoped slots
   - `examples/components-in-depth/dependency-injection.md` - Provide/Inject for dependency injection
   - `examples/components-in-depth/async-components.md` - Async components and code splitting

   **Reusability (逻辑复用)**:
   - `examples/reusability/composables.md` - Creating and using composables (composition functions)
   - `examples/reusability/custom-directives.md` - Creating custom directives
   - `examples/reusability/plugins.md` - Creating and using Vue plugins

   **Built-in Components (内置组件)**:
   - `examples/built-in-components/transition.md` - `<Transition>` component for element transitions
   - `examples/built-in-components/keepalive.md` - `<KeepAlive>` component for caching instances
   - `examples/built-in-components/teleport.md` - `<Teleport>` component for rendering to different DOM locations

   **Scaling Up (应用规模化)**:
   - `examples/scaling-up/single-file-components.md` - Single File Components (SFC) structure
   - `examples/scaling-up/routing.md` - Vue Router setup and navigation
   - `examples/scaling-up/state-management.md` - Pinia state management

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Vue 3 Composition API with `<script setup>` syntax
   - Examples include both JavaScript and TypeScript versions where applicable
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/reactivity-core/ref.md` - `ref()` API reference
   - `api/reactivity-core/reactive.md` - `reactive()` API reference
   - `api/reactivity-core/computed.md` - `computed()` API reference
   - `api/reactivity-core/watch.md` - `watch()` API reference
   - `api/reactivity-utilities/toRef.md` - `toRef()` and `toRefs()` API reference
   - `api/lifecycle/onMounted.md` - Lifecycle hooks API reference
   - `api/component/defineProps.md` - Component APIs (`defineProps()`, `defineEmits()`, `defineExpose()`)

5. **Use templates** from the `templates/` directory:
   - `templates/project-structure.md` - Standard Vue 3 project organization, component templates, composable templates, store templates, router templates, and Vite configuration templates

### 1. Understanding Vue 3 Fundamentals

Vue 3 is a progressive JavaScript framework for building user interfaces. It's designed to be incrementally adoptable, meaning you can use as much or as little of it as needed.

**Key Concepts**:
- **Progressive Framework**: Vue can be used from simple enhancements to full-featured SPAs
- **Declarative Rendering**: Use template syntax to declaratively render data to the DOM
- **Reactivity System**: Automatic DOM updates when reactive state changes
- **Component-Based**: Build reusable components that encapsulate logic and UI

### 2. Project Setup

**Using Vite (Recommended)**:

```bash
# Create a new Vue 3 project
npm create vue@latest my-vue-app

# Or using yarn
yarn create vue my-vue-app

# Navigate to project
cd my-vue-app

# Install dependencies
npm install

# Start development server
npm run dev
```

**Project Structure**:
```
my-vue-app/
├── src/
│   ├── components/      # Reusable components
│   ├── views/          # Page components
│   ├── router/         # Vue Router configuration
│   ├── stores/         # Pinia stores
│   ├── composables/    # Reusable composition functions
│   ├── assets/         # Static assets
│   ├── App.vue         # Root component
│   └── main.js         # Application entry point
├── public/             # Public static files
├── package.json
└── vite.config.js     # Vite configuration
```

### 3. Declarative Rendering

Vue uses a template syntax that extends HTML, allowing you to declaratively describe the output based on your component's state.

**Basic Example**:

```vue
<script setup>
import { ref } from 'vue'

const message = ref('Hello Vue 3!')
const count = ref(0)

function increment() {
  count.value++
}
</script>

<template>
  <div>
    <h1>{{ message }}</h1>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>
```

**Key Points**:
- Use `{{ }}` for text interpolation
- Use `v-bind` (or `:`) for attribute binding
- Use `v-on` (or `@`) for event handling
- Use `v-model` for two-way data binding

### 4. Composition API vs Options API

Vue 3 supports two API styles:

**Composition API (Recommended)**:

```vue
<script setup>
import { ref, computed, watch, onMounted } from 'vue'

// Reactive state
const count = ref(0)
const doubleCount = computed(() => count.value * 2)

// Watchers
watch(count, (newVal, oldVal) => {
  console.log(`Count changed from ${oldVal} to ${newVal}`)
})

// Lifecycle hooks
onMounted(() => {
  console.log('Component mounted')
})

// Methods
function increment() {
  count.value++
}
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="increment">+1</button>
  </div>
</template>
```

**Options API (Traditional)**:

```vue
<script>
export default {
  data() {
    return {
      count: 0
    }
  },
  computed: {
    doubleCount() {
      return this.count * 2
    }
  },
  watch: {
    count(newVal, oldVal) {
      console.log(`Count changed from ${oldVal} to ${newVal}`)
    }
  },
  mounted() {
    console.log('Component mounted')
  },
  methods: {
    increment() {
      this.count++
    }
  }
}
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="increment">+1</button>
  </div>
</template>
```

**When to Use Each**:
- **Composition API**: Better for complex components, better TypeScript support, easier logic reuse
- **Options API**: More familiar for Vue 2 developers, better for simple components, more intuitive for object-oriented developers

### 5. Reactive State

Vue 3's reactivity system automatically tracks dependencies and updates the DOM when reactive state changes.

**ref() - For Primitive Values and Objects**:

```vue
<script setup>
import { ref } from 'vue'

// Primitive values
const count = ref(0)
const message = ref('Hello')

// Objects (ref wraps the object)
const user = ref({
  name: 'Vue',
  age: 3
})

// Access with .value in script
console.log(count.value)      // 0
console.log(user.value.name)  // 'Vue'

// In template, .value is automatically unwrapped
</script>

<template>
  <div>
    <p>{{ count }}</p>           <!-- No .value needed -->
    <p>{{ user.name }}</p>       <!-- No .value needed -->
  </div>
</template>
```

**reactive() - For Objects and Arrays**:

```vue
<script setup>
import { reactive } from 'vue'

const state = reactive({
  count: 0,
  message: 'Hello',
  user: {
    name: 'Vue',
    age: 3
  }
})

// Direct access (no .value)
state.count++
state.user.name = 'Vue 3'
</script>

<template>
  <div>
    <p>{{ state.count }}</p>
    <p>{{ state.user.name }}</p>
  </div>
</template>
```

**Key Differences**:
- `ref()`: Use for primitives or when you need to replace the entire object
- `reactive()`: Use for objects/arrays, but cannot be reassigned
- `ref()` requires `.value` in script, `reactive()` doesn't
- Both are automatically unwrapped in templates

### 6. Computed Properties

Computed properties are cached and only re-evaluate when their reactive dependencies change.

```vue
<script setup>
import { ref, computed } from 'vue'

const firstName = ref('John')
const lastName = ref('Doe')

// Computed property
const fullName = computed(() => {
  return `${firstName.value} ${lastName.value}`
})

// Computed with getter and setter
const fullNameWithSetter = computed({
  get() {
    return `${firstName.value} ${lastName.value}`
  },
  set(newValue) {
    const parts = newValue.split(' ')
    firstName.value = parts[0]
    lastName.value = parts[1] || ''
  }
})
</script>

<template>
  <div>
    <p>Full Name: {{ fullName }}</p>
    <input v-model="fullNameWithSetter" />
  </div>
</template>
```

### 7. Watchers

Watchers allow you to perform side effects when reactive state changes.

**watch() - Watch a Single Source**:

```vue
<script setup>
import { ref, watch } from 'vue'

const count = ref(0)
const message = ref('')

// Watch a single ref
watch(count, (newVal, oldVal) => {
  console.log(`Count: ${oldVal} -> ${newVal}`)
  message.value = `Count changed to ${newVal}`
})

// Watch with options
watch(count, (newVal, oldVal) => {
  // Side effect
}, {
  immediate: true,    // Run immediately
  deep: true,          // Deep watch for objects
  flush: 'post'        // Timing of callback
})
</script>
```

**watchEffect() - Automatic Dependency Tracking**:

```vue
<script setup>
import { ref, watchEffect } from 'vue'

const count = ref(0)
const doubleCount = ref(0)

// Automatically tracks dependencies
watchEffect(() => {
  doubleCount.value = count.value * 2
  console.log(`Double count: ${doubleCount.value}`)
})
</script>
```

**watch() vs watchEffect()**:
- `watch()`: Explicitly specify what to watch, lazy by default
- `watchEffect()`: Automatically tracks dependencies, runs immediately

### 8. Lifecycle Hooks

Vue 3 provides lifecycle hooks that allow you to run code at specific stages of a component's lifecycle.

```vue
<script setup>
import {
  onBeforeMount,
  onMounted,
  onBeforeUpdate,
  onUpdated,
  onBeforeUnmount,
  onUnmounted
} from 'vue'

onBeforeMount(() => {
  console.log('Before mount')
})

onMounted(() => {
  console.log('Mounted - DOM is ready')
  // Good place for API calls, DOM manipulation
})

onBeforeUpdate(() => {
  console.log('Before update')
})

onUpdated(() => {
  console.log('Updated - DOM updated')
})

onBeforeUnmount(() => {
  console.log('Before unmount')
})

onUnmounted(() => {
  console.log('Unmounted - cleanup')
  // Good place for cleanup (timers, subscriptions, etc.)
})
</script>
```

**Lifecycle Diagram**:
```
setup() / beforeCreate
  ↓
created
  ↓
onBeforeMount / beforeMount
  ↓
onMounted / mounted
  ↓
onBeforeUpdate / beforeUpdate (when data changes)
  ↓
onUpdated / updated
  ↓
onBeforeUnmount / beforeUnmount
  ↓
onUnmounted / unmounted
```

### 9. Template Syntax

Vue's template syntax extends HTML with special directives and syntax.

**Text Interpolation**:

```vue
<template>
  <div>
    <p>Message: {{ message }}</p>
    <p v-text="message"></p>
    <p v-html="htmlContent"></p>  <!-- Use with caution! -->
  </div>
</template>
```

**Attribute Binding**:

```vue
<template>
  <div>
    <!-- v-bind or : -->
    <a v-bind:href="url">Link</a>
    <a :href="url">Link (shorthand)</a>
    <img :src="imageSrc" :alt="imageAlt" />
    
    <!-- Boolean attributes -->
    <button :disabled="isDisabled">Button</button>
    
    <!-- Dynamic attribute names -->
    <div :[attributeName]="value"></div>
  </div>
</template>
```

**Event Handling**:

```vue
<template>
  <div>
    <!-- v-on or @ -->
    <button v-on:click="handleClick">Click</button>
    <button @click="handleClick">Click (shorthand)</button>
    
    <!-- Inline handlers -->
    <button @click="count++">Increment</button>
    
    <!-- Method handlers -->
    <button @click="handleClick">Click</button>
    
    <!-- Event modifiers -->
    <form @submit.prevent="onSubmit">
      <input @keyup.enter="submit" />
    </form>
    
    <!-- Multiple modifiers -->
    <a @click.stop.prevent="handleLink">Link</a>
  </div>
</template>

<script setup>
function handleClick(event) {
  console.log('Clicked', event)
}

function onSubmit() {
  // Form won't submit
}

function submit() {
  // Triggered on Enter key
}
</script>
```

**Two-Way Binding (v-model)**:

```vue
<template>
  <div>
    <!-- Text input -->
    <input v-model="message" />
    <p>Message: {{ message }}</p>
    
    <!-- Checkbox -->
    <input type="checkbox" v-model="checked" />
    <p>Checked: {{ checked }}</p>
    
    <!-- Multiple checkboxes -->
    <input type="checkbox" value="vue" v-model="frameworks" />
    <input type="checkbox" value="react" v-model="frameworks" />
    <p>Frameworks: {{ frameworks }}</p>
    
    <!-- Radio -->
    <input type="radio" value="vue" v-model="framework" />
    <input type="radio" value="react" v-model="framework" />
    <p>Framework: {{ framework }}</p>
    
    <!-- Select -->
    <select v-model="selected">
      <option value="vue">Vue</option>
      <option value="react">React</option>
    </select>
    <p>Selected: {{ selected }}</p>
    
    <!-- Custom v-model -->
    <CustomInput v-model="customValue" />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('')
const checked = ref(false)
const frameworks = ref([])
const framework = ref('vue')
const selected = ref('vue')
const customValue = ref('')
</script>
```

**Conditional Rendering**:

```vue
<template>
  <div>
    <!-- v-if / v-else-if / v-else -->
    <p v-if="type === 'A'">Type A</p>
    <p v-else-if="type === 'B'">Type B</p>
    <p v-else>Type C</p>
    
    <!-- v-show (always renders, toggles display) -->
    <p v-show="isVisible">Visible content</p>
    
    <!-- v-if vs v-show -->
    <!-- v-if: Conditional rendering, lazy, higher toggle cost -->
    <!-- v-show: Always renders, toggles display, higher initial cost -->
  </div>
</template>
```

**List Rendering**:

```vue
<template>
  <div>
    <!-- Basic v-for -->
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }}
      </li>
    </ul>
    
    <!-- v-for with index -->
    <ul>
      <li v-for="(item, index) in items" :key="item.id">
        {{ index }}: {{ item.name }}
      </li>
    </ul>
    
    <!-- v-for with object -->
    <ul>
      <li v-for="(value, key, index) in object" :key="key">
        {{ key }}: {{ value }}
      </li>
    </ul>
    
    <!-- v-for with range -->
    <span v-for="n in 10" :key="n">{{ n }}</span>
    
    <!-- v-for on template -->
    <template v-for="item in items" :key="item.id">
      <p>{{ item.name }}</p>
      <p>{{ item.description }}</p>
    </template>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, name: 'Vue', description: 'Progressive Framework' },
  { id: 2, name: 'React', description: 'UI Library' }
])

const object = ref({
  title: 'How to do lists in Vue',
  author: 'Jane Doe',
  publishedAt: '2016-04-10'
})
</script>
```

### 10. Component Basics

Components are reusable Vue instances with a name.

**Component Definition**:

```vue
<!-- MyComponent.vue -->
<script setup>
import { defineProps, defineEmits, defineExpose } from 'vue'

// Props definition
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  count: {
    type: Number,
    default: 0
  },
  items: {
    type: Array,
    default: () => []
  }
})

// With TypeScript
// const props = defineProps<{
//   title: string
//   count?: number
//   items?: Array<any>
// }>()

// Emits definition
const emit = defineEmits(['update', 'delete'])

// With TypeScript
// const emit = defineEmits<{
//   update: [id: number]
//   delete: [id: number]
// }>()

// Expose methods to parent
const reset = () => {
  // Reset logic
}
defineExpose({ reset })
</script>

<template>
  <div>
    <h2>{{ title }}</h2>
    <p>Count: {{ count }}</p>
    <button @click="emit('update', count + 1)">Update</button>
    <button @click="emit('delete', count)">Delete</button>
  </div>
</template>
```

**Using Components**:

```vue
<script setup>
import MyComponent from './MyComponent.vue'
import { ref } from 'vue'

const count = ref(0)

function handleUpdate(newCount) {
  count.value = newCount
}

function handleDelete(id) {
  console.log('Delete', id)
}
</script>

<template>
  <div>
    <MyComponent
      title="My Component"
      :count="count"
      @update="handleUpdate"
      @delete="handleDelete"
    />
  </div>
</template>
```

**Slots**:

```vue
<!-- BaseLayout.vue -->
<template>
  <div class="container">
    <header>
      <slot name="header"></slot>
    </header>
    <main>
      <slot></slot>  <!-- Default slot -->
    </main>
    <footer>
      <slot name="footer"></slot>
    </footer>
  </div>
</template>

<!-- Using slots -->
<template>
  <BaseLayout>
    <template #header>
      <h1>Header Content</h1>
    </template>
    
    <p>Main content</p>
    
    <template #footer>
      <p>Footer Content</p>
    </template>
  </BaseLayout>
</template>
```

**Scoped Slots**:

```vue
<!-- MyList.vue -->
<template>
  <ul>
    <li v-for="item in items" :key="item.id">
      <slot :item="item" :index="index"></slot>
    </li>
  </ul>
</template>

<!-- Using scoped slots -->
<template>
  <MyList :items="items">
    <template #default="{ item, index }">
      <span>{{ index }}: {{ item.name }}</span>
    </template>
  </MyList>
</template>
```

### 11. Provide / Inject

Provide and Inject allow ancestor components to provide data to all descendant components.

```vue
<!-- Parent Component -->
<script setup>
import { provide, ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

const theme = ref('dark')

provide('theme', theme)
provide('updateTheme', (newTheme) => {
  theme.value = newTheme
})
</script>

<template>
  <ChildComponent />
</template>

<!-- Child Component (any level deep) -->
<script setup>
import { inject } from 'vue'

const theme = inject('theme', 'light')  // 'light' is default
const updateTheme = inject('updateTheme')

function toggleTheme() {
  updateTheme(theme === 'dark' ? 'light' : 'dark')
}
</script>

<template>
  <div :class="theme">
    <button @click="toggleTheme">Toggle Theme</button>
  </div>
</template>
```

### 12. Vue Router

Vue Router is the official router for Vue.js applications.

**Router Setup**:

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/user/:id',
    name: 'User',
    component: () => import('../views/User.vue'),
    props: true  // Pass route params as props
  },
  {
    path: '/admin',
    component: () => import('../views/Admin.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: 'dashboard',
        component: () => import('../views/Dashboard.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guards
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next('/login')
  } else {
    next()
  }
})

export default router
```

**Using Router in Components**:

```vue
<script setup>
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// Programmatic navigation
function goToAbout() {
  router.push('/about')
  // Or: router.push({ name: 'About' })
  // Or: router.push({ path: '/about', query: { id: '123' } })
}

// Get route params
const userId = route.params.id
const queryParam = route.query.search

// Navigation methods
function navigate() {
  router.push('/path')        // Navigate forward
  router.replace('/path')     // Replace current entry
  router.go(-1)              // Go back
  router.go(1)               // Go forward
  router.back()              // Go back
  router.forward()           // Go forward
}
</script>

<template>
  <div>
    <!-- Declarative navigation -->
    <router-link to="/">Home</router-link>
    <router-link :to="{ name: 'About' }">About</router-link>
    <router-link :to="{ path: '/user', params: { id: '123' } }">User</router-link>
    
    <!-- Router view -->
    <router-view />
    
    <!-- Named views -->
    <router-view name="sidebar" />
  </div>
</template>
```

### 13. State Management with Pinia

Pinia is the official state management library for Vue 3.

**Store Definition**:

```javascript
// stores/counter.js
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0,
    name: 'Vue 3'
  }),
  
  getters: {
    doubleCount: (state) => state.count * 2,
    // Access other getters
    doubleCountPlusOne() {
      return this.doubleCount + 1
    }
  },
  
  actions: {
    increment() {
      this.count++
    },
    decrement() {
      this.count--
    },
    async fetchData() {
      const response = await fetch('/api/data')
      this.name = await response.json()
    }
  }
})
```

**Using Store in Components**:

```vue
<script setup>
import { useCounterStore } from '@/stores/counter'
import { storeToRefs } from 'pinia'

const counterStore = useCounterStore()

// Access state (loses reactivity if destructured)
const { count, name } = storeToRefs(counterStore)

// Or access directly (maintains reactivity)
console.log(counterStore.count)
console.log(counterStore.doubleCount)

// Call actions
counterStore.increment()
counterStore.decrement()

// Reset store
counterStore.$reset()

// Watch store changes
counterStore.$subscribe((mutation, state) => {
  console.log('Store changed', mutation, state)
})
</script>

<template>
  <div>
    <p>Count: {{ counterStore.count }}</p>
    <p>Double: {{ counterStore.doubleCount }}</p>
    <button @click="counterStore.increment">+</button>
    <button @click="counterStore.decrement">-</button>
  </div>
</template>
```

### 14. Composables (Composition Functions)

Composables are reusable composition functions that encapsulate and reuse stateful logic.

**Creating a Composable**:

```javascript
// composables/useCounter.js
import { ref, computed } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)
  
  const doubleCount = computed(() => count.value * 2)
  
  const increment = () => {
    count.value++
  }
  
  const decrement = () => {
    count.value--
  }
  
  const reset = () => {
    count.value = initialValue
  }
  
  return {
    count,
    doubleCount,
    increment,
    decrement,
    reset
  }
}
```

**Using a Composable**:

```vue
<script setup>
import { useCounter } from '@/composables/useCounter'

const { count, doubleCount, increment, decrement, reset } = useCounter(10)
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="increment">+</button>
    <button @click="decrement">-</button>
    <button @click="reset">Reset</button>
  </div>
</template>
```

**More Composable Examples**:

```javascript
// composables/useMouse.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)
  
  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }
  
  onMounted(() => {
    window.addEventListener('mousemove', update)
  })
  
  onUnmounted(() => {
    window.removeEventListener('mousemove', update)
  })
  
  return { x, y }
}

// composables/useFetch.js
import { ref } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)
  const loading = ref(false)
  
  async function fetchData() {
    loading.value = true
    error.value = null
    try {
      const response = await fetch(url)
      data.value = await response.json()
    } catch (e) {
      error.value = e
    } finally {
      loading.value = false
    }
  }
  
  fetchData()
  
  return { data, error, loading, refetch: fetchData }
}
```

### 15. TypeScript Support

Vue 3 has excellent TypeScript support.

**Component with TypeScript**:

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

interface User {
  id: number
  name: string
  email: string
}

const user = ref<User>({
  id: 1,
  name: 'John Doe',
  email: 'john@example.com'
})

const userName = computed(() => user.value.name.toUpperCase())

// Props with TypeScript
interface Props {
  title: string
  count?: number
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
})

// Emits with TypeScript
interface Emits {
  (e: 'update', value: number): void
  (e: 'delete', id: number): void
}

const emit = defineEmits<Emits>()

function handleUpdate() {
  emit('update', props.count + 1)
}
</script>

<template>
  <div>
    <h2>{{ props.title }}</h2>
    <p>Count: {{ props.count }}</p>
    <button @click="handleUpdate">Update</button>
  </div>
</template>
```

### 16. Performance Optimization

**Lazy Loading Components**:

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

// Lazy load component
const HeavyComponent = defineAsyncComponent(() => 
  import('./HeavyComponent.vue')
)

// With loading and error components
const AsyncComponent = defineAsyncComponent({
  loader: () => import('./AsyncComponent.vue'),
  loadingComponent: LoadingComponent,
  errorComponent: ErrorComponent,
  delay: 200,
  timeout: 3000
})
</script>

<template>
  <HeavyComponent />
</template>
```

**Optimizing Lists**:

```vue
<template>
  <div>
    <!-- v-memo: Cache v-for items -->
    <div
      v-for="item in list"
      :key="item.id"
      v-memo="[item.id, item.selected]"
    >
      {{ item.name }}
    </div>
    
    <!-- v-once: Render once -->
    <div v-once>{{ expensiveComputation() }}</div>
    
    <!-- v-show vs v-if -->
    <div v-show="isVisible">Always rendered</div>
    <div v-if="isVisible">Conditionally rendered</div>
  </div>
</template>
```

**Shallow Refs**:

```vue
<script setup>
import { shallowRef, triggerRef } from 'vue'

// Use shallowRef for large objects (doesn't deep watch)
const largeObject = shallowRef({ /* large data */ })

// Manually trigger update
function updateLargeObject() {
  largeObject.value.newProperty = 'value'
  triggerRef(largeObject)
}
</script>
```

## Best Practices

### 1. Code Organization

- **Use `<script setup>`**: Prefer Composition API with `<script setup>` syntax
- **Organize by feature**: Group related logic together
- **Extract composables**: Create reusable composition functions for shared logic
- **Single Responsibility**: Keep components focused on a single responsibility

### 2. Component Structure

```vue
<script setup>
// 1. Imports
import { ref, computed } from 'vue'
import MyComponent from './MyComponent.vue'

// 2. Props & Emits
const props = defineProps({...})
const emit = defineEmits([...])

// 3. Reactive state
const count = ref(0)

// 4. Computed properties
const doubleCount = computed(() => count.value * 2)

// 5. Watchers
watch(count, (newVal) => {...})

// 6. Lifecycle hooks
onMounted(() => {...})

// 7. Methods
function handleClick() {...}
</script>

<template>
  <!-- Template content -->
</template>

<style scoped>
/* Component styles */
</style>
```

### 3. Naming Conventions

- **Components**: PascalCase (e.g., `MyComponent.vue`)
- **Composables**: camelCase with `use` prefix (e.g., `useCounter.js`)
- **Props**: camelCase in script, kebab-case in template
- **Events**: kebab-case (e.g., `update-count`)

### 4. Performance Tips

- Use `v-show` for frequent toggles, `v-if` for conditional rendering
- Use `v-memo` for expensive list items
- Lazy load routes and heavy components
- Use `shallowRef` and `shallowReactive` for large objects
- Avoid unnecessary reactivity with `markRaw()`

### 5. TypeScript Best Practices

- Always use TypeScript for larger projects
- Define interfaces for props, emits, and data structures
- Use `defineProps<T>()` and `defineEmits<T>()` for type safety
- Leverage Vue's TypeScript utilities

### 6. Testing

- Write unit tests for components
- Test composables in isolation
- Use Vue Test Utils or Vitest
- Test user interactions and state changes

## Common Patterns

### 1. Form Handling

```vue
<script setup>
import { ref } from 'vue'

const form = ref({
  name: '',
  email: '',
  age: 0
})

const errors = ref({})

function validate() {
  errors.value = {}
  if (!form.value.name) {
    errors.value.name = 'Name is required'
  }
  if (!form.value.email) {
    errors.value.email = 'Email is required'
  }
}

async function submit() {
  validate()
  if (Object.keys(errors.value).length === 0) {
    // Submit form
  }
}
</script>

<template>
  <form @submit.prevent="submit">
    <input v-model="form.name" />
    <span v-if="errors.name">{{ errors.name }}</span>
    
    <input v-model="form.email" type="email" />
    <span v-if="errors.email">{{ errors.email }}</span>
    
    <button type="submit">Submit</button>
  </form>
</template>
```

### 2. API Integration

```vue
<script setup>
import { ref, onMounted } from 'vue'

const data = ref(null)
const loading = ref(false)
const error = ref(null)

async function fetchData() {
  loading.value = true
  error.value = null
  try {
    const response = await fetch('/api/data')
    data.value = await response.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchData()
})
</script>

<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error }}</div>
    <div v-else>{{ data }}</div>
  </div>
</template>
```

### 3. Modal/Dialog Pattern

```vue
<!-- Modal.vue -->
<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  modelValue: Boolean
})

const emit = defineEmits(['update:modelValue'])

function close() {
  emit('update:modelValue', false)
}
</script>

<template>
  <Teleport to="body">
    <div v-if="modelValue" class="modal" @click.self="close">
      <div class="modal-content">
        <slot />
        <button @click="close">Close</button>
      </div>
    </div>
  </Teleport>
</template>

<!-- Using the modal -->
<template>
  <button @click="showModal = true">Open Modal</button>
  <Modal v-model="showModal">
    <h2>Modal Content</h2>
  </Modal>
</template>
```

## Examples and Templates

This skill includes detailed examples organized to match the Vue 3 official documentation structure. All examples are in the `examples/` directory, organized by topic:

### Essentials (基础) - `examples/essentials/`

- `examples/essentials/creating-an-app.md` - Creating a Vue application with `createApp()`
- `examples/essentials/template-syntax.md` - Template syntax, interpolation, and expressions
- `examples/essentials/reactivity-fundamentals.md` - `ref()` and `reactive()` for reactive state
- `examples/essentials/computed-properties.md` - Computed properties with `computed()`
- `examples/essentials/class-and-style-bindings.md` - Dynamic class and style bindings
- `examples/essentials/conditional-rendering.md` - `v-if`, `v-else-if`, `v-else`, and `v-show`
- `examples/essentials/list-rendering.md` - `v-for` directive for rendering lists
- `examples/essentials/event-handling.md` - Event handling with `v-on` and event modifiers
- `examples/essentials/form-input-binding.md` - Two-way binding with `v-model` for form inputs
- `examples/essentials/watchers.md` - `watch()` and `watchEffect()` for side effects
- `examples/essentials/template-refs.md` - Accessing DOM elements and component instances
- `examples/essentials/component-basics.md` - Component basics, props, events, and slots
- `examples/essentials/lifecycle.md` - Component lifecycle hooks

### Components In Depth (深入组件) - `examples/components-in-depth/`

- `examples/components-in-depth/registration.md` - Global and local component registration
- `examples/components-in-depth/props.md` - Props definition, validation, and TypeScript support
- `examples/components-in-depth/events.md` - Emitting events and event validation
- `examples/components-in-depth/component-v-model.md` - Using `v-model` with custom components
- `examples/components-in-depth/attrs.md` - Fallthrough attributes and `$attrs`
- `examples/components-in-depth/slots.md` - Default, named, and scoped slots
- `examples/components-in-depth/dependency-injection.md` - Provide/Inject for dependency injection
- `examples/components-in-depth/async-components.md` - Async components and code splitting

### Reusability (逻辑复用) - `examples/reusability/`

- `examples/reusability/composables.md` - Creating and using composables (composition functions)
- `examples/reusability/custom-directives.md` - Creating custom directives
- `examples/reusability/plugins.md` - Creating and using Vue plugins

### Built-in Components (内置组件) - `examples/built-in-components/`

- `examples/built-in-components/transition.md` - `<Transition>` component for element transitions
- `examples/built-in-components/keepalive.md` - `<KeepAlive>` component for caching instances
- `examples/built-in-components/teleport.md` - `<Teleport>` component for rendering to different DOM locations

### Scaling Up (应用规模化) - `examples/scaling-up/`

- `examples/scaling-up/single-file-components.md` - Single File Components (SFC) structure
- `examples/scaling-up/routing.md` - Vue Router setup and navigation
- `examples/scaling-up/state-management.md` - Pinia state management

### Templates Directory (`templates/`)

- `templates/project-structure.md` - Standard Vue 3 project organization, component templates, composable templates, store templates, router templates, and Vite configuration templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/project-structure.md` for organizing Vue 3 projects
- Use component templates as starting points for new components
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Vue 3 API documentation structure:

### Reactivity Core (`api/reactivity-core/`)
- `api/reactivity-core/ref.md` - `ref()` for creating reactive references
- `api/reactivity-core/reactive.md` - `reactive()` for creating reactive objects
- `api/reactivity-core/computed.md` - `computed()` for computed properties
- `api/reactivity-core/watch.md` - `watch()` for watching reactive sources

### Reactivity Utilities (`api/reactivity-utilities/`)
- `api/reactivity-utilities/toRef.md` - `toRef()` and `toRefs()` for maintaining reactivity when destructuring

### Lifecycle (`api/lifecycle/`)
- `api/lifecycle/onMounted.md` - All lifecycle hooks: `onBeforeMount()`, `onMounted()`, `onBeforeUpdate()`, `onUpdated()`, `onBeforeUnmount()`, `onUnmounted()`

### Component (`api/component/`)
- `api/component/defineProps.md` - `defineProps()`, `defineEmits()`, `defineExpose()` for component definition

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Resources

- **Official Documentation**: https://cn.vuejs.org/guide/introduction
- **API Reference**: https://cn.vuejs.org/api/
- **Vue Router**: https://router.vuejs.org/
- **Pinia**: https://pinia.vuejs.org/
- **Vite**: https://vitejs.dev/
- **VueUse**: https://vueuse.org/

## Keywords

Vue 3, Vue.js, Composition API, Options API, script setup, reactive, ref, computed, watch, watchEffect, lifecycle hooks, template syntax, directives, v-if, v-for, v-model, v-bind, v-on, components, props, emits, slots, provide, inject, Vue Router, Pinia, composables, TypeScript, Vite, single-file components, SFC, progressive framework, declarative rendering, reactivity system, performance optimization, best practices, 渐进式框架, 声明式渲染, 响应式系统, 组合式 API, 选项式 API, 单文件组件, 模板语法, 指令, 组件, 路由, 状态管理