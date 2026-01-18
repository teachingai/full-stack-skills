# Named Views

## Instructions

This example demonstrates named views and multiple router-view components.

### Key Concepts

- Named router-view
- Multiple views
- Components object
- View components

### Example: Basic Named Views

```vue
<template>
  <div>
    <router-view name="header" />
    <router-view />
    <router-view name="footer" />
  </div>
</template>
```

### Example: Route with Named Views

```javascript
// router/index.js
const routes = [
  {
    path: '/',
    components: {
      default: Home,
      header: Header,
      footer: Footer
    }
  }
]
```

### Example: Named Views with Nested Routes

```javascript
const routes = [
  {
    path: '/settings',
    components: {
      default: Settings,
      sidebar: SettingsSidebar
    },
    children: [
      {
        path: 'profile',
        components: {
          default: ProfileSettings,
          sidebar: SettingsSidebar
        }
      }
    ]
  }
]
```

### Example: Different Components for Different Views

```javascript
const routes = [
  {
    path: '/dashboard',
    components: {
      default: Dashboard,
      header: DashboardHeader,
      sidebar: DashboardSidebar
    }
  },
  {
    path: '/admin',
    components: {
      default: Admin,
      header: AdminHeader,
      sidebar: AdminSidebar
    }
  }
]
```

### Key Points

- Use `name` prop on `<router-view>` for named views
- Use `components` (plural) object in route config
- Default view uses `default` key
- Named views allow multiple components per route
- Useful for complex layouts with multiple sections
