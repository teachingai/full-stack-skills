# Dynamic Routes

## Instructions

This example demonstrates dynamic routes in Pages Router.

### Key Concepts

- Dynamic routes
- Catch-all routes
- Optional catch-all
- getStaticPaths

### Example: Single Dynamic Route

```typescript
// pages/blog/[slug].tsx
export default function BlogPost({ post }) {
  return <article>{post.title}</article>
}

export async function getStaticPaths() {
  const posts = await getPosts()
  return {
    paths: posts.map(post => ({
      params: { slug: post.slug }
    })),
    fallback: false
  }
}

export async function getStaticProps({ params }) {
  const post = await getPost(params.slug)
  return {
    props: {
      post
    }
  }
}
```

### Example: Multiple Dynamic Segments

```typescript
// pages/shop/[category]/[product].tsx
export default function Product({ product }) {
  return <h1>{product.name}</h1>
}

export async function getStaticPaths() {
  return {
    paths: [
      { params: { category: 'electronics', product: 'laptop' } },
      { params: { category: 'books', product: 'novel' } }
    ],
    fallback: false
  }
}
```

### Example: Catch-All Routes

```typescript
// pages/docs/[...slug].tsx
export default function Docs({ page }) {
  return <div>{page.content}</div>
}

export async function getStaticPaths() {
  return {
    paths: [
      { params: { slug: ['getting-started'] } },
      { params: { slug: ['api', 'reference'] } }
    ],
    fallback: false
  }
}
```

### Example: Optional Catch-All

```typescript
// pages/shop/[[...slug]].tsx
export default function Shop({ products }) {
  return (
    <div>
      {products.map(product => (
        <div key={product.id}>{product.name}</div>
      ))}
    </div>
  )
}

export async function getStaticPaths() {
  return {
    paths: [
      { params: { slug: [] } },
      { params: { slug: ['electronics'] } }
    ],
    fallback: false
  }
}
```

### Key Points

- Use brackets [param] for dynamic segments
- Catch-all uses [...slug]
- Optional catch-all uses [[...slug]]
- Use getStaticPaths for SSG
- Access params in getStaticProps/getServerSideProps
