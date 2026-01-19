# storeToRefs API | storeToRefs API

## API Reference

The `storeToRefs()` utility for destructuring stores while maintaining reactivity.

### storeToRefs()

Extracts state and getters as refs from a store.

**Signature:**
```typescript
function storeToRefs<SS extends StoreGeneric>(store: SS): ToRefs<StoreState<SS> & StoreGetters<SS>>
```

**Parameters:**
- `store`: Store instance

**Returns:**
- Object with state and getters as refs

**Example:**
```javascript
import { storeToRefs } from 'pinia'
import { useCounterStore } from '@/stores/counter'

const counterStore = useCounterStore()

// Destructure state and getters (maintains reactivity)
const { count, doubleCount } = storeToRefs(counterStore)

// Actions can be destructured directly (not reactive)
const { increment } = counterStore
```

### Key Points

- Use `storeToRefs()` to destructure state and getters
- Maintains reactivity when destructuring
- Only extracts state and getters (not actions)
- Actions can be destructured directly from store
- Useful in Composition API setup functions
- Returns refs that can be used in templates
