# Fonts

## Instructions

This example demonstrates font optimization in Next.js.

### Key Concepts

- next/font
- Font optimization
- Google Fonts
- Local fonts
- Font display

### Example: Google Fonts

```typescript
// app/layout.tsx
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({ children }) {
  return (
    <html className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

### Example: Local Fonts

```typescript
// app/layout.tsx
import localFont from 'next/font/local'

const myFont = localFont({
  src: './fonts/my-font.woff2',
  display: 'swap',
})

export default function RootLayout({ children }) {
  return (
    <html className={myFont.className}>
      <body>{children}</body>
    </html>
  )
}
```

### Example: Multiple Fonts

```typescript
import { Inter, Roboto } from 'next/font/google'

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' })
const roboto = Roboto({ 
  weight: ['400', '700'],
  subsets: ['latin'],
  variable: '--font-roboto'
})

export default function RootLayout({ children }) {
  return (
    <html className={`${inter.variable} ${roboto.variable}`}>
      <body>{children}</body>
    </html>
  )
}
```

### Example: Font with CSS Variables

```typescript
const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
})

// Use in CSS
// .text {
//   font-family: var(--font-inter);
// }
```

### Key Points

- Use next/font for automatic optimization
- Fonts are self-hosted automatically
- Reduces layout shift
- Improves performance
- Supports Google Fonts and local fonts
