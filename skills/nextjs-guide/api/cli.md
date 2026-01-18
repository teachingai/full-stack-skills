# Next.js CLI API

## API Reference

Next.js CLI commands and options.

### next dev

Start development server.

**Usage:**
```bash
next dev
```

**Options:**
- `-p, --port <port>` - Port number
- `-H, --hostname <hostname>` - Hostname
- `-t, --turbo` - Enable Turbopack

**Example:**
```bash
next dev -p 3000
```

### next build

Build application for production.

**Usage:**
```bash
next build
```

**Options:**
- `-d, --debug` - Debug mode

**Example:**
```bash
next build
```

### next start

Start production server.

**Usage:**
```bash
next start
```

**Options:**
- `-p, --port <port>` - Port number
- `-H, --hostname <hostname>` - Hostname

**Example:**
```bash
next start -p 3000
```

### next lint

Run ESLint.

**Usage:**
```bash
next lint
```

**Options:**
- `--dir <directory>` - Directory to lint
- `--file <file>` - File to lint

**See also:** `examples/getting-started/installation.md`
