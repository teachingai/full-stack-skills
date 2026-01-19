# Static Site Generation

## Instructions

This example demonstrates Static Site Generation (SSG) in Pages Router.

### Key Concepts

- Static generation
- getStaticProps
- Pre-rendering
- Build time generation

### Example: Basic SSG

```typescript
// pages/about.tsx
export default function About({ data }) {
  return <h1>{data.title}</h1>
}

export async function getStaticProps() {
  const data = await fetchData()
  return {
    props: {
      data
    }
  }
}
```

### Example: SSG with Dynamic Routes

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

### Example: SSG with Fallback

```typescript
export async function getStaticPaths() {
  return {
    paths: [],
    fallback: 'blocking'  // or true
  }
}
```

### Key Points

- Pages are generated at build time
- Use getStaticProps for data fetching
- Use getStaticPaths for dynamic routes
- Fastest rendering option
- Good for static content
