# Routing

## Instructions

This example demonstrates routing fundamentals in Next.js.

### Key Concepts

- File-based routing
- App Router vs Pages Router
- Dynamic routes
- Route groups

### Example: Basic Routes (App Router)

```typescript
// app/page.tsx → /
export default function Home() {
  return <h1>Home</h1>
}

// app/about/page.tsx → /about
export default function About() {
  return <h1>About</h1>
}

// app/blog/page.tsx → /blog
export default function Blog() {
  return <h1>Blog</h1>
}
```

### Example: Dynamic Routes (App Router)

```typescript
// app/blog/[slug]/page.tsx → /blog/:slug
export default function BlogPost({ params }: { params: { slug: string } }) {
  return <h1>Post: {params.slug}</h1>
}

// app/shop/[...slug]/page.tsx → /shop/* (catch-all)
export default function Shop({ params }: { params: { slug: string[] } }) {
  return <h1>Shop: {params.slug.join('/')}</h1>
}
```

### Example: Route Groups (App Router)

```typescript
// app/(marketing)/about/page.tsx → /about
// app/(marketing)/contact/page.tsx → /contact
// app/(shop)/products/page.tsx → /products
// Groups don't affect URL structure
```

### Example: Pages Router Routes

```typescript
// pages/index.tsx → /
export default function Home() {
  return <h1>Home</h1>
}

// pages/about.tsx → /about
export default function About() {
  return <h1>About</h1>
}

// pages/blog/[slug].tsx → /blog/:slug
export default function BlogPost({ params }) {
  return <h1>Post: {params.slug}</h1>
}
```

### Example: Navigation

```typescript
// Using Link component
import Link from 'next/link'

export default function Navigation() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
    </nav>
  )
}
```

### Key Points

- File-based routing determines URLs
- App Router uses app/ directory
- Pages Router uses pages/ directory
- Dynamic routes use brackets [param]
- Route groups organize without affecting URLs
