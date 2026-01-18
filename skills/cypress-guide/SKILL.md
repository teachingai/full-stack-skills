---
name: cypress-guide
description: Cypress 完整使用指南，基于官方文档（https://docs.cypress.io/），涵盖 E2E 测试、组件测试、API 等核心概念和最佳实践。Cypress 是一个现代化的端到端测试框架，也支持组件测试，特别适合 Vue、React 等框架的组件测试。适用于编写可靠的 E2E 测试和组件测试。
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Cypress for E2E testing
- Write component tests for Vue or React components
- Configure Cypress for a project
- Use Cypress commands and APIs
- Debug tests with Cypress
- Set up test fixtures and data
- Handle async operations in tests
- Test user interactions and workflows
- Mock API calls and network requests
- Test component rendering and behavior
- Configure Cypress for CI/CD
- Use Cypress utilities and helpers
- Understand Cypress best practices
- Troubleshoot Cypress issues

## How to use this skill

This skill is organized to match the Cypress official documentation structure (https://docs.cypress.io/app/get-started/why-cypress, https://docs.cypress.io/api/table-of-contents). When working with Cypress:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/`
   - Component testing/组件测试 → `examples/component-testing/`
   - API/API 文档 → `api/`
   - Commands/命令 → `api/commands.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始)**:
   - `examples/why-cypress.md` - Why use Cypress, key benefits
   - `examples/getting-started/open-the-app.md` - Opening Cypress App
   - `examples/getting-started/configuration-choices.md` - Configuration choices

   **Component Testing (组件测试)**:
   - `examples/component-testing/overview.md` - Component testing overview
   - `examples/component-testing/examples-vue.md` - Vue component testing examples
   - `examples/component-testing/configuration.md` - Component testing configuration
   - `examples/component-testing/styling-components.md` - Styling components in tests

   **E2E Testing (端到端测试)**:
   - `examples/e2e-testing/basics.md` - Basic E2E testing
   - `examples/e2e-testing/commands.md` - Common commands
   - `examples/e2e-testing/assertions.md` - Assertions
   - `examples/e2e-testing/network-requests.md` - Network request handling

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Cypress supports both E2E and Component testing
   - Component testing works with Vue, React, and other frameworks
   - Examples include both JavaScript and TypeScript versions
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/table-of-contents.md` - API table of contents
   - `api/commands.md` - Commands API reference
   - `api/cypress-api.md` - Cypress global API
   - `api/utilities.md` - Utilities API
   - `api/node-events.md` - Node events API

5. **Use templates** from the `templates/` directory:
   - `templates/cypress-config.md` - Cypress configuration templates
   - `templates/test-examples.md` - Test example templates

### 1. Understanding Cypress

Cypress is a next-generation front-end testing tool built for the modern web. It enables you to write tests that can run both in the browser (E2E) and in isolation (Component Testing).

**Key Concepts**:
- **E2E Testing**: Test entire user workflows in a real browser
- **Component Testing**: Test individual components in isolation
- **Time Travel**: See exactly what happened at each step
- **Real-time Reloads**: See commands execute in real time
- **Automatic Waiting**: No need for manual waits or sleeps

### 2. Installation

**Using npm**:

```bash
npm install -D cypress
```

**Using yarn**:

```bash
yarn add -D cypress
```

**Using pnpm**:

```bash
pnpm add -D cypress
```

### 3. Opening Cypress

```bash
# Open Cypress App
npx cypress open

# Run tests headlessly
npx cypress run
```

### 4. Basic Test Example

```javascript
// cypress/e2e/example.cy.js
describe('My First Test', () => {
  it('Does not do much!', () => {
    expect(true).to.equal(true)
  })
})
```

## Examples and Templates

This skill includes detailed examples organized to match the Cypress official documentation structure (https://docs.cypress.io/). All examples are in the `examples/` directory, organized by topic:

### Getting Started (快速开始) - `examples/getting-started/`

- `examples/why-cypress.md` - Why use Cypress, key benefits and features
- `examples/getting-started/open-the-app.md` - Opening Cypress App and Launchpad
- `examples/getting-started/configuration-choices.md` - Configuration choices and testing types

### Component Testing (组件测试) - `examples/component-testing/`

- `examples/component-testing/overview.md` - Component testing overview and framework support
- `examples/component-testing/examples-vue.md` - Vue component testing examples with cy.mount()
- `examples/component-testing/configuration.md` - Component testing configuration
- `examples/component-testing/styling-components.md` - Styling components in tests

### E2E Testing (端到端测试) - `examples/e2e-testing/`

- `examples/e2e-testing/basics.md` - Basic E2E testing concepts
- `examples/e2e-testing/commands.md` - Common Cypress commands
- `examples/e2e-testing/assertions.md` - Assertions and expectations
- `examples/e2e-testing/network-requests.md` - Network request handling and mocking

### Templates Directory (`templates/`)

- `templates/cypress-config.md` - Cypress configuration templates
- `templates/test-examples.md` - Test example templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/cypress-config.md` for Cypress configuration templates
- Use `templates/test-examples.md` for test example templates
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Cypress API documentation structure:

### API Table of Contents (`api/table-of-contents.md`)
- Overview of all Cypress APIs
- Commands, Cypress API, Utilities, Node Events

### Commands API (`api/commands.md`)
- Action commands (click, type, select, etc.)
- Query commands (get, find, contains, etc.)
- Assertion commands (should, expect, etc.)

### Cypress API (`api/cypress-api.md`)
- Cypress global API
- Configuration methods
- Custom commands
- Version and environment info

### Utilities API (`api/utilities.md`)
- Cypress utilities (Cypress._, Cypress.Blob, etc.)
- jQuery integration
- Helper functions

### Node Events API (`api/node-events.md`)
- Node-level events
- Plugin events
- Task events

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use data-cy attributes**: Prefer data-cy over class names for selectors
2. **Avoid hard waits**: Let Cypress automatically wait for elements
3. **Use custom commands**: Create reusable custom commands for common actions
4. **Organize tests**: Group related tests with describe blocks
5. **Use fixtures**: Load test data from fixtures
6. **Mock network requests**: Use cy.intercept() for API mocking
7. **Test user workflows**: Focus on testing user interactions, not implementation

## Resources

- **Official Documentation**: https://docs.cypress.io/
- **Getting Started**: https://docs.cypress.io/app/get-started/why-cypress
- **Component Testing**: https://docs.cypress.io/app/component-testing
- **API Reference**: https://docs.cypress.io/api/table-of-contents
- **GitHub Repository**: https://github.com/cypress-io/cypress

## Keywords

Cypress, cypress, E2E testing, end-to-end testing, component testing, test framework, cy commands, assertions, fixtures, mocking, cy.mount, cy.get, cy.click, cy.type, cy.intercept, 端到端测试, 组件测试, 测试框架, 断言, 模拟, 测试命令
