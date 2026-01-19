# Server-Side Rendering

## Instructions

This example demonstrates Server-Side Rendering (SSR) in Pages Router.

### Key Concepts

- Server-side rendering
- getServerSideProps
- Request-time rendering
- Dynamic content

### Example: Basic SSR

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

### Example: SSR with Redirect

```typescript
export async function getServerSideProps(context) {
  const user = await getUser(context.req)
  
  if (!user) {
    return {
      redirect: {
        destination: '/login',
        permanent: false
      }
    }
  }
  
  return {
    props: {
      user
    }
  }
}
```

### Example: SSR with Not Found

```typescript
export async function getServerSideProps(context) {
  const post = await getPost(context.params.id)
  
  if (!post) {
    return {
      notFound: true
    }
  }
  
  return {
    props: {
      post
    }
  }
}
```

### Key Points

- Pages are rendered on each request
- Use getServerSideProps for data fetching
- Access to request object
- Can redirect or return notFound
- Good for dynamic content
