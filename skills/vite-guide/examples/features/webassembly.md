# WebAssembly

## Instructions

This example demonstrates WebAssembly support in Vite.

### Key Concepts

- WASM imports
- WASM instantiation
- WASM modules

### Example: Importing WASM

```javascript
// Import WASM module
import init, { add, multiply } from './wasm/math.wasm'

// Initialize
await init()

// Use functions
const result = add(1, 2)
const product = multiply(3, 4)
```

### Example: WASM with ?init

```javascript
// Import with ?init suffix
import init from './wasm/math.wasm?init'

const wasm = await init()
const result = wasm.exports.add(1, 2)
```

### Example: WASM Module

```javascript
// wasm/math.wasm compiled from Rust/C/C++
// Exports: add, multiply functions

// main.js
import init from './wasm/math.wasm?init'

const wasm = await init()
console.log(wasm.exports.add(5, 3))  // 8
```

### Key Points

- WASM files can be imported directly
- Use `?init` suffix for initialization
- WASM modules are loaded asynchronously
- Supports Rust, C, C++ compiled WASM
