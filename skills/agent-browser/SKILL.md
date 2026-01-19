---
name: agent-browser
description: A comprehensive skill for using agent-browser, a CLI tool for browser automation designed for AI agents, developed by Vercel Labs. This skill covers installation, core commands, selectors (refs, CSS, XPath, semantic locators), agent mode, sessions, options, and best practices. Use this skill whenever the user needs to automate browser interactions via CLI commands, especially for AI agents that need to interact with web pages.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Automate browser interactions via CLI commands
- Use browser automation for AI agents
- Navigate websites and interact with pages using command-line tools
- Use refs-based element selection for deterministic automation
- Integrate browser automation into AI agent workflows
- Capture snapshots of web pages with accessibility trees
- Fill forms, click elements, and extract content via CLI
- Use semantic locators for more reliable element selection
- Work with browser automation in agent mode with JSON output
- Manage multiple browser sessions
- Debug browser automation with headed mode
- Use authenticated sessions with custom headers
- Connect to existing browsers via CDP
- Stream browser viewport for live preview

## How to use this skill

This skill is organized to match the agent-browser official documentation structure (https://github.com/vercel-labs/agent-browser/blob/main/README.md). When working with agent-browser:

1. **Install agent-browser**:
   - Load `examples/getting-started/installation.md` for installation instructions

2. **Quick Start**:
   - Load `examples/quick-start/quick-start.md` for basic workflow examples

3. **Learn core commands**:
   - Load `examples/commands/basic-commands.md` for basic commands (open, click, fill, etc.)
   - Load `examples/commands/advanced-commands.md` for advanced commands (snapshot, eval, etc.)
   - Load `examples/commands/get-info/` for information retrieval commands
   - Load `examples/commands/check-state/` for state checking commands
   - Load `examples/commands/find-elements/` for semantic locator commands
   - Load `examples/commands/wait/` for wait commands
   - Load `examples/commands/mouse-control/` for mouse control commands
   - Load `examples/commands/browser-settings/` for browser configuration
   - Load `examples/commands/cookies-storage/` for cookies and storage management
   - Load `examples/commands/network/` for network interception
   - Load `examples/commands/tabs-windows/` for tab and window management
   - Load `examples/commands/frames/` for iframe handling
   - Load `examples/commands/dialogs/` for dialog handling
   - Load `examples/commands/debug/` for debugging commands
   - Load `examples/commands/navigation/` for navigation commands
   - Load `examples/commands/setup/` for setup commands

4. **Understand selectors**:
   - Load `examples/selectors/refs.md` for refs-based selection (@e1, @e2, etc.)
   - Load `examples/selectors/traditional-selectors.md` for CSS, XPath, and semantic locators

5. **Use agent mode**:
   - Load `examples/agent-mode/introduction.md` for agent mode overview
   - Load `examples/agent-mode/optimal-workflow.md` for optimal AI workflow
   - Load `examples/agent-mode/integration.md` for integrating with AI agents

6. **Advanced features**:
   - Load `examples/advanced/sessions.md` for session management
   - Load `examples/advanced/headed-mode.md` for debugging with visible browser
   - Load `examples/advanced/authenticated-sessions.md` for authentication via headers
   - Load `examples/advanced/custom-executable.md` for custom browser executable
   - Load `examples/advanced/cdp-mode.md` for Chrome DevTools Protocol integration
   - Load `examples/advanced/streaming.md` for browser viewport streaming
   - Load `examples/advanced/architecture.md` for architecture overview
   - Load `examples/advanced/platforms.md` for platform support
   - Load `examples/advanced/usage-with-agents.md` for AI agent integration patterns

7. **Configure options**:
   - Load `examples/options/global-options.md` for global CLI options
   - Load `examples/options/snapshot-options.md` for snapshot-specific options
   - Load `examples/options/session-options.md` for session management options

8. **Reference API documentation** when needed:
   - `api/commands.md` - Complete command reference
   - `api/selectors.md` - Selector reference
   - `api/options.md` - Options reference

9. **Use templates** for quick start:
   - `templates/basic-automation.md` - Basic automation workflow
   - `templates/ai-agent-workflow.md` - AI agent workflow template

## Examples and Templates

### Getting Started
- **Installation**: `examples/getting-started/installation.md` - Installing agent-browser CLI tool
- **Quick Start**: `examples/quick-start/quick-start.md` - Basic workflow examples

### Commands
- **Basic Commands**: `examples/commands/basic-commands.md` - Core commands (open, click, fill, type, etc.)
- **Advanced Commands**: `examples/commands/advanced-commands.md` - Advanced commands (snapshot, eval, screenshot, etc.)
- **Get Info**: `examples/commands/get-info/` - Information retrieval commands (get text, get html, get value, etc.)
- **Check State**: `examples/commands/check-state/` - State checking commands (is visible, is enabled, is checked)
- **Find Elements**: `examples/commands/find-elements/` - Semantic locator commands (find role, find text, find label, etc.)
- **Wait**: `examples/commands/wait/` - Wait commands (wait for element, wait for text, wait for URL, etc.)
- **Mouse Control**: `examples/commands/mouse-control/` - Mouse control commands (mouse move, mouse down, mouse up, mouse wheel)
- **Browser Settings**: `examples/commands/browser-settings/` - Browser configuration (set viewport, set device, set geo, etc.)
- **Cookies & Storage**: `examples/commands/cookies-storage/` - Cookies and storage management
- **Network**: `examples/commands/network/` - Network interception and mocking
- **Tabs & Windows**: `examples/commands/tabs-windows/` - Tab and window management
- **Frames**: `examples/commands/frames/` - Iframe handling
- **Dialogs**: `examples/commands/dialogs/` - Dialog handling (accept, dismiss)
- **Debug**: `examples/commands/debug/` - Debugging commands (trace, console, errors, highlight, state)
- **Navigation**: `examples/commands/navigation/` - Navigation commands (back, forward, reload)
- **Setup**: `examples/commands/setup/` - Setup commands (install)

### Selectors
- **Refs**: `examples/selectors/refs.md` - Using refs (@e1, @e2) for deterministic element selection
- **Traditional Selectors**: `examples/selectors/traditional-selectors.md` - CSS selectors, XPath, semantic locators

### Agent Mode
- **Introduction**: `examples/agent-mode/introduction.md` - Agent mode overview and JSON output
- **Optimal Workflow**: `examples/agent-mode/optimal-workflow.md` - Optimal AI workflow patterns
- **Integration**: `examples/agent-mode/integration.md` - Integrating with AI agents (Claude, Cursor, Copilot, etc.)

### Advanced Features
- **Sessions**: `examples/advanced/sessions.md` - Managing multiple isolated browser sessions
- **Headed Mode**: `examples/advanced/headed-mode.md` - Running browser in visible mode for debugging
- **Authenticated Sessions**: `examples/advanced/authenticated-sessions.md` - Using custom headers for authentication
- **Custom Executable**: `examples/advanced/custom-executable.md` - Using custom browser executable path
- **CDP Mode**: `examples/advanced/cdp-mode.md` - Connecting to existing browsers via Chrome DevTools Protocol
- **Streaming**: `examples/advanced/streaming.md` - Streaming browser viewport for live preview
- **Architecture**: `examples/advanced/architecture.md` - Architecture overview (client-daemon model)
- **Platforms**: `examples/advanced/platforms.md` - Platform support information
- **Usage with AI Agents**: `examples/advanced/usage-with-agents.md` - Integration patterns for AI agents

### Options
- **Global Options**: `examples/options/global-options.md` - Global CLI options (--session, --headers, --headed, --json, etc.)
- **Snapshot Options**: `examples/options/snapshot-options.md` - Snapshot-specific options (-i, -c, -d, -s)
- **Session Options**: `examples/options/session-options.md` - Session management options

### Templates
- **Basic Automation**: `templates/basic-automation.md` - Basic browser automation workflow
- **AI Agent Workflow**: `templates/ai-agent-workflow.md` - Complete AI agent workflow template

## API Reference

- **Commands API**: `api/commands.md` - Complete command reference with syntax and examples
- **Selectors API**: `api/selectors.md` - Selector types and usage reference
- **Options API**: `api/options.md` - All options reference

## Best Practices

1. **Use Refs**: Prefer refs (@e1, @e2) over traditional selectors for deterministic automation
2. **Snapshot First**: Always snapshot before interacting with elements to get refs
3. **Agent Mode**: Use `--json` flag for machine-readable output in agent mode
4. **Session Management**: Use `--session` to maintain state across commands
5. **Interactive Snapshot**: Use `-i` flag for interactive snapshot selection
6. **Semantic Locators**: Use semantic locators (role/name) when refs are not available
7. **Error Handling**: Check command exit codes and error messages
8. **Wait for Navigation**: Commands automatically wait for navigation to complete
9. **Headed Mode**: Use `--headed` for debugging, headless for production
10. **CDP Integration**: Use `--cdp` for Chrome DevTools Protocol integration
11. **Streaming**: Use `AGENT_BROWSER_STREAM_PORT` for live browser preview
12. **Authenticated Sessions**: Use `--headers` for authentication without login flows
13. **Custom Executable**: Use `--executable-path` for serverless deployments or custom browsers
14. **Snapshot Options**: Combine `-i`, `-c`, `-d`, `-s` options to optimize snapshot output

## Resources

- **GitHub Repository**: https://github.com/vercel-labs/agent-browser
- **Official README**: https://github.com/vercel-labs/agent-browser/blob/main/README.md
- **Agent Mode Documentation**: https://agent-browser.dev/agent-mode
- **Issues**: https://github.com/vercel-labs/agent-browser/issues

## Keywords

agent-browser, CLI browser automation, AI agents, browser automation CLI, refs, snapshot, agent mode, semantic locators, browser automation tool, command-line browser, AI agent browser, deterministic selectors, accessibility tree, browser commands, web automation CLI, sessions, headed mode, authenticated sessions, CDP mode, streaming, Chrome DevTools Protocol, Playwright, browser automation for AI
