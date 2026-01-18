# 全栈技能树规划文档（Role-Based Skills Tree Planning）

> **状态**：规划阶段，待确认后实现  
> **目标**：按岗位组织技能树，每个岗位在 marketplace.json 中对应一个 plugin，plugin 内包含该岗位所需的一组 skills

---

## 一、技能树组织原则

### 1.1 三层结构

```
Marketplace (full-stack-skills)
  └── Plugins (每个岗位一个 plugin)
      └── Skills (每个 plugin 包含一组 skills)
          ├── 岗位核心 skill (roles/{role-name})
          └── 支撑 skills (文档/工具/图表等)
```

### 1.2 命名规范

- **Plugin 名称**：`{kebab-role-name}`（例如：`product-manager`）
- **岗位 Skill 目录**：`skills/roles/{kebab-role-name}/`
- **岗位 Skill 文件**：`skills/roles/{kebab-role-name}/SKILL.md`

### 1.3 技能包设计原则

每个岗位的 plugin 应包含：
1. **岗位核心 skill**：该岗位的职责、工作流程、输出标准
2. **文档生成 skills**：该岗位需要生成的文档类型（PRD/架构/测试等）
3. **图表绘制 skills**：该岗位需要的图表类型（流程图/架构图/ER图等）
4. **工具类 skills**：该岗位常用的工具/脚本

---

## 二、按阶段划分的岗位技能树规划

### 阶段 1：产品调研阶段

#### 1.1 产品经理（Product Manager / PM）

**职责**：
- 市场趋势分析、竞品对标、用户需求挖掘、消费行为研究
- 输出调研报告，为产品定位与功能规划提供数据支撑

**工作场景**：
- 用户访谈、问卷设计、数据分析、行业报告撰写

**Plugin：`product-manager`**

**Skills 包**：
- `./skills/roles/product-manager`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（产品调研模板、PRD模板）
- `./skills/mermaid`（用户旅程图、流程图）
- `./skills/docx`（Word 文档输出）

**输出产物**：
- 产品调研报告
- PRD 文档
- 用户画像
- 竞品分析报告

---

#### 1.2 产品调研专员（Product Research Specialist / PRS）

**职责**：
- 市场趋势分析、竞品对标、用户需求挖掘、消费行为研究
- 输出调研报告，为产品定位与功能规划提供数据支撑

**工作场景**：
- 用户访谈、问卷设计、数据分析、行业报告撰写

**Plugin：`product-research-specialist`**

**Skills 包**：
- `./skills/roles/product-research-specialist`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（产品调研模板）
- `./skills/mermaid`（用户旅程图、数据流程图）
- `./skills/xlsx`（问卷数据、分析表格）

**输出产物**：
- 产品调研报告
- 用户访谈记录
- 问卷分析报告
- 竞品对标分析

---

#### 1.3 产品分析师（Product Analyst / PA）

**职责**：
- 市场趋势分析、竞品对标、用户需求挖掘、消费行为研究
- 输出调研报告，为产品定位与功能规划提供数据支撑

**工作场景**：
- 用户访谈、问卷设计、数据分析、行业报告撰写

**Plugin：`product-analyst`**

**Skills 包**：
- `./skills/roles/product-analyst`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（产品调研模板、需求分析模板）
- `./skills/mermaid`（数据流程图、用户画像图）
- `./skills/xlsx`（数据分析表格）

**输出产物**：
- 数据分析报告
- 用户行为分析
- 产品定位建议

---

### 阶段 2：市场调研阶段

#### 2.1 市场调研分析师（Market Research Analyst / MRA）

**职责**：
- 聚焦行业动态、市场规模、竞争格局、定价策略、渠道分布
- 协同产品经理完成商业可行性评估

**数据来源**：
- 第三方平台（如艾瑞、易观）、电商平台（亚马逊、淘宝）、用户行为数据

**Plugin：`market-research-analyst`**

**Skills 包**：
- `./skills/roles/market-research-analyst`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（市场调研模板）
- `./skills/mermaid`（市场分析图、竞争格局图）
- `./skills/xlsx`（市场数据表格）
- `./skills/pptx`（市场分析演示文稿）

**输出产物**：
- 市场调研报告
- 竞争格局分析
- 商业可行性评估
- 定价策略建议

---

#### 2.2 市场专员（Marketing Specialist / MS）

**职责**：
- 聚焦行业动态、市场规模、竞争格局、定价策略、渠道分布
- 协同产品经理完成商业可行性评估

**Plugin：`marketing-specialist`**

**Skills 包**：
- `./skills/roles/marketing-specialist`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（市场调研模板）
- `./skills/mermaid`（渠道分布图、营销漏斗图）
- `./skills/pptx`（营销方案演示）

**输出产物**：
- 营销策略文档
- 渠道分析报告
- 推广方案

---

### 阶段 3：技术调研阶段

#### 3.1 技术研究工程师（Research Engineer / REng）

**职责**：
- 评估技术选型（如微服务 vs 单体）、框架可行性（SpringCloud、Kubernetes）、开源方案
- 跟踪AI、大模型、边缘计算等前沿技术的落地可能性
- 输出技术预研报告与POC验证结果

**Plugin：`tech-research-engineer`**

**Skills 包**：
- `./skills/roles/tech-research-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（技术文档生成）
- `./skills/mermaid`（技术架构图、技术选型对比图）
- `./skills/zh-product-doc-generator`（技术调研模板）

**输出产物**：
- 技术预研报告
- 技术选型对比
- POC 验证报告
- 技术风险评估

---

#### 3.2 系统架构师（System Architect / SA (Arch)）

**职责**：
- 评估技术选型（如微服务 vs 单体）、框架可行性（SpringCloud、Kubernetes）、开源方案
- 跟踪AI、大模型、边缘计算等前沿技术的落地可能性
- 输出技术预研报告与POC验证结果

**Plugin：`system-architect`**

**Skills 包**：
- `./skills/roles/system-architect`（岗位核心 skill）
- `./skills/ddd4j-project-builder`（DDD 项目结构、架构模式）
- `./skills/mermaid`（系统架构图、C4图、部署图）
- `./skills/documentation-builder`（架构文档）
- `./skills/zh-product-doc-generator`（系统架构设计模板）

**输出产物**：
- 系统架构设计文档
- 技术选型报告
- 架构图（C4、部署拓扑）
- 技术风险评估

---

#### 3.3 云计算工程师（Cloud Engineer / CE）

**职责**：
- 评估技术选型（如微服务 vs 单体）、框架可行性（SpringCloud、Kubernetes）、开源方案
- 跟踪AI、大模型、边缘计算等前沿技术的落地可能性
- 输出技术预研报告与POC验证结果

**Plugin：`cloud-engineer`**

**Skills 包**：
- `./skills/roles/cloud-engineer`（岗位核心 skill）
- `./skills/mermaid`（云架构图、部署拓扑图）
- `./skills/documentation-builder`（云架构文档）
- `./skills/zh-product-doc-generator`（技术调研模板）

**输出产物**：
- 云架构设计文档
- 容器化方案
- 云资源规划

---

### 阶段 4：需求分析阶段

#### 4.1 需求分析师（Requirements Analyst / RA）

**职责**：
- 将业务需求转化为系统需求，明确功能边界与非功能性需求（性能、安全、兼容性）
- 编写《软件需求规格说明书》（SRS）或《产品需求文档》（PRD）
- 主导需求评审会议，协调开发、测试、设计三方达成共识

**Plugin：`requirements-analyst`**

**Skills 包**：
- `./skills/roles/requirements-analyst`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（需求分析模板、PRD模板）
- `./skills/mermaid`（需求流程图、用例图）
- `./skills/docx`（需求文档输出）

**输出产物**：
- 软件需求规格说明书（SRS）
- 产品需求文档（PRD）
- 需求评审记录
- 需求变更记录

---

#### 4.2 系统分析师（System Analyst / SA）

**职责**：
- 将业务需求转化为系统需求，明确功能边界与非功能性需求（性能、安全、兼容性）
- 编写《软件需求规格说明书》（SRS）或《产品需求文档》（PRD）
- 主导需求评审会议，协调开发、测试、设计三方达成共识

**Plugin：`system-analyst`**

**Skills 包**：
- `./skills/roles/system-analyst`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（需求分析模板、系统分析模板）
- `./skills/mermaid`（系统流程图、数据流图）
- `./skills/documentation-builder`（系统分析文档）

**输出产物**：
- 系统分析文档
- 功能需求清单
- 非功能性需求清单

---

### 阶段 5：PRD文档编写阶段

#### 5.1 产品经理（Product Manager / PM）

**职责**：
- PRD是产品开发的"宪法"，需清晰定义：目标用户、核心功能、业务流程、验收标准
- 现代PRD趋向轻量化，常结合用户故事（User Story）、验收标准（Acceptance Criteria）

**工具推荐**：墨刀、Axure、Confluence、飞书多维表格

**Plugin：`product-manager`**（已在阶段1定义，此处复用）

**输出产物**：
- PRD 文档
- 用户故事（User Story）
- 验收标准（Acceptance Criteria）

---

### 阶段 6：视觉交互规范制定阶段

#### 6.1 交互设计师（UX Designer / UX）

**职责**：
- 设计用户旅程图（User Journey）、信息架构（IA）、原型流程图
- 制定交互规范：按钮状态、动效逻辑、反馈机制、无障碍访问标准
- 与UI设计师协同，确保体验一致性

**Plugin：`ux-designer`**

**Skills 包**：
- `./skills/roles/ux-designer`（岗位核心 skill）
- `./skills/frontend-design`（交互设计规范）
- `./skills/mermaid`（用户旅程图、信息架构图、流程图）
- `./skills/zh-product-doc-generator`（视觉与交互 DNA 规范模板）

**输出产物**：
- 用户旅程图（User Journey）
- 信息架构（IA）
- 交互规范文档
- 原型流程图

---

### 阶段 7：UI设计阶段

#### 7.1 UI设计师（UI Designer / UI）

**职责**：
- 基于交互规范进行视觉呈现：色彩系统、图标设计、排版布局、动效细节
- 输出高保真设计稿、设计规范文档（Design System）

**工具**：Figma、Sketch、Adobe XD

**Plugin：`ui-designer`**

**Skills 包**：
- `./skills/roles/ui-designer`（岗位核心 skill）
- `./skills/frontend-design`（UI设计规范、设计系统）
- `./skills/mermaid`（设计系统结构图）
- `./skills/zh-product-doc-generator`（UI 设计说明模板）

**输出产物**：
- 高保真设计稿
- 设计规范文档（Design System）
- 色彩系统
- 图标库

---

### 阶段 8：领域模型设计阶段

#### 8.1 系统架构师（System Architect / SA (Arch)）

**职责**：
- 应用领域驱动设计（DDD）方法，划分限界上下文（Bounded Context）
- 定义实体（Entity）、值对象（Value Object）、聚合根（Aggregate Root）、领域事件
- 输出领域模型图，指导后端服务拆分与数据建模

**Plugin：`system-architect`**（已在阶段3定义，此处扩展）

**Skills 包**（扩展）：
- `./skills/ddd4j-project-builder`（DDD 项目结构、领域模型）
- `./skills/mermaid`（领域模型图、ER图、类图）
- `./skills/zh-product-doc-generator`（领域模型说明模板）

**输出产物**：
- 领域模型文档
- 限界上下文划分
- 聚合设计
- 领域事件定义

---

#### 8.2 领域专家（Domain Expert / DE）

**职责**：
- 应用领域驱动设计（DDD）方法，划分限界上下文（Bounded Context）
- 定义实体（Entity）、值对象（Value Object）、聚合根（Aggregate Root）、领域事件
- 输出领域模型图，指导后端服务拆分与数据建模

**Plugin：`domain-expert`**

**Skills 包**：
- `./skills/roles/domain-expert`（岗位核心 skill）
- `./skills/ddd4j-project-builder`（DDD 项目结构、领域模型）
- `./skills/mermaid`（领域模型图、ER图）
- `./skills/zh-product-doc-generator`（领域模型说明模板）

**输出产物**：
- 领域模型文档
- 统一语言（Ubiquitous Language）
- 业务规则定义

---

### 阶段 9：系统架构设计阶段

#### 9.1 系统架构师（System Architect / SA (Arch)）

**职责**：
- 设计整体技术栈：微服务、单体、Serverless、消息队列、缓存策略
- 规划高可用架构：负载均衡、容灾备份、服务熔断、链路追踪
- 输出架构图、接口规范、部署拓扑图

**Plugin：`system-architect`**（已在阶段3定义，此处复用）

**输出产物**：
- 系统架构设计文档
- 架构图（C4、部署拓扑）
- 接口规范
- 技术栈选型

---

#### 9.2 技术架构师（Technical Architect / TA）

**职责**：
- 设计整体技术栈：微服务、单体、Serverless、消息队列、缓存策略
- 规划高可用架构：负载均衡、容灾备份、服务熔断、链路追踪
- 输出架构图、接口规范、部署拓扑图

**Plugin：`technical-architect`**

**Skills 包**：
- `./skills/roles/technical-architect`（岗位核心 skill）
- `./skills/ddd4j-project-builder`（架构模式、技术栈）
- `./skills/mermaid`（技术架构图、部署拓扑图、时序图）
- `./skills/documentation-builder`（技术架构文档）
- `./skills/zh-product-doc-generator`（系统架构设计模板）

**输出产物**：
- 技术架构设计文档
- 技术栈选型
- 接口规范
- 部署拓扑图

---

#### 9.3 云计算架构师（Cloud Architect / CA）

**职责**：
- 设计整体技术栈：微服务、单体、Serverless、消息队列、缓存策略
- 规划高可用架构：负载均衡、容灾备份、服务熔断、链路追踪
- 输出架构图、接口规范、部署拓扑图

**Plugin：`cloud-architect`**

**Skills 包**：
- `./skills/roles/cloud-architect`（岗位核心 skill）
- `./skills/mermaid`（云架构图、部署拓扑图）
- `./skills/documentation-builder`（云架构文档）
- `./skills/zh-product-doc-generator`（系统架构设计模板）

**输出产物**：
- 云架构设计文档
- 容器化方案
- 高可用架构设计

---

### 阶段 10：需求技术细分阶段

#### 10.1 前端开发工程师（Frontend Engineer / FE）

**职责**：
- 负责网页/APP界面交互设计，需掌握HTML/CSS/JavaScript及React/Vue框架
- 将PRD/SRS拆解为可执行的技术任务（Task）
- 划分模块边界、定义API接口、估算开发工时

**Plugin：`frontend-engineer`**

**Skills 包**：
- `./skills/roles/frontend-engineer`（岗位核心 skill）
- `./skills/code-generator`（前端代码生成）
- `./skills/frontend-design`（前端设计规范）
- `./skills/documentation-builder`（接口文档、技术文档）
- `./skills/mermaid`（前端架构图、组件关系图）

**输出产物**：
- 前端技术任务清单
- 前端接口文档
- 前端组件设计
- 前端代码

---

#### 10.2 后端开发工程师（Backend Engineer / BE）

**职责**：
- 处理业务逻辑与数据库操作，需精通Java/Python及Spring Boot等框架
- 将PRD/SRS拆解为可执行的技术任务（Task）
- 划分模块边界、定义API接口、估算开发工时

**Plugin：`backend-engineer`**

**Skills 包**：
- `./skills/roles/backend-engineer`（岗位核心 skill）
- `./skills/code-generator`（后端代码生成）
- `./skills/ddd4j-project-builder`（DDD 项目结构）
- `./skills/documentation-builder`（接口文档、技术文档）
- `./skills/mermaid`（数据库ER图、接口时序图）

**输出产物**：
- 后端技术任务清单
- API 接口文档（Swagger）
- 数据库ER图
- 后端代码

---

#### 10.3 移动开发工程师（Mobile Engineer / ME）

**职责**：
- 专攻iOS（Swift）或Android（Kotlin）应用开发，跨平台可选Flutter
- 将PRD/SRS拆解为可执行的技术任务（Task）

**Plugin：`mobile-engineer`**

**Skills 包**：
- `./skills/roles/mobile-engineer`（岗位核心 skill）
- `./skills/code-generator`（移动端代码生成）
- `./skills/frontend-design`（移动端设计规范）
- `./skills/documentation-builder`（移动端技术文档）
- `./skills/mermaid`（移动端架构图）

**输出产物**：
- 移动端技术任务清单
- 移动端接口文档
- 移动端代码

---

#### 10.4 数据库管理师（DataBase Administrator / DBA）

**职责**：
- 数据库设计、优化、备份、安全
- 将PRD/SRS拆解为可执行的技术任务（Task）

**Plugin：`dba`**

**Skills 包**：
- `./skills/roles/dba`（岗位核心 skill）
- `./skills/mermaid`（数据库ER图、数据流图）
- `./skills/documentation-builder`（数据库设计文档）
- `./skills/zh-product-doc-generator`（技术细分模板）

**输出产物**：
- 数据库设计文档
- 数据库ER图
- 数据库优化方案

---

### 阶段 11：功能测试阶段

**阶段概述**：
- 写测试用例、自动化测试脚本、进行功能测试、缺陷跟踪记录、编写测试报告、QA 测试计划、质量评估报告等

---

#### 11.1 测试工程师（Test Engineer / TE）

**职责定位**：**技术实现导向**，专注于自动化测试工具开发与测试技术实现

**核心职责**：
- 基于需求文档编写功能测试、边界测试、异常流测试用例
- **设计并开发自动化测试脚本**（Selenium、PyTest、Appium、Jest、Cypress）
- 搭建和维护自动化测试框架
- 进行功能测试执行（自动化为主）
- 输出测试用例库、测试报告、缺陷跟踪记录

**Plugin：`test-engineer`**

**Skills 包**：
- `./skills/roles/test-engineer`（岗位核心 skill）
- `./skills/test-writer`（测试用例编写）
- `./skills/webapp-testing`（Web 应用测试）
- `./skills/code-generator`（自动化测试脚本生成）
- `./skills/documentation-builder`（测试文档）
- `./skills/zh-product-doc-generator`（测试结果模板）

**输出产物**：
- 测试用例库
- **自动化测试脚本**
- 测试报告
- 缺陷跟踪记录
- 测试框架与工具

---

#### 11.2 QA工程师（Quality Assurance Engineer / QA）

**职责定位**：**质量保证流程导向**，专注于测试计划制定、质量评估与流程管控

**核心职责**：
- 制定 QA 测试计划与测试策略
- 基于需求文档编写功能测试、边界测试、异常流测试用例
- 设计自动化测试脚本（偏重策略与框架选择）
- 进行功能测试执行（手工+自动化结合）
- **质量评估与质量报告**（质量度量、质量趋势分析）
- 缺陷跟踪记录与缺陷分析
- 编写测试报告与质量评估报告

**Plugin：`qa-engineer`**

**Skills 包**：
- `./skills/roles/qa-engineer`（岗位核心 skill）
- `./skills/test-writer`（测试用例编写）
- `./skills/webapp-testing`（Web 应用测试）
- `./skills/documentation-builder`（QA 文档）
- `./skills/zh-product-doc-generator`（测试结果模板、功能提测模板、质量评估报告模板）

**输出产物**：
- **QA 测试计划**
- 测试用例库
- 测试报告
- **质量评估报告**
- 缺陷跟踪记录与分析
- 质量度量指标

---

#### 11.3 测试员（Testor / TT）

**职责定位**：**测试执行导向**，专注于手工测试执行与基础测试用例编写

**核心职责**：
- 基于需求文档编写功能测试、边界测试、异常流测试用例（偏基础）
- **进行功能测试执行**（手工测试为主）
- 缺陷跟踪记录
- 编写测试报告（基础）

**Plugin：`testor`**

**Skills 包**：
- `./skills/roles/testor`（岗位核心 skill）
- `./skills/test-writer`（测试用例编写）
- `./skills/webapp-testing`（Web 应用测试）
- `./skills/zh-product-doc-generator`（测试结果模板）

**输出产物**：
- 测试用例（基础）
- 测试报告（基础）
- 缺陷记录

---

### 阶段 12：功能上线发布阶段

#### 12.1 DevOps工程师（DevOps Engineer / DevOps）

**职责**：
- 通过CI/CD流水线实现自动化构建、测试、部署
- 关键环节：代码提交 → 单元测试 → 镜像打包 → 容器部署 → 灰度发布 → 监控验证

**工具链**：GitLab CI、Jenkins、Docker、Kubernetes、ArgoCD

**Plugin：`devops-engineer`**

**Skills 包**：
- `./skills/roles/devops-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（CI/CD 文档）
- `./skills/mermaid`（CI/CD 流程图、部署架构图）
- `./skills/zh-product-doc-generator`（上线通知模板）

