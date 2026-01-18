# RouterLink and RouterView Components | RouterLink 和 RouterView 组件

## API Reference

Vue Router component APIs.

### RouterLink

Component for declarative navigation.

**Props:**
```typescript
interface RouterLinkProps {
  to: RouteLocationRaw
  replace?: boolean
  custom?: boolean
  activeClass?: string
  exactActiveClass?: string
  ariaCurrentValue?: 'page' | 'step' | 'location' | 'date' | 'time' | 'true' | 'false'
}
```

**Example:**
```vue
<RouterLink to="/home">Home</RouterLink>
<RouterLink :to="{ name: 'User', params: { id: '123' } }">User</RouterLink>
<RouterLink to="/about" replace>About</RouterLink>
```

### RouterView

Component for rendering matched route component.

**Props:**
```typescript
interface RouterViewProps {
  name?: string
  route?: RouteLocationNormalizedLoaded
}
```

**Example:**
```vue
<RouterView />
<RouterView name="sidebar" />
```

### RouterLink Slots

```vue
<RouterLink to="/home" custom v-slot="{ href, route, navigate, isActive, isExactActive }">
  <a :href="href" @click="navigate" :class="{ active: isActive }">
    {{ route.name }}
  </a>
</RouterLink>
```

### Key Points

- RouterLink provides declarative navigation
- RouterView renders matched components
- Can use named views with `name` prop
- Custom slot provides full control
- Active classes for styling active links
