# Not Found

## Instructions

This example demonstrates custom 404 pages in App Router.

### Key Concepts

- not-found.tsx file
- notFound() function
- 404 handling
- Custom error pages

### Example: Not Found Page

```typescript
// app/not-found.tsx
export default function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      <p>Could not find requested resource</p>
      <a href="/">Return Home</a>
    </div>
  )
}
```

### Example: Using notFound()

```typescript
// app/blog/[slug]/page.tsx
import { notFound } from 'next/navigation'

async function getPost(slug: string) {
  const res = await fetch(`https://api.example.com/posts/${slug}`)
  if (!res.ok) {
    notFound()
  }
  return res.json()
}

export default async function BlogPost({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug)
  return <article>{post.title}</article>
}
```

### Example: Nested Not Found

```typescript
// app/dashboard/not-found.tsx
export default function DashboardNotFound() {
  return (
    <div>
      <h2>Dashboard page not found</h2>
    </div>
  )
}
```

### Key Points

- not-found.tsx creates custom 404 pages
- Use notFound() to trigger 404
- Can be nested for route segments
- Shows when route doesn't match
- Improves user experience
