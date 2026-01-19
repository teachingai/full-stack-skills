# Installation | 安装

## Instructions

This example demonstrates how to install Pinia and set it up in a Vue 3 application.

### Key Concepts

- Installing Pinia
- Creating a Pinia instance
- Registering Pinia with Vue app
- Basic configuration

### Example: Installation

```bash
# Using npm
npm install pinia

# Using yarn
yarn add pinia

# Using pnpm
pnpm add pinia
```

### Example: Creating Pinia Instance

```javascript
// main.js
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)
app.mount('#app')
```

### Example: With TypeScript

```typescript
// main.ts
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)
app.mount('#app')
```

### Example: With Vite

```javascript
// main.js
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

createApp(App).use(createPinia()).mount('#app')
```

### Key Points

- Install Pinia via npm, yarn, or pnpm
- Create a Pinia instance with `createPinia()`
- Register Pinia with Vue app using `app.use(pinia)`
- Pinia must be installed before using stores
- Works with both JavaScript and TypeScript
