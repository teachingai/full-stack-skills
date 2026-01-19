# Store Instance API | Store 实例 API

## API Reference

Store instance properties and methods.

### Store Properties

#### $id

Store identifier.

**Type:** `string`

**Example:**
```javascript
const store = useCounterStore()
console.log(store.$id) // 'counter'
```

#### $state

Store state object.

**Type:** `State`

**Example:**
```javascript
const store = useCounterStore()
console.log(store.$state) // { count: 0 }

// Replace entire state
store.$state = { count: 10 }
```

### Store Methods

#### $patch()

Partially update state.

**Signature:**
```typescript
$patch(partialState: Partial<State>): void
$patch(mutator: (state: State) => void): void
```

**Example:**
```javascript
// Patch with object
store.$patch({
  count: 10,
  name: 'John'
})

// Patch with function
store.$patch((state) => {
  state.items.push({ id: 1, name: 'Item' })
  state.count++
})
```

#### $reset()

Reset state to initial values.

**Signature:**
```typescript
$reset(): void
```

**Example:**
```javascript
store.$reset() // Resets state to initial values
```

#### $subscribe()

Subscribe to state changes.

**Signature:**
```typescript
$subscribe(callback: (mutation: StoreMutation, state: State) => void, options?: SubscribeOptions): () => void
```

**Example:**
```javascript
const unsubscribe = store.$subscribe((mutation, state) => {
  console.log('State changed:', mutation.type, mutation.payload)
})

// Unsubscribe
unsubscribe()
```

#### $onAction()

Subscribe to actions.

**Signature:**
```typescript
$onAction(callback: (context: ActionContext) => void): () => void
```

**Example:**
```javascript
const unsubscribe = store.$onAction(({
  name,
  args,
  after,
  onError
}) => {
  console.log('Action:', name, args)
  
  after((result) => {
    console.log('Action completed:', result)
  })
  
  onError((error) => {
    console.error('Action error:', error)
  })
})

// Unsubscribe
unsubscribe()
```

### Key Points

- `$id`: Store identifier
- `$state`: Access or replace entire state
- `$patch()`: Update state partially
- `$reset()`: Reset state to initial values
- `$subscribe()`: Watch state changes
- `$onAction()`: Watch actions
- All methods return unsubscribe functions
