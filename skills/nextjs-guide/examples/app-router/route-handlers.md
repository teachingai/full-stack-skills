# Route Handlers

## Instructions

This example demonstrates route handlers (API routes) in App Router.

### Key Concepts

- Route handlers
- HTTP methods
- Request/Response
- API routes

### Example: Basic Route Handler

```typescript
// app/api/hello/route.ts
export async function GET() {
  return Response.json({ message: 'Hello' })
}
```

### Example: Multiple HTTP Methods

```typescript
// app/api/users/route.ts
export async function GET() {
  const users = await getUsers()
  return Response.json(users)
}

export async function POST(request: Request) {
  const body = await request.json()
  const user = await createUser(body)
  return Response.json(user, { status: 201 })
}
```

### Example: Route Handler with Params

```typescript
// app/api/users/[id]/route.ts
export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  const user = await getUser(params.id)
  if (!user) {
    return Response.json({ error: 'Not found' }, { status: 404 })
  }
  return Response.json(user)
}
```

### Example: Route Handler with Query

```typescript
// app/api/search/route.ts
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url)
  const query = searchParams.get('q')
  
  const results = await search(query)
  return Response.json(results)
}
```

### Example: Route Handler with Headers

```typescript
// app/api/data/route.ts
export async function GET(request: Request) {
  const authHeader = request.headers.get('authorization')
  
  if (!authHeader) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }
  
  const data = await getData(authHeader)
  return Response.json(data)
}
```

### Key Points

- Route handlers are API endpoints
- Export functions named after HTTP methods
- Use Request and Response objects
- Can access route params and query strings
- File path determines API route URL
