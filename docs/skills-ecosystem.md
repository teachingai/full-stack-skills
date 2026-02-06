# 技能生态与主文档入口

本仓库（**full-stack-skills**）为全链路**阶段→技能**映射与**基础技能**的主入口。权威映射表见 [pipeline-stage-to-skills.md](pipeline-stage-to-skills.md)。

**说明**：tui/t2ui 类技能（需求转译、ASCII 界面、Pencil 设计语言等）以 **t2ui-skills** 为准，本仓库不再保留 `skills/tui-skills`。Pencil MCP 使用与 .pen 编辑以 **pencil-skills** 为准，本仓库不再保留 `skills/pencil`。

---

## 关联技能仓库

| 仓库 | 职责 | 阶段/用途 |
|------|------|-----------|
| [t2ui-skills](https://github.com/partme-ai/t2ui-skills) | 需求转译：PRD → ASCII 界面、Stitch 设计语言、Pencil 设计语言 | 设计阶段 |
| [stitch-skills](https://github.com/partme-ai/stitch-skills) | 原型设计：Stitch 设计语言 → Stitch MCP → 原型图 | 设计阶段 |
| [pencil-skills](https://github.com/partme-ai/pencil-skills) | 界面设计：Pencil 设计语言 → Pencil MCP → 产品图（.pen） | 设计阶段 |
| [tauri-skills](https://github.com/partme-ai/tauri-skills) | Tauri 跨平台桌面/移动应用开发 | 开发阶段（桌面/跨平台） |
| **full-stack-skills**（本仓库） | 基础技能（文档/架构/测试/部署、nvm 等）、speckit-*、阶段映射 | 全阶段 |

各仓库的 README/AGENTS 应指向本文档或 [pipeline-stage-to-skills.md](pipeline-stage-to-skills.md)。

---

## nvm 相关技能（本仓库内）

**Node 版本管理**等基础开发环境技能当前在 **full-stack-skills** 内，不作为独立仓库：

- nvm-install、nvm-setup、nvm-usage-basics、nvm-defaults-and-nvmrc、nvm-shell-integration、nvm-docker-ci、nvm-troubleshooting-macos、nvm-global-packages 等。

若未来拆出独立 nvm-skills 仓库，将在本文档与 pipeline 中补充对应条目。Tauri 技能规划清单见 [tauri-skills.md](tauri-skills.md)。
