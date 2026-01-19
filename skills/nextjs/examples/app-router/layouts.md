# Layouts

## Instructions

This example demonstrates creating and using layouts in App Router.

### Key Concepts

- Root layout
- Nested layouts
- Layout hierarchy
- Shared UI

### Example: Root Layout

```typescript
// app/layout.tsx
export const metadata = {
  title: 'My App',
  description: 'My app description',
}

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
      <nav>
        <a href="/dashboard">Dashboard</a>
        <a href="/dashboard/settings">Settings</a>
      </nav>
      <main>{children}</main>
    </div>
  )
}
```

### Example: Layout with Client Component

```typescript
// app/layout.tsx
import Navigation from './components/Navigation'

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <Navigation />
        {children}
      </body>
    </html>
  )
}

// app/components/Navigation.tsx
'use client'

export default function Navigation() {
  return <nav>Navigation</nav>
}
```

### Example: Multiple Layouts

```typescript
// app/layout.tsx - Root layout
// app/(auth)/layout.tsx - Auth layout
// app/(auth)/login/page.tsx - Uses both layouts
```

### Key Points

- Layouts wrap pages and child layouts
- Layouts are shared across routes
- Root layout must include <html> and <body>
- Layouts can contain Client Components
- Nested layouts create layout hierarchy
