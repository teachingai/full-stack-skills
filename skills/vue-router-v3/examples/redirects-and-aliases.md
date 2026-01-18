# Redirects and Aliases

## Instructions

This example demonstrates redirects and aliases in Vue Router v3.

### Key Concepts

- Redirects
- Aliases
- Redirect with function
- Alias vs redirect

### Example: Basic Redirect

```javascript
// router/index.js
const routes = [
  { path: '/home', redirect: '/' },
  { path: '/', component: Home }
]
```

### Example: Redirect to Named Route

```javascript
const routes = [
  { path: '/old-path', redirect: { name: 'home' } },
  { path: '/', name: 'home', component: Home }
]
```

### Example: Redirect with Function

```javascript
const routes = [
  {
    path: '/user/:id',
    redirect: to => {
      // Redirect based on route params
      return { name: 'profile', params: { id: to.params.id } }
    }
  }
]
```

### Example: Alias

```javascript
const routes = [
  {
    path: '/',
    component: Home,
    alias: '/home'  // Both / and /home render Home
  }
]
```

### Example: Multiple Aliases

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    alias: ['/u/:id', '/profile/:id']  // Multiple aliases
  }
]
```

### Example: Alias in Nested Routes

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        path: 'profile',
        component: Profile,
        alias: 'p'  // /user/:id/p renders Profile
      }
    ]
  }
]
```

### Key Points

- Redirect changes URL, alias keeps original URL
- Redirect can be string, object, or function
- Alias allows multiple URLs for same route
- Redirect creates new navigation entry
- Alias renders component without changing URL
