# Dynamic Routes

## Instructions

This example demonstrates dynamic routes in App Router.

### Key Concepts

- Dynamic segments
- Route parameters
- Catch-all routes
- Optional catch-all

### Example: Single Dynamic Segment

```typescript
// app/blog/[slug]/page.tsx
export default function BlogPost({ params }: { params: { slug: string } }) {
  return <h1>Post: {params.slug}</h1>
}
```

### Example: Multiple Dynamic Segments

```typescript
// app/shop/[category]/[product]/page.tsx
export default function Product({
  params,
}: {
  params: { category: string; product: string }
}) {
  return (
    <div>
      <h1>Category: {params.category}</h1>
      <h2>Product: {params.product}</h2>
    </div>
  )
}
```

### Example: Catch-All Routes

```typescript
// app/docs/[...slug]/page.tsx
export default function Docs({ params }: { params: { slug: string[] } }) {
  return <h1>Docs: {params.slug.join('/')}</h1>
}
// Matches: /docs/a, /docs/a/b, /docs/a/b/c, etc.
```

### Example: Optional Catch-All

```typescript
// app/shop/[[...slug]]/page.tsx
export default function Shop({ params }: { params: { slug?: string[] } }) {
  if (!params.slug) {
    return <h1>Shop Home</h1>
  }
  return <h1>Shop: {params.slug.join('/')}</h1>
}
// Matches: /shop, /shop/a, /shop/a/b, etc.
```

### Example: Generating Static Params

```typescript
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await getPosts()
  return posts.map((post) => ({
    slug: post.slug,
  }))
}

export default function BlogPost({ params }: { params: { slug: string } }) {
  return <h1>{params.slug}</h1>
}
```

### Key Points

- Use brackets [param] for dynamic segments
- Access params via params prop
- Catch-all routes use [...slug]
- Optional catch-all uses [[...slug]]
- Use generateStaticParams for static generation
