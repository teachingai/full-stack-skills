# Installation

## Instructions

This example demonstrates how to install Tauri.

### Key Concepts

- Prerequisites
- CLI installation
- Project setup
- Dependencies

### Example: Prerequisites

**Required:**
- Node.js (v16 or higher)
- Rust (latest stable)
- System dependencies (varies by platform)

### Example: Install Rust

```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Verify installation
rustc --version
```

### Example: Install Tauri CLI

```bash
# Using npm
npm install -D @tauri-apps/cli

# Using cargo
cargo install tauri-cli
```

### Example: System Dependencies

**macOS:**
```bash
# Install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install libwebkit2gtk-4.0-dev \
  build-essential \
  curl \
  wget \
  libssl-dev \
  libgtk-3-dev \
  libayatana-appindicator3-dev \
  librsvg2-dev
```

**Windows:**
- Install Microsoft Visual Studio C++ Build Tools
- Install WebView2

### Example: Create Tauri Project

```bash
# Using npm
npm create tauri-app

# Using cargo
cargo tauri init
```

### Key Points

- Install Rust first
- Install Tauri CLI
- Install system dependencies
- Create project with CLI
- Follow platform-specific setup
