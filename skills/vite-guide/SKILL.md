---
name: vite-guide
description: Vite 完整使用指南，基于官方文档（https://cn.vitejs.dev/guide/），涵盖项目创建、配置、开发服务器、构建、插件系统、静态资源处理、环境变量、HMR、代码分割、优化等核心概念和最佳实践。适用于使用 Vite 作为前端构建工具的场景。
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create a new Vite project or configure an existing one
- Set up development server with Vite
- Configure Vite build options and optimizations
- Use Vite plugins and extend functionality
- Handle static assets and resources in Vite
- Configure environment variables in Vite
- Optimize Vite build performance and code splitting
- Set up proxy and server configuration
- Use CSS preprocessors with Vite
- Configure path aliases and resolve options
- Deploy Vite applications
- Use Vite with different frameworks (Vue, React, Svelte, etc.)
- Understand Vite's HMR (Hot Module Replacement) system
- Configure TypeScript with Vite
- Set up testing with Vite
- Use Vite for library development

## How to use this skill

This skill is organized to match the Vite official documentation structure (https://cn.vitejs.dev/guide/, https://cn.vitejs.dev/config/, https://cn.vitejs.dev/plugins/). When working with Vite:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/guide/getting-started.md`
   - Why Vite/为什么选择 Vite → `examples/guide/why-vite.md`
   - HTML/HTML 特性 → `examples/guide/features/html.md`
   - Static assets/静态资源 → `examples/guide/features/static-assets.md`
   - Environment variables/环境变量 → `examples/guide/features/env-and-mode.md`
   - Build for production/生产构建 → `examples/guide/features/build-for-production.md`
   - Preview/预览 → `examples/guide/features/preview.md`
   - Library mode/库模式 → `examples/guide/features/library-mode.md`
   - Multi-page app/多页面应用 → `examples/guide/features/multi-page-app.md`
   - Using plugins/使用插件 → `examples/guide/using-plugins.md`
   - NPM dependency resolving/依赖解析 → `examples/features/npm-dependency-resolving.md`
   - HMR/热模块替换 → `examples/features/hot-module-replacement.md`
   - TypeScript → `examples/features/typescript.md`
   - CSS → `examples/features/css.md`
   - JSON → `examples/features/json.md`
   - Glob import/全局导入 → `examples/features/glob-import.md`
   - Dynamic import/动态导入 → `examples/features/dynamic-import.md`
   - WebAssembly → `examples/features/webassembly.md`
   - Web Workers → `examples/features/web-workers.md`
   - Configuration/配置 → `examples/config/shared-options.md`
   - Server options/服务器选项 → `examples/config/server-options.md`
   - Build options/构建选项 → `examples/config/build-options.md`
   - SSR options/SSR 选项 → `examples/config/ssr-options.md`
   - Dependency optimization/依赖优化 → `examples/config/dependency-optimization.md`
   - Plugin API/插件 API → `examples/plugin-api/plugin-api-intro.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Guide (指南) - `examples/guide/`**:
   - `examples/guide/getting-started.md` - Creating a Vite project and basic setup
   - `examples/guide/why-vite.md` - Why Vite exists and what problems it solves
   - `examples/guide/features/html.md` - HTML handling and transformation
   - `examples/guide/features/static-assets.md` - Static asset handling
   - `examples/guide/features/env-and-mode.md` - Environment variables and modes
   - `examples/guide/features/build-for-production.md` - Production builds
   - `examples/guide/features/preview.md` - Previewing builds
   - `examples/guide/features/library-mode.md` - Building libraries
   - `examples/guide/features/multi-page-app.md` - Multi-page applications
   - `examples/guide/using-plugins.md` - Using plugins

   **Features (特性) - `examples/features/`**:
   - `examples/features/npm-dependency-resolving.md` - NPM dependency resolving
   - `examples/features/hot-module-replacement.md` - HMR (Hot Module Replacement)
   - `examples/features/typescript.md` - TypeScript support
   - `examples/features/css.md` - CSS features and preprocessing
   - `examples/features/static-assets.md` - Static asset handling
   - `examples/features/json.md` - JSON importing
   - `examples/features/glob-import.md` - Glob import
   - `examples/features/dynamic-import.md` - Dynamic import
   - `examples/features/webassembly.md` - WebAssembly support
   - `examples/features/web-workers.md` - Web Workers support

   **Build (构建) - `examples/`**:
   - `examples/build.md` - Production build configuration
   - `examples/build-options.md` - Build options and optimization
   - `examples/chunking-strategy.md` - Code splitting and chunking
   - `examples/library-mode.md` - Building libraries with Vite

   **Deployment (部署) - `examples/`**:
   - `examples/deployment.md` - Deployment strategies and configurations

   **Configuration (配置) - `examples/config/`**:
   - `examples/config/shared-options.md` - Shared configuration options (root, base, mode, define, plugins, publicDir)
   - `examples/config/server-options.md` - Development server options (host, port, proxy, https, etc.)
   - `examples/config/build-options.md` - Build options (outDir, assetsDir, minify, rollupOptions, etc.)
   - `examples/config/ssr-options.md` - SSR (Server-Side Rendering) options (external, noExternal, target, resolve)
   - `examples/config/dependency-optimization.md` - Dependency optimization options (optimizeDeps)
   - `examples/config/env-and-mode-config.md` - Environment variables and mode configuration

   **Plugin API (插件 API) - `examples/plugin-api/`**:
   - `examples/plugin-api/plugin-api-intro.md` - Plugin API introduction
   - `examples/plugin-api/plugin-hooks.md` - Plugin hooks and lifecycle
   - `examples/plugin-api/creating-plugins.md` - Creating custom plugins
   - `examples/plugin-api/using-plugins.md` - Using plugins
   - `examples/plugin-api/environment-api.md` - Environment API for plugins

   **Advanced (高级) - `examples/`**:
   - `examples/dependency-pre-bundling.md` - Dependency pre-bundling
   - `examples/optimize-dependencies.md` - Optimizing dependencies
   - `examples/multi-page-app.md` - Multi-page application setup
   - `examples/client-types.md` - Client types and imports

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Vite's configuration format
   - Examples include both JavaScript and TypeScript configurations
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/config.md` - Vite configuration API reference
   - `api/plugin-api.md` - Plugin API reference
   - `api/cli.md` - CLI commands reference

5. **Use templates** from the `templates/` directory:
   - `templates/vite-config.md` - Vite configuration templates
   - `templates/project-structure.md` - Project structure templates

## Examples and Templates

This skill includes detailed examples organized to match the Vite official documentation structure (https://cn.vitejs.dev/guide/, https://cn.vitejs.dev/config/, https://cn.vitejs.dev/plugins/). All examples are in the `examples/` directory, organized by topic:

### Guide (指南) - `examples/guide/`

- `examples/guide/getting-started.md` - Creating a Vite project, project structure, and basic setup
- `examples/guide/why-vite.md` - Why Vite exists, what problems it solves, and comparison with other tools
- `examples/guide/features/html.md` - HTML as entry point, HTML transformation, and asset references
- `examples/guide/features/static-assets.md` - Static asset handling and importing
- `examples/guide/features/env-and-mode.md` - Environment variables and modes
- `examples/guide/features/build-for-production.md` - Production build process
- `examples/guide/features/preview.md` - Previewing production builds
- `examples/guide/features/library-mode.md` - Building libraries with Vite
- `examples/guide/features/multi-page-app.md` - Multi-page application setup
- `examples/guide/using-plugins.md` - Using plugins in Vite projects

### Features (特性) - `examples/features/`

- `examples/features/npm-dependency-resolving.md` - NPM dependency resolving and pre-bundling
- `examples/features/hot-module-replacement.md` - HMR (Hot Module Replacement) system
- `examples/features/typescript.md` - TypeScript configuration and usage
- `examples/features/css.md` - CSS features, preprocessing, and modules
- `examples/features/static-assets.md` - Static asset handling and importing
- `examples/features/json.md` - JSON importing and transformation
- `examples/features/glob-import.md` - Glob import patterns
- `examples/features/dynamic-import.md` - Dynamic import and code splitting
- `examples/features/webassembly.md` - WebAssembly support
- `examples/features/web-workers.md` - Web Workers support

### Build (构建) - `examples/`

- `examples/build.md` - Production build process and configuration
- `examples/build-options.md` - Build options, optimization, and rollup options
- `examples/chunking-strategy.md` - Code splitting and chunking strategies
- `examples/library-mode.md` - Building libraries with Vite

### Deployment (部署) - `examples/`

- `examples/deployment.md` - Deployment strategies for static hosting, SSR, and more

### Configuration (配置) - `examples/config/`

- `examples/config/shared-options.md` - Shared configuration options (root, base, mode, define, plugins, publicDir)
- `examples/config/server-options.md` - Development server configuration (host, port, proxy, https, etc.)
- `examples/config/build-options.md` - Build options (outDir, assetsDir, minify, rollupOptions, etc.)
- `examples/config/ssr-options.md` - SSR (Server-Side Rendering) options (external, noExternal, target, resolve)
- `examples/config/dependency-optimization.md` - Dependency optimization options (optimizeDeps)
- `examples/config/env-and-mode-config.md` - Environment variables and mode configuration

### Plugin API (插件 API) - `examples/plugin-api/`

- `examples/plugin-api/plugin-api-intro.md` - Plugin API introduction and basic concepts
- `examples/plugin-api/plugin-hooks.md` - Plugin hooks (buildStart, transform, resolveId, load, etc.)
- `examples/plugin-api/creating-plugins.md` - Creating custom plugins with examples
- `examples/plugin-api/using-plugins.md` - Using plugins in Vite projects
- `examples/plugin-api/environment-api.md` - Environment API (import.meta.env, import.meta.hot, import.meta.glob)

### Advanced (高级) - `examples/`

- `examples/dependency-pre-bundling.md` - Dependency pre-bundling configuration
- `examples/optimize-dependencies.md` - Optimizing dependencies
- `examples/multi-page-app.md` - Multi-page application setup
- `examples/client-types.md` - Client types and client-side imports

### Templates Directory (`templates/`)

- `templates/vite-config.md` - Vite configuration templates for different scenarios (Vue, React, TypeScript, etc.)
- `templates/project-structure.md` - Standard Vite project organization and structure templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/vite-config.md` for Vite configuration templates
- Use `templates/project-structure.md` for organizing Vite projects
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Vite API documentation structure:

### Config API (`api/config.md`)
- `defineConfig()` - Configuration helper
- All configuration options: `plugins`, `server`, `build`, `resolve`, `css`, `json`, `esbuild`, `optimizeDeps`, `ssr`, `worker`, etc.

### Plugin API (`api/plugin-api.md`)
- Plugin development API
- Plugin hooks and utilities
- Common plugin patterns

### CLI API (`api/cli.md`)
- `vite` - CLI commands
- `vite build` - Build command options
- `vite preview` - Preview command options
- `vite optimize` - Optimize dependencies command

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use path aliases**: Configure `resolve.alias` for cleaner imports
2. **Optimize dependencies**: Use `optimizeDeps` to pre-bundle dependencies
3. **Code splitting**: Configure `build.rollupOptions.output.manualChunks` for optimal chunking
4. **Environment variables**: Use `VITE_` prefix and proper TypeScript types
5. **CSS preprocessing**: Configure `css.preprocessorOptions` for global styles
6. **Proxy configuration**: Use `server.proxy` for API proxying in development
7. **Build optimization**: Enable source maps for production debugging, configure minification

## Resources

- **Official Guide**: https://cn.vitejs.dev/guide/
- **Config Reference**: https://cn.vitejs.dev/config/
- **Plugin API**: https://cn.vitejs.dev/plugins/
- **Migration Guide**: https://cn.vitejs.dev/guide/migration.html

## Keywords

Vite, build tool, frontend, development server, HMR, hot module replacement, production build, Rollup, plugins, static assets, environment variables, code splitting, chunking, optimization, TypeScript, CSS preprocessing, path aliases, proxy, deployment, library mode, multi-page app, web workers, WebAssembly, 构建工具, 开发服务器, 热模块替换, 生产构建, 插件, 静态资源, 环境变量, 代码分割, 优化, 部署