**输出产物**：
- CI/CD 配置
- 部署文档
- 上线检查清单
- 灰度发布方案

---

#### 12.2 发布工程师（Release Engineer / RE）

**职责**：
- 通过CI/CD流水线实现自动化构建、测试、部署
- 关键环节：代码提交 → 单元测试 → 镜像打包 → 容器部署 → 灰度发布 → 监控验证

**Plugin：`release-engineer`**

**Skills 包**：
- `./skills/roles/release-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（发布文档）
- `./skills/mermaid`（发布流程图）
- `./skills/zh-product-doc-generator`（上线通知模板）

**输出产物**：
- 发布计划
- 上线检查清单
- 回滚方案
- 上线通知

---

### 阶段 13：项目运维阶段

#### 13.1 运维工程师（Operations Engineer / OE）

**职责定位**：**传统运维导向**，专注于基础设施运维、系统监控与故障处理

**核心职责**：
- 负责系统监控（Prometheus + Grafana）、日志分析（ELK）、告警响应
- 实施容量规划、灾备演练、性能调优、安全加固
- 基础设施管理（服务器、网络、存储）
- 日常运维操作（备份、恢复、升级、维护）
- 故障处理与应急响应

**Plugin：`operations-engineer`**

**Skills 包**：
- `./skills/roles/operations-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（运维文档）
- `./skills/mermaid`（监控架构图、运维流程图、故障处理流程图）
- `./skills/zh-product-doc-generator`（项目运维模板）

**输出产物**：
- 运维手册
- 监控告警配置
- 故障处理预案
- 容量规划文档
- 基础设施运维文档

---

#### 13.2 SRE工程师（Site Reliability Engineer / SRE）

**职责定位**：**可靠性工程导向**，专注于系统可靠性设计、自动化运维与工程化实践

**核心职责**：
- 负责系统监控（Prometheus + Grafana）、日志分析（ELK）、告警响应
- 实施容量规划、灾备演练、性能调优、安全加固
- **推行"运维即代码"（IaC）**、自动化修复、混沌工程
- **可靠性设计**（SLO/SLI 定义、错误预算管理）
- **故障复盘与持续改进**（Postmortem、根因分析）
- **自动化运维**（自愈系统、自动化扩缩容）

**Plugin：`sre-engineer`**

**Skills 包**：
- `./skills/roles/sre-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（SRE 文档）
- `./skills/mermaid`（SRE 架构图、故障处理流程图、可靠性设计图）
- `./skills/zh-product-doc-generator`（项目运维模板）

**输出产物**：
- SRE 手册
- **可靠性设计文档**（SLO/SLI 定义）
- **故障复盘报告**（Postmortem）
- **混沌工程方案**
- 自动化运维方案

---

## 三、技能依赖关系与共享机制

### 3.1 技能分层结构

```
Marketplace (full-stack-skills)
├── 支撑 Skills Plugins（独立 plugin，可被多个岗位共享）
│   ├── document-skills（文档处理：docx、pptx、pdf、xlsx）
│   ├── markdown-skills（Markdown：mermaid）
│   ├── development-skills（开发：code-generator、test-writer、documentation-builder、ddd4j-project-builder、frontend-design、webapp-testing 等）
│   └── zh-product-doc-generator（项目文档生成：独立 skill）
│
└── 岗位 Skills Plugins（每个岗位一个 plugin）
    ├── product-manager
    ├── test-engineer
    └── ...
    └── 每个岗位 plugin 通过路径引用共享支撑 skills
