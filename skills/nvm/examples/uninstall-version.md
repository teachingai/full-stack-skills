# Uninstall Version

## Instructions

This example demonstrates how to uninstall Node.js versions using nvm.

### Key Concepts

- Uninstalling versions
- Removing versions
- Cleaning up

### Example: Uninstall Specific Version

```bash
# Uninstall specific version
nvm uninstall 18.17.0

# Uninstall current version (switch first)
nvm use 20.5.0
nvm uninstall 18.17.0
```

### Example: Uninstall Multiple Versions

```bash
# Uninstall multiple versions
nvm uninstall 16.20.0
nvm uninstall 17.9.0
nvm uninstall 18.0.0
```

### Example: Check Before Uninstalling

```bash
# List installed versions first
nvm ls

# Then uninstall specific version
nvm uninstall 18.17.0
```

### Example: Uninstall and Clean

```bash
# Uninstall version
nvm uninstall 18.17.0

# Clean up (optional)
nvm cache clear
```

### Key Points

- Cannot uninstall currently active version
- Switch to another version first
- Uninstalling removes version directory
- Use `nvm ls` to verify removal
- Cache cleanup is optional
