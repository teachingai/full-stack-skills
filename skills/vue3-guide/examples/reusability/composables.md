# Composables

## Instructions

This example demonstrates creating and using composables (composition functions) for logic reuse.

### Key Concepts

- Creating composables
- Composable naming conventions
- Sharing stateful logic
- Composable best practices

### Example: useCounter Composable

```javascript
// composables/useCounter.js
import { ref, computed } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)
  const doubleCount = computed(() => count.value * 2)
  
  const increment = () => count.value++
  const decrement = () => count.value--
  const reset = () => count.value = initialValue
  
  return { count, doubleCount, increment, decrement, reset }
}
```

### Example: useMouse Composable

```javascript
// composables/useMouse.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)
  
  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }
  
  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))
  
  return { x, y }
}
```

### Key Points

- Prefix composables with `use`
- Return reactive values to maintain reactivity
- Clean up side effects in `onUnmounted`
- Composable functions encapsulate reusable logic
