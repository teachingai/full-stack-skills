# useRouter and useRoute | useRouter 和 useRoute

## API Reference

Composition API functions for accessing router and route in setup functions.

### useRouter()

Returns the router instance.

**Signature:**
```typescript
function useRouter(): Router
```

**Example:**
```javascript
import { useRouter } from 'vue-router'

const router = useRouter()
router.push('/home')
```

### useRoute()

Returns the current route location (reactive).

**Signature:**
```typescript
function useRoute(): RouteLocationNormalizedLoaded
```

**Example:**
```javascript
import { useRoute } from 'vue-router'

const route = useRoute()
console.log(route.path)
console.log(route.params)
console.log(route.query)
```

### Route Location Properties

```typescript
interface RouteLocationNormalizedLoaded {
  path: string
  name: string | symbol | null | undefined
  params: RouteParams
  query: RouteQuery
  hash: string
  fullPath: string
  matched: RouteRecordNormalized[]
  meta: RouteMeta
  redirectedFrom: RouteLocation | undefined
}
```

### Example: Complete Usage

```vue
<script setup>
import { useRouter, useRoute } from 'vue-router'
import { watch } from 'vue'

const router = useRouter()
const route = useRoute()

// Access route properties
console.log(route.path)
console.log(route.params.id)
console.log(route.query.search)

// Navigate
function goHome() {
  router.push('/')
}

// Watch route changes
watch(() => route.params.id, (newId) => {
  console.log('Route param changed:', newId)
})
</script>
```
