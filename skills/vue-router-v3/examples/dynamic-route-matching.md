# Dynamic Route Matching

## Instructions

This example demonstrates dynamic route matching with parameters in Vue Router v3.

### Key Concepts

- Route parameters
- Dynamic segments
- Catch-all routes
- Regular expressions
- Route params access

### Example: Basic Dynamic Route

```javascript
// router/index.js
const routes = [
  { path: '/user/:id', component: User }
]
```

```vue
<!-- User.vue -->
<template>
  <div>
    <h1>User {{ $route.params.id }}</h1>
  </div>
</template>
```

### Example: Multiple Parameters

```javascript
const routes = [
  { path: '/user/:userId/post/:postId', component: Post }
]
```

```vue
<!-- Post.vue -->
<template>
  <div>
    <p>User ID: {{ $route.params.userId }}</p>
    <p>Post ID: {{ $route.params.postId }}</p>
  </div>
</template>
```

### Example: Optional Parameters

```javascript
const routes = [
  { path: '/user/:id?', component: User }  // id is optional
]
```

### Example: Catch-All Route

```javascript
const routes = [
  { path: '/user/:id', component: User },
  { path: '/user-*', component: NotFound }  // Catch-all
]
```

### Example: Regular Expression Matching

```javascript
const routes = [
  // Only match numeric IDs
  { path: '/user/:id(\\d+)', component: User },
  // Match specific pattern
  { path: '/files/:path(.*)', component: FileViewer }
]
```

### Example: Accessing Params in Component

```vue
<script>
export default {
  computed: {
    userId() {
      return this.$route.params.id
    }
  },
  watch: {
    '$route'(to, from) {
      // React to route changes
      console.log('Route changed from', from.path, 'to', to.path)
    }
  }
}
</script>
```

### Key Points

- Use `:paramName` for dynamic segments
- Access params via `$route.params`
- Use `?` for optional parameters
- Use `*` for catch-all routes
- Use regex in parentheses for pattern matching
