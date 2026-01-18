# KeepAlive

## Instructions

This example demonstrates the `<KeepAlive>` component for caching component instances.

### Key Concepts

- KeepAlive component
- include/exclude props
- max prop
- Lifecycle hooks

### Example: Basic KeepAlive

```vue
<template>
  <KeepAlive>
    <component :is="currentComponent" />
  </KeepAlive>
</template>
```

### Example: KeepAlive with include

```vue
<template>
  <KeepAlive :include="['TabA', 'TabB']">
    <component :is="currentTab" />
  </KeepAlive>
</template>
```

### Key Points

- Caches component instances
- Use `include`/`exclude` to control which components are cached
- Use `max` to limit cache size
- Components use `activated`/`deactivated` hooks instead of `mounted`/`unmounted`