```

### 3.2 支撑 Skills Plugins（独立 plugin）

支撑 skills 作为**独立的 plugin**，可以被多个岗位 plugin 共享使用：

#### document-skills（文档处理技能集合）

**Plugin 名称**：`document-skills`

**包含 Skills**：
- `./skills/docx`（Word 文档处理）
- `./skills/pptx`（PowerPoint 演示文稿处理）
- `./skills/pdf`（PDF 文档处理）
- `./skills/xlsx`（Excel 表格处理）
- `./skills/doc-coauthoring`（文档协作）

**使用场景**：需要生成或处理办公文档的岗位

---

#### markdown-skills（Markdown 技能集合）

**Plugin 名称**：`markdown-skills`

**包含 Skills**：
- `./skills/mermaid`（Mermaid 图表绘制：流程图、架构图、ER图等）

**使用场景**：需要绘制图表的岗位（架构师、设计师、开发工程师等）

---

#### development-skills（开发技能集合）

**Plugin 名称**：`development-skills`

**包含 Skills**：
- `./skills/code-generator`（代码生成）
- `./skills/test-writer`（测试用例编写）
- `./skills/documentation-builder`（文档生成）
- `./skills/ddd4j-project-builder`（DDD 项目结构）
- `./skills/frontend-design`（前端设计规范）
- `./skills/webapp-testing`（Web 应用测试）
- `./skills/mcp-builder`（MCP 构建器）
- `./skills/web-artifacts-builder`（Web 构建工具）
- `./skills/theme-factory`（主题工厂）

**使用场景**：开发、测试、架构相关岗位

---

#### zh-product-doc-generator（项目文档生成技能）

**Plugin 名称**：`zh-product-doc-generator`（或作为独立 skill 直接引用）

**包含 Skills**：
- `./skills/zh-product-doc-generator`（项目文档生成：14 种文档模板）

**使用场景**：产品、需求、架构、测试、运维相关岗位

### 3.3 岗位 Plugin 共享机制

**岗位 plugin 通过直接引用支撑 skills 的路径来共享使用**，例如：

```json
{
  "name": "product-manager",
  "skills": [
    "./skills/roles/product-manager",           // 岗位核心 skill
    "./skills/zh-product-doc-generator",        // 引用共享 skill
    "./skills/mermaid",                          // 引用共享 skill
    "./skills/docx"                                // 引用共享 skill
  ]
}
```

**优势**：
1. **避免重复**：支撑 skills 只需定义一次，多个岗位 plugin 可以共享
2. **独立维护**：支撑 skills 可以独立更新，所有引用它的岗位 plugin 自动获得更新
3. **灵活组合**：每个岗位 plugin 可以根据需要选择引用的支撑 skills
4. **清晰依赖**：通过路径引用，明确显示岗位对支撑 skills 的依赖关系

---

## 四、Marketplace.json 结构规划

### 4.1 完整结构（包含支撑 Skills Plugins 和岗位 Plugins）

```json
{
  "name": "full-stack-skills",
  "plugins": [
    // ========== 支撑 Skills Plugins（独立 plugin，可被多个岗位共享）==========
    
    {
      "name": "document-skills",
      "description": "文档处理技能集合，支持 Excel、Word、PowerPoint、PDF 等办公文档的创建、编辑和处理",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/docx",
        "./skills/pptx",
        "./skills/pdf",
        "./skills/xlsx",
        "./skills/doc-coauthoring"
      ]
    },
    {
      "name": "markdown-skills",
      "description": "Markdown 相关技能集合，包括 Mermaid 图表绘制等",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/mermaid"
      ]
    },
    {
      "name": "development-skills",
      "description": "开发技能集合，包括代码生成、测试编写、文档构建、项目文档生成、MCP 构建器、Web 开发、前端设计等",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/code-generator",
        "./skills/test-writer",
        "./skills/ddd4j-project-builder",
        "./skills/documentation-builder",
        "./skills/zh-product-doc-generator",
        "./skills/mcp-builder",
        "./skills/webapp-testing",
        "./skills/frontend-design",
        "./skills/web-artifacts-builder",
        "./skills/theme-factory"
      ]
    },
    
    // ========== 岗位 Skills Plugins（每个岗位一个 plugin，引用共享支撑 skills）==========
    
    // 产品类岗位
    {
      "name": "product-manager",
      "description": "产品经理岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/product-manager",
        "./skills/zh-product-doc-generator",
        "./skills/mermaid",
        "./skills/docx"
      ]
    },
    {
      "name": "product-research-specialist",
      "description": "产品调研专员岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/product-research-specialist",
        "./skills/zh-product-doc-generator",
        "./skills/mermaid",
        "./skills/xlsx"
      ]
    },
    {
      "name": "product-analyst",
      "description": "产品分析师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/product-analyst",
        "./skills/zh-product-doc-generator",
        "./skills/mermaid",
        "./skills/xlsx"
      ]
    },
    
    // 市场类岗位
    {
      "name": "market-research-analyst",
      "description": "市场调研分析师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/market-research-analyst",
        "./skills/zh-product-doc-generator",
        "./skills/mermaid",
        "./skills/xlsx",
        "./skills/pptx"
      ]
    },
    {
      "name": "marketing-specialist",
      "description": "市场专员岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/marketing-specialist",
        "./skills/zh-product-doc-generator",
        "./skills/mermaid",
        "./skills/pptx"
      ]
    },
    
    // 技术调研类岗位
    {
      "name": "tech-research-engineer",
      "description": "技术研究工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/tech-research-engineer",
        "./skills/documentation-builder",
        "./skills/mermaid",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "system-architect",
      "description": "系统架构师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/system-architect",
        "./skills/ddd4j-project-builder",
        "./skills/mermaid",
        "./skills/documentation-builder",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "cloud-engineer",
      "description": "云计算工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/cloud-engineer",
        "./skills/mermaid",
        "./skills/documentation-builder",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "cloud-architect",
      "description": "云计算架构师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/cloud-architect",
        "./skills/mermaid",
        "./skills/documentation-builder",
        "./skills/zh-product-doc-generator"
      ]
    },
    
    // 需求分析类岗位
    {
      "name": "requirements-analyst",
      "description": "需求分析师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/requirements-analyst",
        "./skills/zh-product-doc-generator",
        "./skills/mermaid",
        "./skills/docx"
      ]
    },
    {
      "name": "system-analyst",
      "description": "系统分析师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/system-analyst",
        "./skills/zh-product-doc-generator",
        "./skills/mermaid",
        "./skills/documentation-builder"
      ]
    },
    
    // 设计类岗位
    {
      "name": "ux-designer",
      "description": "交互设计师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/ux-designer",
        "./skills/frontend-design",
        "./skills/mermaid",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "ui-designer",
      "description": "UI设计师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/ui-designer",
        "./skills/frontend-design",
        "./skills/mermaid",
        "./skills/zh-product-doc-generator"
      ]
    },
    
    // 领域/架构类岗位
    {
      "name": "domain-expert",
      "description": "领域专家岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/domain-expert",
        "./skills/ddd4j-project-builder",
        "./skills/mermaid",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "technical-architect",
      "description": "技术架构师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/technical-architect",
        "./skills/ddd4j-project-builder",
        "./skills/mermaid",
        "./skills/documentation-builder",
        "./skills/zh-product-doc-generator"
      ]
    },
    
    // 开发类岗位
    {
      "name": "frontend-engineer",
      "description": "前端开发工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/frontend-engineer",
        "./skills/code-generator",
        "./skills/frontend-design",
        "./skills/documentation-builder",
        "./skills/mermaid"
      ]
    },
    {
      "name": "backend-engineer",
      "description": "后端开发工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/backend-engineer",
        "./skills/code-generator",
        "./skills/ddd4j-project-builder",
        "./skills/documentation-builder",
        "./skills/mermaid"
      ]
    },
    {
      "name": "mobile-engineer",
      "description": "移动开发工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/mobile-engineer",
        "./skills/code-generator",
        "./skills/frontend-design",
        "./skills/documentation-builder",
        "./skills/mermaid"
      ]
    },
    {
      "name": "dba",
      "description": "数据库管理师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/dba",
        "./skills/mermaid",
        "./skills/documentation-builder",
        "./skills/zh-product-doc-generator"
      ]
    },
    
    // 测试类岗位
    {
      "name": "test-engineer",
      "description": "测试工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/test-engineer",
        "./skills/test-writer",
        "./skills/webapp-testing",
        "./skills/code-generator",
        "./skills/documentation-builder",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "qa-engineer",
      "description": "QA工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/qa-engineer",
        "./skills/test-writer",
        "./skills/webapp-testing",
        "./skills/documentation-builder",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "testor",
      "description": "测试员岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/testor",
        "./skills/test-writer",
        "./skills/webapp-testing",
        "./skills/zh-product-doc-generator"
      ]
    },
    
    // 发布/运维类岗位
    {
      "name": "devops-engineer",
      "description": "DevOps工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/devops-engineer",
        "./skills/documentation-builder",
        "./skills/mermaid",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "release-engineer",
      "description": "发布工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/release-engineer",
        "./skills/documentation-builder",
        "./skills/mermaid",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "operations-engineer",
      "description": "运维工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/operations-engineer",
        "./skills/documentation-builder",
        "./skills/mermaid",
        "./skills/zh-product-doc-generator"
      ]
    },
    {
      "name": "sre-engineer",
      "description": "SRE工程师岗位技能包",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/roles/sre-engineer",
        "./skills/documentation-builder",
        "./skills/mermaid",
        "./skills/zh-product-doc-generator"
      ]
    }
  ]
}
```

### 4.2 共享机制说明

1. **支撑 Skills Plugins**：
   - `document-skills`、`markdown-skills`、`development-skills` 等作为**独立的 plugin**
   - 用户可以直接安装这些支撑 plugin 使用通用技能

2. **岗位 Skills Plugins**：
   - 每个岗位 plugin 通过**直接引用支撑 skills 的路径**来共享使用
   - 例如：`./skills/mermaid`、`./skills/zh-product-doc-generator` 等
   - 岗位 plugin 包含：岗位核心 skill（`./skills/roles/{role-name}`）+ 引用的支撑 skills

3. **优势**：
   - **避免重复**：支撑 skills 只需定义一次
   - **独立维护**：支撑 skills 可以独立更新
   - **灵活组合**：每个岗位 plugin 可以根据需要选择引用的支撑 skills
   - **清晰依赖**：通过路径引用，明确显示依赖关系

---

## 五、测试岗位职责边界分析

### 5.1 三个测试岗位的职责对比

| 岗位 | 职责定位 | 核心差异 | 是否重复 |
|------|---------|---------|---------|
| **测试工程师（TE）** | 技术实现导向 | 专注于**自动化测试工具开发**与测试技术实现 | ❌ 不重复 |
| **QA工程师（QA）** | 质量保证流程导向 | 专注于**测试计划制定、质量评估与流程管控** | ❌ 不重复 |
| **测试员（TT）** | 测试执行导向 | 专注于**手工测试执行**与基础测试用例编写 | ❌ 不重复 |

### 5.2 职责边界说明

#### 测试工程师（TE）vs QA工程师（QA）

**相同点**：
- 都编写测试用例
- 都设计自动化测试脚本
- 都进行功能测试
- 都输出测试报告和缺陷跟踪记录

**不同点**：
- **TE**：更偏向**技术实现**，负责自动化测试框架搭建、脚本开发、工具选型
- **QA**：更偏向**流程管控**，负责测试计划制定、质量评估、质量度量、缺陷分析

**建议**：
- 在**中小型团队**中，TE 和 QA 可以合并为一个岗位（`test-engineer` 或 `qa-engineer`）
- 在**大型团队**中，建议分开，TE 专注技术，QA 专注流程

#### 测试员（TT）vs 测试工程师（TE）/QA工程师（QA）

**相同点**：
- 都编写测试用例
- 都进行功能测试
- 都输出测试报告和缺陷记录

**不同点**：
- **TT**：**手工测试为主**，不涉及自动化测试脚本开发
- **TE/QA**：**自动化测试为主**，涉及脚本开发和框架搭建

**建议**：
- **TT** 可以作为**初级测试岗位**或**手工测试专项岗位**保留
- 如果团队规模较小，可以合并到 TE 或 QA 中

### 5.3 推荐方案

#### 方案 A：保留三个岗位（推荐用于大型团队）

- **测试工程师（TE）**：自动化测试技术实现
- **QA工程师（QA）**：质量保证流程管控
- **测试员（TT）**：手工测试执行

**适用场景**：大型团队，职责分工明确

#### 方案 B：合并为两个岗位（推荐用于中小型团队）

- **测试工程师（TE）**：自动化测试技术实现 + 手工测试执行
- **QA工程师（QA）**：质量保证流程管控

**适用场景**：中小型团队，TE 兼顾手工和自动化测试

#### 方案 C：合并为一个岗位（推荐用于小型团队）

- **QA工程师（QA）**：质量保证全流程（测试计划 + 测试执行 + 自动化 + 质量评估）

**适用场景**：小型团队，一人负责所有测试工作

### 5.4 当前规划采用方案

**当前规划采用方案 A**（保留三个岗位），原因：
1. 覆盖不同团队规模的需求
2. 职责边界清晰，便于后续扩展
3. 用户可以根据实际需求选择安装对应的 plugin

**如果确认需要合并**，可以在实现阶段根据实际需求调整。

---

## 六、运维岗位职责边界分析

### 6.1 三个运维岗位的职责对比（已处理冲突）

| 岗位 | 职责定位 | 核心差异 | 是否冲突 |
|------|---------|---------|---------|
| **运维工程师（OE）** | 传统运维导向 | 专注于**基础设施运维、系统监控与故障处理** | ❌ 不冲突 |
| **SRE工程师（SRE）** | 可靠性工程导向 | 专注于**系统可靠性设计、自动化运维与工程化实践** | ❌ 不冲突 |
| **系统工程师（SE）** | ~~职责重叠~~ | ~~职责完全被 OE 和 SRE 覆盖~~ | ✅ **已删除** |

### 6.2 职责冲突分析

#### 原始冲突问题

**系统工程师（SE）的职责**：
- 负责系统监控（Prometheus + Grafana）、日志分析（ELK）、告警响应
- 实施容量规划、灾备演练、性能调优、安全加固

**冲突点**：
- SE 的职责**完全被运维工程师（OE）和 SRE 工程师（SRE）覆盖**
- SE 没有独特的职责定位，属于冗余岗位
- "系统工程师"名称过于宽泛，容易与"系统架构师（SA）"混淆

#### 解决方案

**已删除系统工程师（SE）**，原因：
1. **职责完全重叠**：SE 的所有职责都在 OE 和 SRE 的职责范围内
2. **定位不清晰**："系统工程师"在不同公司可能有不同含义（可能是系统架构师、运维工程师、或硬件工程师）
3. **避免混淆**：与"系统架构师（System Architect / SA）"名称相似，容易造成混淆

### 6.3 运维工程师（OE）vs SRE工程师（SRE）

#### 相同点
- 都负责系统监控（Prometheus + Grafana）、日志分析（ELK）、告警响应
- 都实施容量规划、灾备演练、性能调优、安全加固
- 都处理故障和应急响应

#### 不同点

| 维度 | 运维工程师（OE） | SRE工程师（SRE） |
|------|----------------|----------------|
| **工作方式** | 传统运维，手动操作较多 | 工程化运维，自动化为主 |
| **核心关注** | 基础设施稳定运行 | 系统可靠性设计（SLO/SLI） |
| **技术深度** | 运维工具使用 | 自动化开发、IaC、混沌工程 |
| **工作重点** | 日常运维、故障处理 | 可靠性设计、故障复盘、持续改进 |
| **输出产物** | 运维手册、监控配置 | SLO/SLI 定义、Postmortem、混沌工程方案 |

#### 职责边界

- **运维工程师（OE）**：
  - 更偏向**传统运维**，专注于基础设施的稳定运行
  - 负责日常运维操作（备份、恢复、升级、维护）
  - 故障处理与应急响应
  - 基础设施管理（服务器、网络、存储）

- **SRE工程师（SRE）**：
  - 更偏向**可靠性工程**，专注于系统可靠性的设计与改进
  - 推行"运维即代码"（IaC）、自动化修复、混沌工程
  - 可靠性设计（SLO/SLI 定义、错误预算管理）
  - 故障复盘与持续改进（Postmortem、根因分析）
  - 自动化运维（自愈系统、自动化扩缩容）

### 6.4 推荐方案

#### 方案 A：保留两个岗位（推荐用于中大型团队）

- **运维工程师（OE）**：传统运维，基础设施管理
- **SRE工程师（SRE）**：可靠性工程，自动化运维

**适用场景**：中大型团队，职责分工明确

#### 方案 B：合并为一个岗位（推荐用于小型团队）

- **SRE工程师（SRE）**：兼顾传统运维和可靠性工程

**适用场景**：小型团队，一人负责所有运维工作

### 6.5 当前规划采用方案

**当前规划采用方案 A**（保留两个岗位：OE 和 SRE），原因：
1. **职责边界清晰**：OE 专注传统运维，SRE 专注可靠性工程
2. **覆盖不同团队需求**：大型团队可以分开，小型团队可以选择其中一个
3. **避免混淆**：删除 SE，避免与系统架构师（SA）混淆

---

## 七、各岗位详细 Skills 规划（细粒度工具技能）

> **说明**：本节基于实际工作场景，为每个岗位规划完整的 skills 列表。技能颗粒度细化到**工具使用级别**，例如：
> - `database-mysql-install`（MySQL 数据库安装技能）
> - `database-mysql-config`（MySQL 数据库配置技能）
> - `database-mysql-query`（MySQL 查询技能）
> 
> 包括：
> - ✅ **已存在的 skills**：可以直接引用
> - 🆕 **需要新增的细粒度工具 skills**：需要后续实现
> - 🔧 **工具分类**：按工具类型组织技能（数据库、框架、测试工具、部署工具等）

---

### 7.1 产品类岗位

#### 项目经理（Project Manager / PM）

**工作场景**：
- 项目计划、项目进度管理
- 风险管理、资源协调
- 项目汇报、项目复盘

**常用工具**：
- 项目管理：Jira、Teambition、禅道、Microsoft Project、Asana
- 协作工具：Confluence、飞书文档、Notion
- 甘特图：Microsoft Project、Jira、GanttProject
- 沟通工具：Zoom、腾讯会议、飞书会议、Slack、钉钉
- 文档工具：Markdown、Word、Excel、PowerPoint、PPTX、XLSX
- 项目计划模板：Word、Excel、Markdown
- 项目汇报PPT模板：Word、PPTX
- AI 能力：MCP、Skills、Search


**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/project-manager`（岗位核心 skill）
- `./skills/mermaid`（甘特图、里程碑图、项目流程图）
- `./skills/zh-product-doc-generator`（项目计划模板）
- `./skills/pptx`（项目汇报PPT）
- `./skills/xlsx`（项目进度表、资源分配表）

🆕 **需要新增的细粒度工具 skills**：

**项目管理工具类**：
- `./skills/tool-jira-project`（Jira 项目管理）
- `./skills/tool-jira-sprint`（Jira Sprint 管理）
- `./skills/tool-teambition-project`（Teambition 项目管理）
- `./skills/tool-zentao-project`（禅道项目管理）
- `./skills/tool-ms-project`（Microsoft Project 项目计划）
- `./skills/tool-asana-project`（Asana 项目管理）

**协作工具类**：
- `./skills/tool-confluence-project`（Confluence 项目文档）
- `./skills/tool-feishu-project`（飞书项目协作）
- `./skills/tool-notion-project`（Notion 项目管理）

**甘特图工具类**：
- `./skills/tool-ms-project-gantt`（Microsoft Project 甘特图）
- `./skills/tool-jira-gantt`（Jira 甘特图）
- `./skills/tool-ganttproject`（GanttProject 使用）

**沟通工具类**：
- `./skills/tool-zoom-meeting`（Zoom 项目会议）
- `./skills/tool-teams-meeting`（腾讯会议项目沟通）
- `./skills/tool-feishu-meeting`（飞书项目会议）
- `./skills/tool-slack-communication`（Slack 项目沟通）
- `./skills/tool-dingtalk-communication`（钉钉项目沟通）

**业务技能类**：
- `./skills/project-planning-wbs`（WBS 工作分解）
- `./skills/project-planning-schedule`（项目进度计划）
- `./skills/project-planning-milestone`（里程碑规划）
- `./skills/project-progress-tracking`（项目进度跟踪）
- `./skills/project-progress-reporting`（项目进度汇报）
- `./skills/project-risk-identification`（风险识别）
- `./skills/project-risk-management`（风险管理）
- `./skills/project-resource-allocation`（资源分配）
- `./skills/project-resource-coordination`（资源协调）
- `./skills/project-reporting-status`（项目状态报告）
- `./skills/project-reporting-retrospective`（项目复盘）

---

#### 产品经理（Product Manager / PM）

**工作场景**：
- 市场调研、竞品分析、用户研究
- PRD 编写、需求管理、优先级排序
- 产品规划、版本规划、路线图制定
- 跨部门协作、需求评审、验收测试

**常用工具**：
- 文档工具：Word、PowerPoint、Excel、Confluence、飞书文档
- 原型工具：Axure、墨刀、Figma、Sketch
- 项目管理：Jira、禅道、Teambition、Notion
- 数据分析：Google Analytics、Mixpanel、神策数据、GrowingIO
- 图表工具：Mermaid、Draw.io、ProcessOn
- 数据可视化工具：Tableau、Power BI、Domo、Looker
- AI 能力：MCP、Skills、Search

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/product-manager`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（产品调研模板、PRD模板）
- `./skills/mermaid`（用户旅程图、流程图、甘特图）
- `./skills/docx`（Word 文档输出）
- `./skills/pptx`（演示文稿）
- `./skills/xlsx`（数据分析表格）

🆕 **需要新增的细粒度工具 skills**：

**文档工具类**：
- `./skills/tool-confluence-create`（Confluence 文档创建）
- `./skills/tool-confluence-collaborate`（Confluence 协作编辑）
- `./skills/tool-feishu-doc`（飞书文档使用）
- `./skills/tool-notion-setup`（Notion 工作区搭建）

**原型工具类**：
- `./skills/tool-axure-prototype`（Axure 原型设计）
- `./skills/tool-modao-prototype`（墨刀原型设计）
- `./skills/tool-figma-prototype`（Figma 原型设计）

**项目管理工具类**：
- `./skills/tool-jira-requirement`（Jira 需求管理）
- `./skills/tool-jira-roadmap`（Jira 路线图规划）
- `./skills/tool-zentao-requirement`（禅道需求管理）
- `./skills/tool-teambition-project`（Teambition 项目管理）

**数据分析工具类**：
- `./skills/tool-google-analytics-setup`（Google Analytics 配置）
- `./skills/tool-google-analytics-report`（Google Analytics 报表分析）
- `./skills/tool-mixpanel-funnel`（Mixpanel 漏斗分析）
- `./skills/tool-shence-event`（神策数据事件分析）
- `./skills/tool-growingio-analysis`（GrowingIO 用户行为分析）

**图表工具类**：
- `./skills/tool-drawio-flowchart`（Draw.io 流程图绘制）
- `./skills/tool-processon-mindmap`（ProcessOn 思维导图）

**业务技能类**：
- `./skills/user-research-interview`（用户访谈：访谈提纲、访谈记录、洞察提取）
- `./skills/user-research-persona`（用户画像：Persona 创建、用户分群）
- `./skills/user-research-journey`（用户旅程图：旅程映射、触点分析）
- `./skills/competitor-analysis-comparison`（竞品对比：Feature Comparison 表格）
- `./skills/competitor-analysis-swot`（竞品 SWOT 分析）
- `./skills/roadmap-planner-quarterly`（季度路线图规划）
- `./skills/roadmap-planner-yearly`（年度路线图规划）
- `./skills/requirement-management-pool`（需求池管理）
- `./skills/requirement-priority-rice`（RICE 模型优先级排序）
- `./skills/requirement-priority-aarrr`（AARRR 模型优先级排序）
- `./skills/user-story-write`（用户故事编写：User Story、Acceptance Criteria）
- `./skills/product-metrics-kpi`（KPI 指标定义）
- `./skills/product-metrics-dashboard`（数据看板设计）

---

#### 产品调研专员（Product Research Specialist / PRS）

**工作场景**：
- 用户访谈、焦点小组、问卷设计
- 数据分析、用户行为分析
- 调研报告撰写

**常用工具**：
- 问卷工具：问卷星、腾讯问卷、Google Forms、Typeform
- 访谈工具：Zoom、腾讯会议、飞书会议
- 数据分析：Excel、SPSS、Python、R
- 可视化：Tableau、Power BI、Python Matplotlib
- AI 能力：MCP、Skills、Search

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/product-research-specialist`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（产品调研模板）
- `./skills/mermaid`（用户旅程图、数据流程图）
- `./skills/xlsx`（问卷数据、分析表格）

