# Lazy Loading

## Instructions

This example demonstrates lazy loading routes for code splitting.

### Key Concepts

- Dynamic imports
- Code splitting
- Lazy route components
- Webpack chunk names

### Example: Basic Lazy Loading

```javascript
// router/index.js
const routes = [
  {
    path: '/about',
    component: () => import('@/views/About.vue')
  }
]
```

### Example: Lazy Loading with Chunk Name

```javascript
const routes = [
  {
    path: '/about',
    component: () => import(/* webpackChunkName: "about" */ '@/views/About.vue')
  },
  {
    path: '/contact',
    component: () => import(/* webpackChunkName: "contact" */ '@/views/Contact.vue')
  }
]
```

### Example: Grouped Lazy Loading

```javascript
const routes = [
  {
    path: '/user/:id',
    component: () => import(/* webpackChunkName: "user" */ '@/views/User.vue'),
    children: [
      {
        path: 'profile',
        component: () => import(/* webpackChunkName: "user" */ '@/views/UserProfile.vue')
      },
      {
        path: 'posts',
        component: () => import(/* webpackChunkName: "user" */ '@/views/UserPosts.vue')
      }
    ]
  }
]
```

### Example: Lazy Loading with Loading Component

```javascript
const AsyncComponent = () => ({
  component: import('@/views/Heavy.vue'),
  loading: LoadingComponent,
  error: ErrorComponent,
  delay: 200,
  timeout: 3000
})

const routes = [
  {
    path: '/heavy',
    component: AsyncComponent
  }
]
```

### Example: Prefetching

```javascript
const routes = [
  {
    path: '/about',
    component: () => import(/* webpackPrefetch: true */ '@/views/About.vue')
  }
]
```

### Key Points

- Use dynamic import() for lazy loading
- Webpack automatically code splits
- Use webpackChunkName comment for chunk naming
- Group related routes in same chunk
- Improves initial load time
