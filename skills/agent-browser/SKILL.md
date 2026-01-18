---
name: agent-browser
description: A comprehensive skill for using agent-browser, a CLI tool for browser automation designed for AI agents, developed by Vercel Labs. This skill covers installation, core commands, selectors (refs, CSS, XPath, semantic locators), agent mode, options, and best practices. Use this skill whenever the user needs to automate browser interactions via CLI commands, especially for AI agents that need to interact with web pages.
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

## How to use this skill

This skill is organized to match the agent-browser official documentation structure (https://github.com/vercel-labs/agent-browser/blob/main/README.md). When working with agent-browser:

1. **Install agent-browser**:
   - Load `examples/getting-started/installation.md` for installation instructions

2. **Learn core commands**:
   - Load `examples/commands/basic-commands.md` for basic commands (open, click, fill, etc.)
   - Load `examples/commands/advanced-commands.md` for advanced commands (snapshot, eval, etc.)

3. **Understand selectors**:
   - Load `examples/selectors/refs.md` for refs-based selection (@e1, @e2, etc.)
   - Load `examples/selectors/traditional-selectors.md` for CSS, XPath, and semantic locators

4. **Use agent mode**:
   - Load `examples/agent-mode/introduction.md` for agent mode overview
   - Load `examples/agent-mode/optimal-workflow.md` for optimal AI workflow
   - Load `examples/agent-mode/integration.md` for integrating with AI agents

5. **Configure options**:
   - Load `examples/options/global-options.md` for global options
   - Load `examples/options/snapshot-options.md` for snapshot-specific options
   - Load `examples/options/session-options.md` for session management

6. **Reference API documentation** when needed:
   - `api/commands.md` - Complete command reference
   - `api/selectors.md` - Selector reference
   - `api/options.md` - Options reference

7. **Use templates** for quick start:
   - `templates/basic-automation.md` - Basic automation workflow
   - `templates/ai-agent-workflow.md` - AI agent workflow template

## Examples and Templates

### Getting Started
- **Installation**: `examples/getting-started/installation.md` - Installing agent-browser CLI tool

### Commands
- **Basic Commands**: `examples/commands/basic-commands.md` - Core commands (open, click, fill, type, etc.)
- **Advanced Commands**: `examples/commands/advanced-commands.md` - Advanced commands (snapshot, eval, screenshot, etc.)

### Selectors
- **Refs**: `examples/selectors/refs.md` - Using refs (@e1, @e2) for deterministic element selection
- **Traditional Selectors**: `examples/selectors/traditional-selectors.md` - CSS selectors, XPath, semantic locators

### Agent Mode
- **Introduction**: `examples/agent-mode/introduction.md` - Agent mode overview and JSON output
- **Optimal Workflow**: `examples/agent-mode/optimal-workflow.md` - Optimal AI workflow patterns
- **Integration**: `examples/agent-mode/integration.md` - Integrating with AI agents (Claude, Cursor, Copilot, etc.)

### Options
- **Global Options**: `examples/options/global-options.md` - Global CLI options (--session, --headers, --headed, etc.)
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

## Resources

- **GitHub Repository**: https://github.com/vercel-labs/agent-browser
- **Official README**: https://github.com/vercel-labs/agent-browser/blob/main/README.md
- **Agent Mode Documentation**: https://agent-browser.dev/agent-mode
- **Issues**: https://github.com/vercel-labs/agent-browser/issues

## Keywords

agent-browser, CLI browser automation, AI agents, browser automation CLI, refs, snapshot, agent mode, semantic locators, browser automation tool, command-line browser, AI agent browser, deterministic selectors, accessibility tree, browser commands, web automation CLI
