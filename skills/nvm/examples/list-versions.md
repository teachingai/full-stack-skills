# List Versions

## Instructions

This example demonstrates how to list available and installed Node.js versions.

### Key Concepts

- Listing installed versions
- Listing remote versions
- Filtering versions
- Version information

### Example: List Installed Versions

```bash
# List all installed versions
nvm ls

# Alternative command
nvm list

# Show current version with arrow
nvm ls
# Output example:
# ->     v18.17.0
#        v20.5.0
#        default -> 18.17.0
```

### Example: List Remote Versions

```bash
# List all remote available versions
nvm ls-remote

# List LTS versions only
nvm ls-remote --lts

# List versions matching pattern
nvm ls-remote | grep "v18"
```

### Example: List Specific Version Range

```bash
# List versions for specific major version
nvm ls-remote 18

# List versions for specific minor version
nvm ls-remote 18.17
```

### Example: Show Current Version

```bash
# Show current active version
nvm current

# Show version with node command
node --version
```

### Example: List with Additional Info

```bash
# List with npm versions
nvm ls --no-colors

# List and show aliases
nvm ls
```

### Key Points

- `nvm ls` shows installed versions
- `nvm ls-remote` shows available versions
- Arrow (->) indicates current active version
- `default` shows default version alias
- Use grep to filter remote versions
