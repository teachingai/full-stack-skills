---
name: tauri-app-frontend-selection
description: Guidance on selecting and configuring the frontend framework for Tauri v2 applications. Helps users choose between JS/TS, Rust, and .NET based frontends.
---

# Tauri App Frontend Selection

## When to use this skill

**Use this skill when:**
- User asks "Which frontend should I use with Tauri?"
- User wants to use a specific framework (React, Vue, Next.js) with Tauri.
- User asks about "Frontend Independent" or compatibility.
- User needs to configure their frontend build for Tauri (SSG vs SSR).

**Trigger phrases include:**
- "Tauri 前端选型", "Tauri 支持 React 吗", "Next.js on Tauri"
- "Vue vs Svelte for Tauri"
- "配置 Vite for Tauri"
- "Rust frontend", "Yew", "Leptos"

## How to use this skill

### 1. Understand "Frontend Independent"
**Reference**: https://v2.tauri.app/start/

Explain that Tauri works with **any** frontend framework that compiles to HTML, JavaScript, and CSS. The app uses the OS's native webview (WebView2 on Windows, WebKit on macOS/Linux).

### 2. Select a Framework
**Reference**: https://v2.tauri.app/start/create-project/

Guide the user based on their preferred language:

**Option A: JavaScript / TypeScript (Most Popular)**
*   **Recommended Toolchain**: **Vite** (Fast, configured out-of-the-box by `create-tauri-app`).
*   **Frameworks**:
    *   **React**: Huge ecosystem, standard choice.
    *   **Vue**: Easy to learn, great performance.
    *   **Svelte**: Highly recommended for Tauri due to small bundle size and high performance (no virtual DOM).
    *   **Solid**: Extremely fast, React-like syntax.
    *   **Angular / Preact**: Fully supported.

**Option B: Rust (Full Stack Rust)**
*   **Yew**: Component-based, React-like, mature.
*   **Leptos**: High performance, signal-based, fine-grained reactivity (modern favorite).
*   **Sycamore**: Reactive library for Rust.

**Option C: .NET**
*   **Blazor**: Run Blazor WASM inside Tauri.

### 3. Framework Configuration Rules
**Reference**: https://v2.tauri.app/start/create-project/

**CRITICAL CONFIGURATION CHECKLIST:**

1.  **Static Output (SSG)**:
    *   Tauri embeds the frontend files. The framework MUST output static HTML/CSS/JS.
    *   **Next.js**: Must use `output: 'export'` in `next.config.js`. API routes won't work (use Rust commands instead).
    *   **Nuxt**: Use `nuxi generate`.

2.  **Dev Server & Build Output**:
    *   Ensure `tauri.conf.json` points to the correct dev URL (e.g., `http://localhost:5173`) and dist directory (e.g., `../dist`).

3.  **Mobile Support**:
    *   If targeting mobile, ensure the UI framework is responsive and touch-friendly.