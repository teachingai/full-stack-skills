# Class and Style Bindings

## Instructions

This example demonstrates binding HTML classes and inline styles dynamically.

### Key Concepts

- Binding classes with `:class`
- Binding styles with `:style`
- Object and array syntax
- Dynamic class/style bindings

### Example: Class Binding - Object Syntax

```vue
<template>
  <div>
    <!-- Object syntax -->
    <div :class="{ active: isActive, 'text-danger': hasError }">
      Content
    </div>
    
    <!-- Computed object -->
    <div :class="classObject">Content</div>
    
    <!-- Inline object -->
    <div :class="{ active: isActive && !isDisabled }">Content</div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const isActive = ref(true)
const hasError = ref(false)
const isDisabled = ref(false)

const classObject = computed(() => ({
  active: isActive.value && !isDisabled.value,
  'text-danger': hasError.value
}))
</script>
```

### Example: Class Binding - Array Syntax

```vue
<template>
  <div>
    <!-- Array syntax -->
    <div :class="[activeClass, errorClass]">Content</div>
    
    <!-- Array with object -->
    <div :class="[{ active: isActive }, errorClass]">Content</div>
    
    <!-- Conditional in array -->
    <div :class="[isActive ? activeClass : '', errorClass]">Content</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isActive = ref(true)
const activeClass = ref('active')
const errorClass = ref('text-danger')
</script>
```

### Example: Style Binding - Object Syntax

```vue
<template>
  <div>
    <!-- Object syntax -->
    <div :style="{ color: activeColor, fontSize: fontSize + 'px' }">
      Content
    </div>
    
    <!-- Computed object -->
    <div :style="styleObject">Content</div>
    
    <!-- Multiple style objects -->
    <div :style="[baseStyles, overridingStyles]">Content</div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const activeColor = ref('red')
const fontSize = ref(30)

const styleObject = computed(() => ({
  color: activeColor.value,
  fontSize: fontSize.value + 'px'
}))

const baseStyles = ref({
  color: 'blue',
  fontSize: '14px'
})

const overridingStyles = ref({
  fontSize: '20px'
})
</script>
```

### Example: CSS Property Names

```vue
<template>
  <div>
    <!-- camelCase -->
    <div :style="{ fontSize: '14px' }">Content</div>
    
    <!-- kebab-case (with quotes) -->
    <div :style="{ 'font-size': '14px' }">Content</div>
    
    <!-- Both work the same -->
  </div>
</template>
```

### Example: Multiple Values

```vue
<template>
  <div>
    <!-- Array of values -->
    <div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }">
      Content
    </div>
  </div>
</template>
```

### Example: Auto-prefixing

```vue
<template>
  <div>
    <!-- Vue automatically adds vendor prefixes -->
    <div :style="{ transform: 'scale(1.2)' }">Content</div>
  </div>
</template>
```

### Key Points

- Use object syntax for conditional classes/styles
- Use array syntax for multiple classes/styles
- CSS property names can use camelCase or kebab-case
- Vue automatically adds vendor prefixes for CSS properties
- Computed properties are useful for complex class/style objects
