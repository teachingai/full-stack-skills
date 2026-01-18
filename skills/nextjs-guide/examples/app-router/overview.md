# App Router Overview

## Instructions

This example provides an overview of the App Router in Next.js.

### Key Concepts

- App Router architecture
- Server Components
- Client Components
- Layouts and pages
- File conventions

### Example: App Router Structure

```
app/
├── layout.tsx          # Root layout
├── page.tsx            # Home page (/)
├── loading.tsx         # Loading UI
├── error.tsx           # Error boundary
├── not-found.tsx       # 404 page
├── about/
│   └── page.tsx       # /about
└── blog/
    ├── layout.tsx      # Blog layout
    └── [slug]/
        └── page.tsx   # /blog/:slug
```

### Example: Server Component (Default)

```typescript
// app/page.tsx
// Server Component by default
export default async function Home() {
  const data = await fetch('https://api.example.com/data')
  const json = await data.json()
  
  return (
    <div>
      <h1>{json.title}</h1>
    </div>
  )
}
```

### Example: Client Component

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

### Key Points

- App Router is the recommended routing system
- Components are Server Components by default
- Use 'use client' for Client Components
- Layouts wrap pages and child layouts
- File-based routing determines URL structure
