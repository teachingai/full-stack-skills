---
name: vue-router-v3
description: Vue Router v3 完整使用指南，基于官方文档（https://v3.router.vuejs.org/），涵盖路由配置、导航、嵌套路由、路由守卫、动态路由匹配、命名视图、重定向和别名等核心概念和最佳实践。适用于使用 Vue Router v3（适配 Vue 2）开发单页面应用的场景。
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Vue Router v3 in a Vue 2 application
- Configure routes and navigation
- Implement nested routes
- Use dynamic route matching
- Set up navigation guards
- Handle route parameters and query strings
- Implement programmatic navigation
- Use named views and multiple router views
- Configure redirects and aliases
- Set up history mode or hash mode
- Customize scroll behavior
- Pass props to route components
- Handle lazy loading and code splitting
- Work with route meta fields
- Implement route transitions
- Troubleshoot Vue Router v3 issues

## How to use this skill

This skill is organized to match the Vue Router v3 official documentation structure (https://v3.router.vuejs.org/installation.html, https://v3.router.vuejs.org/guide/, https://v3.router.vuejs.org/api/). When working with Vue Router v3:

1. **Identify the topic** from the user's request:
   - Installation/安装 → `examples/installation.md`
   - Getting started/快速开始 → `examples/getting-started.md`
   - Dynamic route matching/动态路由匹配 → `examples/dynamic-route-matching.md`
   - Nested routes/嵌套路由 → `examples/nested-routes.md`
   - Navigation/导航 → `examples/navigation.md`
   - Programmatic navigation/编程式导航 → `examples/programmatic-navigation.md`
   - Route params and query/路由参数和查询 → `examples/route-params-and-query.md`
   - Navigation guards/导航守卫 → `examples/navigation-guards.md`
   - Named views/命名视图 → `examples/named-views.md`
   - Redirects and aliases/重定向和别名 → `examples/redirects-and-aliases.md`
   - History mode/History 模式 → `examples/history-mode.md`
   - Scroll behavior/滚动行为 → `examples/scroll-behavior.md`
   - Route props/路由 Props → `examples/route-props.md`
   - Lazy loading/懒加载 → `examples/lazy-loading.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始)**:
   - `examples/installation.md` - Installing Vue Router v3
   - `examples/getting-started.md` - Basic setup and configuration

   **Essentials (基础)**:
   - `examples/dynamic-route-matching.md` - Dynamic route matching with parameters
   - `examples/nested-routes.md` - Nested routes and router-view
   - `examples/navigation.md` - Using router-link for navigation
   - `examples/programmatic-navigation.md` - Programmatic navigation with router methods

   **Advanced (高级)**:
   - `examples/route-params-and-query.md` - Route parameters and query strings
   - `examples/navigation-guards.md` - Navigation guards (global, per-route, in-component)
   - `examples/named-views.md` - Named views and multiple router views
   - `examples/redirects-and-aliases.md` - Redirects and aliases
   - `examples/history-mode.md` - History mode vs hash mode
   - `examples/scroll-behavior.md` - Custom scroll behavior
   - `examples/route-props.md` - Passing props to route components
   - `examples/lazy-loading.md` - Lazy loading routes

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Vue Router v3 is for Vue 2 applications
   - Vue 3 applications should use Vue Router v4
   - All examples follow Vue 2 Options API syntax
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/router-instance.md` - Router instance properties and methods
   - `api/route-object.md` - Route object properties
   - `api/router-link.md` - RouterLink component API
   - `api/router-view.md` - RouterView component API
   - `api/route-config.md` - Route configuration options
   - `api/navigation-guards.md` - Navigation guards API
   - `api/router-options.md` - Router constructor options

5. **Use templates** from the `templates/` directory:
   - `templates/router-config.md` - Router configuration templates
   - `templates/route-config.md` - Route configuration templates

### 1. Understanding Vue Router v3

Vue Router is the official router for Vue.js. It deeply integrates with Vue.js core to make building Single Page Applications with Vue.js a breeze.

**Key Concepts**:
- **SPA Routing**: Client-side routing for single-page applications
- **Route Matching**: Maps URLs to components
- **Navigation**: Declarative and programmatic navigation
- **Nested Routes**: Hierarchical route structures
- **Navigation Guards**: Control navigation flow

### 2. Installation

**Using npm**:

```bash
npm install vue-router@3
```

**Using yarn**:

```bash
yarn add vue-router@3
```

**Using CDN**:

```html
<script src="https://unpkg.com/vue-router@3/dist/vue-router.js"></script>
```

### 3. Basic Setup

```javascript
// router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import About from '@/views/About.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
]

const router = new VueRouter({
  routes
})

export default router
```

```javascript
// main.js
import Vue from 'vue'
import App from './App.vue'
import router from './router'

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

## Examples and Templates

This skill includes detailed examples organized to match the Vue Router v3 official documentation structure (https://v3.router.vuejs.org/guide/). All examples are in the `examples/` directory, organized by topic:

### Getting Started (快速开始) - `examples/`

- `examples/installation.md` - Installing Vue Router v3 via npm, yarn, or CDN
- `examples/getting-started.md` - Basic router setup, route configuration, and router-link/router-view usage

### Essentials (基础) - `examples/`

- `examples/dynamic-route-matching.md` - Dynamic route matching with parameters, catch-all routes, and regex
- `examples/nested-routes.md` - Nested routes, child routes, and nested router-view
- `examples/navigation.md` - Using router-link component, active classes, and exact matching
- `examples/programmatic-navigation.md` - Programmatic navigation with router.push(), router.replace(), router.go()

### Advanced (高级) - `examples/`

- `examples/route-params-and-query.md` - Route parameters ($route.params) and query strings ($route.query)
- `examples/navigation-guards.md` - Global guards, per-route guards, and component guards
- `examples/named-views.md` - Named views and multiple router-view components
- `examples/redirects-and-aliases.md` - Redirects and route aliases
- `examples/history-mode.md` - History mode vs hash mode configuration
- `examples/scroll-behavior.md` - Custom scroll behavior on route changes
- `examples/route-props.md` - Passing props to route components
- `examples/lazy-loading.md` - Lazy loading routes and code splitting

### Templates Directory (`templates/`)

- `templates/router-config.md` - Router configuration templates for different scenarios
- `templates/route-config.md` - Route configuration templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/router-config.md` for router configuration templates
- Use `templates/route-config.md` for route configuration templates
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Vue Router v3 API documentation structure:

### Router Instance (`api/router-instance.md`)
- Router instance properties: `mode`, `currentRoute`, `options`
- Router instance methods: `push()`, `replace()`, `go()`, `back()`, `forward()`, `onReady()`, `onError()`, `addRoutes()`, `resolve()`

### Route Object (`api/route-object.md`)
- Route object properties: `path`, `params`, `query`, `hash`, `fullPath`, `matched`, `name`, `redirectedFrom`

### Components (`api/`)
- `api/router-link.md` - RouterLink component props and usage
- `api/router-view.md` - RouterView component props and usage

### Configuration (`api/`)
- `api/route-config.md` - Route configuration options (path, component, name, children, redirect, alias, props, meta, etc.)
- `api/router-options.md` - Router constructor options (mode, base, linkActiveClass, scrollBehavior, etc.)
- `api/navigation-guards.md` - Navigation guards API (beforeEach, beforeResolve, afterEach, beforeRouteEnter, etc.)

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use history mode for production**: Configure server for history mode fallback
2. **Lazy load routes**: Use dynamic imports for code splitting
3. **Use route meta fields**: Store route-specific metadata
4. **Implement navigation guards**: Control access and handle navigation logic
5. **Use named routes**: Reference routes by name instead of paths
6. **Pass props to routes**: Use route props instead of accessing $route directly
7. **Handle scroll behavior**: Configure scroll behavior for better UX

## Resources

- **Official Documentation**: https://v3.router.vuejs.org/
- **Installation Guide**: https://v3.router.vuejs.org/installation.html
- **Guide**: https://v3.router.vuejs.org/guide/
- **API Reference**: https://v3.router.vuejs.org/api/
- **GitHub Repository**: https://github.com/vuejs/vue-router/tree/v3

## Keywords

Vue Router, vue-router, Vue Router v3, routing, SPA, single page application, router-link, router-view, navigation, nested routes, dynamic routes, route params, query strings, navigation guards, route guards, history mode, hash mode, redirect, alias, named views, lazy loading, code splitting, 路由, 单页面应用, 导航, 嵌套路由, 动态路由, 路由参数, 查询字符串, 导航守卫, 历史模式, 哈希模式, 重定向, 别名, 命名视图, 懒加载, 代码分割
