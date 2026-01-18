# Images

## Instructions

This example demonstrates image optimization with next/image.

### Key Concepts

- next/image component
- Image optimization
- Responsive images
- Image loading

### Example: Basic Image

```typescript
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/hero.jpg"
      alt="Hero image"
      width={800}
      height={600}
    />
  )
}
```

### Example: Responsive Image

```typescript
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/hero.jpg"
      alt="Hero"
      width={800}
      height={600}
      sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      style={{ width: '100%', height: 'auto' }}
    />
  )
}
```

### Example: External Image

```typescript
// next.config.js
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
      },
    ],
  },
}

// Component
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="https://example.com/image.jpg"
      alt="External image"
      width={800}
      height={600}
    />
  )
}
```

### Example: Image with Priority

```typescript
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/hero.jpg"
      alt="Hero"
      width={800}
      height={600}
      priority
    />
  )
}
```

### Key Points

- Use next/image for automatic optimization
- Always specify width and height
- Use sizes for responsive images
- Configure remotePatterns for external images
- Use priority for above-the-fold images
