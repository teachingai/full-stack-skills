# Event Handling

## Instructions

This example demonstrates handling DOM events with `v-on` directive and event modifiers.

### Key Concepts

- Event listeners with `v-on` or `@`
- Inline handlers vs method handlers
- Event modifiers
- Key modifiers
- Mouse button modifiers

### Example: Basic Event Handling

```vue
<template>
  <div>
    <!-- Method handler -->
    <button v-on:click="counter++">Add 1</button>
    <p>The button above has been clicked {{ counter }} times.</p>
    
    <!-- Shorthand -->
    <button @click="counter++">Add 1</button>
    
    <!-- Method handler -->
    <button @click="greet">Greet</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const counter = ref(0)

function greet(event) {
  alert(`Hello ${name.value}!`)
  // event is the native DOM event
  if (event) {
    alert(event.target.tagName)
  }
}
</script>
```

### Example: Inline Handlers with Arguments

```vue
<template>
  <div>
    <button @click="say('hello')">Say hello</button>
    <button @click="say('bye')">Say bye</button>
    
    <!-- Accessing native event -->
    <button @click="warn('Form cannot be submitted yet.', $event)">
      Submit
    </button>
    
    <!-- Or use inline arrow function -->
    <button @click="(event) => warn('Form cannot be submitted yet.', event)">
      Submit
    </button>
  </div>
</template>

<script setup>
function say(message) {
  alert(message)
}

function warn(message, event) {
  if (event) {
    event.preventDefault()
  }
  alert(message)
}
</script>
```

### Example: Event Modifiers

```vue
<template>
  <div>
    <!-- .stop - stopPropagation -->
    <div @click.stop="doThis">...</div>
    
    <!-- .prevent - preventDefault -->
    <form @submit.prevent="onSubmit">...</form>
    
    <!-- .self - only trigger if event.target is the element -->
    <div @click.self="doThat">...</div>
    
    <!-- Chained modifiers -->
    <a @click.stop.prevent="doThat">...</a>
    
    <!-- .once - trigger at most once -->
    <button @click.once="doThis">...</button>
    
    <!-- .capture - use capture mode -->
    <div @click.capture="doThis">...</div>
    
    <!-- .passive - passive listener -->
    <div @scroll.passive="onScroll">...</div>
  </div>
</template>
```

### Example: Key Modifiers

```vue
<template>
  <div>
    <!-- Specific key -->
    <input @keyup.enter="submit" />
    
    <!-- Key aliases -->
    <input @keyup.enter="submit" />
    <input @keyup.delete="confirmDelete" />
    <input @keyup.esc="cancel" />
    <input @keyup.space="pause" />
    <input @keyup.up="moveUp" />
    <input @keyup.down="moveDown" />
    <input @keyup.left="moveLeft" />
    <input @keyup.right="moveRight" />
    
    <!-- System modifier keys -->
    <input @keyup.ctrl.enter="submit" />
    <input @keyup.shift.enter="submit" />
    <input @keyup.alt.enter="submit" />
    <input @keyup.meta.enter="submit" />
    
    <!-- .exact modifier -->
    <button @click.ctrl.exact="onCtrlClick">Only Ctrl</button>
    <button @click.exact="onClick">No modifiers</button>
  </div>
</template>

<script setup>
function submit() {
  console.log('Submitted')
}

function confirmDelete() {
  console.log('Delete confirmed')
}

function cancel() {
  console.log('Cancelled')
}

function pause() {
  console.log('Paused')
}

function moveUp() {
  console.log('Move up')
}

function moveDown() {
  console.log('Move down')
}

function moveLeft() {
  console.log('Move left')
}

function moveRight() {
  console.log('Move right')
}

function onCtrlClick() {
  console.log('Ctrl clicked')
}

function onClick() {
  console.log('Clicked without modifiers')
}
</script>
```

### Example: Mouse Button Modifiers

```vue
<template>
  <div>
    <button @click.left="onLeftClick">Left click</button>
    <button @click.right="onRightClick">Right click</button>
    <button @click.middle="onMiddleClick">Middle click</button>
  </div>
</template>

<script setup>
function onLeftClick() {
  console.log('Left button clicked')
}

function onRightClick() {
  console.log('Right button clicked')
}

function onMiddleClick() {
  console.log('Middle button clicked')
}
</script>
```

### Key Points

- Use `v-on` or `@` for event listeners
- Event modifiers can be chained
- Key modifiers listen for specific keys
- System modifiers require modifier key to be pressed
- `.exact` modifier ensures exact key combination
