---
name: tauri-app-creator
description: Comprehensive guide for creating, initializing, and setting up Tauri v2 applications. Covers system prerequisites, project scaffolding, and structure explanation.
---

# Tauri App Creator

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Creating a new Tauri project ("new tauri app", "create tauri project", "init tauri")
- Setting up a Tauri environment ("install tauri", "prerequisites", "setup tauri")
- Understanding Tauri project structure ("folder structure", "src-tauri")
- Requests to "Create a Tauri app" or "Start a Tauri project"

**Trigger phrases include:**
- "创建 Tauri 项目", "新建 Tauri 应用", "初始化 Tauri"
- "Tauri 环境配置", "安装 Rust", "安装 Tauri 依赖"
- "Tauri 项目结构", "目录说明"
- "How to start with Tauri", "Tauri create app"

## How to use this skill

**CRITICAL: Follow the official Tauri v2 documentation flow strictly.**

### 1. Check & Install Prerequisites
**Reference**: https://v2.tauri.app/start/prerequisites/

Before creating a project, you MUST verify or guide the user to install system dependencies:

*   **Rust (Mandatory)**:
    *   Check: `rustc --version`
    *   Install (Unix): `curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh`
    *   Install (Windows): Download `rustup-init.exe`
*   **Operating System Dependencies**:
    *   **macOS**: Requires Xcode or Command Line Tools (`xcode-select --install`).
    *   **Windows**: Requires **Microsoft C++ Build Tools** (Select "Desktop development with C++") and **WebView2 Runtime**.
    *   **Linux**: Requires system libraries (e.g., `libwebkit2gtk-4.1-dev`, `build-essential`, `curl`, `wget`, `libssl-dev`, etc.).
*   **Mobile Targets (Optional)**:
    *   Android: Android Studio, SDK, NDK, and env vars (`JAVA_HOME`, `ANDROID_HOME`, `NDK_HOME`).
    *   iOS: Xcode (macOS only).

### 2. Create the Project
**Reference**: https://v2.tauri.app/start/create-project/

**Method A: Using `create-tauri-app` (Recommended)**
Guide the user to use the scaffolding tool which handles frontend and backend setup together.

**Command:**
```bash
# Interactive mode (Best for most users)
npm create tauri-app@latest
# Or
yarn create tauri-app
# Or
pnpm create tauri-app
# Or
cargo create-tauri-app
# Or
sh <(curl https://create.tauri.app/sh)
```

**Selection Steps:**
1.  **Project Name**: The name of the project folder.
2.  **Identifier**: Unique bundle identifier (e.g., `com.example.app`).
3.  **Frontend Language**: TypeScript / JavaScript, Rust, or .NET.
4.  **Package Manager**: npm, yarn, pnpm, or bun.
5.  **UI Template**: Vanilla, Vue, Svelte, React, Solid, Angular, Preact, Yew, Leptos, Sycamore, Blazor.
6.  **UI Flavor**: TypeScript or JavaScript.

**Method B: Manual Setup (Add to existing project)**
1.  Create frontend first (e.g., `npm create vite@latest`).
2.  Install Tauri CLI: `npm install -D @tauri-apps/cli@latest`.
3.  Initialize Tauri: `npx tauri init`.
    *   Set **Web Assets** path (e.g., `../dist`).
    *   Set **Dev Server URL** (e.g., `http://localhost:5173`).

### 3. Explain Project Structure
**Reference**: https://v2.tauri.app/start/project-structure/

Explain the key files generated:
*   `src-tauri/`: The Rust backend process.
    *   `tauri.conf.json`: Core configuration (allowlist, windows, bundle settings).
    *   `Cargo.toml`: Rust dependencies.
    *   `src/lib.rs` / `src/main.rs`: The entry point of the Tauri application.
*   `src/`: The frontend source code (Vue, React, Svelte, etc.).

### 4. Run the Application
**Reference**: https://v2.tauri.app/start/

*   Install dependencies: `npm install`
*   Start Dev Server: `npm run tauri dev`
    *   This will compile the Rust code and open the native window with web content.