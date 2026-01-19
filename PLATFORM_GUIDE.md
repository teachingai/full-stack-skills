# 跨平台使用指南

**full-stack-skills** 不仅可以在 Claude Code 中使用，还可以在其他 AI 平台使用，如 Cursor、Trae、Qoder、CodeBuddy、Windsurf 等。

## 支持的平台

- **Claude Code** - 原生支持，通过 Marketplace 安装（推荐）
- **Claude.ai** - 通过 Skills API 使用（付费套餐中部分技能已默认可用）
- **Cursor** - 转换为 Cursor 自定义指令格式
- **Trae** - 转换为 Trae 插件格式
- **Qoder** - 转换为 Qoder Agent 格式
- **CodeBuddy** - 转换为 CodeBuddy Workflow 格式
- **Windsurf** - 转换为 Windsurf Cascade Skills 格式

## 在 Claude Code 中使用

### 1. 注册 Marketplace

在 Claude Code 中运行以下命令，将本仓库注册为插件市场：

```bash
/plugin marketplace add https://github.com/teachingai/full-stack-skills.git
```

或者使用简写形式：

```bash
/plugin marketplace add teachingai/full-stack-skills
```

### 2. 安装插件

```bash
# 按技能种类安装（推荐）
/plugin install development-skills@full-stack-skills
/plugin install design-skills@full-stack-skills
/plugin install testing-skills@full-stack-skills
/plugin install devops-skills@full-stack-skills
# ... 更多插件请参考 README.md
```

**注意：** 本仓库按**技能种类**组织插件，而非按岗位划分。如需按岗位使用，请参考 [AGENTS_PROMPT.md](AGENTS_PROMPT.md) 中的角色定义。

详细说明请参考 [README.md](README.md)。

## 在其他平台使用

### 使用适配器工具转换

本仓库提供了自动转换工具，可以将 Agent Skills 转换为不同平台的格式。

#### 快速转换所有平台

```bash
cd adapters
python convert_all.py ../skills ../adapters-output
```

#### 转换单个平台

**Cursor:**
```bash
cd adapters/cursor
python convert_to_cursor.py --all ../../skills ../../adapters-output/cursor
```

**Trae:**
```bash
cd adapters/trae
python convert_to_trae.py --all ../../skills ../../adapters-output/trae
```

**Qoder:**
```bash
cd adapters/qoder
python convert_to_qoder.py --all ../../skills ../../adapters-output/qoder
```

**CodeBuddy:**
```bash
cd adapters/codebuddy
python convert_to_codebuddy.py --all ../../skills ../../adapters-output/codebuddy
```

**Windsurf:**
```bash
cd adapters/windsurf
python convert_to_windsurf.py --all ../../skills ../../adapters-output/windsurf
```

**注意：** 所有转换脚本都需要从对应的子目录运行，或者使用 `convert_all.py` 一次性转换所有平台。

### 输出目录结构

转换后的文件将保存在 `adapters-output/` 目录下，按平台分类：

```
adapters-output/
├── cursor/
│   └── .cursor/
│       └── rules/
│           ├── vue3.md
│           ├── react.md
│           └── ...
├── trae/
│   ├── vue3/
│   │   ├── trae-plugin.json
│   │   └── SKILL.md
│   └── ...
├── qoder/
│   ├── vue3-agent/
│   │   ├── qoder-agent-config.json
│   │   ├── SKILL.md
│   │   └── vue3_agent.py
│   └── ...
├── codebuddy/
│   ├── vue3/
│   │   ├── manifest.json
│   │   ├── workflows/
│   │   └── skills/
│   └── ...
└── windsurf/
    ├── vue3/
    │   ├── SKILL.md
    │   └── ...
    └── ...
```

## 平台特定说明

### Cursor

Cursor 使用自定义指令（Custom Rules）来扩展 AI 能力。

**使用步骤：**
1. 运行转换脚本生成 `.cursor/rules/` 目录下的规则文件
2. 将生成的规则文件复制到你的项目 `.cursor/rules/` 目录
3. Cursor 会自动加载这些规则

