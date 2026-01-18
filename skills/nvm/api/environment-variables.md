# Environment Variables API

## API Reference

Environment variables that affect nvm behavior.

### NVM_DIR

nvm installation directory.

**Default:** `$HOME/.nvm`

**Example:**
```bash
export NVM_DIR="$HOME/.nvm"
```

**Notes:**
- Set before installation to use custom location
- Must be set for nvm to work
- Used by nvm scripts

### NVM_NODEJS_ORG_MIRROR

Custom Node.js download mirror.

**Example:**
```bash
export NVM_NODEJS_ORG_MIRROR=https://npmmirror.com/mirrors/node/
nvm install node
```

**Notes:**
- Useful for regions with slow Node.js downloads
- Must be set before installing versions
- Affects all version downloads

### NVM_IOJS_ORG_MIRROR

Custom io.js download mirror.

**Example:**
```bash
export NVM_IOJS_ORG_MIRROR=https://npmmirror.com/mirrors/iojs/
nvm install iojs
```

**Notes:**
- For io.js downloads only
- Set before installing io.js versions

### XDG_CONFIG_HOME

XDG config directory (affects nvm location).

**Example:**
```bash
export XDG_CONFIG_HOME="$HOME/.config"
# nvm will be installed to $XDG_CONFIG_HOME/nvm
```

**Notes:**
- If set, nvm uses `$XDG_CONFIG_HOME/nvm` instead of `$HOME/.nvm`
- Set before installation
- Follows XDG Base Directory specification

### PROFILE

Shell profile file location.

**Example:**
```bash
export PROFILE="$HOME/.bashrc"
```

**Notes:**
- Used by install script to add nvm sourcing
- Defaults to `.bashrc`, `.bash_profile`, or `.zshrc`
- Can be customized for different shells
