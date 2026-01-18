# History Mode

## Instructions

This example demonstrates history mode vs hash mode in Vue Router v3.

### Key Concepts

- History mode
- Hash mode
- Server configuration
- Fallback handling

### Example: History Mode Configuration

```javascript
// router/index.js
const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About }
  ]
})
```

### Example: Hash Mode (Default)

```javascript
const router = new VueRouter({
  mode: 'hash',  // Default mode
  routes: [...]
})
// URLs: http://example.com/#/about
```

### Example: Abstract Mode

```javascript
const router = new VueRouter({
  mode: 'abstract',  // For non-browser environments
  routes: [...]
})
```

### Example: Server Configuration (Apache)

```apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteBase /
  RewriteRule ^index\.html$ - [L]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule . /index.html [L]
</IfModule>
```

### Example: Server Configuration (Nginx)

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

### Example: Fallback Configuration

```javascript
const router = new VueRouter({
  mode: 'history',
  fallback: true,  // Fallback to hash mode in IE9
  routes: [...]
})
```

### Key Points

- History mode uses HTML5 History API
- Hash mode uses URL hash (#)
- History mode requires server configuration
- Hash mode works without server config
- Use fallback for browser compatibility
