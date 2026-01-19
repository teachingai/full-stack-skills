# Installation

## Instructions

This example demonstrates how to install and set up Next.js.

### Key Concepts

- Installing Next.js
- Creating a new project
- Project setup options
- Requirements

### Example: Create Next.js Project

```bash
# Create a new Next.js app
npx create-next-app@latest my-app

# With TypeScript
npx create-next-app@latest my-app --typescript

# With specific options
npx create-next-app@latest my-app --typescript --tailwind --app
```

### Example: Manual Installation

```bash
# Install dependencies
npm install next react react-dom

# Or with yarn
yarn add next react react-dom

# Or with pnpm
pnpm add next react react-dom
```

### Example: Package.json Scripts

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
```

### Example: Basic Setup

```javascript
// pages/_app.js (Pages Router)
export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

```typescript
// app/layout.tsx (App Router)
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

### Key Points

- Use `create-next-app` for quick setup
- Next.js requires React and React DOM
- Choose between App Router and Pages Router
- TypeScript support is built-in
- Configure scripts in package.json
