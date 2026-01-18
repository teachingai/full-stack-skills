# Route Props

## Instructions

This example demonstrates passing props to route components.

### Key Concepts

- Route props
- Boolean mode
- Object mode
- Function mode
- Props vs $route

### Example: Boolean Mode

```javascript
// router/index.js
const routes = [
  {
    path: '/user/:id',
    component: User,
    props: true  // Pass $route.params as props
  }
]
```

```vue
<!-- User.vue -->
<script>
export default {
  props: ['id'],  // Receive id as prop
  // Instead of this.$route.params.id
}
</script>
```

### Example: Object Mode

```javascript
const routes = [
  {
    path: '/promo',
    component: Promo,
    props: { newsletterPopup: false }  // Static props
  }
]
```

```vue
<!-- Promo.vue -->
<script>
export default {
  props: {
    newsletterPopup: Boolean
  }
}
</script>
```

### Example: Function Mode

```javascript
const routes = [
  {
    path: '/search',
    component: Search,
    props: (route) => ({
      query: route.query.q,
      page: parseInt(route.query.page) || 1
    })
  }
]
```

```vue
<!-- Search.vue -->
<script>
export default {
  props: {
    query: String,
    page: Number
  }
}
</script>
```

### Example: Props in Nested Routes

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    props: true,
    children: [
      {
        path: 'profile',
        component: Profile,
        props: { showEdit: true }
      }
    ]
  }
]
```

### Key Points

- Use props to decouple components from $route
- Boolean mode: pass params as props
- Object mode: pass static props
- Function mode: create props from route
- Makes components more reusable and testable
