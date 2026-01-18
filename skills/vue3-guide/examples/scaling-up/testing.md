# Testing

## Instructions

This example demonstrates testing Vue 3 applications using various testing frameworks.

### Key Concepts

- Unit testing
- Component testing
- E2E testing
- Testing utilities
- Mocking

### Example: Vitest Setup

```bash
# Install Vitest
npm install -D vitest @vue/test-utils jsdom
```

### Example: Vitest Configuration

```javascript
// vitest.config.js
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    environment: 'jsdom',
    globals: true
  }
})
```

### Example: Component Testing

```javascript
// Counter.spec.js
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import Counter from './Counter.vue'

describe('Counter', () => {
  it('renders correctly', () => {
    const wrapper = mount(Counter)
    expect(wrapper.text()).toContain('Count: 0')
  })

  it('increments count on button click', async () => {
    const wrapper = mount(Counter)
    await wrapper.find('button').trigger('click')
    expect(wrapper.text()).toContain('Count: 1')
  })
})
```

### Example: Testing with Composition API

```javascript
// useCounter.spec.js
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import { useCounter } from './useCounter'

describe('useCounter', () => {
  it('increments count', () => {
    const wrapper = mount({
      setup() {
        const { count, increment } = useCounter()
        return { count, increment }
      },
      template: '<div>{{ count }}</div>'
    })
    
    expect(wrapper.text()).toBe('0')
    wrapper.vm.increment()
    expect(wrapper.text()).toBe('1')
  })
})
```

### Example: E2E Testing with Playwright

```bash
# Install Playwright
npm install -D @playwright/test
```

```javascript
// e2e/example.spec.js
import { test, expect } from '@playwright/test'

test('homepage loads', async ({ page }) => {
  await page.goto('http://localhost:5173')
  await expect(page.locator('h1')).toContainText('Vue 3')
})
```

### Key Points

- Vitest is recommended for unit testing
- @vue/test-utils provides component testing utilities
- Use jsdom for DOM environment in tests
- Playwright or Cypress for E2E testing
- Mock external dependencies in tests
