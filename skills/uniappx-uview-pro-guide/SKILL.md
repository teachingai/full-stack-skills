---
name: uniappx-uview-pro-guide
description: A comprehensive skill for integrating and using uView Pro with UniAppX projects. This skill focuses on how to integrate uView Pro into UniAppX applications, configure UniAppX projects to work with uView Pro, handle platform-specific behaviors, and leverage UniAppX features with uView Pro components. Use this skill whenever the user needs to build UniAppX applications using uView Pro component library.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Integrate uView Pro into UniAppX projects
- Configure UniAppX projects to work with uView Pro
- Handle platform-specific behaviors when using uView Pro in UniAppX
- Use UniAppX features (pages.json, manifest.json, etc.) with uView Pro
- Build cross-platform UniAppX applications with uView Pro
- Configure easycom for automatic uView Pro component import in UniAppX
- Handle navigation and routing with uView Pro in UniAppX
- Use UniAppX APIs with uView Pro components
- Optimize UniAppX projects using uView Pro

## How to use this skill

To use uView Pro with UniAppX:

1. **Install and integrate** uView Pro into UniAppX project:
   - Load `examples/getting-started/installation.md` for installation in UniAppX
   - Load `examples/getting-started/project-setup.md` for UniAppX project configuration
   - Load `examples/getting-started/easycom-config.md` for easycom configuration

2. **Integrate with UniAppX features**:
   - Load `examples/integration/pages-config.md` for pages.json configuration
   - Load `examples/integration/manifest-config.md` for manifest.json configuration
   - Load `examples/integration/navigation.md` for navigation with uView Pro
   - Load `examples/integration/uniappx-api.md` for using UniAppX APIs with uView Pro

3. **Handle platform-specific behaviors**:
   - Load `examples/platform-specific/h5.md` for H5 platform considerations
   - Load `examples/platform-specific/miniprogram.md` for mini-program considerations
   - Load `examples/platform-specific/app.md` for App platform considerations
   - Load `examples/platform-specific/nvue.md` for nvue considerations

4. **Advanced integration**:
   - Load `examples/advanced/custom-theme.md` for theme customization in UniAppX
   - Load `examples/advanced/build-optimization.md` for build optimization
   - Load `examples/advanced/multi-platform.md` for multi-platform deployment

5. **Reference the API documentation** when needed:
   - `api/integration-api.md` - UniAppX and uView Pro integration API
   - `api/config-api.md` - Configuration API reference

6. **Use templates** for quick start:
   - `templates/basic-uniappx-project.md` - Basic UniAppX project with uView Pro
   - `templates/pages-template.md` - Pages configuration template
   - `templates/manifest-template.md` - Manifest configuration template

## Examples and Templates

### Getting Started
- **Installation**: `examples/getting-started/installation.md` - How to install uView Pro in UniAppX projects
- **Project Setup**: `examples/getting-started/project-setup.md` - Setting up UniAppX project with uView Pro
- **Easycom Config**: `examples/getting-started/easycom-config.md` - Configuring easycom for automatic component import

### Integration
- **Pages Config**: `examples/integration/pages-config.md` - Configuring pages.json with uView Pro
- **Manifest Config**: `examples/integration/manifest-config.md` - Configuring manifest.json for uView Pro
- **Navigation**: `examples/integration/navigation.md` - Navigation and routing with uView Pro
- **UniAppX API**: `examples/integration/uniappx-api.md` - Using UniAppX APIs with uView Pro components

### Platform-Specific
- **H5**: `examples/platform-specific/h5.md` - H5 platform considerations with uView Pro
- **Mini-Program**: `examples/platform-specific/miniprogram.md` - Mini-program considerations with uView Pro
- **App**: `examples/platform-specific/app.md` - App platform considerations with uView Pro
- **nvue**: `examples/platform-specific/nvue.md` - nvue considerations with uView Pro

### Advanced
- **Custom Theme**: `examples/advanced/custom-theme.md` - Customizing themes in UniAppX projects
- **Build Optimization**: `examples/advanced/build-optimization.md` - Optimizing UniAppX builds with uView Pro
- **Multi-Platform**: `examples/advanced/multi-platform.md` - Multi-platform deployment strategies

### Templates
- **Basic Project**: `templates/basic-uniappx-project.md` - Basic UniAppX project structure with uView Pro
- **Pages Template**: `templates/pages-template.md` - pages.json configuration template
- **Manifest Template**: `templates/manifest-template.md` - manifest.json configuration template

## API Reference

- **Integration API**: `api/integration-api.md` - UniAppX and uView Pro integration API reference
- **Config API**: `api/config-api.md` - Configuration API reference for UniAppX projects

## Best Practices

1. **Use easycom**: Configure easycom in pages.json for automatic uView Pro component import
2. **Platform Testing**: Test on all target platforms (H5, mini-programs, App)
3. **Use rpx Units**: Use rpx for responsive sizing in UniAppX, px for fixed sizes
4. **SCSS Support**: Ensure SCSS is properly configured in UniAppX project
5. **Manifest Configuration**: Properly configure manifest.json for each platform
6. **Conditional Compilation**: Use conditional compilation for platform-specific code
7. **Performance**: Optimize for each platform's specific requirements
8. **Navigation**: Use UniAppX navigation API with uView Pro components

## Resources

- **Official Plugin**: https://ext.dcloud.net.cn/plugin?id=24633
- **UniAppX Documentation**: https://uniapp.dcloud.net.cn/uni-app-x/
- **uView Pro**: https://uviewpro.cn/

## Keywords

uniappx, uniapp-x, uview-pro, uview pro, uniappx integration, uniappx configuration, easycom, pages.json, manifest.json, uni-app-x, 小程序, 跨平台, H5, App, nvue, 条件编译, 平台差异
