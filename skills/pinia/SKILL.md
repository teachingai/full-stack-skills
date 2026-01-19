---
name: pinia
description: Provides comprehensive guidance for Pinia state management including stores, state, getters, actions, plugins, and TypeScript support. Use when the user asks about Pinia, needs to manage application state, create stores, implement state persistence, or migrate from Vuex.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Pinia state management in Vue 3 applications
- Create stores with defineStore()
- Work with state, getters, and actions
- Use Pinia with Composition API
- Use Pinia with Options API
- Implement SSR (Server-Side Rendering) with Pinia
- Create and use Pinia plugins
- Access stores in components
- Share state between components
- Persist state with plugins
- Test Pinia stores
- Migrate from Vuex to Pinia

## How to use this skill

This skill is organized to match the Pinia official documentation structure (https://pinia.vuejs.org/introduction.html, https://pinia.vuejs.org/api/). When working with Pinia:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/installation.md` or `examples/getting-started/basic-usage.md`
   - Defining a store/定义 Store → `examples/core-concepts/defining-a-store.md`
   - State/状态 → `examples/core-concepts/state.md`
   - Getters/计算属性 → `examples/core-concepts/getters.md`
   - Actions/操作 → `examples/core-concepts/actions.md`
   - Plugins/插件 → `examples/plugins/basics.md`
   - SSR/服务端渲染 → `examples/ssr/setup.md`
   - TypeScript/类型支持 → `examples/core-concepts/typescript.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/installation.md` - Installing Pinia and basic setup
   - `examples/getting-started/basic-usage.md` - Basic store usage in components

   **Core Concepts (核心概念) - `examples/core-concepts/`**:
   - `examples/core-concepts/defining-a-store.md` - Creating stores with defineStore()
   - `examples/core-concepts/state.md` - Working with state
   - `examples/core-concepts/getters.md` - Creating and using getters
   - `examples/core-concepts/actions.md` - Creating and using actions
   - `examples/core-concepts/typescript.md` - TypeScript support
   - `examples/core-concepts/composition-api.md` - Using Pinia with Composition API
   - `examples/core-concepts/options-api.md` - Using Pinia with Options API

   **Plugins (插件) - `examples/plugins/`**:
   - `examples/plugins/basics.md` - Creating and using plugins
   - `examples/plugins/persistence.md` - State persistence plugins

   **SSR (服务端渲染) - `examples/ssr/`**:
   - `examples/ssr/setup.md` - Setting up Pinia for SSR
   - `examples/ssr/hydration.md` - State hydration

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Pinia best practices
   - Examples include both JavaScript and TypeScript versions where applicable
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/defineStore.md` - defineStore() API reference
   - `api/store.md` - Store instance API
   - `api/storeToRefs.md` - storeToRefs() utility
   - `api/createPinia.md` - createPinia() API
   - `api/plugins.md` - Plugin API

5. **Use templates** from the `templates/` directory:
   - `templates/store-setup.md` - Pinia setup templates
   - `templates/store-template.md` - Store template
   - `templates/composition-store.md` - Composition API store template
   - `templates/options-store.md` - Options API store template

## Examples and Templates

This skill includes detailed examples organized to match the Pinia official documentation structure (https://pinia.vuejs.org/introduction.html, https://pinia.vuejs.org/api/). All examples are in the `examples/` directory, organized by topic:

### Getting Started (快速开始) - `examples/getting-started/`

- `examples/getting-started/installation.md` - Installing Pinia, creating a Pinia instance, and registering it with Vue app
- `examples/getting-started/basic-usage.md` - Basic store usage in components, accessing state, getters, and actions

### Core Concepts (核心概念) - `examples/core-concepts/`

- `examples/core-concepts/defining-a-store.md` - Creating stores with defineStore(), store IDs, and store options
- `examples/core-concepts/state.md` - Defining state, accessing state, resetting state, and replacing state
- `examples/core-concepts/getters.md` - Creating getters, accessing other getters, passing arguments to getters, and accessing other stores
- `examples/core-concepts/actions.md` - Creating actions, accessing state and getters, accessing other stores, and async actions
- `examples/core-concepts/typescript.md` - TypeScript support, typed stores, and type inference
- `examples/core-concepts/composition-api.md` - Using Pinia with Composition API (setup script)
- `examples/core-concepts/options-api.md` - Using Pinia with Options API

### Plugins (插件) - `examples/plugins/`

- `examples/plugins/basics.md` - Creating and using plugins, plugin context, and adding properties to stores
- `examples/plugins/persistence.md` - State persistence plugins

### SSR (服务端渲染) - `examples/ssr/`

- `examples/ssr/setup.md` - Setting up Pinia for SSR
- `examples/ssr/hydration.md` - State hydration and preventing state pollution

### Templates Directory (`templates/`)

- `templates/store-setup.md` - Pinia setup templates for different scenarios
- `templates/store-template.md` - Basic store template
- `templates/composition-store.md` - Composition API store template
- `templates/options-store.md` - Options API store template

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/store-setup.md` for Pinia setup
- Use store templates for quick setup
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Pinia API documentation structure:

### defineStore API (`api/defineStore.md`)
- `defineStore()` - Creating a store
- Store options: state, getters, actions
- Store ID and naming

### Store Instance API (`api/store.md`)
- Store properties: `$id`, `$state`, `$patch()`, `$reset()`, `$subscribe()`, `$onAction()`
- Store methods and utilities

### Utilities API (`api/storeToRefs.md`)
- `storeToRefs()` - Converting store to refs
- `mapStores()`, `mapState()`, `mapWritableState()`, `mapGetters()`, `mapActions()`

### createPinia API (`api/createPinia.md`)
- `createPinia()` - Creating a Pinia instance
- Pinia options and configuration

### Plugins API (`api/plugins.md`)
- Plugin creation and usage
- Plugin context and API

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use defineStore()**: Always use defineStore() to create stores
2. **Store naming**: Use descriptive store IDs
3. **State structure**: Keep state flat and normalized when possible
4. **Getters**: Use getters for computed values derived from state
5. **Actions**: Use actions for async operations and mutations
6. **TypeScript**: Use TypeScript for type safety
7. **Store composition**: Split large stores into smaller, focused stores
8. **SSR**: Use proper SSR setup for server-side rendering
9. **Plugins**: Use plugins for cross-cutting concerns
10. **Testing**: Write tests for stores and actions

## Resources

- **Official Documentation**: https://pinia.vuejs.org/
- **Introduction**: https://pinia.vuejs.org/introduction.html
- **API Reference**: https://pinia.vuejs.org/api/
- **GitHub Repository**: https://github.com/vuejs/pinia

## Keywords

Pinia, state management, store, Vue 3, Composition API, Options API, defineStore, state, getters, actions, plugins, SSR, server-side rendering, TypeScript, Vuex migration, 状态管理, 存储, 组合式 API, 选项式 API, 插件, 服务端渲染, 类型支持
