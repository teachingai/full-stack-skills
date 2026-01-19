---
name: vant-vue3
description: Provides comprehensive guidance for Vant Vue 3 mobile component library including mobile components, themes, and best practices. Use when the user asks about Vant, needs to build mobile applications with Vue 3, or implement mobile UI components.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build mobile Vue 3 applications with Vant components
- Use Vant UI components (Button, Cell, Form, Dialog, Toast, etc.)
- Create mobile-friendly interfaces
- Customize Vant theme
- Implement internationalization with Vant
- Use Vant with TypeScript
- Handle mobile gestures and interactions
- Implement mobile navigation patterns
- Use mobile form components
- Create mobile data display components

## How to use this skill

This skill is organized to match the Vant Vue 3.0 official documentation structure (https://vant-ui.github.io/vant/#/zh-CN). When working with Vant:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/installation.md` or `examples/getting-started/basic-usage.md`
   - Button/按钮 → `examples/components/button.md`
   - Cell/单元格 → `examples/components/cell.md`
   - Form/表单 → `examples/components/form.md`
   - Dialog/对话框 → `examples/components/dialog.md`
   - Toast/提示 → `examples/components/toast.md`
   - Popup/弹出层 → `examples/components/popup.md`
   - Theme/主题 → `examples/advanced/theme-customization.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/installation.md` - Installing Vant and basic setup
   - `examples/getting-started/basic-usage.md` - Basic component usage

   **Components (组件) - `examples/components/`**:
   - `examples/components/button.md` - Button component
   - `examples/components/cell.md` - Cell component
   - `examples/components/icon.md` - Icon component
   - `examples/components/image.md` - Image component
   - `examples/components/popup.md` - Popup component
   - `examples/components/toast.md` - Toast component
   - `examples/components/dialog.md` - Dialog component
   - `examples/components/form.md` - Form component
   - `examples/components/field.md` - Field component
   - `examples/components/picker.md` - Picker component
   - `examples/components/calendar.md` - Calendar component
   - `examples/components/tabs.md` - Tabs component
   - `examples/components/tabbar.md` - Tabbar component
   - `examples/components/navbar.md` - Navbar component
   - `examples/components/list.md` - List component
   - `examples/components/grid.md` - Grid component
   - `examples/components/card.md` - Card component
   - `examples/components/badge.md` - Badge component
   - `examples/components/loading.md` - Loading component
   - `examples/components/action-sheet.md` - ActionSheet component

   **Advanced (高级) - `examples/advanced/`**:
   - `examples/advanced/theme-customization.md` - Customizing Vant theme
   - `examples/advanced/internationalization.md` - Internationalization setup
   - `examples/advanced/typescript.md` - TypeScript support

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Vant Vue 3.0 API
   - Examples use Composition API syntax
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns
   - Vant is optimized for mobile devices

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/components.md` - Component API reference
   - `api/config-provider.md` - ConfigProvider API
   - `api/hooks.md` - Composition Hooks API

5. **Use templates** from the `templates/` directory:
   - `templates/project-setup.md` - Project setup templates
   - `templates/component-template.md` - Component usage templates

## Examples and Templates

This skill includes detailed examples organized to match the Vant Vue 3.0 official documentation structure (https://vant-ui.github.io/vant/#/zh-CN). All examples are in the `examples/` directory, organized by topic:

### Getting Started (快速开始) - `examples/getting-started/`

- `examples/getting-started/installation.md` - Installing Vant, importing styles, and basic setup
- `examples/getting-started/basic-usage.md` - Basic component usage examples

### Components (组件) - `examples/components/`

**Basic (基础)**:
- `examples/components/button.md` - Button component
- `examples/components/cell.md` - Cell component
- `examples/components/icon.md` - Icon component
- `examples/components/image.md` - Image component
- `examples/components/popup.md` - Popup component

**Form (表单)**:
- `examples/components/form.md` - Form component
- `examples/components/field.md` - Field component
- `examples/components/picker.md` - Picker component
- `examples/components/calendar.md` - Calendar component
- `examples/components/checkbox.md` - Checkbox component
- `examples/components/radio.md` - Radio component
- `examples/components/switch.md` - Switch component
- `examples/components/uploader.md` - Uploader component

**Feedback (反馈)**:
- `examples/components/toast.md` - Toast component
- `examples/components/dialog.md` - Dialog component
- `examples/components/loading.md` - Loading component
- `examples/components/action-sheet.md` - ActionSheet component
- `examples/components/notify.md` - Notify component

**Display (展示)**:
- `examples/components/list.md` - List component
- `examples/components/card.md` - Card component
- `examples/components/badge.md` - Badge component
- `examples/components/tag.md` - Tag component
- `examples/components/empty.md` - Empty component
- `examples/components/skeleton.md` - Skeleton component

**Navigation (导航)**:
- `examples/components/tabs.md` - Tabs component
- `examples/components/tabbar.md` - Tabbar component
- `examples/components/navbar.md` - Navbar component
- `examples/components/grid.md` - Grid component
- `examples/components/sidebar.md` - Sidebar component

### Advanced (高级) - `examples/advanced/`

- `examples/advanced/theme-customization.md` - Customizing Vant theme
- `examples/advanced/internationalization.md` - Internationalization setup
- `examples/advanced/typescript.md` - TypeScript support

### Templates Directory (`templates/`)

- `templates/project-setup.md` - Vant project setup templates
- `templates/component-template.md` - Component usage templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/project-setup.md` for project setup
- Use component templates for quick setup
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Vant Vue 3.0 API documentation structure:

### Components API (`api/components.md`)
- All component props and APIs
- Component events and slots
- Component types and interfaces

### ConfigProvider API (`api/config-provider.md`)
- ConfigProvider component API
- Global configuration options
- Theme configuration

### Hooks API (`api/hooks.md`)
- Composition hooks (useClickAway, useWindowSize, etc.)
- Utility hooks

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Import Vant CSS**: Import Vant CSS in your entry file
2. **Use Composition API**: Prefer Composition API for Vue 3 projects
3. **Tree-shaking**: Import components individually for better tree-shaking
4. **Mobile-first**: Design for mobile devices first
5. **Touch interactions**: Consider touch gestures and interactions
6. **Performance**: Optimize for mobile performance
7. **Theme customization**: Use CSS variables for consistent theming
8. **Internationalization**: Use ConfigProvider with locale for i18n
9. **TypeScript**: Use TypeScript for better type safety
10. **Component composition**: Compose components for complex UIs

## Resources

- **Official Website**: https://vant-ui.github.io/
- **Documentation**: https://vant-ui.github.io/vant/#/zh-CN
- **GitHub Repository**: https://github.com/youzan/vant

## Keywords

Vant, Vant Vue 3, mobile UI, Vue 3, components, Button, Cell, Form, Dialog, Toast, Popup, Tabs, Tabbar, Navbar, theme, customization, internationalization, i18n, TypeScript, 组件库, 按钮, 单元格, 表单, 对话框, 提示, 弹出层, 标签页, 标签栏, 导航栏, 主题定制, 国际化
