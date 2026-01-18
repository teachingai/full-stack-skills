# History Modes API | 历史模式 API

## API Reference

History mode creation functions.

### createWebHistory()

Creates HTML5 history mode.

**Signature:**
```typescript
function createWebHistory(base?: string): RouterHistory
```

**Example:**
```javascript
import { createWebHistory } from 'vue-router'

const history = createWebHistory()
const historyWithBase = createWebHistory('/my-app/')
```

### createWebHashHistory()

Creates hash history mode.

**Signature:**
```typescript
function createWebHashHistory(base?: string): RouterHistory
```

**Example:**
```javascript
import { createWebHashHistory } from 'vue-router'

const history = createWebHashHistory()
```

### createMemoryHistory()

Creates memory history mode (for SSR/testing).

**Signature:**
```typescript
function createMemoryHistory(base?: string): RouterHistory
```

**Example:**
```javascript
import { createMemoryHistory } from 'vue-router'

const history = createMemoryHistory()
```

### Key Points

- `createWebHistory` for clean URLs (requires server config)
- `createWebHashHistory` for hash-based URLs (no server config needed)
- `createMemoryHistory` for SSR and testing
- All accept optional `base` parameter
