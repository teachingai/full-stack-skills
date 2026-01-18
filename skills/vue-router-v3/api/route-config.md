# Route Configuration API

## API Reference

Route configuration options for defining routes.

### Route Config Properties

#### path

**Type:** `string`

Required. The path pattern for the route.

**Example:**
```javascript
{ path: '/user/:id', component: User }
```

#### component

**Type:** `Component`

The component to render when the route is matched.

**Example:**
```javascript
{ path: '/home', component: Home }
```

#### components

**Type:** `{ [name: string]: Component }`

Named components for named views.

**Example:**
```javascript
{
  path: '/',
  components: {
    default: Home,
    header: Header,
    footer: Footer
  }
}
```

#### name

**Type:** `string`

Named route for programmatic navigation.

**Example:**
```javascript
{ path: '/user/:id', name: 'user', component: User }
```

#### redirect

**Type:** `string | Location | Function`

Redirect to another route.

**Example:**
```javascript
{ path: '/home', redirect: '/' }
{ path: '/old', redirect: { name: 'new' } }
{ path: '/a', redirect: to => '/b' }
```

#### alias

**Type:** `string | Array<string>`

Alias for the route.

**Example:**
```javascript
{ path: '/home', alias: '/', component: Home }
{ path: '/user/:id', alias: ['/u/:id', '/profile/:id'], component: User }
```

#### children

**Type:** `Array<RouteConfig>`

Nested routes.

**Example:**
```javascript
{
  path: '/user/:id',
  component: User,
  children: [
    { path: 'profile', component: Profile }
  ]
}
```

#### props

**Type:** `boolean | Object | Function`

Pass props to route component.

**Example:**
```javascript
{ path: '/user/:id', props: true, component: User }
{ path: '/promo', props: { show: true }, component: Promo }
{ path: '/search', props: route => ({ q: route.query.q }), component: Search }
```

#### meta

**Type:** `any`

Custom metadata for the route.

**Example:**
```javascript
{
  path: '/admin',
  meta: { requiresAuth: true, requiresAdmin: true },
  component: Admin
}
```

#### beforeEnter

**Type:** `NavigationGuard`

Per-route navigation guard.

**Example:**
```javascript
{
  path: '/admin',
  beforeEnter: (to, from, next) => {
    if (isAdmin()) next()
    else next('/')
  },
  component: Admin
}
```

**See also:** `examples/dynamic-route-matching.md`, `examples/nested-routes.md`, `examples/redirects-and-aliases.md`, `examples/route-props.md`