**参考文档：**
- [Cursor 文档](https://docs.cursor.com/)
- [适配器说明](adapters/cursor/README.md)

### Trae

Trae 使用插件系统来扩展 AI 能力。

**使用步骤：**
1. 运行转换脚本生成 Trae 插件格式文件
2. 在 Trae 中导入插件配置
3. 激活插件使用

**参考文档：**
- [Trae 官网](https://trae.ai/)
- [适配器说明](adapters/trae/README.md)

### Qoder

Qoder 使用 Agent 系统来扩展 AI 能力。

**使用步骤：**
1. 运行转换脚本生成 Qoder Agent 配置
2. 在 Qoder 中创建新的 Agent
3. 导入生成的配置文件
4. 激活 Agent 使用

**参考文档：**
- [Qoder 官网](https://qoder.com/)
- [适配器说明](adapters/qoder/README.md)

### CodeBuddy

CodeBuddy 使用 Workflow 系统来扩展 AI 能力。

**使用步骤：**
1. 运行转换脚本生成 CodeBuddy Workflow 配置
2. 在 CodeBuddy 中导入 Workflow
3. 配置 Workflow 参数
4. 运行 Workflow

**参考文档：**
- [CodeBuddy 官网](https://codebuddy.ai/)
- [适配器说明](adapters/codebuddy/README.md)

### Windsurf

Windsurf 使用 Cascade Skills 系统来扩展 AI 能力。

**使用步骤：**
1. 运行转换脚本生成 Windsurf Skills 配置
2. 在 Windsurf 中导入 Skills
3. 激活 Skills 使用

**参考文档：**
- [Windsurf 官网](https://windsurf.ai/)
- [适配器说明](adapters/windsurf/README.md)

## 依赖要求

转换脚本需要以下 Python 包：

```bash
pip install pyyaml
```

安装依赖：

```bash
cd adapters
pip install -r requirements.txt
```

## 验证状态

| 平台 | 转换脚本 | 格式验证 | 平台验证 |
|------|---------|---------|---------|
| Cursor | ✅ 完成 | ⚠️ 需要验证 | ⚠️ 需要验证 |
| Trae | ✅ 完成 | ⚠️ 需要验证 | ⚠️ 需要验证 |
| Qoder | ✅ 完成 | ⚠️ 需要验证 | ⚠️ 需要验证 |
| CodeBuddy | ✅ 完成 | ⚠️ 需要验证 | ⚠️ 需要验证 |
| Windsurf | ✅ 完成 | ⚠️ 需要验证 | ⚠️ 需要验证 |

## 注意事项

⚠️ **重要说明：这些适配器工具为理论性实现，尚未经过实际平台验证。**

- 转换脚本基于平台的一般特性和常见适配模式
- 生成的配置文件格式可能需要根据实际平台 API 调整
- **建议在实际使用前查阅目标平台的官方文档并进行测试**
- 转换脚本会自动提取 `SKILL.md` 中的 frontmatter 和内容
- 脚本会尝试提取工作流步骤，但可能需要手动调整

## 贡献

如果你验证了某个平台的适配方案，欢迎贡献：

1. 测试转换脚本生成的输出
2. 在实际平台上验证功能
3. 报告问题和改进建议
4. 提交 Pull Request

## 相关资源

- [适配器工具文档](adapters/README.md) - 详细的适配器使用说明
- [适配器示例](adapters/EXAMPLES.md) - 转换后的示例文件
- [Agent Skills 规范](https://agentskills.io/) - Agent Skills 官方规范（如链接不可访问，请参考 [Anthropic 官方文档](https://support.claude.com/en/articles/12512198-creating-custom-skills)）
- [项目主文档](README.md) - full-stack-skills 完整文档

## 常见问题

### Q: 转换后的文件可以直接使用吗？

A: 转换脚本生成的配置文件格式可能需要根据实际平台 API 调整。建议在实际使用前查阅目标平台的官方文档并进行测试。

### Q: 如何验证转换是否正确？

A: 可以查看 `adapters-output/` 目录下生成的文件，检查格式是否符合目标平台的要求。建议在实际平台上进行功能验证。

### Q: 转换后的技能功能是否完整？

A: 转换脚本会尽可能保留原始技能的功能，但某些平台特定的功能可能需要手动调整。建议根据实际需求进行定制。

### Q: 如何贡献新的平台适配器？

A: 欢迎创建新的适配器脚本。可以参考现有适配器的实现方式，并遵循 Agent Skills 规范。完成后请提交 Pull Request。
