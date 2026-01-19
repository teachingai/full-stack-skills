# Incremental Static Regeneration

## Instructions

This example demonstrates ISR in Pages Router.

### Key Concepts

- Incremental Static Regeneration
- Revalidation
- On-demand revalidation
- Stale-while-revalidate

### Example: ISR with Revalidate

```typescript
// pages/products.tsx
export default function Products({ products }) {
  return (
    <div>
      {products.map(product => (
        <div key={product.id}>{product.name}</div>
      ))}
    </div>
  )
}

export async function getStaticProps() {
  const products = await getProducts()
  return {
    props: {
      products
    },
    revalidate: 3600  // Revalidate every hour
  }
}
```

### Example: On-Demand Revalidation

```typescript
// pages/api/revalidate.ts
export default async function handler(req, res) {
  if (req.query.secret !== process.env.REVALIDATE_SECRET) {
    return res.status(401).json({ message: 'Invalid token' })
  }
  
  try {
    await res.revalidate('/products')
    return res.json({ revalidated: true })
  } catch (err) {
    return res.status(500).send('Error revalidating')
  }
}
```

### Example: ISR with Fallback

```typescript
export async function getStaticPaths() {
  return {
    paths: [],
    fallback: 'blocking'
  }
}

export async function getStaticProps({ params }) {
  const post = await getPost(params.slug)
  return {
    props: {
      post
    },
    revalidate: 60
  }
}
```

### Key Points

- Pages are statically generated
- Revalidated at specified interval
- Use revalidate option
- On-demand revalidation via API
- Combines benefits of SSG and SSR
