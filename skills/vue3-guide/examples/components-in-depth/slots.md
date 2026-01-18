# Slots

## Instructions

This example demonstrates slots including default, named, and scoped slots.

### Key Concepts

- Default slots
- Named slots
- Scoped slots
- Slot fallback content

### Example: Default Slot

```vue
<!-- FancyButton.vue -->
<template>
  <button class="fancy-btn">
    <slot></slot>
  </button>
</template>

<!-- Using the component -->
<template>
  <FancyButton>
    Click me!
  </FancyButton>
</template>
```

### Example: Named Slots

```vue
<!-- BaseLayout.vue -->
<template>
  <div class="container">
    <header>
      <slot name="header"></slot>
    </header>
    <main>
      <slot></slot>
    </main>
    <footer>
      <slot name="footer"></slot>
    </footer>
  </div>
</template>

<!-- Using the component -->
<template>
  <BaseLayout>
    <template #header>
      <h1>Here might be a page title</h1>
    </template>
    
    <p>A paragraph for the main content.</p>
    
    <template #footer>
      <p>Here's some contact info</p>
    </template>
  </BaseLayout>
</template>
```

### Example: Scoped Slots

```vue
<!-- MyList.vue -->
<template>
  <ul>
    <li v-for="item in items" :key="item.id">
      <slot :item="item" :index="index"></slot>
    </li>
  </ul>
</template>

<script setup>
defineProps(['items'])
</script>

<!-- Using the component -->
<template>
  <MyList :items="items">
    <template #default="{ item, index }">
      <span>{{ index }}: {{ item.name }}</span>
    </template>
  </MyList>
</template>
```

### Example: Slot Fallback

```vue
<!-- SubmitButton.vue -->
<template>
  <button type="submit">
    <slot>Submit</slot>
  </button>
</template>

<!-- Using with content -->
<template>
  <SubmitButton>Save</SubmitButton>
</template>

<!-- Using without content (uses fallback) -->
<template>
  <SubmitButton />
</template>
```

### Key Points

- Slots allow passing template content to components
- Named slots use `#` or `v-slot:name`
- Scoped slots provide data to parent
- Fallback content is shown when slot is empty
