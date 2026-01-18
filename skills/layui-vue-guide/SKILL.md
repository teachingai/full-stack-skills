---
name: layui-vue-guide
description: Layui Vue 完整使用指南，基于官方文档（https://www.layui-vue.com/），涵盖组件使用、API 参考、配置选项等核心概念和最佳实践。Layui Vue 是一个基于 Vue 3 的组件库，提供丰富的 UI 组件，包括按钮、表格、日期选择器、弹层等常用组件。
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and set up Layui Vue in a Vue 3 project
- Use Layui Vue components (Button, Table, DatePicker, etc.)
- Configure Layui Vue (theme, i18n, etc.)
- Use Layer component for modals and dialogs
- Implement forms with Layui Vue components
- Use data tables with sorting and pagination
- Handle file uploads
- Create dropdowns and tooltips
- Use date and time pickers
- Customize component styles
- Understand Layui Vue API and methods
- Troubleshoot Layui Vue issues

## How to use this skill

This skill is organized to match the Layui Vue official documentation structure (https://www.layui-vue.com/zh-CN/index, https://www.layui-vue.com/zh-CN/guide/introduce, https://www.layui-vue.com/zh-CN/components). When working with Layui Vue:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started.md`
   - Introduction/介绍 → `examples/introduce.md`
   - Components/组件 → `examples/components/`
   - API/API 文档 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始)**:
   - `examples/getting-started.md` - Installation and setup
   - `examples/introduce.md` - Introduction to Layui Vue

   **Components (组件)**:
   - `examples/components/button.md` - Button component
   - `examples/components/table.md` - Table component
   - `examples/components/date-picker.md` - DatePicker component
   - `examples/components/dropdown.md` - Dropdown component
   - `examples/components/tooltip.md` - Tooltip component
   - `examples/components/layer.md` - Layer component (modals/dialogs)
   - `examples/components/segmented.md` - Segmented component
   - `examples/components/tag-input.md` - TagInput component
   - `examples/components/time-select.md` - TimeSelect component
   - `examples/components/upload.md` - Upload component
   - `examples/components/form.md` - Form component
   - `examples/components/input.md` - Input component
   - `examples/components/select.md` - Select component
   - `examples/components/checkbox.md` - Checkbox component
   - `examples/components/radio.md` - Radio component
   - `examples/components/switch.md` - Switch component

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Layui Vue is built for Vue 3
   - Components use Composition API
   - Supports TypeScript
   - Examples include both JavaScript and TypeScript versions
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/layer-api.md` - Layer API methods
   - `api/component-api.md` - Component API reference

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/component-usage.md` - Component usage templates

### 1. Understanding Layui Vue

Layui Vue is a Vue 3 component library that provides a rich set of UI components, following the design philosophy of Layui.

**Key Concepts**:
- **Vue 3 Support**: Built with Vue 3 Composition API
- **Rich Components**: Button, Table, DatePicker, Layer, etc.
- **TypeScript**: Full TypeScript support
- **Theme Customization**: Support for theme customization
- **i18n**: Internationalization support

### 2. Installation

**Using npm**:

```bash
npm install @layui/layui-vue
```

**Using yarn**:

```bash
yarn add @layui/layui-vue
```

**Using pnpm**:

```bash
pnpm add @layui/layui-vue
```

### 3. Basic Setup

```javascript
// main.js
import { createApp } from 'vue'
import LayuiVue from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(LayuiVue)
app.mount('#app')
```

### 4. Basic Component Usage

```vue
<template>
  <lay-button type="primary">Button</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
</script>
```

## Examples and Templates

This skill includes detailed examples organized to match the Layui Vue official documentation structure (https://www.layui-vue.com/zh-CN/components). All examples are in the `examples/` directory, organized by topic:

### Getting Started (快速开始) - `examples/`

- `examples/getting-started.md` - Installation and setup guide
- `examples/introduce.md` - Introduction to Layui Vue

### Components (组件) - `examples/components/`

- `examples/components/button.md` - Button component usage
- `examples/components/table.md` - Table component with data, sorting, pagination
- `examples/components/date-picker.md` - DatePicker component
- `examples/components/dropdown.md` - Dropdown component
- `examples/components/tooltip.md` - Tooltip component
- `examples/components/layer.md` - Layer component for modals and dialogs
- `examples/components/segmented.md` - Segmented component
- `examples/components/tag-input.md` - TagInput component
- `examples/components/time-select.md` - TimeSelect component
- `examples/components/upload.md` - Upload component
- `examples/components/form.md` - Form component
- `examples/components/input.md` - Input component
- `examples/components/select.md` - Select component
- `examples/components/checkbox.md` - Checkbox component
- `examples/components/radio.md` - Radio component
- `examples/components/switch.md` - Switch component

### Templates Directory (`templates/`)

- `templates/installation.md` - Installation and setup templates
- `templates/component-usage.md` - Component usage templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/installation.md` for installation templates
- Use `templates/component-usage.md` for component usage templates
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Layui Vue API documentation structure:

### Layer API (`api/layer-api.md`)
- `layer.open()` - Open modal/dialog
- `layer.close()` - Close layer
- `layer.msg()` - Show message
- `layer.confirm()` - Show confirmation dialog
- `layer.load()` - Show loading
- `layer.drawer()` - Show drawer

### Component API (`api/component-api.md`)
- Component props and events
- Component methods
- Component slots

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use TypeScript**: Take advantage of TypeScript support
2. **Import on demand**: Import only needed components
3. **Follow component API**: Use props and events correctly
4. **Customize theme**: Use theme variables for customization
5. **Handle events**: Properly handle component events
6. **Use Layer API**: Use Layer API for modals and dialogs

## Resources

- **Official Documentation**: https://www.layui-vue.com/zh-CN/index
- **Getting Started**: https://www.layui-vue.com/zh-CN/guide/introduce
- **Components**: https://www.layui-vue.com/zh-CN/components
- **GitHub Repository**: https://github.com/layui-vue/layui-vue

## Keywords

Layui Vue, layui-vue, Vue 3, component library, UI components, Button, Table, DatePicker, Layer, Dropdown, Tooltip, Form, Input, Select, Checkbox, Radio, Switch, Upload, 组件库, 按钮, 表格, 日期选择器, 弹层, 下拉菜单, 提示, 表单, 输入框, 选择器, 复选框, 单选框, 开关, 上传
