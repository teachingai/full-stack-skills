# Pages

## Instructions

This example demonstrates creating pages in Pages Router.

### Key Concepts

- Page components
- Page exports
- getStaticProps
- getServerSideProps

### Example: Basic Page

```typescript
// pages/index.tsx
export default function Home() {
  return <h1>Home</h1>
}
```

### Example: Page with Static Props

```typescript
// pages/about.tsx
export default function About({ title }) {
  return <h1>{title}</h1>
}

export async function getStaticProps() {
  return {
    props: {
      title: 'About Us'
    }
  }
}
```

### Example: Page with Server-Side Props

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

### Key Points

- Pages are React components
- Export default component
- Use getStaticProps for SSG
- Use getServerSideProps for SSR
- File path determines route URL
