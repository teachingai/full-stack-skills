---
name: nvm
description: Node Version Manager (nvm) 是一个 POSIX shell 脚本，用于管理多个 Node.js 版本。支持安装、切换、卸载、别名等功能，适用于需要在不同 Node.js 版本间切换的开发场景。基于官方文档 https://github.com/nvm-sh/nvm/blob/master/README.md。
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install or manage multiple Node.js versions
- Switch between different Node.js versions
- Install a specific Node.js version
- Set up a default Node.js version
- Create aliases for Node.js versions
- List available or installed Node.js versions
- Uninstall Node.js versions
- Run commands with a specific Node.js version
- Configure nvm for their system
- Update nvm to the latest version
- Set up bash completion for nvm
- Work with LTS (Long Term Support) versions
- Configure nvm in CI/CD environments
- Troubleshoot nvm installation or usage issues

## How to use this skill

This skill is organized to match the nvm official documentation structure (https://github.com/nvm-sh/nvm/blob/master/README.md). When working with nvm:

1. **Identify the task** from the user's request:
   - Installation/安装 → `examples/installation.md`
   - Update/更新 → `examples/update.md`
   - Install Node.js version/安装 Node.js 版本 → `examples/install-version.md`
   - Use/switch version/切换版本 → `examples/use-version.md`
   - List versions/列出版本 → `examples/list-versions.md`
   - Uninstall version/卸载版本 → `examples/uninstall-version.md`
   - Create alias/创建别名 → `examples/aliases.md`
   - Set default version/设置默认版本 → `examples/default-version.md`
   - Run command with version/使用指定版本运行命令 → `examples/run-exec-which.md`
   - Special aliases/特殊别名 → `examples/special-aliases.md`
   - Bash completion/自动补全 → `examples/bash-completion.md`
   - Important notes/重要提示 → `examples/important-notes.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Installation and Update (安装和更新)**:
   - `examples/installation.md` - Installing nvm using curl or wget
   - `examples/update.md` - Updating nvm to the latest version

   **Basic Usage (基本使用)**:
   - `examples/install-version.md` - Installing Node.js versions
   - `examples/use-version.md` - Switching between Node.js versions
   - `examples/list-versions.md` - Listing available and installed versions
   - `examples/uninstall-version.md` - Uninstalling Node.js versions

   **Advanced Usage (高级使用)**:
   - `examples/aliases.md` - Creating and managing aliases
   - `examples/default-version.md` - Setting default Node.js version
   - `examples/run-exec-which.md` - Running commands with specific versions
   - `examples/special-aliases.md` - Special aliases (node, stable, lts/*, etc.)

   **Configuration (配置)**:
   - `examples/bash-completion.md` - Enabling bash completion
   - `examples/important-notes.md` - Important notes and troubleshooting

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - nvm is a POSIX-compliant shell script
   - Works on Unix, macOS, and WSL (Windows Subsystem for Linux)
   - Do not use `sudo` with nvm commands
   - Each Node.js version is installed with its bundled npm
   - Environment variables can affect nvm behavior

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/commands.md` - Complete command reference
   - `api/environment-variables.md` - Environment variables reference

5. **Use templates** from the `templates/` directory:
   - `templates/shell-config.md` - Shell configuration templates

### 1. Understanding nvm

nvm (Node Version Manager) is a version manager for Node.js, designed to be installed per-user and invoked per-shell. nvm works on any POSIX-compliant shell (sh, dash, ksh, zsh, bash), particularly on Unix, macOS, and WSL.

**Key Concepts**:
- **Version Management**: Install and switch between multiple Node.js versions
- **Per-User Installation**: Each user has their own nvm installation
- **Per-Shell Invocation**: nvm must be sourced in each shell session
- **Isolated Environments**: Each version has its own node_modules and global packages

### 2. Installation

**Using curl**:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

**Using wget**:

```bash
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

**Manual installation**:

```bash
git clone https://github.com/nvm-sh/nvm.git ~/.nvm
cd ~/.nvm
git checkout v0.39.0
. ./nvm.sh
```

### 3. Basic Usage

**Install a Node.js version**:

```bash
nvm install 18.17.0
nvm install node        # Install latest version
nvm install lts/*       # Install latest LTS version
```

**Use a Node.js version**:

```bash
nvm use 18.17.0
nvm use node
nvm use default
```

**List versions**:

```bash
nvm ls                 # List installed versions
nvm ls-remote          # List remote available versions
nvm ls-remote --lts    # List LTS versions
```

## Examples and Templates

This skill includes detailed examples organized to match the nvm official documentation structure (https://github.com/nvm-sh/nvm/blob/master/README.md). All examples are in the `examples/` directory, organized by topic:

### Installation and Update (安装和更新) - `examples/`

- `examples/installation.md` - Installing nvm using curl, wget, or manual git clone
- `examples/update.md` - Updating nvm to the latest version

### Basic Usage (基本使用) - `examples/`

- `examples/install-version.md` - Installing Node.js versions (specific version, latest, LTS)
- `examples/use-version.md` - Switching between Node.js versions
- `examples/list-versions.md` - Listing available and installed versions
- `examples/uninstall-version.md` - Uninstalling Node.js versions

### Advanced Usage (高级使用) - `examples/`

- `examples/aliases.md` - Creating and managing version aliases
- `examples/default-version.md` - Setting and using default Node.js version
- `examples/run-exec-which.md` - Running commands with specific Node.js versions
- `examples/special-aliases.md` - Special aliases (node, stable, iojs, lts/*, etc.)

### Configuration (配置) - `examples/`

- `examples/bash-completion.md` - Enabling bash completion for nvm commands
- `examples/important-notes.md` - Important notes, troubleshooting, and best practices

### Templates Directory (`templates/`)

- `templates/shell-config.md` - Shell configuration templates for different shells (bash, zsh, fish)

**To use examples:**
- Identify the task from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the commands to your specific use case

**To use templates:**
- Reference `templates/shell-config.md` for shell configuration templates
- Adapt templates to your specific shell and needs

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official nvm documentation structure:

### Commands API (`api/commands.md`)
- `nvm install` - Install Node.js versions
- `nvm use` - Switch Node.js versions
- `nvm ls` / `nvm list` - List installed versions
- `nvm ls-remote` - List remote available versions
- `nvm uninstall` - Uninstall Node.js versions
- `nvm alias` - Manage version aliases
- `nvm run` - Run command with specific version
- `nvm exec` - Execute command with specific version
- `nvm which` - Show path to Node.js executable
- `nvm current` - Show current active version
- `nvm deactivate` - Deactivate nvm in current shell

### Environment Variables API (`api/environment-variables.md`)
- `NVM_DIR` - nvm installation directory
- `NVM_NODEJS_ORG_MIRROR` - Custom Node.js mirror
- `NVM_IOJS_ORG_MIRROR` - Custom io.js mirror
- `XDG_CONFIG_HOME` - XDG config directory (affects nvm location)

**To use API reference:**
1. Identify the command or environment variable you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the command syntax, parameters, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Do not use sudo**: Never use `sudo` with nvm commands
2. **Source nvm in each shell**: Add nvm sourcing to your shell profile (.bashrc, .zshrc, etc.)
3. **Use .nvmrc files**: Create `.nvmrc` files in projects to specify Node.js version
4. **Set default version**: Use `nvm alias default <version>` to set a default version
5. **Use LTS versions**: Prefer LTS (Long Term Support) versions for production
6. **Keep nvm updated**: Regularly update nvm to get the latest features
7. **Check system requirements**: Ensure build tools are installed before installing Node.js

## Resources

- **Official Repository**: https://github.com/nvm-sh/nvm
- **Official README**: https://github.com/nvm-sh/nvm/blob/master/README.md
- **Node.js Releases**: https://nodejs.org/en/download/releases/

## Keywords

nvm, node version manager, node.js, version management, install node, switch node version, node aliases, lts, long term support, node.js installation, node.js versions, bash completion, shell script, posix, unix, macos, wsl, 节点版本管理, 安装 node, 切换 node 版本, node 别名, 长期支持版本
