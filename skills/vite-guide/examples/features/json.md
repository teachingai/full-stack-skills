# JSON

## Instructions

This example demonstrates JSON importing and transformation in Vite.

### Key Concepts

- JSON importing
- Named imports
- JSON stringify
- JSON5 support

### Example: Basic JSON Import

```javascript
// data.json
{
  "name": "Vite",
  "version": "5.0.0"
}

// main.js
import data from './data.json'
console.log(data.name)  // "Vite"
```

### Example: Named Imports

```javascript
// vite.config.js
export default defineConfig({
  json: {
    namedExports: true,
    stringify: false
  }
})

// main.js
import { name, version } from './data.json'
```

### Example: JSON Stringify

```javascript
// vite.config.js
export default defineConfig({
  json: {
    stringify: true  // Import as string
  }
})

// main.js
import jsonString from './data.json'
console.log(jsonString)  // String representation
```

### Example: JSON5 Support

```javascript
// Install json5 plugin
// npm install -D vite-plugin-json5

import json5 from 'vite-plugin-json5'

export default defineConfig({
  plugins: [json5()]
})

// data.json5
{
  name: 'Vite',
  version: '5.0.0'
}
```

### Key Points

- JSON files can be imported directly
- Enable `namedExports` for named imports
- Use `stringify: true` to import as string
- JSON5 requires additional plugin
