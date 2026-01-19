# Data Fetching

## Instructions

This example demonstrates data fetching in App Router.

### Key Concepts

- Server Components data fetching
- fetch API
- Caching
- Revalidation
- Streaming

### Example: Basic Data Fetching

```typescript
// app/products/page.tsx
async function getProducts() {
  const res = await fetch('https://api.example.com/products')
  return res.json()
}

export default async function Products() {
  const products = await getProducts()
  return (
    <div>
      {products.map(product => (
        <div key={product.id}>{product.name}</div>
      ))}
    </div>
  )
}
```

### Example: Data Fetching with Options

```typescript
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    cache: 'no-store',  // Always fetch fresh data
    next: { revalidate: 3600 }  // Revalidate every hour
  })
  return res.json()
}
```

### Example: Parallel Data Fetching

```typescript
export default async function Page() {
  const [users, posts] = await Promise.all([
    fetch('https://api.example.com/users').then(r => r.json()),
    fetch('https://api.example.com/posts').then(r => r.json())
  ])
  
  return (
    <div>
      <UsersList users={users} />
      <PostsList posts={posts} />
    </div>
  )
}
```

### Example: Sequential Data Fetching

```typescript
export default async function Page() {
  const user = await fetch('https://api.example.com/user/1').then(r => r.json())
  const posts = await fetch(`https://api.example.com/posts?userId=${user.id}`).then(r => r.json())
  
  return <UserProfile user={user} posts={posts} />
}
```

### Example: Using Database

```typescript
import { sql } from '@vercel/postgres'

export default async function Page() {
  const { rows } = await sql`SELECT * FROM users`
  return <UsersList users={rows} />
}
```

### Key Points

- Server Components can fetch data directly
- fetch is extended with caching options
- Use cache: 'no-store' for dynamic data
- Use revalidate for time-based revalidation
- Fetch requests are automatically deduplicated
