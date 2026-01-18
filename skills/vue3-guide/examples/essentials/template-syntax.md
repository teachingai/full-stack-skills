# Template Syntax

## Instructions

This example demonstrates Vue 3 template syntax including interpolation, directives, and expressions.

### Key Concepts

- Text interpolation with `{{ }}`
- Raw HTML with `v-html`
- Attribute bindings with `v-bind`
- JavaScript expressions in templates

### Example: Text Interpolation

```vue
<template>
  <div>
    <p>Message: {{ message }}</p>
    <p>Count: {{ count }}</p>
    <p>Reversed: {{ message.split('').reverse().join('') }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('Hello Vue 3')
const count = ref(0)
</script>
```

### Example: Raw HTML

```vue
<template>
  <div>
    <p>Using mustaches: {{ rawHtml }}</p>
    <p>Using v-html: <span v-html="rawHtml"></span></p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const rawHtml = ref('<span style="color: red">This should be red.</span>')
</script>
```

**Warning:** Only use `v-html` on trusted content to avoid XSS attacks.

### Example: Attribute Bindings

```vue
<template>
  <div>
    <!-- v-bind with full syntax -->
    <a v-bind:href="url">Link</a>
    
    <!-- v-bind shorthand -->
    <a :href="url">Link</a>
    
    <!-- Boolean attributes -->
    <button :disabled="isButtonDisabled">Button</button>
    
    <!-- Multiple attributes -->
    <div v-bind="objectOfAttrs"></div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const url = ref('https://vuejs.org')
const isButtonDisabled = ref(false)
const objectOfAttrs = reactive({
  id: 'container',
  class: 'wrapper'
})
</script>
```

### Example: JavaScript Expressions

```vue
<template>
  <div>
    <p>{{ number + 1 }}</p>
    <p>{{ ok ? 'YES' : 'NO' }}</p>
    <p>{{ message.split('').reverse().join('') }}</p>
    <div :id="`list-${id}`"></div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const number = ref(1)
const ok = ref(true)
const message = ref('Hello')
const id = ref(1)
</script>
```

### Key Points

- Use `{{ }}` for text interpolation
- Use `v-html` for raw HTML (use with caution)
- Use `v-bind` or `:` for attribute bindings
- JavaScript expressions are supported in templates
- Only single expressions are allowed (no statements)
