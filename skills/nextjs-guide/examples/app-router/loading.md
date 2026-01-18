# Loading UI

## Instructions

This example demonstrates loading states and Suspense in App Router.

### Key Concepts

- loading.tsx file
- Suspense boundaries
- Loading states
- Streaming

### Example: Loading File

```typescript
// app/loading.tsx
export default function Loading() {
  return <div>Loading...</div>
}

// app/dashboard/loading.tsx
export default function Loading() {
  return (
    <div>
      <div className="skeleton">Loading dashboard...</div>
    </div>
  )
}
```

### Example: Suspense Boundary

```typescript
// app/page.tsx
import { Suspense } from 'react'
import Loading from './loading'

export default function Home() {
  return (
    <div>
      <Suspense fallback={<Loading />}>
        <AsyncComponent />
      </Suspense>
    </div>
  )
}
```

### Example: Loading with Skeleton

```typescript
// app/loading.tsx
export default function Loading() {
  return (
    <div className="animate-pulse">
      <div className="h-4 bg-gray-200 rounded w-3/4"></div>
      <div className="h-4 bg-gray-200 rounded w-1/2"></div>
    </div>
  )
}
```

### Key Points

- loading.tsx shows loading state automatically
- Works with Suspense boundaries
- Shows while page/route is loading
- Can be nested for nested routes
- Improves user experience with instant feedback
