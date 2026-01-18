# Navigation Guards API

## API Reference

Navigation guards for controlling navigation flow.

### Global Guards

#### router.beforeEach(guard)

**Type:** `Function`

Register a global before guard.

**Parameters:**
- `guard: NavigationGuard` - Guard function

**Example:**
```javascript
router.beforeEach((to, from, next) => {
  // Navigation logic
  next()
})
```

#### router.beforeResolve(guard)

**Type:** `Function`

Register a global resolve guard.

**Parameters:**
- `guard: NavigationGuard` - Guard function

**Example:**
```javascript
router.beforeResolve((to, from, next) => {
  // Called after beforeRouteEnter and beforeRouteUpdate
  next()
})
```

#### router.afterEach(hook)

**Type:** `Function`

Register a global after hook.

**Parameters:**
- `hook: AfterNavigationHook` - Hook function

**Example:**
```javascript
router.afterEach((to, from) => {
  // Called after navigation is confirmed
  console.log('Navigated to:', to.path)
})
```

### Per-Route Guard

#### beforeEnter

**Type:** `NavigationGuard`

Guard defined directly on the route configuration.

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

### Component Guards

#### beforeRouteEnter

**Type:** `NavigationGuard`

Called before the route that renders this component is confirmed.

**Example:**
```javascript
beforeRouteEnter(to, from, next) {
  // Cannot access this
  // Can access component via next(vm => {})
  next(vm => {
    vm.loadData()
  })
}
```

#### beforeRouteUpdate

**Type:** `NavigationGuard`

Called when the route that renders this component has changed, but this component is reused.

**Example:**
```javascript
beforeRouteUpdate(to, from, next) {
  // Can access this
  this.userId = to.params.id
  next()
}
```

#### beforeRouteLeave

**Type:** `NavigationGuard`

Called when the route that renders this component is about to be navigated away from.

**Example:**
```javascript
beforeRouteLeave(to, from, next) {
  if (this.hasUnsavedChanges) {
    if (confirm('Leave without saving?')) {
      next()
    } else {
      next(false)
    }
  } else {
    next()
  }
}
```

### NavigationGuard Function Signature

```typescript
type NavigationGuard = (
  to: Route,
  from: Route,
  next: (to?: RawLocation | false | ((vm: Component) => any) | void) => void
) => any
```

### Guard Execution Order

1. Navigation triggered
2. Call `beforeRouteLeave` guards in deactivated components
3. Call global `beforeEach` guards
4. Call `beforeRouteUpdate` guards in reused components
5. Call `beforeEnter` in route configs
6. Call `beforeRouteEnter` in activated components
7. Call global `beforeResolve` guards
8. Navigation confirmed
9. Call global `afterEach` hooks

**See also:** `examples/navigation-guards.md`
