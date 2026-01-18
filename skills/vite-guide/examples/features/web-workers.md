# Web Workers

## Instructions

This example demonstrates Web Workers support in Vite.

### Key Concepts

- Worker imports
- Shared Workers
- Worker communication
- Inline workers

### Example: Basic Worker

```javascript
// worker.js
self.onmessage = (e) => {
  const result = e.data.a + e.data.b
  self.postMessage({ result })
}

// main.js
import MyWorker from './worker.js?worker'

const worker = new MyWorker()
worker.postMessage({ a: 1, b: 2 })
worker.onmessage = (e) => {
  console.log(e.data.result)  // 3
}
```

### Example: Shared Worker

```javascript
// shared-worker.js
self.onconnect = (e) => {
  const port = e.ports[0]
  port.onmessage = (e) => {
    port.postMessage({ result: e.data.a + e.data.b })
  }
}

// main.js
import SharedWorker from './shared-worker.js?sharedworker'

const worker = new SharedWorker()
worker.port.postMessage({ a: 1, b: 2 })
worker.port.onmessage = (e) => {
  console.log(e.data.result)
}
```

### Example: Inline Worker

```javascript
// Create worker from string
const workerCode = `
  self.onmessage = (e) => {
    self.postMessage({ result: e.data * 2 })
  }
`

const blob = new Blob([workerCode], { type: 'application/javascript' })
const worker = new Worker(URL.createObjectURL(blob))
```

### Example: Worker with TypeScript

```typescript
// worker.ts
self.onmessage = (e: MessageEvent<{ a: number; b: number }>) => {
  const result = e.data.a + e.data.b
  self.postMessage({ result })
}

// main.ts
import MyWorker from './worker.ts?worker'

const worker = new MyWorker()
```

### Key Points

- Use `?worker` suffix for Worker imports
- Use `?sharedworker` for Shared Workers
- Workers run in separate threads
- Supports TypeScript workers
- Workers are bundled separately
