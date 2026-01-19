# Commands API

## API Reference

Complete nvm command reference with syntax and examples.

### nvm install

Install a Node.js version.

**Syntax:**
```bash
nvm install <version>
nvm install node          # Install latest
nvm install --lts         # Install latest LTS
nvm install lts/*         # Install latest LTS
nvm install lts/<name>    # Install specific LTS
```

**Options:**
- `--lts` - Install latest LTS version
- `--default` - Set as default after install
- `--latest-npm` - Install latest npm
- `--reinstall-packages-from=<version>` - Reinstall packages from version
- `--no-npm` - Install without npm

**Examples:**
```bash
nvm install 18.17.0
nvm install node --default
nvm install --lts
```

**See also:** `examples/install-version.md`

### nvm use

Switch to a Node.js version.

**Syntax:**
```bash
nvm use <version>
nvm use node
nvm use default
nvm use --lts
```

**Options:**
- `--silent` - Suppress output

**Examples:**
```bash
nvm use 18.17.0
nvm use default
```

**See also:** `examples/use-version.md`

### nvm ls / nvm list

List installed Node.js versions.

**Syntax:**
```bash
nvm ls
nvm list
```

**Examples:**
```bash
nvm ls
nvm list
```

**See also:** `examples/list-versions.md`

### nvm ls-remote

List remote available Node.js versions.

**Syntax:**
```bash
nvm ls-remote
nvm ls-remote --lts
nvm ls-remote <version>
```

**Options:**
- `--lts` - List LTS versions only

**Examples:**
```bash
nvm ls-remote
nvm ls-remote --lts
nvm ls-remote 18
```

**See also:** `examples/list-versions.md`

### nvm uninstall

Uninstall a Node.js version.

**Syntax:**
```bash
nvm uninstall <version>
```

**Examples:**
```bash
nvm uninstall 18.17.0
```

**See also:** `examples/uninstall-version.md`

### nvm alias

Manage version aliases.

**Syntax:**
```bash
nvm alias <name> <version>    # Create alias
nvm alias                     # List aliases
nvm alias <name>              # Show alias
nvm unalias <name>            # Delete alias
```

**Examples:**
```bash
nvm alias my-version 18.17.0
nvm alias default 18.17.0
nvm alias
```

**See also:** `examples/aliases.md`

### nvm run

Run a Node.js script with a specific version.

**Syntax:**
```bash
nvm run <version> [--] <script> [args]
```

**Examples:**
```bash
nvm run 18.17.0 app.js
nvm run node -- app.js --arg value
```

**See also:** `examples/run-exec-which.md`

### nvm exec

Execute a command with a specific version.

**Syntax:**
```bash
nvm exec <version> [--] <command> [args]
```

**Examples:**
```bash
nvm exec 18.17.0 npm install
nvm exec node -- npm test
```

**See also:** `examples/run-exec-which.md`

### nvm which

Show path to Node.js executable.

**Syntax:**
```bash
nvm which <version>
nvm which                      # Current version
```

**Examples:**
```bash
nvm which 18.17.0
nvm which
```

**See also:** `examples/run-exec-which.md`

### nvm current

Show current active version.

**Syntax:**
```bash
nvm current
```

**Examples:**
```bash
nvm current
```

**See also:** `examples/list-versions.md`

### nvm deactivate

Deactivate nvm in current shell.

**Syntax:**
```bash
nvm deactivate
```

**Examples:**
```bash
nvm deactivate
```
