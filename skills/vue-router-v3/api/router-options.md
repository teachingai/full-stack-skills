# Router Options API

## API Reference

VueRouter constructor options.

### Router Options

#### routes

**Type:** `Array<RouteConfig>`

Required. Array of route configuration objects.

**Example:**
```javascript
const router = new VueRouter({
  routes: [
    { path: '/', component: Home }
  ]
})
```

#### mode

**Type:** `string`

Default: `"hash"`

Router mode: `"hash"` | `"history"` | `"abstract"`

**Example:**
```javascript
const router = new VueRouter({
  mode: 'history',
  routes: [...]
})
```

#### base

**Type:** `string`

Default: `"/"`

Base URL for the app.

**Example:**
```javascript
const router = new VueRouter({
  base: '/my-app/',
  routes: [...]
})
```

#### linkActiveClass

**Type:** `string`

Default: `"router-link-active"`

Global configuration for `<router-link>` default active class.

**Example:**
```javascript
const router = new VueRouter({
  linkActiveClass: 'active',
  routes: [...]
})
```

#### linkExactActiveClass

**Type:** `string`

Default: `"router-link-exact-active"`

Global configuration for `<router-link>` default exact active class.

**Example:**
```javascript
const router = new VueRouter({
  linkExactActiveClass: 'exact-active',
  routes: [...]
})
```

#### scrollBehavior

**Type:** `Function`

Function to control scroll behavior.

**Example:**
```javascript
const router = new VueRouter({
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  },
  routes: [...]
})
```

#### parseQuery / stringifyQuery

**Type:** `Function`

Custom functions to parse/stringify query strings.

**Example:**
```javascript
const router = new VueRouter({
  parseQuery: (query) => { /* custom parse */ },
  stringifyQuery: (query) => { /* custom stringify */ },
  routes: [...]
})
```

#### fallback

**Type:** `boolean`

Default: `true`

Whether to fallback to hash mode when the browser doesn't support history.pushState.

**Example:**
```javascript
const router = new VueRouter({
  mode: 'history',
  fallback: false,  // Don't fallback to hash mode
  routes: [...]
})
```

**See also:** `examples/history-mode.md`, `examples/scroll-behavior.md`
