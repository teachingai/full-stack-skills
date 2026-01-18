# Default Version

## Instructions

This example demonstrates how to set and use the default Node.js version.

### Key Concepts

- Setting default version
- Default alias
- Auto-activation
- Shell startup

### Example: Set Default Version

```bash
# Set default version
nvm alias default 18.17.0

# Set default to latest LTS
nvm alias default lts/*

# Set default to latest
nvm alias default node
```

### Example: Install and Set Default

```bash
# Install and set as default
nvm install 18.17.0 --default

# Install latest and set as default
nvm install node --default
```

### Example: Check Default Version

```bash
# Check default alias
nvm alias default

# List all aliases
nvm alias
```

### Example: Use Default Version

```bash
# Use default version
nvm use default

# Default activates automatically in new shells
# (if nvm is sourced in shell profile)
```

### Example: Change Default Version

```bash
# Change default to different version
nvm alias default 20.5.0

# Verify change
nvm current
node --version
```

### Key Points

- Default version activates in new shell sessions
- Set with `nvm alias default <version>`
- Can use `--default` flag during install
- Default persists across shell sessions
- Use `nvm use default` to activate manually
