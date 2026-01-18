# Project Structure

## Instructions

This example demonstrates Next.js project structure and file conventions.

### Key Concepts

- App Router structure
- Pages Router structure
- File conventions
- Special files

### Example: App Router Structure

```
my-app/
├── app/
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Home page
│   ├── loading.tsx         # Loading UI
│   ├── error.tsx           # Error UI
│   ├── not-found.tsx       # 404 page
│   ├── (group)/            # Route group
│   │   └── page.tsx
│   ├── [slug]/             # Dynamic route
│   │   └── page.tsx
│   └── api/                # API routes
│       └── route.ts
├── public/                 # Static files
├── next.config.js          # Next.js config
└── package.json
```

### Example: Pages Router Structure

```
my-app/
├── pages/
│   ├── _app.tsx            # Custom App
│   ├── _document.tsx       # Custom Document
│   ├── index.tsx           # Home page
│   ├── about.tsx           # About page
│   ├── [id].tsx            # Dynamic route
│   └── api/                # API routes
│       └── hello.js
├── public/                 # Static files
├── next.config.js
└── package.json
```

### Example: Special Files (App Router)

```typescript
// app/layout.tsx - Root layout
export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  )
}

// app/page.tsx - Home page
export default function Home() {
  return <h1>Home</h1>
}

// app/loading.tsx - Loading UI
export default function Loading() {
  return <div>Loading...</div>
}

// app/error.tsx - Error boundary
'use client'
export default function Error({ error, reset }) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={reset}>Try again</button>
    </div>
  )
}

// app/not-found.tsx - 404 page
export default function NotFound() {
  return <h1>Not Found</h1>
}
```

### Key Points

- App Router uses `app/` directory
- Pages Router uses `pages/` directory
- Special files have specific names (layout.tsx, page.tsx, etc.)
- File-based routing determines URL structure
- `public/` contains static assets
