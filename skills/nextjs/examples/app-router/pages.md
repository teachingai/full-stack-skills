# Pages

## Instructions

This example demonstrates creating pages in App Router.

### Key Concepts

- Page component
- Page metadata
- Page exports
- Route segments

### Example: Basic Page

```typescript
// app/page.tsx
export default function Home() {
  return <h1>Home Page</h1>
}
```

### Example: Page with Metadata

```typescript
// app/about/page.tsx
export const metadata = {
  title: 'About',
  description: 'About our company',
}

export default function About() {
  return <h1>About</h1>
}
```

### Example: Dynamic Page

```typescript
// app/blog/[slug]/page.tsx
export async function generateMetadata({ params }: { params: { slug: string } }) {
  return {
    title: `Post: ${params.slug}`,
  }
}

export default async function BlogPost({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug)
  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  )
}
```

### Example: Page with Data Fetching

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

### Key Points

- Pages are defined with page.tsx files
- Pages are Server Components by default
- Use generateMetadata for dynamic metadata
- Pages can fetch data directly
- File path determines route URL
