# Computed Properties

## Instructions

This example demonstrates computed properties that automatically update when their dependencies change.

### Key Concepts

- Creating computed properties with `computed()`
- Computed vs methods
- Writable computed properties
- Computed caching

### Example: Basic Computed Property

```vue
<script setup>
import { ref, computed } from 'vue'

const firstName = ref('John')
const lastName = ref('Doe')

// Computed property
const fullName = computed(() => {
  return `${firstName.value} ${lastName.value}`
})

// Computed is cached - only re-evaluates when dependencies change
console.log(fullName.value)  // "John Doe"

firstName.value = 'Jane'
console.log(fullName.value)  // "Jane Doe" (recomputed)
</script>

<template>
  <div>
    <input v-model="firstName" placeholder="First name" />
    <input v-model="lastName" placeholder="Last name" />
    <p>Full Name: {{ fullName }}</p>
  </div>
</template>
```

### Example: Computed vs Methods

```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([
  { id: 1, name: 'Item 1', price: 10 },
  { id: 2, name: 'Item 2', price: 20 },
  { id: 3, name: 'Item 3', price: 30 }
])

// Computed - cached, only re-evaluates when items change
const totalPrice = computed(() => {
  console.log('Computing total...')
  return items.value.reduce((sum, item) => sum + item.price, 0)
})

// Method - runs every time it's called
function getTotalPrice() {
  console.log('Calculating total...')
  return items.value.reduce((sum, item) => sum + item.price, 0)
}
</script>

<template>
  <div>
    <p>Total (computed): {{ totalPrice }}</p>
    <p>Total (method): {{ getTotalPrice() }}</p>
    <!-- totalPrice is cached, getTotalPrice() runs every render -->
  </div>
</template>
```

### Example: Writable Computed

```vue
<script setup>
import { ref, computed } from 'vue'

const firstName = ref('John')
const lastName = ref('Doe')

// Writable computed with getter and setter
const fullName = computed({
  get() {
    return `${firstName.value} ${lastName.value}`
  },
  set(newValue) {
    const parts = newValue.split(' ')
    firstName.value = parts[0] || ''
    lastName.value = parts[1] || ''
  }
})

// Can set the computed value
fullName.value = 'Jane Smith'
console.log(firstName.value)  // "Jane"
console.log(lastName.value)    // "Smith"
</script>

<template>
  <div>
    <input v-model="fullName" placeholder="Full name" />
    <p>First: {{ firstName }}</p>
    <p>Last: {{ lastName }}</p>
  </div>
</template>
```

### Example: Computed with Multiple Dependencies

```vue
<script setup>
import { ref, computed } from 'vue'

const quantity = ref(1)
const price = ref(10)
const discount = ref(0)

const subtotal = computed(() => quantity.value * price.value)
const discountAmount = computed(() => subtotal.value * (discount.value / 100))
const total = computed(() => subtotal.value - discountAmount.value)
</script>

<template>
  <div>
    <input v-model.number="quantity" type="number" />
    <input v-model.number="price" type="number" />
    <input v-model.number="discount" type="number" />
    <p>Subtotal: {{ subtotal }}</p>
    <p>Discount: {{ discountAmount }}</p>
    <p>Total: {{ total }}</p>
  </div>
</template>
```

### Key Points

- Computed properties are cached and only re-evaluate when dependencies change
- Use computed for derived state
- Use methods for event handlers or when you need to trigger side effects
- Computed properties can have getters and setters
- Computed properties are reactive and update automatically