🆕 **需要新增的细粒度工具 skills**：

**问卷工具类**：
- `./skills/tool-wenjuanxing-create`（问卷星问卷创建）
- `./skills/tool-wenjuanxing-analysis`（问卷星数据分析）
- `./skills/tool-google-forms-create`（Google Forms 问卷创建）
- `./skills/tool-typeform-design`（Typeform 问卷设计）

**访谈工具类**：
- `./skills/tool-zoom-interview`（Zoom 用户访谈）
- `./skills/tool-teams-meeting`（腾讯会议访谈）
- `./skills/tool-feishu-meeting`（飞书会议访谈）

**数据分析工具类**：
- `./skills/tool-excel-statistics`（Excel 统计分析）
- `./skills/tool-spss-analysis`（SPSS 数据分析）
- `./skills/tool-python-pandas`（Python Pandas 数据分析）
- `./skills/tool-r-analysis`（R 语言数据分析）

**可视化工具类**：
- `./skills/tool-tableau-dashboard`（Tableau 仪表板创建）
- `./skills/tool-powerbi-report`（Power BI 报表创建）
- `./skills/tool-python-matplotlib`（Python Matplotlib 可视化）

**业务技能类**：
- `./skills/user-interview-outline`（用户访谈提纲设计）
- `./skills/user-interview-record`（用户访谈记录整理）
- `./skills/user-interview-insight`（用户访谈洞察提取）
- `./skills/survey-structure-design`（问卷结构设计）
- `./skills/survey-question-design`（问卷题目设计）
- `./skills/survey-logic-jump`（问卷逻辑跳转设置）
- `./skills/data-analysis-statistics`（统计分析：描述性统计、推断统计）
- `./skills/data-analysis-trend`（趋势分析）
- `./skills/data-analysis-correlation`（相关性分析）
- `./skills/user-persona-create`（用户画像 Persona 创建）
- `./skills/user-segmentation`（用户分群）

---

#### 产品分析师（Product Analyst / PA）

**工作场景**：
- 数据分析、用户行为分析
- 产品指标监控、数据报告
- 业务洞察、决策支持

**常用工具**：
- 数据分析：Google Analytics、Mixpanel、神策数据、GrowingIO、友盟+
- SQL 工具：MySQL Workbench、Navicat、DBeaver
- 可视化：Tableau、Power BI、DataV、ECharts
- 编程：Python、R、SQL

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/product-analyst`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（产品调研模板、需求分析模板）
- `./skills/mermaid`（数据流程图、用户画像图）
- `./skills/xlsx`（数据分析表格）

🆕 **需要新增的细粒度工具 skills**：

**数据分析工具类**：
- `./skills/tool-google-analytics-setup`（Google Analytics 配置）
- `./skills/tool-google-analytics-funnel`（Google Analytics 漏斗分析）
- `./skills/tool-mixpanel-event`（Mixpanel 事件分析）
- `./skills/tool-shence-event`（神策数据事件分析）
- `./skills/tool-growingio-funnel`（GrowingIO 漏斗分析）
- `./skills/tool-umeng-analysis`（友盟+ 数据分析）

**SQL 工具类**：
- `./skills/tool-mysql-workbench`（MySQL Workbench 使用）
- `./skills/tool-navicat-query`（Navicat SQL 查询）
- `./skills/tool-dbeaver-setup`（DBeaver 数据库管理）

**可视化工具类**：
- `./skills/tool-tableau-dashboard`（Tableau 数据看板）
- `./skills/tool-powerbi-report`（Power BI 报表）
- `./skills/tool-datav-dashboard`（DataV 数据可视化）
- `./skills/tool-echarts-chart`（ECharts 图表制作）

**编程工具类**：
- `./skills/tool-python-pandas`（Python Pandas 数据分析）
- `./skills/tool-python-sqlalchemy`（Python SQLAlchemy 数据库操作）
- `./skills/tool-r-tidyverse`（R Tidyverse 数据分析）

**业务技能类**：
- `./skills/data-analysis-statistics`（统计分析）
- `./skills/data-analysis-trend`（趋势分析）
- `./skills/data-analysis-funnel`（漏斗分析）
- `./skills/product-metrics-kpi-define`（KPI 指标定义）
- `./skills/product-metrics-monitor`（指标监控）
- `./skills/product-metrics-dashboard`（数据看板设计）
- `./skills/user-behavior-path`（用户行为路径分析）
- `./skills/user-behavior-heatmap`（用户行为热力图）
- `./skills/user-retention-analysis`（用户留存分析）
- `./skills/business-insight-report`（业务洞察报告）
- `./skills/business-trend-prediction`（趋势预测）
- `./skills/business-decision-support`（决策支持）

---

### 7.2 市场类岗位

#### 市场调研分析师（Market Research Analyst / MRA）

**工作场景**：
- 市场调研、行业分析
- 竞争格局分析、定价策略
- 市场报告撰写

**常用工具**：
- 市场数据：艾瑞、易观、QuestMobile、36氪、虎嗅
- 电商平台：淘宝、京东、亚马逊数据分析
- 数据分析：Excel、Python、Tableau
- 报告工具：PowerPoint、Keynote

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/market-research-analyst`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（市场调研模板）
- `./skills/mermaid`（市场分析图、竞争格局图）
- `./skills/xlsx`（市场数据表格）
- `./skills/pptx`（市场分析演示文稿）

🆕 **需要新增的细粒度工具 skills**：

**市场数据平台类**：
- `./skills/tool-iresearch-data`（艾瑞数据获取与分析）
- `./skills/tool-analysys-data`（易观数据分析）
- `./skills/tool-questmobile-data`（QuestMobile 数据获取）
- `./skills/tool-36kr-research`（36氪行业研究）
- `./skills/tool-huxiu-research`（虎嗅行业分析）

**电商平台分析类**：
- `./skills/tool-taobao-analysis`（淘宝数据分析）
- `./skills/tool-jd-analysis`（京东数据分析）
- `./skills/tool-amazon-analysis`（亚马逊数据分析）

**数据分析工具类**：
- `./skills/tool-excel-market-analysis`（Excel 市场数据分析）
- `./skills/tool-python-market-analysis`（Python 市场数据分析）
- `./skills/tool-tableau-market`（Tableau 市场数据可视化）

**业务技能类**：
- `./skills/market-research-size`（市场规模分析）
- `./skills/market-research-trend`（市场趋势分析）
- `./skills/market-segmentation`（市场细分）
- `./skills/competitor-landscape`（竞争格局分析）
- `./skills/competitor-comparison`（竞品对比分析）
- `./skills/competitor-swot`（竞品 SWOT 分析）
- `./skills/pricing-model`（定价模型设计）
- `./skills/pricing-analysis`（价格分析）
- `./skills/channel-distribution`（渠道分布分析）
- `./skills/channel-effectiveness`（渠道效果分析）

---

#### 市场专员（Marketing Specialist / MS）

**工作场景**：
- 营销策略制定、营销活动策划
- 渠道管理、推广方案
- 营销效果分析

**常用工具**：
- 营销平台：微信、微博、抖音、小红书、B站
- 广告平台：Google Ads、Facebook Ads、巨量引擎、腾讯广告
- 邮件营销：MailChimp、SendGrid、EDM
- 数据分析：Google Analytics、百度统计、神策数据

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/marketing-specialist`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（市场调研模板）
- `./skills/mermaid`（渠道分布图、营销漏斗图）
- `./skills/pptx`（营销方案演示）

🆕 **需要新增的细粒度工具 skills**：

**营销平台类**：
- `./skills/tool-wechat-marketing`（微信营销：公众号、朋友圈、视频号）
- `./skills/tool-weibo-marketing`（微博营销）
- `./skills/tool-douyin-marketing`（抖音营销）
- `./skills/tool-xiaohongshu-marketing`（小红书营销）
- `./skills/tool-bilibili-marketing`（B站营销）

**广告平台类**：
- `./skills/tool-google-ads-setup`（Google Ads 广告投放）
- `./skills/tool-facebook-ads-setup`（Facebook Ads 广告投放）
- `./skills/tool-juliang-engine`（巨量引擎广告投放）
- `./skills/tool-tencent-ads`（腾讯广告投放）

**邮件营销工具类**：
- `./skills/tool-mailchimp-campaign`（MailChimp 邮件营销）
- `./skills/tool-sendgrid-email`（SendGrid 邮件发送）
- `./skills/tool-edm-design`（EDM 邮件设计）

**数据分析工具类**：
- `./skills/tool-google-analytics-marketing`（Google Analytics 营销分析）
- `./skills/tool-baidu-tongji`（百度统计营销分析）
- `./skills/tool-shence-marketing`（神策数据营销分析）

**业务技能类**：
- `./skills/marketing-strategy-plan`（营销计划制定）
- `./skills/marketing-mix`（营销组合：4P、7P 模型）
- `./skills/campaign-planning`（营销活动策划）
- `./skills/campaign-execution`（营销活动执行）
- `./skills/channel-strategy`（渠道策略制定）
- `./skills/channel-effectiveness-analysis`（渠道效果分析）
- `./skills/marketing-roi`（营销 ROI 计算）
- `./skills/marketing-conversion-rate`（转化率分析）
- `./skills/marketing-cac`（获客成本 CAC 分析）

---

### 7.3 技术调研类岗位

#### 技术研究工程师（Research Engineer / REng）

**工作场景**：
- 技术选型、技术预研
- POC 验证、技术评估
- 技术报告撰写

**常用工具**：
- 技术文档：GitHub、GitLab、Confluence、Notion
- 技术社区：Stack Overflow、掘金、InfoQ、技术博客
- 原型工具：Docker、Kubernetes、云平台（AWS/Azure/阿里云）
- 文档工具：Markdown、Mermaid、Draw.io

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/tech-research-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（技术文档生成）
- `./skills/mermaid`（技术架构图、技术选型对比图）
- `./skills/zh-product-doc-generator`（技术调研模板）

🆕 **需要新增的细粒度工具 skills**：

**技术文档工具类**：
- `./skills/tool-github-research`（GitHub 技术调研）
- `./skills/tool-gitlab-research`（GitLab 技术调研）
- `./skills/tool-confluence-tech-doc`（Confluence 技术文档）
- `./skills/tool-notion-tech-doc`（Notion 技术文档）

**技术社区类**：
- `./skills/tool-stackoverflow-research`（Stack Overflow 技术调研）
- `./skills/tool-juejin-research`（掘金技术调研）
- `./skills/tool-infoq-research`（InfoQ 技术调研）

**原型验证工具类**：
- `./skills/tool-docker-poc`（Docker POC 验证）
- `./skills/tool-kubernetes-poc`（Kubernetes POC 验证）
- `./skills/tool-aws-poc`（AWS POC 验证）
- `./skills/tool-azure-poc`（Azure POC 验证）
- `./skills/tool-aliyun-poc`（阿里云 POC 验证）
- `./skills/tool-tencent-poc`（腾讯云 POC 验证）
- `./skills/tool-huawei-poc`（华为云 POC 验证）

**业务技能类**：
- `./skills/tech-evaluation-comparison`（技术对比分析）
- `./skills/tech-evaluation-feasibility`（技术可行性分析）
- `./skills/poc-planning`（POC 方案设计）
- `./skills/poc-execution`（POC 执行验证）
- `./skills/poc-report`（POC 验证报告）
- `./skills/tech-risk-identification`（技术风险识别）
- `./skills/tech-risk-response`（技术风险应对）
- `./skills/tech-trend-tracking`（前沿技术跟踪）

---

#### 系统架构师（System Architect / SA (Arch)）

**工作场景**：
- 系统架构设计、技术选型
- 领域模型设计、架构评审
- 架构文档编写

**常用工具**：
- 架构设计：Draw.io、Lucidchart、C4-PlantUML、Structurizr
- 代码管理：Git、GitHub、GitLab
- 文档工具：Confluence、Notion、Markdown
- 建模工具：PlantUML、Mermaid、Enterprise Architect

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/system-architect`（岗位核心 skill）
- `./skills/ddd4j-project-builder`（DDD 项目结构、架构模式）
- `./skills/mermaid`（系统架构图、C4图、部署图）
- `./skills/documentation-builder`（架构文档）
- `./skills/zh-product-doc-generator`（系统架构设计模板）

🆕 **需要新增的细粒度工具 skills**：

**架构设计工具类**：
- `./skills/tool-drawio-architecture`（Draw.io 架构图绘制）
- `./skills/tool-lucidchart-architecture`（Lucidchart 架构设计）
- `./skills/tool-c4-plantuml`（C4-PlantUML 架构图）
- `./skills/tool-structurizr`（Structurizr 架构文档）

**代码管理工具类**：
- `./skills/tool-git-version-control`（Git 版本控制）
- `./skills/tool-github-architecture`（GitHub 架构文档管理）
- `./skills/tool-gitlab-architecture`（GitLab 架构文档管理）

**文档工具类**：
- `./skills/tool-confluence-architecture`（Confluence 架构文档）
- `./skills/tool-notion-architecture`（Notion 架构文档）
- `./skills/tool-markdown-architecture`（Markdown 架构文档）

**建模工具类**：
- `./skills/tool-plantuml-diagram`（PlantUML 架构图）
- `./skills/tool-enterprise-architect`（Enterprise Architect 建模）

**业务技能类**：
- `./skills/architecture-layered`（分层架构设计）
- `./skills/architecture-microservices`（微服务架构设计）
- `./skills/architecture-event-driven`（事件驱动架构设计）
- `./skills/domain-modeling-bounded-context`（限界上下文划分）
- `./skills/domain-modeling-aggregate`（聚合设计）
- `./skills/domain-modeling-domain-event`（领域事件设计）
- `./skills/tech-stack-comparison`（技术栈对比分析）
- `./skills/tech-stack-matrix`（技术选型矩阵）
- `./skills/architecture-review-checklist`（架构评审清单）
- `./skills/architecture-review-report`（架构评审报告）
- `./skills/nfr-performance`（性能需求设计）
- `./skills/nfr-security`（安全需求设计）
- `./skills/nfr-availability`（可用性需求设计）

---

#### 云计算工程师（Cloud Engineer / CE）

**工作场景**：
- 云架构设计、云资源规划
- 容器化、DevOps 实践
- 云成本优化

