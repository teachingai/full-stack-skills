# Components API | 组件 API

## API Reference

Vant Vue 3.0 component APIs and props.

### Common Props

Most components share common props:

- `custom-style`: Custom style object
- `custom-class`: Custom CSS class
- `disabled`: Disabled state
- `loading`: Loading state

### Button API

**Props:**
- `type`: Button type (primary, success, warning, danger, default)
- `size`: Button size (large, normal, small, mini)
- `shape`: Button shape (square, round)
- `plain`: Plain button style
- `disabled`: Disabled state
- `loading`: Loading state
- `icon`: Icon name
- `@click`: Click handler

### Cell API

**Props:**
- `title`: Cell title
- `value`: Cell value
- `label`: Cell label
- `icon`: Cell icon
- `is-link`: Show arrow
- `arrow-direction`: Arrow direction
- `@click`: Click handler

### Form API

**Props:**
- `@submit`: Submit handler
- `@failed`: Failed handler

**Methods:**
- `validate()`: Validate form
- `resetValidation()`: Reset validation

**Field Props:**
- `v-model`: Field value
- `name`: Field name
- `label`: Field label
- `placeholder`: Placeholder text
- `:rules`: Validation rules
- `disabled`: Disabled state

### Dialog API

**Props:**
- `v-model:show`: Dialog visibility
- `title`: Dialog title
- `message`: Dialog message
- `show-cancel-button`: Show cancel button
- `confirm-button-text`: Confirm button text
- `cancel-button-text`: Cancel button text
- `@confirm`: Confirm handler
- `@cancel`: Cancel handler

**Methods:**
- `showDialog(options)`: Show dialog
- `showConfirmDialog(options)`: Show confirm dialog

### Toast API

**Props (via showToast):**
- `type`: Toast type (success, fail, loading)
- `message`: Toast message
- `duration`: Toast duration (milliseconds)
- `position`: Toast position (top, middle, bottom)

**Methods:**
- `showToast(message | options)`: Show toast
- `showSuccessToast(message)`: Show success toast
- `showFailToast(message)`: Show fail toast
- `showLoadingToast(message)`: Show loading toast

### Popup API

**Props:**
- `v-model:show`: Popup visibility
- `position`: Popup position (top, bottom, left, right, center)
- `round`: Round corners
- `closeable`: Show close button
- `close-icon-position`: Close button position
- `overlay`: Show overlay
- `@close`: Close handler

### Key Points

- All components support custom-style and custom-class props
- Most components support disabled and loading props
- Form components use v-model for two-way binding
- Dialog and Popup use v-model:show for visibility control
- Toast is available via showToast function
- Components are optimized for mobile touch interactions
