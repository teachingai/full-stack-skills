# Important Notes

## Instructions

This example covers important notes, troubleshooting, and best practices for nvm.

### Key Concepts

- System requirements
- Build tools
- macOS considerations
- XDG_CONFIG_HOME
- CI/CD usage
- Common issues

### Example: System Requirements

**macOS**:
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Or install full Xcode
```

**Linux**:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install build-essential libssl-dev

# CentOS/RHEL
sudo yum groupinstall "Development Tools"
sudo yum install openssl-devel
```

### Example: macOS Apple Silicon

```bash
# nvm supports Apple Silicon (M1/M2)
# Node.js will be compiled for arm64
nvm install node
```

### Example: XDG_CONFIG_HOME

```bash
# If XDG_CONFIG_HOME is set, nvm uses it
export XDG_CONFIG_HOME="$HOME/.config"
# nvm will be installed to $XDG_CONFIG_HOME/nvm
```

### Example: Do Not Use Sudo

```bash
# ❌ WRONG - Never use sudo with nvm
sudo nvm install node

# ✅ CORRECT - Use nvm without sudo
nvm install node
```

### Example: CI/CD Usage

```bash
# In CI/CD, source nvm explicitly
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Or use BASH_ENV
export BASH_ENV="$HOME/.nvm/nvm.sh"
```

### Example: npm Version

```bash
# Each Node.js version comes with bundled npm
# To use different npm version:
npm install -g npm@9.0.0

# Or reinstall npm
nvm reinstall-packages <version>
```

### Example: Troubleshooting

```bash
# Check nvm is loaded
command -v nvm

# Check NVM_DIR is set
echo $NVM_DIR

# Reload nvm
source ~/.nvm/nvm.sh

# Clear nvm cache
nvm cache clear
```

### Key Points

- Install build tools before installing Node.js
- Never use `sudo` with nvm commands
- XDG_CONFIG_HOME affects nvm location
- Each version has bundled npm
- Source nvm in CI/CD environments
- Clear cache if experiencing issues