**常用工具**：
- 云平台：AWS、Azure、阿里云、腾讯云、华为云
- 容器化：Docker、Kubernetes、Docker Compose
- IaC：Terraform、CloudFormation、Ansible
- 监控：CloudWatch、Azure Monitor、云监控

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/cloud-engineer`（岗位核心 skill）
- `./skills/mermaid`（云架构图、部署拓扑图）
- `./skills/documentation-builder`（云架构文档）
- `./skills/zh-product-doc-generator`（技术调研模板）

🆕 **需要新增的细粒度工具 skills**：

**AWS 云平台类**：
- `./skills/cloud-aws-ec2`（AWS EC2 云服务器使用）
- `./skills/cloud-aws-s3`（AWS S3 对象存储使用）
- `./skills/cloud-aws-rds`（AWS RDS 数据库使用）
- `./skills/cloud-aws-vpc`（AWS VPC 私有网络使用）
- `./skills/cloud-aws-lambda`（AWS Lambda 函数使用）
- `./skills/cloud-aws-cloudwatch`（AWS CloudWatch 监控使用）

**Azure 云平台类**：
- `./skills/cloud-azure-vm`（Azure VM 虚拟机使用）
- `./skills/cloud-azure-storage`（Azure Storage 存储使用）
- `./skills/cloud-azure-sql`（Azure SQL 数据库使用）
- `./skills/cloud-azure-monitor`（Azure Monitor 监控使用）

**阿里云平台类**：
- `./skills/cloud-aliyun-ecs`（阿里云 ECS 云服务器使用）
- `./skills/cloud-aliyun-oss`（阿里云 OSS 对象存储使用）
- `./skills/cloud-aliyun-rds`（阿里云 RDS 数据库使用）
- `./skills/cloud-aliyun-vpc`（阿里云 VPC 私有网络使用）
- `./skills/cloud-aliyun-monitor`（阿里云监控使用）

**腾讯云平台类**：
- `./skills/cloud-tencent-cvm`（腾讯云 CVM 云服务器使用）
- `./skills/cloud-tencent-cos`（腾讯云 COS 对象存储使用）
- `./skills/cloud-tencent-cdb`（腾讯云 CDB 数据库使用）
- `./skills/cloud-tencent-vpc`（腾讯云 VPC 私有网络使用）
- `./skills/cloud-tencent-clb`（腾讯云 CLB 负载均衡使用）
- `./skills/cloud-tencent-ckafka`（腾讯云 CKafka 消息队列使用）
- `./skills/cloud-tencent-redis`（腾讯云 Redis 缓存使用）
- `./skills/cloud-tencent-monitor`（腾讯云监控使用）

**华为云平台类**：
- `./skills/cloud-huawei-ecs`（华为云 ECS 云服务器使用）
- `./skills/cloud-huawei-obs`（华为云 OBS 对象存储使用）
- `./skills/cloud-huawei-rds`（华为云 RDS 数据库使用）
- `./skills/cloud-huawei-vpc`（华为云 VPC 私有网络使用）
- `./skills/cloud-huawei-elb`（华为云 ELB 负载均衡使用）
- `./skills/cloud-huawei-dms`（华为云 DMS 消息队列使用）
- `./skills/cloud-huawei-dcs`（华为云 DCS Redis 缓存使用）
- `./skills/cloud-huawei-monitor`（华为云监控使用）

**容器化工具类**：
- `./skills/tool-docker-install`（Docker 安装）
- `./skills/tool-docker-image`（Docker 镜像构建）
- `./skills/tool-docker-compose`（Docker Compose 使用）
- `./skills/tool-kubernetes-install`（Kubernetes 集群安装）
- `./skills/tool-kubernetes-deploy`（Kubernetes 部署）

**IaC 工具类**：
- `./skills/tool-terraform-install`（Terraform 安装）
- `./skills/tool-terraform-write`（Terraform 脚本编写）
- `./skills/tool-cloudformation-write`（CloudFormation 模板编写）
- `./skills/tool-ansible-playbook`（Ansible Playbook 编写）

**业务技能类**：
- `./skills/cloud-architecture-design`（云架构设计）
- `./skills/cloud-resource-planning`（云资源规划）
- `./skills/cloud-cost-analysis`（云成本分析）
- `./skills/cloud-cost-optimization`（云成本优化建议）

---

#### 云计算架构师（Cloud Architect / CA）

**工作场景**：
- 云架构设计、混合云方案
- 云迁移、云治理
- 云安全、合规

**常用工具**：
- 云平台：AWS、Azure、阿里云、腾讯云、华为云、混合云
- 架构设计：CloudCraft、AWS Architecture Center、Azure Architecture Center
- 迁移工具：AWS Migration Hub、Azure Migrate、CloudEndure
- 安全工具：AWS Security Hub、Azure Security Center、云安全中心

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/cloud-architect`（岗位核心 skill）
- `./skills/mermaid`（云架构图、部署拓扑图）
- `./skills/documentation-builder`（云架构文档）
- `./skills/zh-product-doc-generator`（系统架构设计模板）

🆕 **需要新增的细粒度工具 skills**：

**架构设计工具类**：
- `./skills/tool-cloudcraft-design`（CloudCraft 云架构设计）
- `./skills/tool-aws-architecture-center`（AWS Architecture Center 参考）
- `./skills/tool-azure-architecture-center`（Azure Architecture Center 参考）

**迁移工具类**：
- `./skills/tool-aws-migration-hub`（AWS Migration Hub 迁移）
- `./skills/tool-azure-migrate`（Azure Migrate 迁移）
- `./skills/tool-cloudendure`（CloudEndure 迁移）

**安全工具类**：
- `./skills/tool-aws-security-hub`（AWS Security Hub 安全中心）
- `./skills/tool-azure-security-center`（Azure Security Center 安全中心）
- `./skills/tool-aliyun-security-center`（阿里云安全中心）
- `./skills/tool-tencent-security-center`（腾讯云安全中心）
- `./skills/tool-huawei-security-center`（华为云安全中心）

**腾讯云平台类**：
- `./skills/cloud-tencent-architecture`（腾讯云架构设计）
- `./skills/cloud-tencent-migration`（腾讯云迁移方案）
- `./skills/cloud-tencent-hybrid-cloud`（腾讯云混合云方案）
- `./skills/cloud-tencent-governance`（腾讯云治理）
- `./skills/cloud-tencent-cvm`（腾讯云 CVM 使用）
- `./skills/cloud-tencent-cos`（腾讯云 COS 使用）
- `./skills/cloud-tencent-cdb`（腾讯云 CDB 使用）

**华为云平台类**：
- `./skills/cloud-huawei-architecture`（华为云架构设计）
- `./skills/cloud-huawei-migration`（华为云迁移方案）
- `./skills/cloud-huawei-hybrid-cloud`（华为云混合云方案）
- `./skills/cloud-huawei-governance`（华为云治理）
- `./skills/cloud-huawei-ecs`（华为云 ECS 使用）
- `./skills/cloud-huawei-obs`（华为云 OBS 使用）
- `./skills/cloud-huawei-rds`（华为云 RDS 使用）

**业务技能类**：
- `./skills/cloud-architecture-hybrid`（混合云架构设计）
- `./skills/cloud-architecture-multi`（多云架构设计）
- `./skills/cloud-migration-strategy`（云迁移策略）
- `./skills/cloud-migration-planning`（云迁移计划）
- `./skills/cloud-governance-resource`（云资源管理）
- `./skills/cloud-governance-compliance`（云合规检查）
- `./skills/cloud-security-architecture`（云安全架构设计）
- `./skills/cloud-security-compliance`（云合规设计）

---

### 7.4 需求分析类岗位

#### 需求分析师（Requirements Analyst / RA）

**工作场景**：
- 需求收集、需求分析
- SRS/PRD 编写、需求评审
- 需求跟踪、需求变更管理

**常用工具**：
- 需求管理：Jira、禅道、Teambition、Azure DevOps
- 文档工具：Word、Confluence、飞书文档
- 建模工具：Enterprise Architect、StarUML、PlantUML
- 协作工具：Zoom、腾讯会议、飞书会议

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/requirements-analyst`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（需求分析模板、PRD模板）
- `./skills/mermaid`（需求流程图、用例图）
- `./skills/docx`（需求文档输出）

🆕 **需要新增的细粒度工具 skills**：

**需求管理工具类**：
- `./skills/tool-jira-requirement`（Jira 需求管理）
- `./skills/tool-jira-traceability`（Jira 需求跟踪）
- `./skills/tool-zentao-requirement`（禅道需求管理）
- `./skills/tool-teambition-requirement`（Teambition 需求管理）
- `./skills/tool-azure-devops-requirement`（Azure DevOps 需求管理）

**文档工具类**：
- `./skills/tool-word-requirement`（Word 需求文档编写）
- `./skills/tool-confluence-requirement`（Confluence 需求文档）
- `./skills/tool-feishu-requirement`（飞书文档需求编写）

**建模工具类**：
- `./skills/tool-enterprise-architect-usecase`（Enterprise Architect 用例建模）
- `./skills/tool-staruml-usecase`（StarUML 用例图）
- `./skills/tool-plantuml-usecase`（PlantUML 用例图）

**协作工具类**：
- `./skills/tool-zoom-requirement-workshop`（Zoom 需求工作坊）
- `./skills/tool-teams-requirement-interview`（腾讯会议需求访谈）

**业务技能类**：
- `./skills/requirement-gathering-interview`（需求访谈）
- `./skills/requirement-gathering-workshop`（需求工作坊）
- `./skills/requirement-analysis-breakdown`（需求拆解）
- `./skills/requirement-priority`（需求优先级排序）
- `./skills/use-case-diagram`（用例图绘制）
- `./skills/use-case-description`（用例描述编写）
- `./skills/requirement-traceability-matrix`（需求跟踪矩阵）
- `./skills/requirement-change-process`（需求变更流程）
- `./skills/requirement-change-impact`（需求变更影响分析）

---

#### 系统分析师（System Analyst / SA）

**工作场景**：
- 系统分析、功能需求分析
- 非功能性需求分析
- 系统分析文档编写

**常用工具**：
- 建模工具：Enterprise Architect、StarUML、Visio、Draw.io
- 文档工具：Word、Confluence、Notion
- 流程图：ProcessOn、Draw.io、Lucidchart

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/system-analyst`（岗位核心 skill）
- `./skills/zh-product-doc-generator`（需求分析模板、系统分析模板）
- `./skills/mermaid`（系统流程图、数据流图）
- `./skills/documentation-builder`（系统分析文档）

🆕 **需要新增的细粒度工具 skills**：

**建模工具类**：
- `./skills/tool-enterprise-architect-system`（Enterprise Architect 系统建模）
- `./skills/tool-staruml-system`（StarUML 系统建模）
- `./skills/tool-visio-flowchart`（Visio 流程图绘制）
- `./skills/tool-drawio-dataflow`（Draw.io 数据流图）

**文档工具类**：
- `./skills/tool-word-system-analysis`（Word 系统分析文档）
- `./skills/tool-confluence-system`（Confluence 系统分析文档）
- `./skills/tool-notion-system`（Notion 系统分析文档）

**流程图工具类**：
- `./skills/tool-processon-business`（ProcessOn 业务流程分析）
- `./skills/tool-lucidchart-system`（Lucidchart 系统流程图）

**业务技能类**：
- `./skills/system-analysis-business-process`（业务流程分析）
- `./skills/system-analysis-boundary`（系统边界分析）
- `./skills/functional-requirements-list`（功能清单）
- `./skills/functional-requirements-description`（功能描述）
- `./skills/nfr-performance-analysis`（性能需求分析）
- `./skills/nfr-security-analysis`（安全需求分析）
- `./skills/nfr-availability-analysis`（可用性需求分析）
- `./skills/data-flow-diagram`（数据流图绘制）
- `./skills/data-dictionary`（数据字典编写）

---

### 7.5 设计类岗位

#### 交互设计师（UX Designer / UX）

**工作场景**：
- 用户研究、信息架构设计
- 交互原型设计、交互规范制定
- 可用性测试

**常用工具**：
- 原型工具：Axure、Figma、Sketch、墨刀、Principle
- AI 设计工具：Figma AI、Uizard、Galileo AI、Midjourney、DALL-E、Stable Diffusion
- 用户研究：UserTesting、Optimal Workshop、Hotjar
- 信息架构：XMind、MindMaster、ProcessOn
- 可用性测试：Maze、UserZoom、Lookback

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/ux-designer`（岗位核心 skill）
- `./skills/frontend-design`（交互设计规范）
- `./skills/mermaid`（用户旅程图、信息架构图、流程图）
- `./skills/zh-product-doc-generator`（视觉与交互 DNA 规范模板）

🆕 **需要新增的细粒度工具 skills**：

**原型工具类**：
- `./skills/tool-axure-prototype`（Axure 交互原型设计）
- `./skills/tool-figma-prototype`（Figma 交互原型设计）
- `./skills/tool-sketch-prototype`（Sketch 交互原型设计）
- `./skills/tool-modao-prototype`（墨刀交互原型设计）
- `./skills/tool-principle-animation`（Principle 交互动效）

**AI 设计工具类**：
- `./skills/tool-figma-ai`（Figma AI 智能设计助手）
- `./skills/tool-uizard-ai`（Uizard AI 原型生成）
- `./skills/tool-galileo-ai`（Galileo AI UI 设计生成）
- `./skills/tool-midjourney-design`（Midjourney AI 图像生成）
- `./skills/tool-dalle-design`（DALL-E AI 图像生成）
- `./skills/tool-stable-diffusion-design`（Stable Diffusion AI 图像生成）

**用户研究工具类**：
- `./skills/tool-usertesting-research`（UserTesting 用户测试）
- `./skills/tool-optimal-workshop`（Optimal Workshop 信息架构测试）
- `./skills/tool-hotjar-behavior`（Hotjar 用户行为分析）

**信息架构工具类**：
- `./skills/tool-xmind-ia`（XMind 信息架构设计）
- `./skills/tool-mindmaster-ia`（MindMaster 信息架构）
- `./skills/tool-processon-ia`（ProcessOn 信息架构图）

**可用性测试工具类**：
- `./skills/tool-maze-testing`（Maze 可用性测试）
- `./skills/tool-userzoom-testing`（UserZoom 远程测试）
- `./skills/tool-lookback-testing`（Lookback 用户访谈）

**业务技能类**：
- `./skills/user-journey-mapping`（用户旅程图绘制）
- `./skills/user-journey-touchpoint`（用户触点分析）
- `./skills/information-architecture-design`（信息架构 IA 设计）
- `./skills/information-architecture-navigation`（导航设计）
- `./skills/interaction-prototype-design`（交互原型设计）
- `./skills/interaction-prototype-spec`（交互说明编写）
- `./skills/interaction-specification-rules`（交互规则定义）
- `./skills/interaction-specification-state`（交互状态定义）
- `./skills/usability-testing-plan`（可用性测试方案）
- `./skills/usability-testing-report`（可用性测试报告）
- `./skills/accessibility-specification`（无障碍规范）
- `./skills/accessibility-check`（无障碍检查）

---

#### UI设计师（UI Designer / UI）

**工作场景**：
- 视觉设计、设计系统构建
- 高保真设计稿、设计规范
- 设计评审、设计交付

**常用工具**：
- 设计工具：Figma、Sketch、Adobe XD、Photoshop、Illustrator
- AI 设计工具：Figma AI、Adobe Firefly、Canva AI、Midjourney、DALL-E、Stable Diffusion、Leonardo AI、Runway ML
- 设计系统：Figma Design System、Storybook、Zeroheight
- 切图工具：Figma、Sketch、Cutterman、PxCook
- 动效工具：After Effects、Principle、Framer

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/ui-designer`（岗位核心 skill）
- `./skills/frontend-design`（UI设计规范、设计系统）
- `./skills/mermaid`（设计系统结构图）
- `./skills/zh-product-doc-generator`（UI 设计说明模板）

🆕 **需要新增的细粒度工具 skills**：

**设计工具类**：
- `./skills/tool-figma-design`（Figma UI 设计）
- `./skills/tool-sketch-design`（Sketch UI 设计）
- `./skills/tool-adobe-xd-design`（Adobe XD UI 设计）
- `./skills/tool-photoshop-design`（Photoshop 图像处理）
- `./skills/tool-illustrator-design`（Illustrator 图标设计）

**AI 设计工具类**：
- `./skills/tool-figma-ai`（Figma AI 智能设计助手）
- `./skills/tool-adobe-firefly`（Adobe Firefly AI 图像生成）
- `./skills/tool-canva-ai`（Canva AI 设计生成）
- `./skills/tool-midjourney-design`（Midjourney AI 图像生成）
- `./skills/tool-dalle-design`（DALL-E AI 图像生成）
- `./skills/tool-stable-diffusion-design`（Stable Diffusion AI 图像生成）
- `./skills/tool-leonardo-ai`（Leonardo AI 图像生成）
- `./skills/tool-runway-ml`（Runway ML AI 视频生成）

**设计系统工具类**：
- `./skills/tool-figma-design-system`（Figma Design System 构建）
- `./skills/tool-storybook-design-system`（Storybook 组件库文档）
- `./skills/tool-zeroheight-design-system`（Zeroheight 设计系统文档）

**切图工具类**：
- `./skills/tool-figma-export`（Figma 切图导出）
- `./skills/tool-sketch-export`（Sketch 切图导出）
- `./skills/tool-cutterman-export`（Cutterman 切图）
- `./skills/tool-pxcook-annotation`（PxCook 设计标注）

**动效工具类**：
- `./skills/tool-after-effects-animation`（After Effects 动效设计）
- `./skills/tool-principle-animation`（Principle 交互动效）
- `./skills/tool-framer-animation`（Framer 交互原型）

**业务技能类**：
- `./skills/design-system-component`（设计系统组件库）
- `./skills/design-system-token`（设计令牌 Design Token）
- `./skills/design-system-specification`（设计系统规范）
- `./skills/visual-design-color`（色彩系统设计）
- `./skills/visual-design-typography`（字体系统设计）
- `./skills/visual-design-icon`（图标系统设计）
- `./skills/design-specification-annotation`（设计标注）
- `./skills/design-specification-slice`（切图规范）
- `./skills/design-handoff-checklist`（设计交付清单）
- `./skills/design-handoff-development`（设计开发对接）

