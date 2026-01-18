# Special Aliases

## Instructions

This example demonstrates special aliases available in nvm.

### Key Concepts

- Built-in aliases
- Node alias
- Stable alias
- LTS aliases
- io.js alias

### Example: Node Alias

```bash
# 'node' refers to latest Node.js version
nvm install node
nvm use node
nvm alias my-latest node
```

### Example: Stable Alias

```bash
# 'stable' refers to latest stable version
nvm install stable
nvm use stable
```

### Example: LTS Aliases

```bash
# 'lts/*' refers to latest LTS version
nvm install lts/*
nvm use lts/*

# Specific LTS aliases
nvm install lts/hydrogen
nvm install lts/iron
nvm install lts/gallium
```

### Example: io.js Alias

```bash
# 'iojs' refers to latest io.js version
nvm install iojs
nvm use iojs
```

### Example: List LTS Versions

```bash
# List available LTS versions
nvm ls-remote --lts

# List specific LTS line
nvm ls-remote lts/hydrogen
```

### Example: Use LTS in .nvmrc

```bash
# Create .nvmrc with LTS alias
echo "lts/*" > .nvmrc

# Use LTS version
nvm use
```

### Key Points

- `node` = latest Node.js version
- `stable` = latest stable version
- `lts/*` = latest LTS version
- `lts/<name>` = specific LTS line
- `iojs` = latest io.js version
- Special aliases are built-in and cannot be deleted
