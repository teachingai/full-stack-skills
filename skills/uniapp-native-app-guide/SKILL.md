---
name: uniapp-native-app-guide
description: A comprehensive skill for uni-app native app offline packaging. Use this skill whenever the user wants to package uni-app as native Android or iOS apps, configure native app settings, customize native features, or integrate native plugins. This skill provides complete documentation, examples, and best practices based on the official native app packaging documentation.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Package uni-app as native Android app
- Package uni-app as native iOS app
- Configure native app settings (manifest, permissions, etc.)
- Customize native app features
- Integrate native plugins
- Configure app signing and certificates
- Handle native app build and distribution

## How to use this skill

To package native apps:

1. **Identify the platform** from the user's request:
   - Android → Use Android examples
   - iOS → Use iOS examples

2. **Load the appropriate example file** from the `examples/` directory:
   - `examples/guide/` - Native app packaging guide
   - `examples/android/` - Android packaging examples
   - `examples/ios/` - iOS packaging examples

3. **Load the appropriate template** from the `templates/` directory:
   - `templates/build-config.md` - Build configuration templates

4. **Follow the specific instructions** in those files for packaging

## Examples and Templates

### Examples

Located in `examples/`:

- **guide/** - Native app packaging guide and setup
- **android/** - Android packaging examples
- **ios/** - iOS packaging examples

### Templates

Located in `templates/`:

- **build-config.md** - Build configuration templates

## Best Practices

1. **Follow platform guidelines**: Adhere to Android and iOS development standards
2. **Optimize app size**: Minimize APK/IPA size
3. **Security**: Properly configure app signing and certificates
4. **Testing**: Test on real devices before release

## Resources

- **Official Documentation**: https://nativesupport.dcloud.net.cn/AppDocs/

## Keywords

native app, 原生App, Android打包, iOS打包, 离线打包, app packaging, native plugin
