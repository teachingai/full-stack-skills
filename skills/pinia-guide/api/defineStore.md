# defineStore API | defineStore API

## API Reference

The `defineStore()` function for creating Pinia stores.

### defineStore()

Creates a store definition.

**Signature:**
```typescript
function defineStore(id: string, options: StoreOptions): StoreDefinition
function defineStore(id: string, setup: () => StoreSetup): StoreDefinition
function defineStore(options: StoreOptionsWithId): StoreDefinition
```

**Parameters:**
- `id`: Store identifier (string or function that returns string)
- `options`: Store options object (for Options API syntax)
- `setup`: Setup function (for Composition API syntax)

**Returns:**
- `StoreDefinition`: Function that returns the store instance

### Options API Syntax

```typescript
interface StoreOptions {
  state?: () => State
  getters?: GettersTree<State>
  actions?: ActionsTree
  id?: string
}
```

**Example:**
```javascript
export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  getters: {
    double: (state) => state.count * 2
  },
  actions: {
    increment() {
      this.count++
    }
  }
})
```

### Setup (Composition API) Syntax

```typescript
function defineStore(id: string, setup: () => StoreSetup): StoreDefinition
```

**Example:**
```javascript
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const double = computed(() => count.value * 2)
  function increment() {
    count.value++
  }
  return { count, double, increment }
})
```

### Store ID

The store ID must be unique and is used to identify the store.

```javascript
// String ID
defineStore('counter', { ... })

// Function that returns ID
defineStore(() => 'counter', { ... })

// ID in options object
defineStore({
  id: 'counter',
  state: () => ({ ... })
})
```

### Key Points

- First argument is the store ID (required)
- Second argument is options object or setup function
- Store ID must be unique across the application
- Returns a function that must be called to get the store instance
- Use `useStoreName()` naming convention for store functions
- Supports both Options API and Composition API syntax
