# Route Records API | 路由记录 API

## API Reference

Route record types and properties.

### RouteRecordRaw

Route configuration type.

**Type:**
```typescript
interface RouteRecordRaw {
  path: string
  name?: string | symbol
  component?: Component
  components?: Record<string, Component>
  redirect?: RouteRecordRedirectOption
  alias?: string | string[]
  children?: RouteRecordRaw[]
  beforeEnter?: NavigationGuard
  meta?: RouteMeta
  props?: boolean | Record<string, any> | RoutePropsFunction
  caseSensitive?: boolean
  pathToRegexpOptions?: PathToRegexpOptions
}
```

### RouteRecordNormalized

Normalized route record.

**Properties:**
- `path`: Route path
- `name`: Route name
- `components`: Route components
- `children`: Child routes
- `meta`: Route meta
- `beforeEnter`: Route guard
- `props`: Props configuration
- `redirect`: Redirect configuration

### Key Points

- `RouteRecordRaw` is the input type for route definitions
- `RouteRecordNormalized` is the processed route record
- All route properties are optional except `path`
- Can use `component` (single) or `components` (named views)
