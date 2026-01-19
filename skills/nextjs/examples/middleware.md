# Middleware

## Instructions

This example demonstrates middleware in Next.js.

### Key Concepts

- Middleware function
- Request modification
- Response modification
- Route matching

### Example: Basic Middleware

```typescript
// middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  return NextResponse.next()
}
```

### Example: Middleware with Redirect

```typescript
// middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  if (request.nextUrl.pathname === '/old') {
    return NextResponse.redirect(new URL('/new', request.url))
  }
}
```

### Example: Middleware with Authentication

```typescript
// middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token')
  
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url))
  }
  
  return NextResponse.next()
}

export const config = {
  matcher: '/dashboard/:path*'
}
```

### Example: Middleware with Headers

```typescript
// middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const response = NextResponse.next()
  response.headers.set('x-custom-header', 'value')
  return response
}
```

### Key Points

- Middleware runs before request completes
- Can modify request and response
- Use config.matcher to specify routes
- Runs on edge runtime
- Useful for authentication, redirects, headers
