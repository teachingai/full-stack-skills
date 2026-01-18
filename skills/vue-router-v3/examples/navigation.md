# Navigation

## Instructions

This example demonstrates using router-link for navigation in Vue Router v3.

### Key Concepts

- Router-link component
- Active classes
- Exact matching
- Link customization
- Programmatic navigation

### Example: Basic Router Link

```vue
<template>
  <div>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
  </div>
</template>
```

### Example: Named Routes

```vue
<template>
  <router-link :to="{ name: 'user', params: { id: 123 }}">
    User Profile
  </router-link>
</template>
```

### Example: Active Classes

```vue
<template>
  <router-link 
    to="/about"
    active-class="active-link"
    exact-active-class="exact-active-link">
    About
  </router-link>
</template>
```

### Example: Exact Matching

```vue
<template>
  <!-- Only active when path exactly matches -->
  <router-link to="/" exact>Home</router-link>
  
  <!-- Active when path starts with /about -->
  <router-link to="/about">About</router-link>
</template>
```

### Example: Custom Tag

```vue
<template>
  <!-- Render as button instead of anchor -->
  <router-link to="/about" tag="button">
    About
  </router-link>
</template>
```

### Example: Replace Navigation

```vue
<template>
  <!-- Replace current history entry -->
  <router-link to="/about" replace>About</router-link>
</template>
```

### Example: Custom Active Class (Global)

```javascript
// router/index.js
const router = new VueRouter({
  routes,
  linkActiveClass: 'router-link-active',
  linkExactActiveClass: 'router-link-exact-active'
})
```

### Key Points

- Use `<router-link>` for declarative navigation
- `to` prop accepts string or route object
- Active classes are applied automatically
- Use `exact` for exact path matching
- Use `replace` to replace history entry
