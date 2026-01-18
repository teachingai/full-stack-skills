# Route Object API

## API Reference

Route object properties available in components via `$route`.

### Route Object Properties

#### $route.path

**Type:** `string`

String of the current path, always resolved as an absolute path.

**Example:**
```javascript
// For route /user/:id
$route.path  // "/user/123"
```

#### $route.params

**Type:** `Object`

Object containing key/value pairs of dynamic segments and star segments.

**Example:**
```javascript
// For route /user/:id/post/:postId
$route.params  // { id: '123', postId: '456' }
```

#### $route.query

**Type:** `Object`

Object containing key/value pairs of the query string.

**Example:**
```javascript
// For URL /search?q=vue&page=1
$route.query  // { q: 'vue', page: '1' }
```

#### $route.hash

**Type:** `string`

Hash of the current route (with the `#`), if it exists.

**Example:**
```javascript
// For URL /about#section1
$route.hash  // "#section1"
```

#### $route.fullPath

**Type:** `string`

Full resolved URL including query and hash.

**Example:**
```javascript
// For URL /user/123?tab=profile#info
$route.fullPath  // "/user/123?tab=profile#info"
```

#### $route.matched

**Type:** `Array<RouteRecord>`

Array containing route records for all nested path segments of the current route.

#### $route.name

**Type:** `string | null`

Name of the current route, if it has one.

**Example:**
```javascript
// For route { path: '/user/:id', name: 'user' }
$route.name  // "user"
```

#### $route.redirectedFrom

**Type:** `string | null`

Name of the route that redirected to this one, if any.

### Route Object is Read-Only

The route object is read-only. Its properties cannot be modified, but they can be watched.

**Example:**
```javascript
watch: {
  '$route'(to, from) {
    // React to route changes
  }
}
```

**See also:** `examples/route-params-and-query.md`
