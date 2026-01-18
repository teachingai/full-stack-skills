# Run, Exec, and Which

## Instructions

This example demonstrates running commands with specific Node.js versions without switching.

### Key Concepts

- Running commands with versions
- Executing commands
- Finding executable paths
- Temporary version usage

### Example: Run Command with Version

```bash
# Run script with specific version
nvm run 18.17.0 app.js

# Run with latest version
nvm run node app.js

# Run with LTS version
nvm run lts/* app.js
```

### Example: Exec Command with Version

```bash
# Execute command with specific version
nvm exec 18.17.0 npm install

# Execute with alias
nvm exec my-version npm test

# Execute multiple commands
nvm exec 18.17.0 npm install && npm test
```

### Example: Which Command

```bash
# Show path to Node.js executable
nvm which 18.17.0

# Show path for current version
nvm which

# Show path for alias
nvm which default
```

### Example: Run with Arguments

```bash
# Run with command arguments
nvm run 18.17.0 -- app.js --arg1 value1

# Exec with arguments
nvm exec 18.17.0 -- npm run build --production
```

### Example: Use in Scripts

```bash
#!/bin/bash
# Run script with specific version
nvm exec 18.17.0 node script.js

# Or use which to get path
NODE_PATH=$(nvm which 18.17.0)
$NODE_PATH script.js
```

### Key Points

- `nvm run` runs Node.js script with specific version
- `nvm exec` executes command with specific version
- `nvm which` shows path to Node.js executable
- Use `--` to separate nvm arguments from command arguments
- Useful for CI/CD and scripts without switching versions
