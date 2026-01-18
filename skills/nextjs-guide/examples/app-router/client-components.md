# Client Components

## Instructions

This example demonstrates Client Components in App Router.

### Key Concepts

- 'use client' directive
- Client-side features
- Interactivity
- Browser APIs

### Example: Basic Client Component

```typescript
// app/components/Counter.tsx
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

### Example: Client Component with Event Handlers

```typescript
// app/components/Form.tsx
'use client'

import { useState } from 'react'

export default function Form() {
  const [value, setValue] = useState('')
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('Submitted:', value)
  }
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  )
}
```

### Example: Client Component with Browser APIs

```typescript
// app/components/WindowSize.tsx
'use client'

import { useState, useEffect } from 'react'

export default function WindowSize() {
  const [size, setSize] = useState({ width: 0, height: 0 })
  
  useEffect(() => {
    const updateSize = () => {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      })
    }
    
    window.addEventListener('resize', updateSize)
    updateSize()
    
    return () => window.removeEventListener('resize', updateSize)
  }, [])
  
  return <div>Window: {size.width} x {size.height}</div>
}
```

### Key Points

- Use 'use client' directive at top of file
- Required for interactivity and hooks
- Can use browser APIs
- Can use event handlers
- JavaScript is sent to client