---

### 7.6 领域/架构类岗位

#### 领域专家（Domain Expert / DE）

**工作场景**：
- 领域知识梳理、统一语言定义
- 领域模型设计、业务规则定义
- 领域文档编写

**常用工具**：
- 建模工具：Enterprise Architect、StarUML、PlantUML
- 文档工具：Confluence、Notion、Markdown
- 知识管理：Obsidian、Notion、语雀

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/domain-expert`（岗位核心 skill）
- `./skills/ddd4j-project-builder`（DDD 项目结构、领域模型）
- `./skills/mermaid`（领域模型图、ER图）
- `./skills/zh-product-doc-generator`（领域模型说明模板）

🆕 **需要新增的细粒度工具 skills**：

**建模工具类**：
- `./skills/tool-enterprise-architect-domain`（Enterprise Architect 领域建模）
- `./skills/tool-staruml-domain`（StarUML 领域模型）
- `./skills/tool-plantuml-domain`（PlantUML 领域模型图）

**文档工具类**：
- `./skills/tool-confluence-domain`（Confluence 领域文档）
- `./skills/tool-notion-domain`（Notion 领域知识库）
- `./skills/tool-markdown-domain`（Markdown 领域文档）

**知识管理工具类**：
- `./skills/tool-obsidian-domain`（Obsidian 领域知识管理）
- `./skills/tool-yuque-domain`（语雀领域知识库）

**业务技能类**：
- `./skills/domain-modeling-bounded-context`（限界上下文划分）
- `./skills/domain-modeling-aggregate`（聚合设计）
- `./skills/domain-modeling-domain-event`（领域事件设计）
- `./skills/ubiquitous-language-glossary`（领域词汇表）
- `./skills/ubiquitous-language-terminology`（术语定义）
- `./skills/business-rules-definition`（业务规则定义）
- `./skills/business-rules-engine`（规则引擎设计）
- `./skills/domain-documentation-knowledge-base`（领域知识库）
- `./skills/domain-documentation-writing`（领域文档编写）

---

#### 技术架构师（Technical Architect / TA）

**工作场景**：
- 技术架构设计、技术栈选型
- 接口设计、技术规范制定
- 技术架构评审

**常用工具**：
- 架构设计：Draw.io、Lucidchart、C4-PlantUML
- API 设计：Swagger、Postman、Apifox、Insomnia
- 文档工具：Confluence、Notion、Markdown
- 代码管理：Git、GitHub、GitLab

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/technical-architect`（岗位核心 skill）
- `./skills/ddd4j-project-builder`（架构模式、技术栈）
- `./skills/mermaid`（技术架构图、部署拓扑图、时序图）
- `./skills/documentation-builder`（技术架构文档）
- `./skills/zh-product-doc-generator`（系统架构设计模板）

🆕 **需要新增的细粒度工具 skills**：

**架构设计工具类**：
- `./skills/tool-drawio-technical-architecture`（Draw.io 技术架构图）
- `./skills/tool-lucidchart-technical`（Lucidchart 技术架构）
- `./skills/tool-c4-plantuml-technical`（C4-PlantUML 技术架构）

**API 设计工具类**：
- `./skills/tool-swagger-api-design`（Swagger API 设计）
- `./skills/tool-postman-api-test`（Postman API 测试）
- `./skills/tool-apifox-api-design`（Apifox API 设计）
- `./skills/tool-insomnia-api-test`（Insomnia API 测试）

**文档工具类**：
- `./skills/tool-confluence-technical`（Confluence 技术文档）
- `./skills/tool-notion-technical`（Notion 技术文档）
- `./skills/tool-markdown-technical`（Markdown 技术文档）

**代码管理工具类**：
- `./skills/tool-git-technical`（Git 技术代码管理）
- `./skills/tool-github-technical`（GitHub 技术文档管理）

**业务技能类**：
- `./skills/technical-architecture-design`（技术架构设计）
- `./skills/technical-architecture-pattern`（架构模式选择）
- `./skills/api-design-restful`（RESTful API 设计）
- `./skills/api-design-graphql`（GraphQL API 设计）
- `./skills/api-design-grpc`（gRPC API 设计）
- `./skills/tech-specification-coding`（编码规范制定）
- `./skills/tech-specification-standard`（技术标准制定）
- `./skills/performance-design-metrics`（性能指标定义）
- `./skills/performance-design-optimization`（性能优化方案）

---

### 7.7 开发类岗位

#### 前端开发工程师（Frontend Engineer / FE）

**工作场景**：
- 前端开发、组件开发
- 前端工程化、性能优化
- 前端测试、代码审查

**常用工具**：
- 框架：React、Vue、Angular、Svelte
- 构建工具：Webpack、Vite、Rollup、Parcel
- 状态管理：Redux、Vuex、Pinia、Zustand
- 测试工具：Jest、Vitest、Cypress、Playwright
- 代码质量：ESLint、Prettier、TypeScript
- 性能工具：Lighthouse、WebPageTest、Chrome DevTools
- UI 库：Ant Design、Element Plus、Material-UI

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/frontend-engineer`（岗位核心 skill）
- `./skills/code-generator`（前端代码生成）
- `./skills/frontend-design`（前端设计规范）
- `./skills/documentation-builder`（接口文档、技术文档）
- `./skills/mermaid`（前端架构图、组件关系图）

🆕 **需要新增的细粒度工具 skills**：

**框架类**：
- `./skills/framework-react-setup`（React 项目初始化）
- `./skills/framework-react-component`（React 组件开发）
- `./skills/framework-react-hooks`（React Hooks 使用）
- `./skills/framework-vue-setup`（Vue 项目初始化）
- `./skills/framework-vue-component`（Vue 组件开发）
- `./skills/framework-vue-composition`（Vue Composition API）
- `./skills/framework-angular-setup`（Angular 项目初始化）
- `./skills/framework-angular-component`（Angular 组件开发）

**构建工具类**：
- `./skills/tool-webpack-config`（Webpack 配置）
- `./skills/tool-webpack-optimize`（Webpack 性能优化）
- `./skills/tool-vite-setup`（Vite 项目搭建）
- `./skills/tool-vite-config`（Vite 配置）
- `./skills/tool-rollup-build`（Rollup 打包配置）

**状态管理类**：
- `./skills/tool-redux-setup`（Redux 状态管理）
- `./skills/tool-redux-toolkit`（Redux Toolkit 使用）
- `./skills/tool-vuex-setup`（Vuex 状态管理）
- `./skills/tool-pinia-setup`（Pinia 状态管理）

**测试工具类**：
- `./skills/tool-jest-setup`（Jest 测试框架配置）
- `./skills/tool-jest-unit-test`（Jest 单元测试编写）
- `./skills/tool-vitest-setup`（Vitest 测试框架配置）
- `./skills/tool-cypress-e2e`（Cypress E2E 测试）
- `./skills/tool-playwright-e2e`（Playwright E2E 测试）

**代码质量类**：
- `./skills/tool-eslint-config`（ESLint 配置）
- `./skills/tool-prettier-config`（Prettier 配置）
- `./skills/tool-typescript-setup`（TypeScript 项目配置）
- `./skills/tool-typescript-type`（TypeScript 类型定义）

**性能工具类**：
- `./skills/tool-lighthouse-audit`（Lighthouse 性能审计）
- `./skills/tool-lighthouse-optimize`（基于 Lighthouse 的性能优化）
- `./skills/tool-webpagetest`（WebPageTest 性能分析）
- `./skills/tool-chrome-devtools`（Chrome DevTools 性能分析）

**UI 库类**：
- `./skills/tool-antd-usage`（Ant Design 使用）
- `./skills/tool-element-plus-usage`（Element Plus 使用）
- `./skills/tool-material-ui-usage`（Material-UI 使用）

**业务技能类**：
- `./skills/component-development-design`（组件设计：可复用组件、组件文档）
- `./skills/component-development-module`（组件模块化：CSS 模块、变量、主题）
- `./skills/responsive-design-layout`（响应式布局：媒体查询、Flexbox、Grid）
- `./skills/frontend-routing-spa`（SPA 路由管理：React Router、Vue Router）
- `./skills/frontend-security-xss`（XSS 防护）
- `./skills/frontend-security-csrf`（CSRF 防护）
- `./skills/frontend-cache-strategy`（前端缓存策略）
- `./skills/frontend-asset-optimize`（静态资源优化）

---

#### 后端开发工程师（Backend Engineer / BE）

**工作场景**：
- 后端开发、API 开发
- 数据库设计、性能优化
- 后端测试、代码审查

**常用工具**：
- 框架：Spring Boot、Spring Cloud、Spring Cloud Alibaba、Spring AI、Spring AI Alibab、Express、Django、FastAPI、NestJS
- 数据库：MySQL、PostgreSQL、MongoDB、Redis
- API 工具：Swagger、Postman、Insomnia、Apifox
- 测试工具：JUnit、pytest、Jest、Mocha
- 消息队列：RabbitMQ、Kafka、RocketMQ
- 缓存：Redis、Memcached
- 监控：Prometheus、Grafana、ELK

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/backend-engineer`（岗位核心 skill）
- `./skills/code-generator`（后端代码生成）
- `./skills/ddd4j-project-builder`（DDD 项目结构）
- `./skills/documentation-builder`（接口文档、技术文档）
- `./skills/mermaid`（数据库ER图、接口时序图）

🆕 **需要新增的细粒度工具 skills**：

**框架类**：
- `./skills/framework-springboot-setup`（Spring Boot 项目初始化）
- `./skills/framework-springboot-config`（Spring Boot 配置）
- `./skills/framework-express-setup`（Express 项目搭建）
- `./skills/framework-django-setup`（Django 项目搭建）
- `./skills/framework-fastapi-setup`（FastAPI 项目搭建）
- `./skills/framework-nestjs-setup`（NestJS 项目搭建）

**数据库类**：
- `./skills/database-mysql-install`（MySQL 数据库安装）
- `./skills/database-mysql-config`（MySQL 配置优化）
- `./skills/database-mysql-query`（MySQL 查询优化）
- `./skills/database-postgresql-install`（PostgreSQL 安装）
- `./skills/database-postgresql-config`（PostgreSQL 配置）
- `./skills/database-mongodb-install`（MongoDB 安装）
- `./skills/database-mongodb-query`（MongoDB 查询）
- `./skills/database-redis-install`（Redis 安装）
- `./skills/database-redis-config`（Redis 配置）
- `./skills/database-redis-usage`（Redis 使用：缓存、队列）

**API 工具类**：
- `./skills/tool-swagger-setup`（Swagger 接口文档生成）
- `./skills/tool-swagger-ui`（Swagger UI 使用）
- `./skills/tool-postman-collection`（Postman 接口测试集合）
- `./skills/tool-postman-automation`（Postman 自动化测试）
- `./skills/tool-insomnia-api`（Insomnia API 测试）
- `./skills/tool-apifox-api`（Apifox API 文档与测试）

**API 开发类**：
- `./skills/api-restful-design`（RESTful API 设计）
- `./skills/api-graphql-setup`（GraphQL API 搭建）
- `./skills/api-grpc-setup`（gRPC API 搭建）
- `./skills/api-versioning`（API 版本管理）

**测试工具类**：
- `./skills/tool-junit-setup`（JUnit 单元测试）
- `./skills/tool-pytest-setup`（pytest 测试框架）
- `./skills/tool-jest-backend`（Jest 后端测试）
- `./skills/tool-mocha-setup`（Mocha 测试框架）

**消息队列类**：
- `./skills/tool-rabbitmq-install`（RabbitMQ 安装配置）
- `./skills/tool-rabbitmq-usage`（RabbitMQ 使用）
- `./skills/tool-kafka-install`（Kafka 安装配置）
- `./skills/tool-kafka-usage`（Kafka 使用）
- `./skills/tool-rocketmq-install`（RocketMQ 安装配置）

**缓存类**：
- `./skills/cache-redis-strategy`（Redis 缓存策略）
- `./skills/cache-memcached-setup`（Memcached 配置）

**监控类**：
- `./skills/tool-prometheus-setup`（Prometheus 监控配置）
- `./skills/tool-grafana-dashboard`（Grafana 仪表板配置）
- `./skills/tool-elk-setup`（ELK 日志系统搭建）

**业务技能类**：
- `./skills/database-design-er`（数据库 ER 图设计）
- `./skills/database-design-table`（数据库表设计）
- `./skills/database-index-optimize`（数据库索引优化）
- `./skills/backend-performance-optimize`（后端性能优化）
- `./skills/backend-cache-strategy`（后端缓存策略）
- `./skills/microservices-split`（微服务拆分）
- `./skills/microservices-governance`（微服务治理）

---

#### 移动开发工程师（Mobile Engineer / ME）

**工作场景**：
- 移动端开发、原生/跨平台开发
- 移动端性能优化、适配
- 移动端测试、发布

**常用工具**：
- 原生开发：Android Studio、Xcode、Swift、Kotlin、Java
- 跨平台：React Native、Flutter、UniApp、Ionic
- 调试工具：ADB、Xcode Simulator、Chrome DevTools、Flipper
- 性能工具：Android Profiler、Instruments、Firebase Performance
- 测试工具：Espresso、XCTest、Appium、Detox
- 发布工具：Google Play Console、App Store Connect、Fastlane

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/mobile-engineer`（岗位核心 skill）
- `./skills/code-generator`（移动端代码生成）
- `./skills/frontend-design`（移动端设计规范）
- `./skills/documentation-builder`（移动端技术文档）
- `./skills/mermaid`（移动端架构图）

🆕 **需要新增的细粒度工具 skills**：

**原生开发工具类**：
- `./skills/tool-android-studio-setup`（Android Studio 项目搭建）
- `./skills/tool-xcode-setup`（Xcode 项目搭建）
- `./skills/tool-swift-development`（Swift 开发）
- `./skills/tool-kotlin-development`（Kotlin 开发）
- `./skills/tool-java-android`（Java Android 开发）

**跨平台框架类**：
- `./skills/framework-react-native-setup`（React Native 项目初始化）
- `./skills/framework-react-native-component`（React Native 组件开发）
- `./skills/framework-flutter-setup`（Flutter 项目初始化）
- `./skills/framework-flutter-widget`（Flutter Widget 开发）
- `./skills/framework-uniapp-setup`（UniApp 项目搭建）
- `./skills/framework-ionic-setup`（Ionic 项目搭建）

**调试工具类**：
- `./skills/tool-adb-debug`（ADB 调试工具）
- `./skills/tool-xcode-simulator`（Xcode Simulator 使用）
- `./skills/tool-chrome-devtools-mobile`（Chrome DevTools 移动端调试）
- `./skills/tool-flipper-debug`（Flipper 移动端调试）

**性能工具类**：
- `./skills/tool-android-profiler`（Android Profiler 性能分析）
- `./skills/tool-instruments-performance`（Instruments 性能分析）
- `./skills/tool-firebase-performance`（Firebase Performance 监控）

**测试工具类**：
- `./skills/tool-espresso-ui-test`（Espresso UI 测试）
- `./skills/tool-xctest-ui-test`（XCTest UI 测试）
- `./skills/tool-appium-mobile-test`（Appium 移动端测试）
- `./skills/tool-detox-e2e`（Detox E2E 测试）

**发布工具类**：
- `./skills/tool-google-play-console`（Google Play Console 发布）
- `./skills/tool-app-store-connect`（App Store Connect 发布）
- `./skills/tool-fastlane-automation`（Fastlane 自动化发布）

**业务技能类**：
- `./skills/mobile-performance-optimize`（移动端性能优化）
- `./skills/mobile-memory-optimize`（内存优化）
- `./skills/mobile-screen-adaptation`（屏幕适配）
- `./skills/mobile-system-adaptation`（系统适配）
- `./skills/mobile-unit-test`（移动端单元测试）
- `./skills/mobile-ui-test`（移动端 UI 测试）
- `./skills/mobile-device-test`（真机测试）
- `./skills/app-store-publishing-process`（应用商店发布流程）
- `./skills/app-store-version-management`（版本管理）

---

#### 数据库工程师（DataBase Administrator / DBA）

**工作场景**：
- 数据库设计、数据库优化
- 数据库备份、数据库安全
- 数据库监控、故障处理

**常用工具**：
- 数据库：MySQL、PostgreSQL、Oracle、SQL Server、MongoDB
- 管理工具：Navicat、DBeaver、MySQL Workbench、pgAdmin
- 监控工具：Prometheus、Grafana、Zabbix、MySQL Enterprise Monitor
- 备份工具：mysqldump、pg_dump、MongoDB Backup、Percona XtraBackup

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/dba`（岗位核心 skill）
- `./skills/mermaid`（数据库ER图、数据流图）
- `./skills/documentation-builder`（数据库设计文档）
- `./skills/zh-product-doc-generator`（技术细分模板）

