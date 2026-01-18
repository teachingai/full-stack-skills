# Watchers

## Instructions

This example demonstrates watching reactive data sources using `watch()` and `watchEffect()`.

### Key Concepts

- Watching reactive sources with `watch()`
- Automatic dependency tracking with `watchEffect()`
- Watch options (immediate, deep, flush)
- Stopping watchers

### Example: Basic watch()

```vue
<script setup>
import { ref, watch } from 'vue'

const question = ref('')
const answer = ref('Questions usually contain a question mark. ;-)')

watch(question, async (newQuestion, oldQuestion) => {
  if (newQuestion.indexOf('?') > -1) {
    answer.value = 'Thinking...'
    try {
      const res = await fetch('https://yesno.wtf/api')
      const data = await res.json()
      answer.value = data.answer
    } catch (error) {
      answer.value = 'Error! Could not reach the API. ' + error
    }
  }
})
</script>

<template>
  <div>
    <p>
      Ask a yes/no question:
      <input v-model="question" />
    </p>
    <p>{{ answer }}</p>
  </div>
</template>
```

### Example: watch() with Options

```vue
<script setup>
import { ref, watch } from 'vue'

const count = ref(0)

// Immediate: run immediately
watch(count, (newVal, oldVal) => {
  console.log(`Count: ${oldVal} -> ${newVal}`)
}, {
  immediate: true
})

// Deep: watch nested properties
const state = ref({ count: 0, nested: { value: 1 } })
watch(state, (newVal, oldVal) => {
  console.log('State changed')
}, {
  deep: true
})

// Flush: timing of callback
watch(count, (newVal) => {
  console.log('Count changed')
}, {
  flush: 'post'  // 'pre' | 'post' | 'sync'
})
</script>
```

### Example: watch() Multiple Sources

```vue
<script setup>
import { ref, watch } from 'vue'

const firstName = ref('')
const lastName = ref('')

watch([firstName, lastName], ([newFirst, newLast], [oldFirst, oldLast]) => {
  console.log(`First: ${oldFirst} -> ${newFirst}`)
  console.log(`Last: ${oldLast} -> ${newLast}`)
})
</script>

<template>
  <div>
    <input v-model="firstName" placeholder="First name" />
    <input v-model="lastName" placeholder="Last name" />
  </div>
</template>
```

### Example: watchEffect()

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

// Runs immediately and whenever count changes
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="count++">Increment</button>
  </div>
</template>
```

### Example: watchEffect() with Cleanup

```vue
<script setup>
import { ref, watchEffect } from 'vue'

const count = ref(0)

watchEffect((onCleanup) => {
  const timer = setInterval(() => {
    console.log(`Count: ${count.value}`)
  }, 1000)
  
  // Cleanup function
  onCleanup(() => {
    clearInterval(timer)
  })
})
</script>
```

### Example: Stopping Watchers

```vue
<script setup>
import { ref, watch, watchEffect, onUnmounted } from 'vue'

const count = ref(0)

// watch() returns a stop function
const stopWatch = watch(count, (newVal) => {
  console.log(`Count: ${newVal}`)
})

// watchEffect() returns a stop function
const stopEffect = watchEffect(() => {
  console.log(`Count: ${count.value}`)
})

// Stop watchers
onUnmounted(() => {
  stopWatch()
  stopEffect()
})
</script>
```

### Example: watch() vs watchEffect()

```vue
<script setup>
import { ref, watch, watchEffect } from 'vue'

const count = ref(0)
const name = ref('Vue')

// watch() - explicit source, lazy by default
watch(count, (newVal) => {
  console.log(`Count changed to ${newVal}`)
})

// watchEffect() - automatic tracking, runs immediately
watchEffect(() => {
  console.log(`Count: ${count.value}, Name: ${name.value}`)
  // Automatically tracks both count and name
})
</script>
```

### Key Points

- `watch()` explicitly specifies what to watch, lazy by default
- `watchEffect()` automatically tracks dependencies, runs immediately
- Use `immediate: true` to run `watch()` immediately
- Use `deep: true` to watch nested properties
- Both return stop functions to stop watching
- `watchEffect()` can register cleanup functions
