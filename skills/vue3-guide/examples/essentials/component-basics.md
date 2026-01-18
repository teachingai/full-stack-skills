# Component Basics

## Instructions

This example demonstrates the basics of Vue components including props, events, and slots.

### Key Concepts

- Defining components
- Using components
- Passing props
- Listening to events
- Using slots

### Example: Basic Component

```vue
<!-- ButtonCounter.vue -->
<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <button @click="count++">
    You clicked me {{ count }} times.
  </button>
</template>

<!-- Using the component -->
<template>
  <div>
    <ButtonCounter />
    <ButtonCounter />
    <ButtonCounter />
  </div>
</template>

<script setup>
import ButtonCounter from './ButtonCounter.vue'
</script>
```

### Example: Passing Props

```vue
<!-- BlogPost.vue -->
<script setup>
defineProps(['title'])
</script>

<template>
  <h4>{{ title }}</h4>
</template>

<!-- Using the component -->
<template>
  <div>
    <BlogPost title="My journey with Vue" />
    <BlogPost title="Blogging with Vue" />
    <BlogPost title="Why Vue is so fun" />
  </div>
</template>

<script setup>
import BlogPost from './BlogPost.vue'
</script>
```

### Example: Listening to Events

```vue
<!-- BlogPost.vue -->
<script setup>
defineProps(['title'])
defineEmits(['enlarge-text'])
</script>

<template>
  <div class="blog-post">
    <h4>{{ title }}</h4>
    <button @click="$emit('enlarge-text')">Enlarge text</button>
  </div>
</template>

<!-- Using the component -->
<template>
  <div :style="{ fontSize: postFontSize + 'em' }">
    <BlogPost
      v-for="post in posts"
      :key="post.id"
      :title="post.title"
      @enlarge-text="postFontSize += 0.1"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BlogPost from './BlogPost.vue'

const posts = ref([
  { id: 1, title: 'My journey with Vue' },
  { id: 2, title: 'Blogging with Vue' },
  { id: 3, title: 'Why Vue is so fun' }
])

const postFontSize = ref(1)
</script>
```

### Example: Using Slots

```vue
<!-- AlertBox.vue -->
<template>
  <div class="alert-box">
    <strong>Error!</strong>
    <slot />
  </div>
</template>

<!-- Using the component -->
<template>
  <AlertBox>
    Something bad happened.
  </AlertBox>
</template>

<script setup>
import AlertBox from './AlertBox.vue'
</script>
```

### Key Points

- Components are reusable Vue instances
- Props flow down (parent to child)
- Events flow up (child to parent)
- Slots allow passing template content to components
- Each component instance has its own isolated scope
