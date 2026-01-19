# Component Template | 组件模板

## Basic Component Usage

```vue
<template>
  <van-component-name
    prop1="value1"
    prop2="value2"
    @event="handleEvent"
  />
</template>

<script setup>
import { ComponentName as VanComponentName } from 'vant'

const handleEvent = () => {
  console.log('Event handled')
}
</script>
```

## Component with v-model

```vue
<template>
  <van-field
    v-model="value"
    placeholder="Enter text"
  />
</template>

<script setup>
import { ref } from 'vue'
import { Field as VanField } from 'vant'

const value = ref('')
</script>
```

## Component in Form

```vue
<template>
  <van-form @submit="onSubmit">
    <van-field
      v-model="form.field"
      name="field"
      label="Field"
      :rules="[{ required: true, message: 'Please enter field' }]"
    />
    <van-button type="primary" native-type="submit">Submit</van-button>
  </van-form>
</template>

<script setup>
import { ref } from 'vue'
import { Form as VanForm, Field as VanField, Button as VanButton } from 'vant'

const form = ref({
  field: ''
})

const onSubmit = (values) => {
  console.log('Form submitted:', values)
}
</script>
```
