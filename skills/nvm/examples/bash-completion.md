# Bash Completion

## Instructions

This example demonstrates how to enable bash completion for nvm commands.

### Key Concepts

- Enabling completion
- Shell configuration
- Completion features
- Tab completion

### Example: Enable Bash Completion

**For bash** (`~/.bashrc` or `~/.bash_profile`):
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

### Example: Enable Zsh Completion

**For zsh** (`~/.zshrc`):
```zsh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

### Example: Verify Completion

```bash
# Reload shell configuration
source ~/.bashrc  # or source ~/.zshrc

# Test completion (type and press Tab)
nvm install <TAB>
nvm use <TAB>
nvm uninstall <TAB>
```

### Example: Completion Features

With completion enabled, you can:
- Tab complete version numbers
- Tab complete aliases
- Tab complete commands
- See available options

### Key Points

- Completion is enabled by sourcing `bash_completion` file
- Works with bash and zsh
- Provides tab completion for commands and versions
- Must be sourced in each shell session
- Installation script adds this automatically
