---
name: nextjs
description: Provides comprehensive guidance for Next.js framework including App Router, Pages Router, routing, data fetching, server components, API routes, middleware, image optimization, and deployment. Use when the user asks about Next.js, needs to create Next.js applications, implement SSR or SSG, set up API routes, or optimize Next.js performance.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create a new Next.js project or configure an existing one
- Set up routing with App Router or Pages Router
- Implement data fetching (SSR, SSG, ISR)
- Create API routes
- Use middleware for request handling
- Optimize Next.js applications
- Configure Next.js for production
- Use Next.js with TypeScript
- Implement authentication and authorization
- Handle images and static assets
- Set up environment variables
- Use Next.js with databases
- Implement server actions
- Use React Server Components
- Configure deployment
- Understand Next.js architecture and rendering strategies

## How to use this skill

This skill is organized to match the Next.js official documentation structure (https://nextjs.org/docs). When working with Next.js:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/`
   - App Router/应用路由 → `examples/app-router/`
   - Pages Router/页面路由 → `examples/pages-router/`
   - Routing/路由 → `examples/routing/`
   - Data fetching/数据获取 → `examples/data-fetching/`
   - Rendering/渲染 → `examples/rendering/`
   - API routes/API 路由 → `examples/api-routes/`
   - Middleware/中间件 → `examples/middleware.md`
   - Images/图片 → `examples/images.md`
   - Fonts/字体 → `examples/fonts.md`
   - Styling/样式 → `examples/styling/`
   - Optimization/优化 → `examples/optimization/`
   - Deployment/部署 → `examples/deployment.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始)**:
   - `examples/getting-started/installation.md` - Installing and setting up Next.js
   - `examples/getting-started/project-structure.md` - Next.js project structure
   - `examples/getting-started/layouts-and-pages.md` - Creating layouts and pages
   - `examples/getting-started/routing.md` - Understanding routing in Next.js

   **App Router (应用路由)**:
   - `examples/app-router/overview.md` - App Router overview and concepts
   - `examples/app-router/layouts.md` - Creating and using layouts
   - `examples/app-router/pages.md` - Creating pages
   - `examples/app-router/loading.md` - Loading UI and Suspense
   - `examples/app-router/error-handling.md` - Error handling and error boundaries
   - `examples/app-router/not-found.md` - Not found pages
   - `examples/app-router/route-groups.md` - Route groups and organization
   - `examples/app-router/dynamic-routes.md` - Dynamic route segments
   - `examples/app-router/parallel-routes.md` - Parallel routes
   - `examples/app-router/intercepting-routes.md` - Intercepting routes
   - `examples/app-router/route-handlers.md` - Route handlers (API routes)
   - `examples/app-router/server-components.md` - React Server Components
   - `examples/app-router/client-components.md` - Client Components
   - `examples/app-router/data-fetching.md` - Data fetching in App Router
   - `examples/app-router/caching.md` - Caching and revalidation
   - `examples/app-router/server-actions.md` - Server Actions

   **Pages Router (页面路由)**:
   - `examples/pages-router/overview.md` - Pages Router overview
   - `examples/pages-router/pages.md` - Creating pages
   - `examples/pages-router/dynamic-routes.md` - Dynamic routes
   - `examples/pages-router/api-routes.md` - API routes
   - `examples/pages-router/data-fetching.md` - Data fetching methods
   - `examples/pages-router/static-generation.md` - Static Site Generation (SSG)
   - `examples/pages-router/server-side-rendering.md` - Server-Side Rendering (SSR)
   - `examples/pages-router/incremental-static-regeneration.md` - ISR

   **Core Features (核心功能)**:
   - `examples/middleware.md` - Middleware for request handling
   - `examples/images.md` - Image optimization with next/image
   - `examples/fonts.md` - Font optimization
   - `examples/styling/css-modules.md` - CSS Modules
   - `examples/styling/tailwind-css.md` - Tailwind CSS
   - `examples/styling/sass.md` - Sass/SCSS
   - `examples/styling/styled-components.md` - Styled Components
   - `examples/optimization/code-splitting.md` - Code splitting
   - `examples/optimization/bundle-analyzer.md` - Bundle analysis

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Next.js supports both App Router (recommended) and Pages Router
   - App Router uses React Server Components by default
   - Examples include both JavaScript and TypeScript versions
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/app-router/` - App Router API reference
   - `api/pages-router/` - Pages Router API reference
   - `api/next-config.md` - Next.js configuration API
   - `api/cli.md` - Next.js CLI commands

5. **Use templates** from the `templates/` directory:
   - `templates/next-config.md` - Next.js configuration templates
   - `templates/project-structure.md` - Project structure templates

### 1. Understanding Next.js

Next.js is a React framework for building full-stack web applications. It provides features like server-side rendering, static site generation, API routes, and automatic code splitting.

**Key Concepts**:
- **App Router**: Modern routing system with layouts, server components, and streaming
- **Pages Router**: Traditional file-based routing system
- **Server Components**: React components that run on the server
- **Client Components**: React components that run in the browser
- **Data Fetching**: Multiple strategies (SSR, SSG, ISR, CSR)

### 2. Project Creation

**Using create-next-app**:

```bash
npx create-next-app@latest my-app
```

**With TypeScript**:

```bash
npx create-next-app@latest my-app --typescript
```

**With specific options**:

```bash
npx create-next-app@latest my-app --typescript --tailwind --app
```

### 3. Basic Project Structure

```
my-app/
├── app/              # App Router (if using)
│   ├── layout.tsx
│   ├── page.tsx
│   └── ...
├── pages/            # Pages Router (if using)
│   ├── _app.tsx
│   ├── index.tsx
│   └── ...
├── public/           # Static files
├── next.config.js    # Next.js configuration
└── package.json
```

## Examples and Templates

This skill includes detailed examples organized to match the Next.js official documentation structure (https://nextjs.org/docs). All examples are in the `examples/` directory, organized by topic:

### Getting Started (快速开始) - `examples/getting-started/`

- `examples/getting-started/installation.md` - Installing Next.js and creating a project
- `examples/getting-started/project-structure.md` - Understanding Next.js project structure
- `examples/getting-started/layouts-and-pages.md` - Creating layouts and pages
- `examples/getting-started/routing.md` - Routing fundamentals

### App Router (应用路由) - `examples/app-router/`

- `examples/app-router/overview.md` - App Router overview and core concepts
- `examples/app-router/layouts.md` - Creating nested layouts
- `examples/app-router/pages.md` - Creating pages
- `examples/app-router/loading.md` - Loading states and Suspense
- `examples/app-router/error-handling.md` - Error boundaries and error handling
- `examples/app-router/not-found.md` - Custom 404 pages
- `examples/app-router/route-groups.md` - Organizing routes with groups
- `examples/app-router/dynamic-routes.md` - Dynamic route segments
- `examples/app-router/parallel-routes.md` - Parallel routes and slots
- `examples/app-router/intercepting-routes.md` - Intercepting routes
- `examples/app-router/route-handlers.md` - Route handlers (API routes)
- `examples/app-router/server-components.md` - React Server Components
- `examples/app-router/client-components.md` - Client Components and 'use client'
- `examples/app-router/data-fetching.md` - Data fetching in App Router
- `examples/app-router/caching.md` - Caching, revalidation, and data cache
- `examples/app-router/server-actions.md` - Server Actions for mutations

### Pages Router (页面路由) - `examples/pages-router/`

- `examples/pages-router/overview.md` - Pages Router overview
- `examples/pages-router/pages.md` - Creating pages
- `examples/pages-router/dynamic-routes.md` - Dynamic routes and catch-all routes
- `examples/pages-router/api-routes.md` - API routes
- `examples/pages-router/data-fetching.md` - getServerSideProps, getStaticProps, getStaticPaths
- `examples/pages-router/static-generation.md` - Static Site Generation (SSG)
- `examples/pages-router/server-side-rendering.md` - Server-Side Rendering (SSR)
- `examples/pages-router/incremental-static-regeneration.md` - ISR

### Core Features (核心功能) - `examples/`

- `examples/middleware.md` - Middleware for request/response modification
- `examples/images.md` - Image optimization with next/image
- `examples/fonts.md` - Font optimization
- `examples/styling/css-modules.md` - CSS Modules
- `examples/styling/tailwind-css.md` - Tailwind CSS setup
- `examples/styling/sass.md` - Sass/SCSS support
- `examples/styling/styled-components.md` - Styled Components
- `examples/optimization/code-splitting.md` - Automatic code splitting
- `examples/optimization/bundle-analyzer.md` - Bundle analysis

### Templates Directory (`templates/`)

- `templates/next-config.md` - Next.js configuration templates
- `templates/project-structure.md` - Project structure templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/next-config.md` for Next.js configuration templates
- Use `templates/project-structure.md` for organizing Next.js projects
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Next.js API documentation structure:

### App Router API (`api/app-router/`)
- `api/app-router/file-conventions.md` - File conventions (layout.tsx, page.tsx, loading.tsx, error.tsx, etc.)
- `api/app-router/functions.md` - Functions (cookies, headers, redirect, notFound, etc.)
- `api/app-router/components.md` - Components (Image, Link, Script, etc.)
- `api/app-router/route-handlers.md` - Route handlers API

### Pages Router API (`api/pages-router/`)
- `api/pages-router/file-conventions.md` - File conventions (_app.tsx, _document.tsx, etc.)
- `api/pages-router/functions.md` - Data fetching functions (getServerSideProps, getStaticProps, getStaticPaths)
- `api/pages-router/api-routes.md` - API routes handler

### Configuration API (`api/`)
- `api/next-config.md` - next.config.js options
- `api/cli.md` - Next.js CLI commands (dev, build, start, export, etc.)

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use App Router for new projects**: App Router is the recommended approach
2. **Use Server Components by default**: Only use Client Components when needed
3. **Optimize images**: Always use next/image for image optimization
4. **Code splitting**: Leverage automatic code splitting
5. **Data fetching**: Choose appropriate strategy (SSR, SSG, ISR) based on use case
6. **Environment variables**: Use proper environment variable naming (NEXT_PUBLIC_)
7. **TypeScript**: Use TypeScript for better type safety

## Resources

- **Official Documentation**: https://nextjs.org/docs
- **App Router**: https://nextjs.org/docs/app
- **Pages Router**: https://nextjs.org/docs/pages
- **API Reference**: https://nextjs.org/docs/app/api-reference
- **Learn Next.js**: https://nextjs.org/learn

## Keywords

Next.js, React framework, App Router, Pages Router, Server Components, Client Components, SSR, SSG, ISR, static generation, server-side rendering, incremental static regeneration, API routes, middleware, next/image, routing, layouts, pages, data fetching, server actions, 全栈框架, 应用路由, 页面路由, 服务器组件, 客户端组件, 服务端渲染, 静态生成, 增量静态再生, API 路由, 中间件, 路由, 布局, 页面, 数据获取
