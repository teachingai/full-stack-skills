# Caching

## Instructions

This example demonstrates caching and revalidation in App Router.

### Key Concepts

- Data cache
- Request cache
- Full route cache
- Revalidation
- Cache tags

### Example: Data Caching

```typescript
// fetch is cached by default
async function getData() {
  const res = await fetch('https://api.example.com/data')
  return res.json()
  // Cached indefinitely
}
```

### Example: Revalidation

```typescript
// Time-based revalidation
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    next: { revalidate: 3600 }  // Revalidate every hour
  })
  return res.json()
}
```

### Example: No Cache

```typescript
// Always fetch fresh data
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    cache: 'no-store'
  })
  return res.json()
}
```

### Example: Cache Tags

```typescript
// Tag-based revalidation
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    next: { tags: ['posts'] }
  })
  return res.json()
}

// Revalidate by tag
import { revalidateTag } from 'next/cache'
revalidateTag('posts')
```

### Example: On-Demand Revalidation

```typescript
// app/api/revalidate/route.ts
import { revalidatePath } from 'next/cache'

export async function POST() {
  revalidatePath('/products')
  return Response.json({ revalidated: true })
}
```

### Key Points

- fetch is cached by default
- Use revalidate for time-based revalidation
- Use cache: 'no-store' for dynamic data
- Use tags for tag-based revalidation
- Use revalidatePath/revalidateTag for on-demand revalidation
