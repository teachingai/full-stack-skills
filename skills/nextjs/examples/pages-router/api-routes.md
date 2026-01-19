# API Routes

## Instructions

This example demonstrates API routes in Pages Router.

### Key Concepts

- API route handlers
- Request/Response
- HTTP methods
- Middleware

### Example: Basic API Route

```typescript
// pages/api/hello.ts
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  res.status(200).json({ message: 'Hello' })
}
```

### Example: API Route with Methods

```typescript
// pages/api/users.ts
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === 'GET') {
    res.status(200).json({ users: [] })
  } else if (req.method === 'POST') {
    res.status(201).json({ message: 'Created' })
  } else {
    res.setHeader('Allow', ['GET', 'POST'])
    res.status(405).end(`Method ${req.method} Not Allowed`)
  }
}
```

### Example: API Route with Dynamic Route

```typescript
// pages/api/users/[id].ts
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { id } = req.query
  
  if (req.method === 'GET') {
    const user = await getUser(id)
    res.status(200).json(user)
  }
}
```

### Key Points

- API routes are in pages/api/
- Handler receives req and res
- Check req.method for HTTP method
- Access params via req.query
- Return JSON with res.json()
