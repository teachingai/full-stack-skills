# Server Components

## Instructions

This example demonstrates React Server Components in App Router.

### Key Concepts

- Server Components by default
- Server-only code
- No client-side JavaScript
- Direct data fetching

### Example: Basic Server Component

```typescript
// app/components/ServerComponent.tsx
// Server Component (default, no 'use client')
async function getData() {
  const res = await fetch('https://api.example.com/data')
  return res.json()
}

export default async function ServerComponent() {
  const data = await getData()
  return <div>{data.title}</div>
}
```

### Example: Server Component with Database

```typescript
// app/components/UserList.tsx
import { sql } from '@vercel/postgres'

export default async function UserList() {
  const { rows } = await sql`SELECT * FROM users`
  
  return (
    <ul>
      {rows.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  )
}
```

### Example: Server Component Limitations

```typescript
// ❌ Cannot use in Server Components:
// - useState, useEffect, etc.
// - Browser APIs (window, document, etc.)
// - Event handlers
// - Browser-only libraries

// ✅ Can use in Server Components:
// - Direct database queries
// - File system access
// - Environment variables
// - Server-only libraries
```

### Example: Server and Client Components Together

```typescript
// app/page.tsx (Server Component)
import ClientCounter from './components/ClientCounter'
import ServerData from './components/ServerData'

export default function Page() {
  return (
    <div>
      <ServerData />  {/* Server Component */}
      <ClientCounter />  {/* Client Component */}
    </div>
  )
}
```

### Key Points

- Components are Server Components by default
- Server Components run only on server
- No JavaScript sent to client
- Can directly access databases and APIs
- Cannot use client-side features
