# RouterLink Component API

## API Reference

RouterLink component props and usage.

### RouterLink Props

#### to

**Type:** `string | Location`

Required. Denotes the target route of the link.

**Example:**
```vue
<router-link to="/home">Home</router-link>
<router-link :to="{ name: 'user', params: { id: 123 }}">User</router-link>
```

#### replace

**Type:** `boolean`

Default: `false`

When present, clicking the link will call `router.replace()` instead of `router.push()`.

**Example:**
```vue
<router-link to="/home" replace>Home</router-link>
```

#### append

**Type:** `boolean`

Default: `false`

When present, the relative path will be appended to the current path.

**Example:**
```vue
<!-- If current path is /user/123 -->
<router-link to="profile" append>Profile</router-link>
<!-- Results in /user/123/profile -->
```

#### tag

**Type:** `string`

Default: `"a"`

Specify which tag to render.

**Example:**
```vue
<router-link to="/home" tag="button">Home</router-link>
```

#### active-class

**Type:** `string`

Default: `"router-link-active"`

Configure the active CSS class applied when the link is active.

**Example:**
```vue
<router-link to="/home" active-class="active">Home</router-link>
```

#### exact

**Type:** `boolean`

Default: `false`

The default active class matching behavior is inclusive match. Setting this prop forces the link into "exact match mode".

**Example:**
```vue
<router-link to="/" exact>Home</router-link>
```

#### exact-active-class

**Type:** `string`

Default: `"router-link-exact-active"`

Configure the active CSS class applied when the link is active with exact match.

**Example:**
```vue
<router-link to="/" exact exact-active-class="exact-active">Home</router-link>
```

#### event

**Type:** `string | Array<string>`

Default: `"click"`

Specify the event(s) that can trigger the link navigation.

**Example:**
```vue
<router-link to="/home" event="mouseover">Home</router-link>
```

### RouterLink Scoped Slot

**Available in Vue Router 3.1.0+**

```vue
<router-link
  to="/home"
  custom
  v-slot="{ href, route, navigate, isActive, isExactActive }">
  <a :href="href" @click="navigate">
    {{ route.name }}
    <span v-if="isActive">(active)</span>
  </a>
</router-link>
```

**See also:** `examples/navigation.md`
