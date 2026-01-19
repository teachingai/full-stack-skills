---
name: tauri
description: Provides comprehensive guidance for Tauri framework including Rust backend, frontend integration, window management, and desktop app development. Use when the user asks about Tauri, needs to create Tauri applications, implement Tauri features, or build lightweight desktop apps.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and set up Tauri in a project
- Create desktop applications with Tauri
- Use Tauri CLI commands
- Configure Tauri applications
- Handle frontend-backend communication
- Use Tauri APIs
- Build and package Tauri applications
- Troubleshoot Tauri issues

## How to use this skill

This skill is organized to match the Tauri official documentation structure (https://v2.tauri.org.cn/, https://v2.tauri.org.cn/start/, https://v2.tauri.org.cn/reference/cli/). When working with Tauri:

1. **Identify the topic** from the user's request:
   - Installation/安装 → `examples/start/installation.md`
   - Quick Start/快速开始 → `examples/start/quick-start.md`
   - Guide/使用指南 → `examples/guide/`
   - CLI/命令行 → `examples/reference/cli.md`
   - API/API 文档 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Start (快速开始)**:
   - `examples/start/intro.md` - Introduction to Tauri
   - `examples/start/installation.md` - Installation guide
   - `examples/start/quick-start.md` - Quick start guide
   - `examples/start/prerequisites.md` - Prerequisites

   **Guide (使用指南)**:
   - `examples/guide/architecture.md` - Architecture
   - `examples/guide/frontend.md` - Frontend setup
   - `examples/guide/backend.md` - Backend (Rust)
   - `examples/guide/commands.md` - Commands
   - `examples/guide/events.md` - Events
   - `examples/guide/window.md` - Window management
   - `examples/guide/filesystem.md` - File system
   - `examples/guide/configuration.md` - Configuration
   - `examples/guide/build.md` - Build and package

   **Reference (参考)**:
   - `examples/reference/cli.md` - CLI commands
   - `examples/reference/config.md` - Configuration reference

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Tauri uses Web frontend and Rust backend
   - Frontend can be any web framework
   - Backend is written in Rust
   - Communication via commands and events
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/tauri-api.md` - Tauri API
   - `api/commands-api.md` - Commands API
   - `api/events-api.md` - Events API
   - `api/window-api.md` - Window API
   - `api/filesystem-api.md` - File system API
   - `api/config-api.md` - Configuration API

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/project-setup.md` - Project setup templates
   - `templates/configuration.md` - Configuration templates

### 1. Understanding Tauri

Tauri is a framework for building desktop applications using web frontend technologies and Rust backend.

**Key Concepts**:
- **Frontend**: Web technologies (HTML, CSS, JavaScript)
- **Backend**: Rust
- **Commands**: Frontend-backend communication
- **Events**: Event system
- **Window**: Window management
- **File System**: File operations

### 2. Installation

**Prerequisites**:
- Node.js
- Rust
- System dependencies

**Using npm**:

```bash
npm install @tauri-apps/cli
```

**Using cargo**:

```bash
cargo install tauri-cli
```

### 3. Basic Setup

```bash
# Create Tauri project
npm create tauri-app

# Or using cargo
cargo tauri init
```


### Doc mapping (one-to-one with official documentation)

- `examples/guide/` or `examples/getting-started/` → https://v2.tauri.org.cn/start/
- `api/` → https://v2.tauri.org.cn/reference/cli/

## Examples and Templates

This skill includes detailed examples organized to match the official documentation structure. All examples are in the `examples/` directory (see mapping above).

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the mapping above
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference templates in `templates/` directory for common scaffolding
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Tauri API documentation structure:

### Tauri API (`api/tauri-api.md`)
- Tauri core API
- API methods
- API types

### Commands API (`api/commands-api.md`)
- Command definition
- Command invocation
- Command parameters

### Events API (`api/events-api.md`)
- Event emission
- Event listening
- Event handling

### Window API (`api/window-api.md`)
- Window creation
- Window management
- Window events

### File System API (`api/filesystem-api.md`)
- File operations
- Directory operations
- Path operations

### Configuration API (`api/config-api.md`)
- Configuration options
- Configuration file
- Environment variables

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Separate frontend and backend**: Keep frontend and backend code separate
2. **Use commands**: Use commands for frontend-backend communication
3. **Handle errors**: Properly handle errors in both frontend and backend
4. **Security**: Follow Tauri security best practices
5. **Performance**: Optimize application performance
6. **Build configuration**: Configure build and package properly
7. **Use TypeScript**: Leverage TypeScript for type safety

## Resources

- **Official Documentation**: https://v2.tauri.org.cn/
- **Quick Start**: https://v2.tauri.org.cn/start/
- **CLI Reference**: https://v2.tauri.org.cn/reference/cli/
- **GitHub Repository**: https://github.com/tauri-apps/tauri

## Keywords

Tauri, tauri, desktop application, 桌面应用, Rust, Web frontend, commands, events, window, file system, CLI, 命令, 事件, 窗口, 文件系统, 命令行, Tauri CLI, Tauri commands, Tauri events, Tauri window, Tauri filesystem, cross-platform, 跨平台
