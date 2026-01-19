# Server Actions

## Instructions

This example demonstrates Server Actions in App Router.

### Key Concepts

- Server Actions
- Form actions
- Mutations
- Progressive enhancement

### Example: Basic Server Action

```typescript
// app/actions.ts
'use server'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  await savePost(title)
  revalidatePath('/posts')
}
```

### Example: Server Action in Component

```typescript
// app/components/CreatePost.tsx
import { createPost } from './actions'

export default function CreatePost() {
  return (
    <form action={createPost}>
      <input name="title" />
      <button type="submit">Create</button>
    </form>
  )
}
```

### Example: Server Action with useTransition

```typescript
'use client'

import { useTransition } from 'react'
import { createPost } from './actions'

export default function CreatePost() {
  const [isPending, startTransition] = useTransition()
  
  async function handleSubmit(formData: FormData) {
    startTransition(async () => {
      await createPost(formData)
    })
  }
  
  return (
    <form action={handleSubmit}>
      <input name="title" />
      <button disabled={isPending}>Create</button>
    </form>
  )
}
```

### Example: Server Action with Validation

```typescript
'use server'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  
  if (!title || title.length < 3) {
    return { error: 'Title must be at least 3 characters' }
  }
  
  await savePost(title)
  return { success: true }
}
```

### Key Points

- Use 'use server' directive
- Can be used in forms with action prop
- Works with progressive enhancement
- Can use useTransition for pending states
- Automatically handles form data
