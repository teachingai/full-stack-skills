# Getting Started

## Instructions

This example demonstrates how to create a new Vite project and understand the basic project structure.

### Key Concepts

- Creating a Vite project
- Project structure
- Basic configuration
- Running the development server

### Example: Creating a Project

```bash
# Using npm
npm create vite@latest my-vue-app -- --template vue

# Using yarn
yarn create vite my-vue-app --template vue

# Using pnpm
pnpm create vite my-vue-app --template vue
```

### Example: Project Structure

```
my-vue-app/
├── index.html              # Entry HTML file
├── package.json            # Dependencies and scripts
├── vite.config.js         # Vite configuration
├── .gitignore
├── public/                 # Static assets (copied as-is)
│   └── favicon.ico
└── src/                    # Source code
    ├── assets/            # Imported assets (processed by Vite)
    │   └── logo.svg
    ├── components/        # Vue components
    │   └── HelloWorld.vue
    ├── App.vue            # Root component
    ├── main.js            # Entry point
    └── style.css          # Styles
```

### Example: Basic Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000,
    open: true
  }
})
```

### Example: Running the Project

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### Key Points

- `index.html` is the entry point (not in `src/`)
- `public/` files are served at root path
- `src/` contains source code that gets processed
- Vite uses native ESM in development
- Production builds use Rollup
