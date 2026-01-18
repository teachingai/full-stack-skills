---
name: dart-sass-guide
description: A comprehensive skill for using Dart Sass, the primary implementation of Sass. Dart Sass is the recommended implementation of Sass, providing fast compilation and full compatibility with the Sass language. Use this skill whenever the user needs to compile Sass/SCSS files, configure Sass in projects, use Sass syntax features, or integrate Sass into build processes.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and configure Dart Sass
- Compile Sass/SCSS files to CSS
- Use Sass syntax features (variables, nesting, mixins, functions, etc.)
- Work with Sass modules and imports
- Integrate Sass into build tools or workflows
- Use Sass CLI commands
- Configure Sass compilation options
- Use Sass in JavaScript or Dart projects
- Optimize Sass compilation performance
- Handle Sass source maps

## How to use this skill

To use Dart Sass:

1. **Install Dart Sass**:
   - Load `examples/getting-started/installation.md` for installation instructions
   - Load `examples/getting-started/basic-usage.md` for basic usage examples
   - Load `examples/getting-started/compiling-modes.md` for different compilation modes

2. **Learn Sass syntax**:
   - Load `examples/syntax/variables.md` for variable usage
   - Load `examples/syntax/nesting.md` for nesting syntax
   - Load `examples/syntax/mixins.md` for mixins
   - Load `examples/syntax/functions.md` for functions
   - Load `examples/syntax/operators.md` for operators
   - Load `examples/syntax/at-rules.md` for at-rules

3. **Use advanced features**:
   - Load `examples/features/modules.md` for module system
   - Load `examples/features/imports.md` for imports
   - Load `examples/features/control-flow.md` for control flow
   - Load `examples/features/built-in-modules.md` for built-in modules
   - Load `examples/features/source-maps.md` for source maps
   - Load `examples/features/custom-functions.md` for custom functions

4. **Reference the API documentation** when needed:
   - `api/js-api.md` - JavaScript API reference
   - `api/dart-api.md` - Dart API reference
   - `api/cli-api.md` - CLI command reference

5. **Use templates** for quick start:
   - `templates/basic-project.md` - Basic Sass project template
   - `templates/modular-project.md` - Modular Sass project template
   - `templates/build-integration.md` - Build tool integration template

## Examples and Templates

### Getting Started
- **Installation**: `examples/getting-started/installation.md` - How to install Dart Sass on different platforms
- **Basic Usage**: `examples/getting-started/basic-usage.md` - Basic compilation examples
- **Compiling Modes**: `examples/getting-started/compiling-modes.md` - Different compilation modes and options

### Syntax
- **Variables**: `examples/syntax/variables.md` - Variable declarations and usage
- **Nesting**: `examples/syntax/nesting.md` - Nesting selectors and properties
- **Mixins**: `examples/syntax/mixins.md` - Mixin definitions and usage
- **Functions**: `examples/syntax/functions.md` - Function definitions and usage
- **Operators**: `examples/syntax/operators.md` - Mathematical and string operators
- **At-Rules**: `examples/syntax/at-rules.md` - @use, @forward, @import, @include, etc.

### Features
- **Modules**: `examples/features/modules.md` - Module system with @use and @forward
- **Imports**: `examples/features/imports.md` - Importing files and modules
- **Control Flow**: `examples/features/control-flow.md` - @if, @for, @each, @while
- **Built-in Modules**: `examples/features/built-in-modules.md` - sass:math, sass:color, sass:string, etc.
- **Source Maps**: `examples/features/source-maps.md` - Source map configuration
- **Custom Functions**: `examples/features/custom-functions.md` - Creating custom Sass functions

### Templates
- **Basic Project**: `templates/basic-project.md` - Basic Sass project structure
- **Modular Project**: `templates/modular-project.md` - Modular Sass project with @use
- **Build Integration**: `templates/build-integration.md` - Integrating Sass with build tools

## API Reference

- **JavaScript API**: `api/js-api.md` - JavaScript API for compiling Sass (compile, compileString, etc.)
- **Dart API**: `api/dart-api.md` - Dart API for compiling Sass
- **CLI API**: `api/cli-api.md` - Command-line interface options and usage

## Best Practices

1. **Use @use instead of @import**: The @import rule is deprecated, use @use and @forward instead
2. **Organize with modules**: Use the module system to organize and share code
3. **Optimize compilation**: Use appropriate output style (compressed for production)
4. **Source maps**: Enable source maps for development, disable for production
5. **Watch mode**: Use --watch for development to automatically recompile on changes
6. **Load paths**: Use --load-path to simplify import paths
7. **Performance**: Use Dart Sass for best performance (faster than Ruby Sass)
8. **Version control**: Don't commit compiled CSS files, only commit Sass source files

## Resources

- **Official Website**: https://sass-lang.com/dart-sass/
- **Installation Guide**: https://sass-lang.com/install/
- **Documentation**: https://sass-lang.com/documentation/
- **GitHub Repository**: https://github.com/sass/dart-sass
- **npm Package**: https://www.npmjs.com/package/sass
- **pub.dev Package**: https://pub.dev/packages/sass

## Keywords

dart-sass, sass, scss, css preprocessor, sass compiler, sass syntax, sass modules, sass mixins, sass functions, sass variables, sass nesting, @use, @forward, @import, @include, @mixin, @function, sass:math, sass:color, sass:string, source maps, sass cli, sass api, 样式预处理器, Sass 编译器, Sass 语法, Sass 模块, Sass 混合, Sass 函数
