# createPinia API | createPinia API

## API Reference

The `createPinia()` function for creating a Pinia instance.

### createPinia()

Creates a Pinia instance.

**Signature:**
```typescript
function createPinia(): Pinia
```

**Returns:**
- `Pinia`: Pinia instance

**Example:**
```javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)
app.mount('#app')
```

### Pinia Instance

The Pinia instance provides methods for managing stores and plugins.

**Properties:**
- `state`: Global state object
- `_s`: Map of stores
- `_p`: Array of plugins

**Methods:**
- `use(plugin)`: Install a plugin
- `install(app)`: Install Pinia in Vue app

### Key Points

- Create one Pinia instance per application
- Register with Vue app using `app.use(pinia)`
- Must be created before using stores
- Can install plugins using `pinia.use(plugin)`
- Instance is shared across all stores
