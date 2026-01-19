---
name: rspack
description: Provides comprehensive guidance for Rspack bundler including configuration, plugins, loaders, optimization, and Webpack compatibility. Use when the user asks about Rspack, needs to configure Rspack, optimize build performance, or migrate from Webpack.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Rspack in a new or existing project
- Configure Rspack for different environments
- Use built-in plugins or create custom plugins
- Migrate from Webpack to Rspack
- Optimize build performance
- Understand Rspack configuration options
- Use Rspack CLI or JavaScript API
- Write custom loaders
- Understand plugin API and hooks
- Configure entry points and output
- Set up code splitting and optimization
- Configure development server
- Handle assets and resources
- Use TypeScript with Rspack
- Troubleshoot Rspack issues

## How to use this skill

This skill is organized to match the Rspack official documentation structure (https://rspack.rs/zh/guide/start/introduction, https://rspack.rs/zh/config/, https://rspack.rs/zh/plugins/, https://rspack.rs/zh/api/). When working with Rspack:

1. **Identify the topic** from the user's request:
   - Getting started/快速上手 → `examples/start/`
   - Configuration/配置 → `examples/config/`
   - Plugins/插件 → `examples/plugins/`
   - API → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速上手)**:
   - `examples/start/introduction.md` - Introduction to Rspack
   - `examples/start/quick-start.md` - Quick start guide

   **Configuration (配置)**:
   - `examples/config/configuration-file.md` - Configuration file setup
   - `examples/config/configuration-formats.md` - Configuration file formats
   - `examples/config/entry.md` - Entry points configuration
   - `examples/config/output.md` - Output configuration
   - `examples/config/module.md` - Module configuration
   - `examples/config/resolve.md` - Module resolution
   - `examples/config/optimization.md` - Optimization options
   - `examples/config/dev-server.md` - Development server
   - `examples/config/plugins.md` - Plugins configuration
   - `examples/config/mode.md` - Mode configuration

   **Plugins (插件)**:
   - `examples/plugins/builtin-plugins.md` - Built-in plugins
   - `examples/plugins/webpack-compat-plugins.md` - Webpack compatibility
   - `examples/plugins/writing-plugins.md` - Writing custom plugins

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Rspack is compatible with most Webpack plugins and loaders
   - Configuration format is similar to Webpack
   - Rspack provides better performance than Webpack
   - Examples include both JavaScript and TypeScript versions
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/cli.md` - Rspack CLI commands
   - `api/javascript-api.md` - JavaScript API
   - `api/loader-api.md` - Loader API
   - `api/plugin-api.md` - Plugin API
   - `api/runtime-api.md` - Runtime API

5. **Use templates** from the `templates/` directory:
   - `templates/rspack-config.md` - Rspack configuration templates
   - `templates/project-structure.md` - Project structure templates

### 1. Understanding Rspack

Rspack is a fast Rust-based web bundler designed to be a drop-in replacement for Webpack, with significantly better performance.

**Key Concepts**:
- **High Performance**: Built with Rust for faster builds
- **Webpack Compatible**: Most Webpack plugins and loaders work
- **Fast HMR**: Hot Module Replacement with better performance
- **TypeScript Support**: Built-in TypeScript support

### 2. Installation

**Using npm**:

```bash
npm install -D @rspack/core @rspack/cli
```

**Using yarn**:

```bash
yarn add -D @rspack/core @rspack/cli
```

**Using pnpm**:

```bash
pnpm add -D @rspack/core @rspack/cli
```

### 3. Basic Configuration

```javascript
// rspack.config.js
const rspack = require('@rspack/core');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  plugins: [
    new rspack.HtmlRspackPlugin({
      template: './index.html',
    }),
  ],
};
```

## Examples and Templates

This skill includes detailed examples organized to match the Rspack official documentation structure (https://rspack.rs/zh/). All examples are in the `examples/` directory, organized by topic:

### Getting Started (快速上手) - `examples/start/`

- `examples/start/introduction.md` - Introduction to Rspack, why use it, and comparison with other bundlers
- `examples/start/quick-start.md` - Quick start guide, installation, and project setup

### Configuration (配置) - `examples/config/`

- `examples/config/configuration-file.md` - Configuration file location and naming
- `examples/config/configuration-formats.md` - Configuration file formats (JS, TS, etc.)
- `examples/config/entry.md` - Entry points configuration
- `examples/config/output.md` - Output configuration
- `examples/config/module.md` - Module configuration (loaders, rules)
- `examples/config/resolve.md` - Module resolution configuration
- `examples/config/optimization.md` - Optimization options (code splitting, minification)
- `examples/config/dev-server.md` - Development server configuration
- `examples/config/plugins.md` - Plugins configuration
- `examples/config/mode.md` - Mode configuration (development, production)

### Plugins (插件) - `examples/plugins/`

- `examples/plugins/builtin-plugins.md` - Built-in plugins (HtmlRspackPlugin, CopyRspackPlugin, etc.)
- `examples/plugins/webpack-compat-plugins.md` - Webpack plugin compatibility
- `examples/plugins/writing-plugins.md` - Writing custom plugins

### Templates Directory (`templates/`)

- `templates/rspack-config.md` - Rspack configuration templates
- `templates/project-structure.md` - Project structure templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/rspack-config.md` for Rspack configuration templates
- Use `templates/project-structure.md` for organizing Rspack projects
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Rspack API documentation structure:

### CLI API (`api/cli.md`)
- Rspack CLI commands and options
- Build, dev, and other commands

### JavaScript API (`api/javascript-api.md`)
- Programmatic API for using Rspack
- Compiler and compilation APIs

### Loader API (`api/loader-api.md`)
- Loader interface and API
- Writing custom loaders

### Plugin API (`api/plugin-api.md`)
- Plugin interface and hooks
- Compiler and compilation hooks

### Runtime API (`api/runtime-api.md`)
- Runtime module API
- HMR API

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use TypeScript for configuration**: Better type safety and autocomplete
2. **Leverage built-in plugins**: Use Rspack plugins when available
3. **Optimize for production**: Use production mode for builds
4. **Code splitting**: Use optimization.splitChunks for better performance
5. **Cache configuration**: Enable persistent caching for faster rebuilds
6. **Use HMR**: Enable Hot Module Replacement for better DX

## Resources

- **Official Documentation**: https://rspack.rs/zh/
- **Getting Started**: https://rspack.rs/zh/guide/start/introduction
- **Configuration**: https://rspack.rs/zh/config/
- **Plugins**: https://rspack.rs/zh/plugins/
- **API Reference**: https://rspack.rs/zh/api/
- **GitHub Repository**: https://github.com/web-infra-dev/rspack

## Keywords

Rspack, rspack, bundler, webpack, rust, build tool, bundling, code splitting, HMR, hot module replacement, loader, plugin, configuration, entry, output, optimization, development server, 打包工具, 构建工具, 代码分割, 热模块替换, 加载器, 插件, 配置, 入口, 输出, 优化, 开发服务器
