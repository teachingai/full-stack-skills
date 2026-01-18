# Form Input Binding

## Instructions

This example demonstrates two-way data binding for form inputs using `v-model`.

### Key Concepts

- `v-model` for two-way binding
- `v-model` with different input types
- `v-model` modifiers
- Custom components with `v-model`

### Example: Text Input

```vue
<template>
  <div>
    <input v-model="message" placeholder="edit me" />
    <p>Message is: {{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('')
</script>
```

### Example: Textarea

```vue
<template>
  <div>
    <textarea v-model="message" placeholder="add multiple lines"></textarea>
    <p style="white-space: pre-line;">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('')
</script>
```

### Example: Checkbox (Single)

```vue
<template>
  <div>
    <input type="checkbox" id="checkbox" v-model="checked" />
    <label for="checkbox">{{ checked }}</label>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const checked = ref(false)
</script>
```

### Example: Checkbox (Multiple)

```vue
<template>
  <div>
    <input type="checkbox" id="jack" value="Jack" v-model="checkedNames" />
    <label for="jack">Jack</label>
    
    <input type="checkbox" id="john" value="John" v-model="checkedNames" />
    <label for="john">John</label>
    
    <input type="checkbox" id="mike" value="Mike" v-model="checkedNames" />
    <label for="mike">Mike</label>
    
    <br />
    <span>Checked names: {{ checkedNames }}</span>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const checkedNames = ref([])
</script>
```

### Example: Radio

```vue
<template>
  <div>
    <input type="radio" id="one" value="One" v-model="picked" />
    <label for="one">One</label>
    <br />
    
    <input type="radio" id="two" value="Two" v-model="picked" />
    <label for="two">Two</label>
    <br />
    
    <span>Picked: {{ picked }}</span>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const picked = ref('')
</script>
```

### Example: Select (Single)

```vue
<template>
  <div>
    <select v-model="selected">
      <option disabled value="">Please select one</option>
      <option>A</option>
      <option>B</option>
      <option>C</option>
    </select>
    <span>Selected: {{ selected }}</span>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selected = ref('')
</script>
```

### Example: Select (Multiple)

```vue
<template>
  <div>
    <select v-model="selected" multiple>
      <option>A</option>
      <option>B</option>
      <option>C</option>
    </select>
    <br />
    <span>Selected: {{ selected }}</span>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selected = ref([])
</script>
```

### Example: v-model Modifiers

```vue
<template>
  <div>
    <!-- .lazy - sync after change event -->
    <input v-model.lazy="msg" />
    <p>{{ msg }}</p>
    
    <!-- .number - convert to number -->
    <input v-model.number="age" type="number" />
    <p>Age type: {{ typeof age }}</p>
    
    <!-- .trim - trim whitespace -->
    <input v-model.trim="msg" />
    <p>Trimmed: "{{ msg }}"</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('')
const age = ref(0)
</script>
```

### Example: Custom Component v-model

```vue
<!-- CustomInput.vue -->
<script setup>
import { computed } from 'vue'

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

<!-- Using CustomInput -->
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

### Key Points

- `v-model` creates two-way data binding
- Works with text, textarea, checkbox, radio, select
- Use `.lazy` to sync after change event
- Use `.number` to convert to number
- Use `.trim` to trim whitespace
- Custom components can use `v-model` with `modelValue` prop and `update:modelValue` emit
