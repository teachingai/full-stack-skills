# Router Instance API

## API Reference

Router instance properties and methods.

### Router Instance Properties

#### router.app

**Type:** `Vue instance`

The root Vue instance the router was injected into.

#### router.mode

**Type:** `string`

The mode the router is using (`"hash"` | `"history"` | `"abstract"`).

#### router.currentRoute

**Type:** `Route`

The current route object.

### Router Instance Methods

#### router.push(location, onComplete?, onAbort?)

**Type:** `Function`

Programmatically navigate to a new route.

**Parameters:**
- `location` - Route location (string or object)
- `onComplete` - Success callback (optional)
- `onAbort` - Abort callback (optional)

**Returns:** `Promise<Route>`

**Example:**
```javascript
router.push('/home')
router.push({ path: '/home' })
router.push({ name: 'user', params: { id: '123' } })
```

#### router.replace(location, onComplete?, onAbort?)

**Type:** `Function`

Navigate to a new route without adding a history entry.

**Parameters:**
- `location` - Route location (string or object)
- `onComplete` - Success callback (optional)
- `onAbort` - Abort callback (optional)

**Returns:** `Promise<Route>`

#### router.go(n)

**Type:** `Function`

Go n steps in the history stack.

**Parameters:**
- `n` - Number of steps (positive for forward, negative for back)

**Example:**
```javascript
router.go(-1)  // Go back
router.go(1)   // Go forward
```

#### router.back()

**Type:** `Function`

Go back one step in history (equivalent to `router.go(-1)`).

#### router.forward()

**Type:** `Function`

Go forward one step in history (equivalent to `router.go(1)`).

#### router.addRoutes(routes)

**Type:** `Function`

Dynamically add routes to the router.

**Parameters:**
- `routes` - Array of route config objects

**Example:**
```javascript
router.addRoutes([
  { path: '/new', component: NewComponent }
])
```

#### router.onReady(callback, errorCallback?)

**Type:** `Function`

Register a callback that's called when the router has completed the initial navigation.

**Parameters:**
- `callback` - Callback function
- `errorCallback` - Error callback (optional)

#### router.onError(callback)

**Type:** `Function`

Register a callback that's called when an error occurs during navigation.

**Parameters:**
- `callback` - Error callback function

#### router.resolve(location, current?, append?)

**Type:** `Function`

Resolve a route location to a normalized route object.

**Parameters:**
- `location` - Route location
- `current` - Current route (optional)
- `append` - Append flag (optional)

**Returns:** `Route`

**See also:** `examples/programmatic-navigation.md`
