# Environment and Mode Configuration

## Instructions

This example demonstrates environment variables and mode configuration.

### Key Concepts

- Environment files
- Mode-specific configuration
- Env prefix
- Load env

### Example: Environment Files

```
.env                # All environments
.env.local          # All environments (local, gitignored)
.env.development    # Development only
.env.production     # Production only
.env.[mode].local   # Mode-specific local
```

### Example: Env Prefix Configuration

```javascript
// vite.config.js
export default defineConfig({
  // Only variables with this prefix are exposed
  envPrefix: 'VITE_',
  
  // Custom prefix
  // envPrefix: ['VITE_', 'CUSTOM_']
})
```

### Example: Load Env

```javascript
import { defineConfig, loadEnv } from 'vite'

export default defineConfig(({ command, mode }) => {
  // Load env file based on mode
  const env = loadEnv(mode, process.cwd(), '')
  
  return {
    define: {
      __APP_VERSION__: JSON.stringify(env.VITE_APP_VERSION)
    }
  }
})
```

### Example: Mode-Specific Configuration

```javascript
export default defineConfig(({ mode }) => {
  if (mode === 'development') {
    return {
      server: {
        port: 3000
      }
    }
  } else if (mode === 'production') {
    return {
      build: {
        minify: 'terser'
      }
    }
  }
})
```

### Example: Custom Modes

```bash
# Create custom mode file
# .env.staging

# Use custom mode
vite --mode staging
```

### Key Points

- Environment files are loaded in order of priority
- `.env.local` files are gitignored by default
- `envPrefix` controls which variables are exposed
- Use `loadEnv()` to access env in config
- Modes can be custom (not just dev/prod)
