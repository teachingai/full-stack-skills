---
name: vitest
description: Provides comprehensive guidance for Vitest testing framework including fast test execution, Vite integration, component testing, mocking, and configuration. Use when the user asks about Vitest, needs to write fast unit tests, test Vue/React components, or configure Vitest with Vite projects.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Vitest in a Vite project
- Write unit tests and component tests
- Configure Vitest for different environments
- Use Vitest API and utilities
- Test Vue, React, or Svelte components
- Use browser mode for testing
- Set up visual regression testing
- Mock functions and modules
- Use snapshots for testing
- Configure test coverage
- Use Vitest UI
- Optimize test performance
- Debug tests
- Understand Vitest best practices
- Troubleshoot Vitest issues

## How to use this skill

This skill is organized to match the Vitest official documentation structure (https://vitest.dev/guide/, https://vitest.dev/api/, https://vitest.dev/config/). When working with Vitest:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started.md`
   - Features/功能特性 → `examples/features.md`
   - Component testing/组件测试 → `examples/component-testing.md`
   - Browser mode/浏览器模式 → `examples/browser-mode.md`
   - API/API 文档 → `api/`
   - Configuration/配置 → `examples/config/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始)**:
   - `examples/getting-started.md` - Installation and first test

   **Features (功能特性)**:
   - `examples/features.md` - Key features and capabilities
   - `examples/ui.md` - Vitest UI
   - `examples/component-testing.md` - Component testing
   - `examples/browser-mode.md` - Browser mode testing
   - `examples/visual-regression-testing.md` - Visual regression testing
   - `examples/trace-view.md` - Trace view

   **Testing (测试)**:
   - `examples/test-api.md` - Test API (test, it, describe, etc.)
   - `examples/mocking.md` - Mocking functions and modules
   - `examples/snapshots.md` - Snapshot testing
   - `examples/coverage.md` - Code coverage

   **Configuration (配置)**:
   - `examples/config/basic-config.md` - Basic configuration
   - `examples/config/environment.md` - Environment configuration
   - `examples/config/browser-config.md` - Browser mode configuration

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Vitest is designed for Vite projects
   - Supports TypeScript, JSX, ESM out of the box
   - Fast watch mode with HMR-like experience
   - Compatible with Jest API
   - Examples include both JavaScript and TypeScript versions
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/test-api.md` - Test API reference
   - `api/vi-utility.md` - vi utility functions
   - `api/expect.md` - Expect assertions
   - `api/mocking.md` - Mocking API

5. **Use templates** from the `templates/` directory:
   - `templates/vitest-config.md` - Vitest configuration templates
   - `templates/test-examples.md` - Test example templates

### 1. Understanding Vitest

Vitest is a blazing fast unit test framework powered by Vite. It's designed to work seamlessly with Vite projects and provides instant feedback during development.

**Key Concepts**:
- **Fast**: Powered by Vite's native ESM support
- **Compatible**: Jest-compatible API
- **Watch Mode**: Smart watch mode with HMR
- **TypeScript**: Native TypeScript support
- **Component Testing**: Test Vue, React, Svelte components

### 2. Installation

**Using npm**:

```bash
npm install -D vitest
```

**Using yarn**:

```bash
yarn add -D vitest
```

**Using pnpm**:

```bash
pnpm add -D vitest
```

### 3. Basic Setup

```javascript
// sum.js
export function sum(a, b) {
  return a + b
}

// sum.test.js
import { describe, it, expect } from 'vitest'
import { sum } from './sum'

describe('sum', () => {
  it('adds two numbers', () => {
    expect(sum(1, 2)).toBe(3)
  })
})
```

### 4. Running Tests

```json
{
  "scripts": {
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:run": "vitest run"
  }
}
```

## Examples and Templates

This skill includes detailed examples organized to match the Vitest official documentation structure (https://vitest.dev/guide/). All examples are in the `examples/` directory, organized by topic:

### Getting Started (快速开始) - `examples/`

- `examples/getting-started.md` - Installation, setup, and first test

### Features (功能特性) - `examples/`

- `examples/features.md` - Key features and capabilities
- `examples/ui.md` - Vitest UI usage
- `examples/component-testing.md` - Component testing setup and examples
- `examples/browser-mode.md` - Browser mode configuration and usage
- `examples/visual-regression-testing.md` - Visual regression testing
- `examples/trace-view.md` - Trace view for debugging

### Testing (测试) - `examples/`

- `examples/test-api.md` - Test API (test, it, describe, hooks)
- `examples/mocking.md` - Mocking functions and modules
- `examples/snapshots.md` - Snapshot testing
- `examples/coverage.md` - Code coverage configuration

### Configuration (配置) - `examples/config/`

- `examples/config/basic-config.md` - Basic Vitest configuration
- `examples/config/environment.md` - Environment configuration (jsdom, happy-dom, etc.)
- `examples/config/browser-config.md` - Browser mode configuration

### Templates Directory (`templates/`)

- `templates/vitest-config.md` - Vitest configuration templates
- `templates/test-examples.md` - Test example templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/vitest-config.md` for Vitest configuration templates
- Use `templates/test-examples.md` for test example templates
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Vitest API documentation structure:

### Test API (`api/test-api.md`)
- `test()`, `it()`, `describe()` - Test functions
- Hooks: `beforeEach()`, `afterEach()`, `beforeAll()`, `afterAll()`
- Test modifiers: `.skip()`, `.only()`, `.todo()`
- `bench()` - Benchmark testing

### vi Utility (`api/vi-utility.md`)
- `vi.fn()` - Create mock functions
- `vi.mock()` - Mock modules
- `vi.spyOn()` - Spy on functions
- `vi.waitFor()`, `vi.waitUntil()` - Async utilities

### Expect API (`api/expect.md`)
- `expect()` - Assertions
- Matchers: `toBe()`, `toEqual()`, `toMatchSnapshot()`, etc.
- Custom matchers

### Mocking API (`api/mocking.md`)
- Module mocking
- Function mocking
- Auto-mocking

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use watch mode**: Leverage Vitest's smart watch mode for faster feedback
2. **Organize tests**: Group related tests with describe blocks
3. **Use TypeScript**: Take advantage of native TypeScript support
4. **Mock effectively**: Use vi.mock() for module mocking
5. **Test components**: Use component testing for Vue/React components
6. **Use UI mode**: Use `--ui` flag for better test debugging experience
7. **Optimize performance**: Use test.only() during development

## Resources

- **Official Documentation**: https://vitest.dev/
- **Getting Started**: https://vitest.dev/guide/
- **API Reference**: https://vitest.dev/api/
- **Configuration**: https://vitest.dev/config/
- **GitHub Repository**: https://github.com/vitest-dev/vitest

## Keywords

Vitest, vitest, test framework, unit testing, component testing, Vite, Jest compatible, watch mode, HMR, TypeScript, ESM, mocking, snapshots, coverage, browser mode, visual regression testing, 测试框架, 单元测试, 组件测试, 监视模式, 热模块替换, 模拟, 快照, 覆盖率, 浏览器模式, 视觉回归测试
