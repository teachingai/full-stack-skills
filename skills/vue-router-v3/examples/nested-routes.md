# Nested Routes

## Instructions

This example demonstrates nested routes and nested router-view components.

### Key Concepts

- Nested route configuration
- Child routes
- Nested router-view
- Route hierarchy

### Example: Basic Nested Routes

```javascript
// router/index.js
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        path: 'profile',
        component: UserProfile
      },
      {
        path: 'posts',
        component: UserPosts
      }
    ]
  }
]
```

### Example: User Component with Nested View

```vue
<!-- User.vue -->
<template>
  <div class="user">
    <h2>User {{ $route.params.id }}</h2>
    <nav>
      <router-link to="/user/1/profile">Profile</router-link>
      <router-link to="/user/1/posts">Posts</router-link>
    </nav>
    <router-view />
  </div>
</template>
```

### Example: Nested Route with Default

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        path: '',
        component: UserHome  // Default child route
      },
      {
        path: 'profile',
        component: UserProfile
      }
    ]
  }
]
```

### Example: Absolute Paths in Nested Routes

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        path: 'profile',
        component: UserProfile  // /user/:id/profile
      },
      {
        path: '/settings',
        component: Settings  // /settings (absolute)
      }
    ]
  }
]
```

### Key Points

- Use `children` array for nested routes
- Nested routes require nested `<router-view>`
- Child routes are relative to parent path
- Use empty path for default child route
- Absolute paths start with `/`
