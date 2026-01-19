# Aliases

## Instructions

This example demonstrates how to create and manage version aliases in nvm.

### Key Concepts

- Creating aliases
- Listing aliases
- Deleting aliases
- Default alias

### Example: Create Alias

```bash
# Create alias for specific version
nvm alias my-version 18.17.0

# Use alias
nvm use my-version
nvm install my-version
```

### Example: Set Default Version

```bash
# Set default version
nvm alias default 18.17.0

# Set default to latest LTS
nvm alias default lts/*

# Set default to latest
nvm alias default node
```

### Example: List Aliases

```bash
# List all aliases
nvm alias

# List specific alias
nvm alias default
```

### Example: Delete Alias

```bash
# Delete alias
nvm unalias my-version

# Cannot delete default alias (must set new default first)
nvm alias default 20.5.0
nvm unalias default  # This won't work
```

### Example: Use Aliases

```bash
# Install using alias
nvm install my-version

# Use alias
nvm use my-version

# Run command with alias
nvm run my-version app.js
```

### Key Points

- Aliases provide convenient names for versions
- `default` is a special alias for default version
- Aliases can point to other aliases
- Cannot delete default alias directly
- Use `nvm alias` to list all aliases
