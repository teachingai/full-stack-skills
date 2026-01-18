# Plugins

## Instructions

This example demonstrates creating and using Vue plugins.

### Key Concepts

- Plugin definition
- Plugin installation
- Plugin options
- Global properties

### Example: Basic Plugin

```javascript
// plugins/myPlugin.js
export default {
  install(app, options) {
    app.config.globalProperties.$myMethod = (key) => {
      return options[key]
    }
    
    app.provide('i18n', options)
  }
}

// main.js
import { createApp } from 'vue'
import App from './App.vue'
import myPlugin from './plugins/myPlugin'

const app = createApp(App)
app.use(myPlugin, {
  greetings: {
    hello: 'Bonjour!'
  }
})
app.mount('#app')
```

### Key Points

- Plugins extend Vue functionality globally
- Use `install` method to define plugin
- Access options in install function
- Use `app.use()` to install plugins
