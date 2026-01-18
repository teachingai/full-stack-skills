# Router API | 路由器 API

## API Reference

Vue Router instance API and methods.

### createRouter()

Creates a router instance.

**Signature:**
```typescript
function createRouter(options: RouterOptions): Router
```

**Example:**
```javascript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [...]
})
```

### Router Instance Methods

#### router.push()

Navigate to a new route.

**Signature:**
```typescript
push(to: RouteLocationRaw): Promise<NavigationFailure | void>
```

**Example:**
```javascript
router.push('/home')
router.push({ name: 'Home' })
router.push({ path: '/user', query: { id: '123' } })
```

#### router.replace()

Replace current route.

**Signature:**
```typescript
replace(to: RouteLocationRaw): Promise<NavigationFailure | void>
```

**Example:**
```javascript
router.replace('/home')
```

#### router.go()

Navigate through history.

**Signature:**
```typescript
go(delta: number): void
```

**Example:**
```javascript
router.go(1)  // Forward
router.go(-1) // Back
```

#### router.back()

Go back in history.

**Signature:**
```typescript
back(): void
```

**Example:**
```javascript
router.back()
```

#### router.forward()

Go forward in history.

**Signature:**
```typescript
forward(): void
```

**Example:**
```javascript
router.forward()
```

#### router.addRoute()

Add a route dynamically.

**Signature:**
```typescript
addRoute(parentName: string | symbol, route: RouteRecordRaw): () => void
addRoute(route: RouteRecordRaw): () => void
```

**Example:**
```javascript
router.addRoute({ path: '/new', component: NewComponent })
router.addRoute('parent', { path: 'child', component: ChildComponent })
```

#### router.removeRoute()

Remove a route dynamically.

**Signature:**
```typescript
removeRoute(name: string | symbol): void
```

**Example:**
```javascript
router.removeRoute('RouteName')
```

#### router.hasRoute()

Check if a route exists.

**Signature:**
```typescript
hasRoute(name: string | symbol): boolean
```

**Example:**
```javascript
if (router.hasRoute('Home')) {
  // Route exists
}
```

#### router.getRoutes()

Get all route records.

**Signature:**
```typescript
getRoutes(): RouteRecordNormalized[]
```

**Example:**
```javascript
const routes = router.getRoutes()
```

### Router Instance Properties

#### router.currentRoute

Current route location (readonly, reactive).

**Type:**
```typescript
Ref<RouteLocationNormalizedLoaded>
```

**Example:**
```javascript
const currentRoute = router.currentRoute.value
```

#### router.options

Router options (readonly).

**Type:**
```typescript
Readonly<RouterOptions>
```

### Router Options

```typescript
interface RouterOptions {
  history: RouterHistory
  routes: RouteRecordRaw[]
  scrollBehavior?: RouterScrollBehavior
  parseQuery?: typeof parseQuery
  stringifyQuery?: typeof stringifyQuery
}
```
