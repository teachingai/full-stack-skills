# Error Handling

## Instructions

This example demonstrates error handling in App Router.

### Key Concepts

- error.tsx file
- Error boundaries
- Error recovery
- Error logging

### Example: Error Boundary

```typescript
// app/error.tsx
'use client'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={reset}>Try again</button>
    </div>
  )
}
```

### Example: Error with Logging

```typescript
// app/error.tsx
'use client'

import { useEffect } from 'react'

export default function Error({ error, reset }) {
  useEffect(() => {
    // Log error to error reporting service
    console.error('Error:', error)
  }, [error])

  return (
    <div>
      <h2>An error occurred</h2>
      <button onClick={reset}>Try again</button>
    </div>
  )
}
```

### Example: Nested Error Boundary

```typescript
// app/dashboard/error.tsx
'use client'

export default function DashboardError({ error, reset }) {
  return (
    <div>
      <h2>Dashboard Error</h2>
      <p>{error.message}</p>
      <button onClick={reset}>Reset</button>
    </div>
  )
}
```

### Key Points

- error.tsx must be a Client Component
- Error boundaries catch errors in child components
- reset() function retries rendering
- Can be nested for granular error handling
- Use for error recovery and user feedback
