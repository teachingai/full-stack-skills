# Layouts and Pages

## Instructions

This example demonstrates creating layouts and pages in Next.js.

### Key Concepts

- Layouts in App Router
- Pages in App Router
- Nested layouts
- Shared layouts

### Example: Basic Layout (App Router)

```typescript
// app/layout.tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

### Example: Nested Layout

```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div>
      <nav>Dashboard Nav</nav>
      {children}
    </div>
  )
}
```

### Example: Page (App Router)

```typescript
// app/page.tsx
export default function Home() {
  return <h1>Home Page</h1>
}

// app/about/page.tsx
export default function About() {
  return <h1>About Page</h1>
}
```

### Example: Pages Router

```typescript
// pages/index.tsx
export default function Home() {
  return <h1>Home</h1>
}

// pages/_app.tsx
export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

### Example: Layout with Metadata

```typescript
// app/layout.tsx
export const metadata = {
  title: 'My App',
  description: 'My app description',
}

export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  )
}
```

### Key Points

- Layouts wrap pages and other layouts
- Layouts are shared across routes
- Pages are route segments
- App Router uses layout.tsx and page.tsx
- Pages Router uses _app.tsx for shared layout
