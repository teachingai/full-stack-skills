# Data Fetching

## Instructions

This example demonstrates data fetching in Pages Router.

### Key Concepts

- getStaticProps
- getServerSideProps
- getStaticPaths
- Client-side fetching

### Example: getStaticProps

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

### Example: getServerSideProps

```typescript
// pages/profile.tsx
export default function Profile({ user }) {
  return <h1>{user.name}</h1>
}

export async function getServerSideProps(context) {
  const user = await getUser(context.req)
  return {
    props: {
      user
    }
  }
}
```

### Example: getStaticPaths

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

### Example: ISR with Revalidate

```typescript
export async function getStaticProps() {
  const data = await fetchData()
  return {
    props: { data },
    revalidate: 3600  // Revalidate every hour
  }
}
```

### Key Points

- getStaticProps for SSG
- getServerSideProps for SSR
- getStaticPaths for dynamic SSG
- Use revalidate for ISR
- Client-side fetching with useEffect
