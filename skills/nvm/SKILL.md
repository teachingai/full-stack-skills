---
name: nvm
description: Guidance for installing, configuring, and using nvm (Node Version Manager) based on the official README. Use when the user needs to manage Node.js versions, install nvm, or troubleshoot nvm usage.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install or update nvm
- Install or switch Node.js versions
- Use or manage `.nvmrc`
- Configure shell integration for nvm
- Troubleshoot nvm on macOS, Linux, WSL, or Alpine
- Manage default aliases, LTS versions, or global packages
- Use nvm in Docker or CI/CD

## How to use this skill

1. **Identify the topic** from the user's request and open the matching example file.
2. **Follow the instructions** in the example file, including prerequisites and shell notes.
3. **Use the exact commands** from the example file unless the user requests a variation.
4. **Call out platform constraints** (macOS, Linux, WSL, Alpine, Docker).
5. **Link back to the official README** when uncertainty exists.

### Example file map

- `examples/intro.md` - Intro and quick start
- `examples/about.md` - What nvm is and supported platforms
- `examples/install-update-script.md` - Install & update script
- `examples/install-additional-notes.md` - Install script notes and env vars
- `examples/install-docker.md` - Install in Docker
- `examples/install-docker-cicd.md` - Docker for CI/CD jobs
- `examples/troubleshooting-linux.md` - Linux install troubleshooting
- `examples/troubleshooting-macos.md` - macOS install troubleshooting
- `examples/ansible.md` - Ansible install task
- `examples/verify-installation.md` - Verify installation
- `examples/important-notes.md` - Important notes and caveats
- `examples/git-install.md` - Git install
- `examples/manual-install.md` - Manual install
- `examples/manual-upgrade.md` - Manual upgrade
- `examples/usage.md` - Core nvm usage
- `examples/long-term-support.md` - LTS usage
- `examples/migrate-global-packages.md` - Reinstall packages while installing
- `examples/default-global-packages.md` - Default packages file
- `examples/iojs.md` - io.js usage
- `examples/system-node.md` - Use system node
- `examples/list-versions.md` - List installed/remote versions
- `examples/colors.md` - Set output colors
- `examples/colors-persist.md` - Persist custom colors in shell profile
- `examples/colors-suppress.md` - Suppress colorized output
- `examples/restore-path.md` - Restore PATH (deactivate)
- `examples/default-version.md` - Set default alias
- `examples/mirror.md` - Use node/iojs mirror
- `examples/mirror-auth-header.md` - Pass auth header to mirror
- `examples/nvmrc.md` - .nvmrc usage and rules
- `examples/shell-integration.md` - Deeper shell integration overview
- `examples/auto-use-bash.md` - Auto `nvm use` in bash
- `examples/auto-use-zsh.md` - Auto `nvm use` in zsh
- `examples/auto-use-fish.md` - Auto `nvm use` in fish
- `examples/tests.md` - Running tests
- `examples/environment-variables.md` - Environment variables
- `examples/bash-completion.md` - Bash completion
- `examples/bash-completion-usage.md` - Bash completion usage examples
- `examples/compatibility-issues.md` - Known compatibility issues
- `examples/alpine-install.md` - Alpine Linux install
- `examples/uninstall.md` - Uninstall / removal
- `examples/docker-dev.md` - Docker dev environment
- `examples/problems.md` - Common problems
- `examples/macos-troubleshooting.md` - macOS troubleshooting
- `examples/wsl-troubleshooting.md` - WSL troubleshooting
- `examples/maintainers.md` - Maintainers
- `examples/project-support.md` - Project support
- `examples/enterprise-support.md` - Enterprise support
- `examples/license.md` - License and copyright
- `examples/copyright-notice.md` - Copyright notice

## Keywords

nvm, node version manager, node.js, install nvm, nvm use, nvm install, .nvmrc, lts, node versions, npm global packages, macos, linux, wsl, alpine, docker