🆕 **需要新增的细粒度工具 skills**：

**数据库管理工具类**：
- `./skills/tool-navicat-mysql`（Navicat MySQL 管理）
- `./skills/tool-navicat-postgresql`（Navicat PostgreSQL 管理）
- `./skills/tool-dbeaver-database`（DBeaver 数据库管理）
- `./skills/tool-mysql-workbench`（MySQL Workbench 使用）
- `./skills/tool-pgadmin-setup`（pgAdmin PostgreSQL 管理）

**监控工具类**：
- `./skills/tool-prometheus-db-monitor`（Prometheus 数据库监控）
- `./skills/tool-grafana-db-dashboard`（Grafana 数据库仪表板）
- `./skills/tool-zabbix-db-monitor`（Zabbix 数据库监控）
- `./skills/tool-mysql-enterprise-monitor`（MySQL Enterprise Monitor）

**备份工具类**：
- `./skills/tool-mysqldump-backup`（mysqldump 备份）
- `./skills/tool-pgdump-backup`（pg_dump 备份）
- `./skills/tool-mongodb-backup`（MongoDB 备份）
- `./skills/tool-xtrabackup-backup`（Percona XtraBackup 备份）

**业务技能类**：
- `./skills/database-design-er`（数据库 ER 图设计）
- `./skills/database-design-table`（数据库表设计）
- `./skills/database-design-index`（索引设计）
- `./skills/database-optimization-sql`（SQL 优化）
- `./skills/database-optimization-index`（索引优化）
- `./skills/database-optimization-query`（查询优化）
- `./skills/database-backup-strategy`（备份策略制定）
- `./skills/database-backup-recovery`（恢复方案设计）
- `./skills/database-security-permission`（权限管理）
- `./skills/database-security-encryption`（数据加密）
- `./skills/database-monitoring-performance`（性能监控）
- `./skills/database-monitoring-alert`（告警配置）

---

### 7.8 测试类岗位

#### 测试工程师（Test Engineer / TE）

**工作场景**：
- 测试用例编写、自动化测试开发
- 测试框架搭建、测试工具开发
- 测试执行、测试报告

**常用工具**：
- UI 自动化：Selenium、Cypress、Playwright、Puppeteer
- API 测试：Postman、RestAssured、JMeter、SoapUI
- 性能测试：JMeter、Locust、Gatling、K6
- 测试框架：Jest、PyTest、JUnit、TestNG
- 测试管理：TestRail、Zentao、Jira
- 缺陷跟踪：Jira、Bugzilla、Mantis

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/test-engineer`（岗位核心 skill）
- `./skills/test-writer`（测试用例编写）
- `./skills/webapp-testing`（Web 应用测试）
- `./skills/code-generator`（自动化测试脚本生成）
- `./skills/documentation-builder`（测试文档）
- `./skills/zh-product-doc-generator`（测试结果模板）

🆕 **需要新增的细粒度工具 skills**：

**UI 自动化工具类**：
- `./skills/tool-selenium-setup`（Selenium 环境搭建）
- `./skills/tool-selenium-webdriver`（Selenium WebDriver 使用）
- `./skills/tool-selenium-pageobject`（Selenium PageObject 模式）
- `./skills/tool-cypress-setup`（Cypress 环境搭建）
- `./skills/tool-cypress-e2e`（Cypress E2E 测试编写）
- `./skills/tool-playwright-setup`（Playwright 环境搭建）
- `./skills/tool-playwright-e2e`（Playwright E2E 测试编写）
- `./skills/tool-puppeteer-setup`（Puppeteer 环境搭建）

**API 测试工具类**：
- `./skills/tool-postman-collection`（Postman 测试集合）
- `./skills/tool-postman-automation`（Postman 自动化测试）
- `./skills/tool-restassured-setup`（RestAssured API 测试）
- `./skills/tool-jmeter-api`（JMeter API 测试）
- `./skills/tool-soapui-setup`（SoapUI 接口测试）

**性能测试工具类**：
- `./skills/tool-jmeter-install`（JMeter 安装配置）
- `./skills/tool-jmeter-script`（JMeter 性能测试脚本）
- `./skills/tool-jmeter-report`（JMeter 性能测试报告）
- `./skills/tool-locust-setup`（Locust 压力测试）
- `./skills/tool-gatling-setup`（Gatling 性能测试）
- `./skills/tool-k6-setup`（K6 性能测试）

**测试框架类**：
- `./skills/tool-jest-setup`（Jest 测试框架配置）
- `./skills/tool-pytest-setup`（PyTest 测试框架配置）
- `./skills/tool-junit-setup`（JUnit 测试框架配置）
- `./skills/tool-testng-setup`（TestNG 测试框架配置）

**测试管理工具类**：
- `./skills/tool-testrail-setup`（TestRail 测试管理）
- `./skills/tool-testrail-case`（TestRail 测试用例管理）
- `./skills/tool-zentao-test`（禅道测试管理）
- `./skills/tool-jira-test`（Jira 测试管理）

**缺陷跟踪工具类**：
- `./skills/tool-jira-bug`（Jira 缺陷跟踪）
- `./skills/tool-bugzilla-setup`（Bugzilla 缺陷管理）
- `./skills/tool-mantis-setup`（Mantis 缺陷跟踪）

**业务技能类**：
- `./skills/test-case-design`（测试用例设计：边界条件、异常路径）
- `./skills/test-plan-write`（测试计划编写）
- `./skills/test-strategy-write`（测试策略文档）
- `./skills/test-automation-framework`（自动化测试框架搭建）
- `./skills/test-data-generate`（测试数据生成）
- `./skills/test-data-cleanup`（测试数据清理）
- `./skills/test-coverage-analysis`（测试覆盖率分析）

---

#### QA工程师（Quality Assurance Engineer / QA）

**工作场景**：
- QA 测试计划、测试策略制定
- 质量评估、质量度量
- 缺陷分析、质量报告

**常用工具**：
- 测试管理：TestRail、Zentao、Jira、Azure DevOps Test Plans
- 缺陷跟踪：Jira、Bugzilla、Mantis、Redmine
- 质量度量：SonarQube、Codecov、JaCoCo、Coverage.py
- 质量看板：Jira Dashboard、Grafana、自建看板

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/qa-engineer`（岗位核心 skill）
- `./skills/test-writer`（测试用例编写）
- `./skills/webapp-testing`（Web 应用测试）
- `./skills/documentation-builder`（QA 文档）
- `./skills/zh-product-doc-generator`（测试结果模板、功能提测模板）

🆕 **需要新增的细粒度工具 skills**：

**测试管理工具类**：
- `./skills/tool-testrail-plan`（TestRail 测试计划管理）
- `./skills/tool-testrail-strategy`（TestRail 测试策略）
- `./skills/tool-zentao-qa`（禅道 QA 管理）
- `./skills/tool-jira-qa`（Jira QA 管理）
- `./skills/tool-azure-devops-test-plans`（Azure DevOps Test Plans）

**缺陷跟踪工具类**：
- `./skills/tool-jira-defect-analysis`（Jira 缺陷分析）
- `./skills/tool-bugzilla-defect`（Bugzilla 缺陷跟踪）
- `./skills/tool-mantis-defect`（Mantis 缺陷分析）
- `./skills/tool-redmine-defect`（Redmine 缺陷跟踪）

**质量度量工具类**：
- `./skills/tool-sonarqube-quality`（SonarQube 代码质量分析）
- `./skills/tool-codecov-coverage`（Codecov 覆盖率分析）
- `./skills/tool-jacoco-coverage`（JaCoCo 覆盖率分析）
- `./skills/tool-coverage-py`（Coverage.py Python 覆盖率）

**质量看板工具类**：
- `./skills/tool-jira-dashboard`（Jira Dashboard 质量看板）
- `./skills/tool-grafana-quality`（Grafana 质量看板）
- `./skills/tool-custom-quality-dashboard`（自建质量看板）

**业务技能类**：
- `./skills/qa-planning-test-plan`（测试计划编写）
- `./skills/qa-planning-test-strategy`（测试策略制定）
- `./skills/quality-metrics-definition`（质量度量指标定义）
- `./skills/quality-metrics-dashboard`（质量看板设计）
- `./skills/defect-analysis-statistics`（缺陷统计）
- `./skills/defect-analysis-root-cause`（根因分析）
- `./skills/quality-assessment-report`（质量评估报告）
- `./skills/quality-improvement-suggestion`（质量改进建议）
- `./skills/test-coverage-analysis`（测试覆盖率分析）
- `./skills/test-coverage-report`（测试覆盖率报告）

---

#### 测试员（Testor / TT）

**工作场景**：
- 手工测试执行、测试用例执行
- 缺陷记录、测试报告

**常用工具**：
- 测试管理：TestRail、Zentao、Jira、Excel
- 缺陷跟踪：Jira、Bugzilla、Mantis、禅道
- 截图工具：Snipaste、QQ截图、Windows截图工具
- 录屏工具：OBS、Bandicam、ScreenFlow

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/testor`（岗位核心 skill）
- `./skills/test-writer`（测试用例编写）
- `./skills/webapp-testing`（Web 应用测试）
- `./skills/zh-product-doc-generator`（测试结果模板）

🆕 **需要新增的细粒度工具 skills**：

**测试管理工具类**：
- `./skills/tool-testrail-execution`（TestRail 测试执行）
- `./skills/tool-zentao-execution`（禅道测试执行）
- `./skills/tool-jira-execution`（Jira 测试执行）
- `./skills/tool-excel-test-case`（Excel 测试用例管理）

**缺陷跟踪工具类**：
- `./skills/tool-jira-bug-record`（Jira 缺陷记录）
- `./skills/tool-bugzilla-record`（Bugzilla 缺陷记录）
- `./skills/tool-mantis-record`（Mantis 缺陷记录）
- `./skills/tool-zentao-bug`（禅道缺陷记录）

**辅助工具类**：
- `./skills/tool-snipaste-screenshot`（Snipaste 截图工具）
- `./skills/tool-obs-recording`（OBS 录屏工具）
- `./skills/tool-bandicam-recording`（Bandicam 录屏工具）

**业务技能类**：
- `./skills/manual-testing-execution`（手工测试执行）
- `./skills/manual-testing-record`（测试记录）
- `./skills/defect-tracking-record`（缺陷记录）
- `./skills/defect-tracking-follow`（缺陷跟踪）
- `./skills/test-report-template`（测试报告模板）
- `./skills/test-report-generate`（测试报告生成）

---

### 7.9 发布/运维类岗位

#### DevOps工程师（DevOps Engineer / DevOps）

**工作场景**：
- CI/CD 流水线、自动化部署
- 容器化、基础设施管理
- 监控告警、故障处理

**常用工具**：
- CI/CD：Jenkins、GitLab CI、GitHub Actions、CircleCI、Travis CI
- 容器化：Docker、Kubernetes、Docker Compose
- IaC：Terraform、CloudFormation、Ansible、Pulumi
- 监控：Prometheus、Grafana、Datadog、New Relic
- 日志：ELK、Loki、Fluentd
- 云平台：AWS、Azure、阿里云、腾讯云

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/devops-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（CI/CD 文档）
- `./skills/mermaid`（CI/CD 流程图、部署架构图）
- `./skills/zh-product-doc-generator`（上线通知模板）

🆕 **需要新增的细粒度工具 skills**：

**CI/CD 工具类**：
- `./skills/tool-jenkins-install`（Jenkins 安装配置）
- `./skills/tool-jenkins-pipeline`（Jenkins Pipeline 编写）
- `./skills/tool-jenkins-job`（Jenkins Job 配置）
- `./skills/tool-gitlab-ci-setup`（GitLab CI 配置）
- `./skills/tool-gitlab-ci-pipeline`（GitLab CI Pipeline 编写）
- `./skills/tool-github-actions-setup`（GitHub Actions 配置）
- `./skills/tool-github-actions-workflow`（GitHub Actions Workflow）
- `./skills/tool-circleci-setup`（CircleCI 配置）
- `./skills/tool-travis-ci-setup`（Travis CI 配置）

**容器化工具类**：
- `./skills/tool-docker-install`（Docker 安装）
- `./skills/tool-docker-image`（Docker 镜像构建）
- `./skills/tool-docker-compose`（Docker Compose 使用）
- `./skills/tool-kubernetes-install`（Kubernetes 集群安装）
- `./skills/tool-kubernetes-deploy`（Kubernetes 部署）
- `./skills/tool-kubernetes-service`（Kubernetes Service 配置）
- `./skills/tool-kubernetes-ingress`（Kubernetes Ingress 配置）

**IaC 工具类**：
- `./skills/tool-terraform-install`（Terraform 安装）
- `./skills/tool-terraform-write`（Terraform 脚本编写）
- `./skills/tool-terraform-apply`（Terraform 应用）
- `./skills/tool-cloudformation-write`（CloudFormation 模板编写）
- `./skills/tool-ansible-setup`（Ansible 配置）
- `./skills/tool-ansible-playbook`（Ansible Playbook 编写）
- `./skills/tool-pulumi-setup`（Pulumi 配置）

**监控工具类**：
- `./skills/tool-prometheus-install`（Prometheus 安装配置）
- `./skills/tool-prometheus-metrics`（Prometheus 指标收集）
- `./skills/tool-grafana-install`（Grafana 安装配置）
- `./skills/tool-grafana-dashboard`（Grafana 仪表板配置）
- `./skills/tool-datadog-setup`（Datadog 监控配置）
- `./skills/tool-newrelic-setup`（New Relic 监控配置）

**日志工具类**：
- `./skills/tool-elk-install`（ELK 日志系统安装）
- `./skills/tool-elk-config`（ELK 日志配置）
- `./skills/tool-loki-setup`（Loki 日志聚合）
- `./skills/tool-fluentd-setup`（Fluentd 日志收集）

**云平台类**：
- `./skills/cloud-aws-ec2`（AWS EC2 使用）
- `./skills/cloud-aws-s3`（AWS S3 使用）
- `./skills/cloud-aws-rds`（AWS RDS 使用）
- `./skills/cloud-azure-vm`（Azure VM 使用）
- `./skills/cloud-aliyun-ecs`（阿里云 ECS 使用）
- `./skills/cloud-aliyun-oss`（阿里云 OSS 使用）
- `./skills/cloud-tencent-cvm`（腾讯云 CVM 使用）
- `./skills/cloud-tencent-cos`（腾讯云 COS 使用）
- `./skills/cloud-tencent-cdb`（腾讯云 CDB 使用）
- `./skills/cloud-huawei-ecs`（华为云 ECS 使用）
- `./skills/cloud-huawei-obs`（华为云 OBS 使用）
- `./skills/cloud-huawei-rds`（华为云 RDS 使用）

**业务技能类**：
- `./skills/cicd-pipeline-design`（CI/CD 流水线设计）
- `./skills/deployment-blue-green`（蓝绿部署）
- `./skills/deployment-canary`（金丝雀部署）
- `./skills/monitoring-alert-rule`（监控告警规则配置）

---
 

#### 运维工程师（Operations Engineer / OE）

**工作场景**：
- 发布计划、发布流程
- 灰度发布、回滚方案
- 发布通知、发布报告

**工作场景**：
- 系统监控、日志分析
- 故障处理、应急响应
- 容量规划、性能调优

**常用工具**：
- 发布工具：Jenkins、GitLab CI、ArgoCD、Spinnaker
- 灰度发布：Istio、Flagger、Argo Rollouts
- 版本管理：Git、Semantic Release、Release Notes Generator
- 通知工具：Slack、钉钉、企业微信、邮件
-
**常用工具**：
- 监控工具：Prometheus、Grafana、Zabbix、Nagios、Datadog
- 日志工具：ELK Stack、Loki、Fluentd、Graylog
- 运维工具：Ansible、Puppet、Chef、SaltStack
- 性能工具：Perf、Strace、Vmstat、Top、Htop
- 云平台：AWS、Azure、阿里云、腾讯云

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/operations-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（运维文档）
- `./skills/mermaid`（监控架构图、运维流程图、故障处理流程图）
- `./skills/zh-product-doc-generator`（项目运维模板）

🆕 **需要新增的细粒度工具 skills**：

**监控工具类**：
- `./skills/tool-prometheus-install`（Prometheus 安装配置）
- `./skills/tool-prometheus-alert`（Prometheus 告警规则）
- `./skills/tool-grafana-dashboard`（Grafana 监控仪表板）
- `./skills/tool-zabbix-setup`（Zabbix 监控配置）
- `./skills/tool-nagios-setup`（Nagios 监控配置）
- `./skills/tool-datadog-monitoring`（Datadog 监控配置）

**日志工具类**：
- `./skills/tool-elk-install`（ELK Stack 安装）
- `./skills/tool-elk-logstash`（Logstash 日志处理）
- `./skills/tool-elk-kibana`（Kibana 日志查询）
- `./skills/tool-loki-setup`（Loki 日志聚合）
- `./skills/tool-fluentd-config`（Fluentd 日志收集）
- `./skills/tool-graylog-setup`（Graylog 日志管理）

**运维自动化工具类**：
- `./skills/tool-ansible-setup`（Ansible 配置管理）
- `./skills/tool-ansible-playbook-ops`（Ansible Playbook 运维）
- `./skills/tool-puppet-setup`（Puppet 配置管理）
- `./skills/tool-chef-setup`（Chef 配置管理）
- `./skills/tool-saltstack-setup`（SaltStack 配置管理）

**性能分析工具类**：
- `./skills/tool-perf-analysis`（Perf 性能分析）
- `./skills/tool-strace-debug`（Strace 系统调用跟踪）
- `./skills/tool-vmstat-monitor`（Vmstat 系统监控）
- `./skills/tool-top-htop`（Top/Htop 进程监控）

**业务技能类**：
- `./skills/system-monitoring-config`（监控配置）
- `./skills/system-monitoring-alert`（监控告警规则）
- `./skills/log-analysis-collect`（日志收集）
- `./skills/log-analysis-query`（日志查询分析）
- `./skills/incident-management-response`（故障应急响应）
- `./skills/incident-management-recovery`（故障恢复）
- `./skills/capacity-planning-evaluation`（容量评估）
- `./skills/capacity-planning-scaling`（扩容方案设计）
- `./skills/performance-tuning-analysis`（性能分析）
- `./skills/performance-tuning-optimization`（性能优化）
 

✅ **已存在的 skills**：
- `./skills/roles/release-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（发布文档）
- `./skills/mermaid`（发布流程图）
- `./skills/zh-product-doc-generator`（上线通知模板）
 

