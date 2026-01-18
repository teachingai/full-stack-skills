# RouterView Component API

## API Reference

RouterView component props and usage.

### RouterView Props

#### name

**Type:** `string`

Default: `"default"`

When a `<router-view>` has a name, it will render the component with the corresponding name in the matched route record's `components` option.

**Example:**
```vue
<router-view name="header" />
<router-view />
<router-view name="footer" />
```

### RouterView Behavior

- Renders the component matched by the route
- Updates when the route changes
- Can be nested for nested routes
- Can be named for named views

### Example: Basic Usage

```vue
<template>
  <div id="app">
    <router-view />
  </div>
</template>
```

### Example: Named Views

```vue
<template>
  <div>
    <router-view name="header" />
    <router-view />
    <router-view name="sidebar" />
  </div>
</template>
```

### Example: With Transition

```vue
<template>
  <transition name="fade" mode="out-in">
    <router-view />
  </transition>
</template>
```

### Example: With Keep-Alive

```vue
<template>
  <keep-alive>
    <router-view />
  </keep-alive>
</template>
```

### Key Points

- Default name is "default"
- Use name prop for named views
- Can be nested for nested routes
- Works with transition and keep-alive
- Updates automatically on route changes

**See also:** `examples/nested-routes.md`, `examples/named-views.md`
