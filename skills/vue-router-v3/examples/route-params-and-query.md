# Route Params and Query

## Instructions

This example demonstrates accessing route parameters and query strings.

### Key Concepts

- Route parameters ($route.params)
- Query strings ($route.query)
- Hash fragment ($route.hash)
- Reacting to route changes

### Example: Accessing Route Params

```vue
<template>
  <div>
    <p>User ID: {{ $route.params.id }}</p>
    <p>Post ID: {{ $route.params.postId }}</p>
  </div>
</template>
```

### Example: Accessing Query Strings

```vue
<template>
  <div>
    <p>Search: {{ $route.query.q }}</p>
    <p>Page: {{ $route.query.page }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    searchQuery() {
      return this.$route.query.q || ''
    },
    currentPage() {
      return parseInt(this.$route.query.page) || 1
    }
  }
}
</script>
```

### Example: Accessing Hash

```vue
<template>
  <div>
    <p>Hash: {{ $route.hash }}</p>
  </div>
</template>
```

### Example: Full Path Information

```vue
<script>
export default {
  computed: {
    fullPath() {
      return this.$route.fullPath  // /user/123?tab=profile#info
    },
    path() {
      return this.$route.path  // /user/123
    }
  }
}
</script>
```

### Example: Reacting to Route Changes

```vue
<script>
export default {
  watch: {
    '$route'(to, from) {
      // React to route changes
      console.log('From:', from.path)
      console.log('To:', to.path)
      console.log('Params:', to.params)
      console.log('Query:', to.query)
    }
  }
}
</script>
```

### Example: Using Route Props

```javascript
// router/index.js
const routes = [
  {
    path: '/user/:id',
    component: User,
    props: true  // Pass params as props
  }
]
```

```vue
<!-- User.vue -->
<script>
export default {
  props: ['id'],  // Receive id as prop instead of $route.params.id
  // ...
}
</script>
```

### Key Points

- Access params via `$route.params`
- Access query via `$route.query`
- Access hash via `$route.hash`
- Use `$route.fullPath` for complete URL
- Watch `$route` to react to changes
- Use route props to avoid coupling to $route
