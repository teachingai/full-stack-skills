# Component v-model

## Instructions

This example demonstrates using `v-model` with custom components.

### Key Concepts

- `v-model` with components
- Multiple `v-model` bindings
- Custom `v-model` modifiers

### Example: Basic v-model

```vue
<!-- CustomInput.vue -->
<script setup>
const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const value = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
})
</script>

<template>
  <input :value="value" @input="value = $event.target.value" />
</template>

<!-- Using the component -->
<template>
  <CustomInput v-model="searchText" />
  <p>Search: {{ searchText }}</p>
</template>

<script setup>
import { ref } from 'vue'
import CustomInput from './CustomInput.vue'

const searchText = ref('')
</script>
```

### Example: Multiple v-model

```vue
<!-- UserName.vue -->
<script setup>
const firstName = defineModel('firstName')
const lastName = defineModel('lastName')
</script>

<template>
  <input v-model="firstName" placeholder="First name" />
  <input v-model="lastName" placeholder="Last name" />
</template>

<!-- Using the component -->
<template>
  <UserName v-model:first-name="first" v-model:last-name="last" />
</template>

<script setup>
import { ref } from 'vue'
import UserName from './UserName.vue'

const first = ref('')
const last = ref('')
</script>
```

### Example: Custom Modifiers

```vue
<!-- MyInput.vue -->
<script setup>
const props = defineProps({
  modelValue: String,
  modelModifiers: { default: () => ({}) }
})

const emit = defineEmits(['update:modelValue'])

function emitValue(e) {
  let value = e.target.value
  if (props.modelModifiers.capitalize) {
    value = value.charAt(0).toUpperCase() + value.slice(1)
  }
  emit('update:modelValue', value)
}
</script>

<template>
  <input :value="modelValue" @input="emitValue" />
</template>

<!-- Using the component -->
<template>
  <MyInput v-model.capitalize="myText" />
</template>
```

### Key Points

- Components can use `v-model` with `modelValue` prop and `update:modelValue` emit
- Use `defineModel()` for simpler syntax (Vue 3.4+)
- Multiple `v-model` bindings use named models
- Custom modifiers are available in `modelModifiers` prop
