# Navigation Helpers | 导航辅助函数

## API Reference

Helper functions for navigation and route utilities.

### NavigationGuard

Type for navigation guard functions.

**Signature:**
```typescript
type NavigationGuard = (
  to: RouteLocationNormalized,
  from: RouteLocationNormalized,
  next: NavigationGuardNext
) => NavigationGuardReturn | Promise<NavigationGuardReturn>
```

### RouteLocationRaw

Type for route location (string, object, or RouteLocation).

**Type:**
```typescript
type RouteLocationRaw = 
  | string 
  | RouteLocation 
  | RouteLocationPathRaw 
  | RouteLocationNamedRaw
```

### Key Points

- Navigation guards control route navigation
- Can return boolean, route location, or Promise
- Use `next()` to continue navigation
- Use `next(false)` to cancel navigation
- Use `next('/path')` to redirect
