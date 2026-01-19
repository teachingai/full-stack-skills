# Pages Router Overview

## Instructions

This example provides an overview of the Pages Router in Next.js.

### Key Concepts

- Pages Router architecture
- File-based routing
- getServerSideProps
- getStaticProps
- getStaticPaths

### Example: Pages Router Structure

```
pages/
├── _app.tsx           # Custom App
├── _document.tsx      # Custom Document
├── index.tsx          # Home page (/)
├── about.tsx          # /about
├── blog/
│   └── [slug].tsx    # /blog/:slug
└── api/
    └── hello.ts      # /api/hello
```

### Example: Basic Page

```typescript
// pages/index.tsx
export default function Home() {
  return <h1>Home</h1>
}
```

### Example: Page with getStaticProps

```typescript
// pages/about.tsx
export default function About({ data }) {
  return <h1>{data.title}</h1>
}

export async function getStaticProps() {
  return {
    props: {
      data: { title: 'About' }
    }
  }
}
```

### Example: Page with getServerSideProps

```typescript
// pages/user/[id].tsx
export default function User({ user }) {
  return <h1>{user.name}</h1>
}

export async function getServerSideProps({ params }) {
  const user = await getUser(params.id)
  return {
    props: {
      user
    }
  }
}
```

### Key Points

- Pages Router uses pages/ directory
- File-based routing determines URLs
- Use getStaticProps for SSG
- Use getServerSideProps for SSR
- Use getStaticPaths for dynamic SSG
