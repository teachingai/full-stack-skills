# Route Groups

## Instructions

This example demonstrates route groups in App Router.

### Key Concepts

- Route groups
- Organizing routes
- Layouts per group
- URL structure

### Example: Basic Route Group

```typescript
// app/(marketing)/about/page.tsx → /about
export default function About() {
  return <h1>About</h1>
}

// app/(marketing)/contact/page.tsx → /contact
export default function Contact() {
  return <h1>Contact</h1>
}

// app/(shop)/products/page.tsx → /products
export default function Products() {
  return <h1>Products</h1>
}
```

### Example: Route Group with Layout

```typescript
// app/(marketing)/layout.tsx
export default function MarketingLayout({ children }) {
  return (
    <div>
      <nav>Marketing Nav</nav>
      {children}
    </div>
  )
}

// app/(shop)/layout.tsx
export default function ShopLayout({ children }) {
  return (
    <div>
      <nav>Shop Nav</nav>
      {children}
    </div>
  )
}
```

### Example: Multiple Route Groups

```
app/
├── (marketing)/
│   ├── layout.tsx
│   ├── about/
│   └── contact/
├── (shop)/
│   ├── layout.tsx
│   └── products/
└── (auth)/
    ├── layout.tsx
    ├── login/
    └── register/
```

### Key Points

- Route groups use parentheses (group)
- Groups don't affect URL structure
- Useful for organizing routes
- Can have separate layouts per group
- Helps organize large applications