**发布工具类**：
- `./skills/tool-jenkins-release`（Jenkins 发布管理）
- `./skills/tool-gitlab-ci-release`（GitLab CI 发布流程）
- `./skills/tool-argocd-deploy`（ArgoCD 部署管理）
- `./skills/tool-spinnaker-deploy`（Spinnaker 发布流水线）

**灰度发布工具类**：
- `./skills/tool-istio-canary`（Istio 金丝雀发布）
- `./skills/tool-flagger-progressive`（Flagger 渐进式发布）
- `./skills/tool-argo-rollouts`（Argo Rollouts 发布策略）

**版本管理工具类**：
- `./skills/tool-git-tag`（Git 版本标签管理）
- `./skills/tool-semantic-release`（Semantic Release 自动版本）
- `./skills/tool-release-notes-generator`（Release Notes 生成）

**通知工具类**：
- `./skills/tool-slack-notification`（Slack 发布通知）
- `./skills/tool-dingtalk-notification`（钉钉发布通知）
- `./skills/tool-wechat-work-notification`（企业微信通知）

**业务技能类**：
- `./skills/release-planning-checklist`（发布检查清单）
- `./skills/release-planning-schedule`（发布计划制定）
- `./skills/gradual-rollout-strategy`（灰度策略设计）
- `./skills/gradual-rollout-monitoring`（灰度监控）
- `./skills/rollback-plan-design`（回滚方案设计）
- `./skills/rollback-execution`（回滚执行流程）
- `./skills/release-communication-notice`（发布通知编写）
- `./skills/release-communication-report`（发布报告编写）

---

#### SRE工程师（Site Reliability Engineer / SRE）

**工作场景**：
- 可靠性设计、SLO/SLI 定义
- 故障复盘、持续改进
- 自动化运维、混沌工程

**常用工具**：
- 监控工具：Prometheus、Grafana、Datadog、New Relic
- 事件管理：PagerDuty、OpsGenie、VictorOps
- 混沌工程：Chaos Monkey、Chaos Mesh、Gremlin、Litmus
- 自动化工具：Kubernetes、Terraform、Ansible
- APM：Jaeger、Zipkin、SkyWalking、OpenTelemetry

**Skills 规划**：

✅ **已存在的 skills**：
- `./skills/roles/sre-engineer`（岗位核心 skill）
- `./skills/documentation-builder`（SRE 文档）
- `./skills/mermaid`（SRE 架构图、故障处理流程图）
- `./skills/zh-product-doc-generator`（项目运维模板）

🆕 **需要新增的细粒度工具 skills**：

**监控与可观测性工具类**：
- `./skills/tool-prometheus-slo`（Prometheus SLO 监控）
- `./skills/tool-grafana-sli`（Grafana SLI 仪表板）
- `./skills/tool-datadog-sre`（Datadog SRE 监控）
- `./skills/tool-newrelic-apm`（New Relic APM 监控）

**事件管理工具类**：
- `./skills/tool-pagerduty-oncall`（PagerDuty 值班管理）
- `./skills/tool-opsgenie-alert`（OpsGenie 告警管理）
- `./skills/tool-victorops-incident`（VictorOps 事件管理）

**混沌工程工具类**：
- `./skills/tool-chaos-monkey-setup`（Chaos Monkey 配置）
- `./skills/tool-chaos-mesh-experiment`（Chaos Mesh 混沌实验）
- `./skills/tool-gremlin-testing`（Gremlin 故障注入）
- `./skills/tool-litmus-chaos`（Litmus 混沌测试）

**自动化工具类**：
- `./skills/tool-kubernetes-autoscaling`（Kubernetes 自动扩缩容）
- `./skills/tool-terraform-automation`（Terraform 自动化）
- `./skills/tool-ansible-automation-ops`（Ansible 自动化运维）

**APM 工具类**：
- `./skills/tool-jaeger-tracing`（Jaeger 分布式追踪）
- `./skills/tool-zipkin-tracing`（Zipkin 追踪）
- `./skills/tool-skywalking-apm`（SkyWalking APM）
- `./skills/tool-opentelemetry-setup`（OpenTelemetry 配置）

**业务技能类**：
- `./skills/reliability-design-slo`（SLO 定义）
- `./skills/reliability-design-sli`（SLI 定义）
- `./skills/reliability-design-error-budget`（错误预算管理）
- `./skills/postmortem-template`（Postmortem 模板）
- `./skills/postmortem-root-cause`（根因分析）
- `./skills/automation-ops-self-healing`（自愈系统设计）
- `./skills/automation-ops-autoscaling`（自动化扩缩容）
- `./skills/chaos-engineering-experiment`（混沌实验设计）
- `./skills/chaos-engineering-injection`（故障注入）
- `./skills/continuous-improvement-plan`（持续改进计划）
- `./skills/continuous-improvement-tracking`（改进跟踪）

---

## 八、技能颗粒度细化原则与命名规范

### 8.1 技能颗粒度细化原则

技能颗粒度细化到**工具使用级别**，遵循以下原则：

1. **明确输入与输出**：每个技能有明确的输入（如工具、配置）和输出（如安装结果、配置文件）
2. **可测量/验收的标准**：每个技能有可验证的完成标准（如"能部署一个 Node.js 应用到 AWS EC2"）
3. **独立可训练、独立可复用**：每个技能可以独立学习和使用
4. **不混合职责**：不把"团队协作沟通"和"技术实现"混为一项技能

### 8.2 工具技能命名规范

工具技能采用以下命名格式：

```
{tool-category}-{tool-name}-{action}
```

**示例**：
- `database-mysql-install`（MySQL 数据库安装）
- `database-mysql-config`（MySQL 数据库配置）
- `database-mysql-query`（MySQL 查询优化）
- `tool-jenkins-install`（Jenkins 安装配置）
- `tool-jenkins-pipeline`（Jenkins Pipeline 编写）
- `framework-react-setup`（React 项目初始化）
- `framework-react-component`（React 组件开发）

**命名规则说明**：
- `{tool-category}`：工具类别（database、tool、framework、cloud 等）
- `{tool-name}`：工具名称（mysql、jenkins、react 等，kebab-case）
- `{action}`：操作类型（install、config、setup、usage、deploy 等）

### 8.3 工具技能分类

#### 数据库类（database-*）
- `database-{name}-install`：数据库安装
- `database-{name}-config`：数据库配置
- `database-{name}-query`：数据库查询优化
- `database-{name}-backup`：数据库备份
- `database-{name}-monitor`：数据库监控

#### 框架类（framework-*）
- `framework-{name}-setup`：框架项目初始化
- `framework-{name}-config`：框架配置
- `framework-{name}-component`：框架组件开发
- `framework-{name}-{feature}`：框架特定功能

#### 工具类（tool-*）
- `tool-{name}-install`：工具安装
- `tool-{name}-setup`：工具配置
- `tool-{name}-usage`：工具使用
- `tool-{name}-{action}`：工具特定操作

#### 云平台类（cloud-*）
- `cloud-{platform}-{service}`：云平台服务使用（主要侧重于使用，而非配置/安装）
- 例如：`cloud-aws-ec2`（AWS EC2 使用）、`cloud-aliyun-ecs`（阿里云 ECS 使用）、`cloud-tencent-cvm`（腾讯云 CVM 使用）
- 架构设计类技能单独命名：`cloud-{platform}-architecture`、`cloud-{platform}-migration` 等

### 8.4 AI 设计工具说明

随着 AI 技术的快速发展，设计领域涌现出大量 AI 辅助设计工具，这些工具可以显著提升设计效率：

**AI 图像生成工具**：
- **Midjourney**：基于 Discord 的 AI 图像生成工具，适合概念设计、视觉探索
- **DALL-E**：OpenAI 的 AI 图像生成工具，支持文本到图像生成
- **Stable Diffusion**：开源的 AI 图像生成模型，支持本地部署和定制
- **Leonardo AI**：专业的 AI 图像生成平台，适合产品设计

**AI 设计辅助工具**：
- **Figma AI**：Figma 内置的 AI 设计助手，支持智能布局、组件生成
- **Adobe Firefly**：Adobe 的 AI 创意工具，集成在 Photoshop、Illustrator 中
- **Canva AI**：Canva 的 AI 设计助手，支持模板生成、内容创作

**AI 原型生成工具**：
- **Uizard**：AI 驱动的原型设计工具，可以从草图生成 UI 设计
- **Galileo AI**：AI UI 设计生成工具，支持从文本描述生成界面

**AI 视频生成工具**：
- **Runway ML**：AI 视频生成和编辑工具，支持视频特效、风格转换

**使用建议**：
- AI 工具作为设计辅助，不能完全替代设计师的创意和判断
- 需要掌握 AI 工具的使用技巧和 Prompt 工程，才能发挥最大价值
- 注意 AI 生成内容的版权和使用规范

### 8.5 云平台技能说明

云平台技能需要覆盖主流云服务提供商，包括：

**国际云平台**：
- **AWS（Amazon Web Services）**：全球市场份额最大的云平台
- **Azure（Microsoft Azure）**：微软云平台，企业级应用广泛

**国内云平台**：
- **阿里云（Alibaba Cloud）**：国内市场份额最大的云平台
- **腾讯云（Tencent Cloud）**：腾讯云平台，游戏、社交、视频等领域优势明显
- **华为云（Huawei Cloud）**：华为云平台，政企市场优势

**腾讯云核心服务**：
- **CVM（Cloud Virtual Machine）**：云服务器，类似 AWS EC2
- **COS（Cloud Object Storage）**：对象存储，类似 AWS S3
- **CDB（Cloud Database）**：云数据库，支持 MySQL、PostgreSQL、MongoDB
- **VPC（Virtual Private Cloud）**：私有网络，网络隔离和配置
- **CLB（Cloud Load Balancer）**：负载均衡，流量分发
- **CKafka**：消息队列服务，高吞吐量消息处理
- **Redis**：缓存服务，高性能数据缓存
- **云监控**：监控告警服务，系统性能监控

**华为云核心服务**：
- **ECS（Elastic Cloud Server）**：弹性云服务器，类似 AWS EC2
- **OBS（Object Storage Service）**：对象存储服务，类似 AWS S3
- **RDS（Relational Database Service）**：关系型数据库，支持 MySQL、PostgreSQL、SQL Server
- **VPC（Virtual Private Cloud）**：虚拟私有云，网络隔离和配置
- **ELB（Elastic Load Balance）**：弹性负载均衡，流量分发
- **DMS（Distributed Message Service）**：分布式消息服务，支持 Kafka、RabbitMQ
- **DCS（Distributed Cache Service）**：分布式缓存服务，Redis 缓存
- **云监控**：监控告警服务，系统性能监控

**华为云核心服务**：
- **ECS（Elastic Cloud Server）**：弹性云服务器，类似 AWS EC2
- **OBS（Object Storage Service）**：对象存储服务，类似 AWS S3
- **RDS（Relational Database Service）**：关系型数据库，支持 MySQL、PostgreSQL、SQL Server
- **VPC（Virtual Private Cloud）**：虚拟私有云，网络隔离和配置
- **ELB（Elastic Load Balance）**：弹性负载均衡，流量分发
- **DMS（Distributed Message Service）**：分布式消息服务，支持 Kafka、RabbitMQ
- **DCS（Distributed Cache Service）**：分布式缓存服务，Redis 缓存
- **云监控**：监控告警服务，系统性能监控

**技能规划原则**：
- **云平台技能主要侧重于"使用"**：包括服务的使用方法、最佳实践、常见场景等
- 技能命名遵循 `cloud-{platform}-{service}` 格式（不使用 `-setup`、`-install` 等后缀）
- 每个云平台的核心服务都需要对应的使用技能
- 支持多云和混合云场景的技能设计
- 架构设计、迁移方案等高级技能单独列出（如 `cloud-tencent-architecture`）

### 8.6 技能来源参考

技能可以从以下来源获取：
- **skillsmp.com**：技能市场，查找符合各岗位的工具使用技能
- **官方文档**：各工具的官方文档和使用指南
- **最佳实践**：行业最佳实践和社区经验
- **AI 工具官方文档**：Midjourney、DALL-E、Figma AI 等工具的官方文档
- **云平台官方文档**：AWS、Azure、阿里云、腾讯云、华为云的官方文档

### 8.7 技能实现优先级

建议按以下优先级实现技能：

1. **P0（核心技能）**：每个岗位最常用的 3-5 个工具技能
2. **P1（重要技能）**：每个岗位常用的 5-10 个工具技能
3. **P2（扩展技能）**：每个岗位的可选工具技能
4. **P3（新兴技能）**：AI 设计工具、新兴云平台服务等

---

## 九、待确认问题

1. **岗位 Skill 的详细程度**：每个岗位的 `SKILL.md` 应该包含哪些内容？
   - 职责描述
   - 工作流程
   - 输入/输出标准
   - 常用工具
   - 协作关系
   - 示例 Prompt

2. **技能颗粒度确认**：当前细化的工具技能颗粒度是否合适？
   - 是否需要进一步细化（如 `database-mysql-install-linux`、`database-mysql-install-windows`）？
   - 还是当前颗粒度已经足够？

3. **技能来源**：是否从 skillsmp.com 或其他技能市场获取现有技能？
   - 如何整合外部技能市场？
   - 是否需要建立技能映射关系？

---

## 十、下一步行动

1. **确认规划**：请确认以上规划是否符合预期
2. **调整细节**：根据反馈调整岗位技能包和依赖关系
3. **技能市场调研**：从 skillsmp.com 等技能市场查找符合各岗位的技能
4. **开始实现**：按优先级逐步实现各岗位的 skill 和 plugin
