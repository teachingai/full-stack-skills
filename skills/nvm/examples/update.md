# Update

## Instructions

This example demonstrates how to update nvm to the latest version.

### Key Concepts

- Updating nvm
- Checking current version
- Git-based update
- Script-based update

### Example: Update using Git

```bash
# Navigate to nvm directory
cd "$NVM_DIR"

# Fetch latest changes
git fetch --tags origin

# Checkout latest release
git checkout `git describe --abbrev=0 --tags --match "v[0-9]*" $(git rev-list --tags --max-count=1)`

# Reload nvm
. "$NVM_DIR/nvm.sh"
```

### Example: Update using Install Script

```bash
# Run the install script again (it will update if nvm exists)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

### Example: Check Current Version

```bash
# Check nvm version
nvm --version

# Or check git tag
cd "$NVM_DIR" && git describe --tags
```

### Example: Update to Specific Version

```bash
cd "$NVM_DIR"
git fetch --tags origin
git checkout v0.39.0
. "$NVM_DIR/nvm.sh"
```

### Key Points

- Update by checking out the latest git tag
- Install script can also be used to update
- Always reload nvm after updating
- Check version with `nvm --version`
- Latest version is available on GitHub releases
