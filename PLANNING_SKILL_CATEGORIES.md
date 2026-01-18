# 全栈技能库规划文档（Skill Categories-Based）

> **状态**：重新规划阶段  
> **目标**：按技能种类组织技能库，面向期望成为全栈技能人才的群体，提供实用的工具技能集合

---

## 一、项目定位

**full-stack-skills** 是一个面向**期望成为全栈技能人才的群体**的技能库，不是按岗位划分，而是按**技能种类**划分。

### 1.1 组织原则

```
Marketplace (full-stack-skills)
  └── Plugins (按技能种类划分)
      └── Skills (每个类别下包含具体的工具技能)
```

### 1.2 技能种类分类

- **设计类**：UI设计、交互设计、原型设计等工具技能
- **开发类**：前端、后端、移动端等开发框架和工具技能
- **架构类**：系统架构、领域建模、技术选型等技能
- **测试类**：单元测试、集成测试、E2E测试等工具技能
- **文档类**：文档生成、文档处理、图表绘制等技能
- **运维类**：CI/CD、容器化、监控告警等技能
- **数据库类**：数据库设计、优化、管理等技能
- **云平台类**：AWS、Azure、阿里云、腾讯云、华为云等使用技能

---

## 二、技能种类详细规划

### 2.1 开发类（Development Skills）

#### 前端开发技能

**Vue 生态**：
- `vue2-guide` - Vue 2.x 开发指南
- `vue3-guide` - Vue 3.x 开发指南（Composition API、Setup Script）
- `vite-guide` - Vite 构建工具使用指南
- `vue-router-guide` - Vue Router 路由管理
- `pinia-guide` - Pinia 状态管理
- `vuex-guide` - Vuex 状态管理（Vue 2）

**React 生态**：
- `react-guide` - React 开发指南
- `react-hooks-guide` - React Hooks 使用指南
- `nextjs-guide` - Next.js 框架指南
- `redux-guide` - Redux 状态管理

**其他前端框架**：
- `angular-guide` - Angular 开发指南
- `svelte-guide` - Svelte 开发指南

**构建工具**：
- `webpack-guide` - Webpack 配置指南
- `rollup-guide` - Rollup 打包指南
- `parcel-guide` - Parcel 打包指南

**UI 框架**：
- `element-plus-guide` - Element Plus 使用指南
- `ant-design-vue-guide` - Ant Design Vue 使用指南
- `ant-design-react-guide` - Ant Design React 使用指南

#### 后端开发技能

**Spring 生态**：
- `spring-boot-guide` - Spring Boot 开发指南
- `spring-cloud-guide` - Spring Cloud 微服务指南
- `spring-cloud-alibaba-guide` - Spring Cloud Alibaba 指南
- `spring-ai-guide` - Spring AI 开发指南
- `spring-ai-alibaba-guide` - Spring AI Alibaba 指南
- `spring-security-guide` - Spring Security 安全指南
- `spring-data-jpa-guide` - Spring Data JPA 数据访问

**Node.js 生态**：
- `express-guide` - Express 框架指南
- `nestjs-guide` - NestJS 框架指南
- `koa-guide` - Koa 框架指南
- `fastify-guide` - Fastify 框架指南

**Python 生态**：
- `django-guide` - Django 框架指南
- `fastapi-guide` - FastAPI 框架指南
- `flask-guide` - Flask 框架指南

**其他后端框架**：
- `gin-guide` - Gin (Go) 框架指南
- `gin-gonic-guide` - Gin-Gonic 框架指南

#### 移动端开发技能

**UniApp 生态**：
- `uniapp-project-creater` - UniApp 项目创建器
- `uniapp-project-guide` - UniApp 项目开发指南
- `uniappx-project-creater` - UniApp-x 项目创建器
- `uniappx-project-guide` - UniApp-x 项目开发指南

**React Native**：
- `react-native-guide` - React Native 开发指南
- `react-native-project-creater` - React Native 项目创建器

**Flutter**：
- `flutter-guide` - Flutter 开发指南
- `flutter-project-creater` - Flutter 项目创建器

**原生开发**：
- `android-kotlin-guide` - Android Kotlin 开发指南
- `ios-swift-guide` - iOS Swift 开发指南

---

### 2.2 设计类（Design Skills）

**设计工具**：
- `figma-guide` - Figma 设计工具使用指南
- `figma-ai-guide` - Figma AI 功能使用指南
- `sketch-guide` - Sketch 设计工具指南
- `adobe-xd-guide` - Adobe XD 设计工具指南

**AI 设计工具**：
- `midjourney-guide` - Midjourney AI 绘图指南
- `dalle-guide` - DALL-E AI 绘图指南
- `stable-diffusion-guide` - Stable Diffusion 使用指南
- `uizard-guide` - Uizard AI 设计工具指南
- `galileo-ai-guide` - Galileo AI 设计工具指南
- `runway-ml-guide` - Runway ML 视频生成指南

**原型工具**：
- `axure-guide` - Axure 原型设计指南
- `modao-guide` - 墨刀原型设计指南
- `framer-guide` - Framer 交互原型指南

---

### 2.3 架构类（Architecture Skills）

**架构设计**：
- `ddd-guide` - DDD 领域驱动设计指南
- `ddd-cola-guide` - COLA (Clean Object-Oriented and Layered Architecture) 架构指南
- `ddd-microservices-guide` - DDD 微服务架构指南
- `ddd-event-driven-guide` - DDD 事件驱动架构指南
- `ddd-hexagonal-architecture-guide` - DDD 六边形架构指南
- `ddd-clean-architecture-guide` - DDD 整洁架构指南

**架构工具**：
- `c4-model-guide` - C4 模型架构图绘制指南
- `plantuml-guide` - PlantUML 架构图绘制指南
- `drawio-architecture-guide` - Draw.io 架构图绘制指南

---

### 2.4 测试类（Testing Skills）

**测试框架**：
- `jest-guide` - Jest 测试框架指南
- `vitest-guide` - Vitest 测试框架指南
- `pytest-guide` - PyTest 测试框架指南
- `junit-guide` - JUnit 测试框架指南

**E2E 测试**：
- `cypress-guide` - Cypress E2E 测试指南
- `playwright-guide` - Playwright E2E 测试指南
- `selenium-guide` - Selenium 自动化测试指南

**移动端测试**：
- `appium-guide` - Appium 移动端测试指南
- `detox-guide` - Detox React Native 测试指南

---

### 2.5 文档类（Documentation Skills）

**文档生成**：
- `zh-product-doc-generator` - 中文产品文档生成器（已存在）
- `documentation-builder` - 技术文档构建器（已存在）
- `api-doc-generator` - API 文档生成器

**文档处理**：
- `docx` - Word 文档处理（已存在）
- `pptx` - PowerPoint 演示文稿处理（已存在）
- `pdf` - PDF 文档处理（已存在）
- `xlsx` - Excel 表格处理（已存在）

**图表绘制**：
- `mermaid` - Mermaid 图表绘制（已存在）
- `drawio-flowchart-guide` - Draw.io 流程图绘制指南
- `processon-mindmap-guide` - ProcessOn 思维导图指南

---

### 2.6 运维类（DevOps Skills）

**CI/CD**：
- `jenkins-guide` - Jenkins CI/CD 指南
- `gitlab-ci-guide` - GitLab CI 指南
- `github-actions-guide` - GitHub Actions 指南

**容器化**：
- `docker-guide` - Docker 容器化指南
- `kubernetes-guide` - Kubernetes 容器编排指南
- `docker-compose-guide` - Docker Compose 使用指南

**IaC**：
- `terraform-guide` - Terraform 基础设施即代码指南
- `ansible-guide` - Ansible 自动化配置指南
- `cloudformation-guide` - CloudFormation 模板指南

---

### 2.7 数据库类（Database Skills）

**关系型数据库**：
- `mysql-guide` - MySQL 使用指南
- `postgresql-guide` - PostgreSQL 使用指南
- `oracle-guide` - Oracle 数据库指南

**NoSQL 数据库**：
- `mongodb-guide` - MongoDB 使用指南
- `redis-guide` - Redis 缓存使用指南
- `elasticsearch-guide` - Elasticsearch 搜索引擎指南

**数据库工具**：
- `navicat-guide` - Navicat 数据库管理工具指南
- `dbeaver-guide` - DBeaver 数据库管理工具指南

---

### 2.8 云平台类（Cloud Platform Skills）

**AWS**：
- `cloud-aws-ec2` - AWS EC2 云服务器使用
- `cloud-aws-s3` - AWS S3 对象存储使用
- `cloud-aws-rds` - AWS RDS 数据库使用
- `cloud-aws-lambda` - AWS Lambda 函数使用

**Azure**：
- `cloud-azure-vm` - Azure VM 虚拟机使用
- `cloud-azure-storage` - Azure Storage 存储使用
- `cloud-azure-sql` - Azure SQL 数据库使用

**阿里云**：
- `cloud-aliyun-ecs` - 阿里云 ECS 云服务器使用
- `cloud-aliyun-oss` - 阿里云 OSS 对象存储使用
- `cloud-aliyun-rds` - 阿里云 RDS 数据库使用

**腾讯云**：
- `cloud-tencent-cvm` - 腾讯云 CVM 云服务器使用
- `cloud-tencent-cos` - 腾讯云 COS 对象存储使用
- `cloud-tencent-cdb` - 腾讯云 CDB 数据库使用

**华为云**：
- `cloud-huawei-ecs` - 华为云 ECS 云服务器使用
- `cloud-huawei-obs` - 华为云 OBS 对象存储使用
- `cloud-huawei-rds` - 华为云 RDS 数据库使用

---

## 三、Marketplace.json 结构规划

### 3.1 Plugin 组织方式

按技能种类组织 plugin，每个类别一个 plugin：

```json
{
  "name": "full-stack-skills",
  "plugins": [
    {
      "name": "development-skills",
      "description": "开发技能集合：前端、后端、移动端开发框架和工具",
      "skills": [
        "./skills/development/frontend/vue2-guide",
        "./skills/development/frontend/vue3-guide",
        "./skills/development/frontend/vite-guide",
        "./skills/development/backend/spring-boot-guide",
        "./skills/development/backend/spring-cloud-guide",
        "./skills/development/mobile/uniapp-project-creater",
        "./skills/development/mobile/uniapp-project-guide",
        "./skills/development/mobile/uniappx-project-creater",
        "./skills/development/mobile/uniappx-project-guide"
      ]
    },
    {
      "name": "design-skills",
      "description": "设计技能集合：UI设计、交互设计、AI设计工具",
      "skills": [
        "./skills/design/figma-guide",
        "./skills/design/figma-ai-guide",
        "./skills/design/midjourney-guide"
      ]
    },
    {
      "name": "architecture-skills",
      "description": "架构技能集合：系统架构、领域建模、技术选型",
      "skills": [
        "./skills/architecture/ddd-guide",
        "./skills/architecture/microservices-guide"
      ]
    },
    {
      "name": "testing-skills",
      "description": "测试技能集合：单元测试、集成测试、E2E测试",
      "skills": [
        "./skills/testing/jest-guide",
        "./skills/testing/cypress-guide"
      ]
    },
    {
      "name": "documentation-skills",
      "description": "文档技能集合：文档生成、文档处理、图表绘制",
      "skills": [
        "./skills/documentation/zh-product-doc-generator",
        "./skills/documentation/docx",
        "./skills/documentation/mermaid"
      ]
    },
    {
      "name": "devops-skills",
      "description": "运维技能集合：CI/CD、容器化、IaC",
      "skills": [
        "./skills/devops/jenkins-guide",
        "./skills/devops/docker-guide"
      ]
    },
    {
      "name": "database-skills",
      "description": "数据库技能集合：数据库使用、优化、管理",
      "skills": [
        "./skills/database/mysql-guide",
        "./skills/database/redis-guide"
      ]
    },
    {
      "name": "cloud-skills",
      "description": "云平台技能集合：AWS、Azure、阿里云、腾讯云、华为云",
      "skills": [
        "./skills/cloud/aws/cloud-aws-ec2",
        "./skills/cloud/aliyun/cloud-aliyun-ecs"
      ]
    }
  ]
}
```

### 3.2 目录结构规划

```
skills/
├── development/              # 开发类技能
│   ├── frontend/            # 前端开发
│   │   ├── vue2-guide/
│   │   ├── vue3-guide/
│   │   ├── vite-guide/
│   │   └── ...
│   ├── backend/            # 后端开发
│   │   ├── spring-boot-guide/
│   │   ├── spring-cloud-guide/
│   │   └── ...
│   └── mobile/              # 移动端开发
│       ├── uniapp-project-creater/
│       ├── uniapp-project-guide/
│       ├── uniappx-project-creater/
│       ├── uniappx-project-guide/
│       └── ...
├── design/                   # 设计类技能
│   ├── figma-guide/
│   ├── figma-ai-guide/
│   └── ...
├── architecture/             # 架构类技能
│   ├── ddd-guide/
│   └── ...
├── testing/                  # 测试类技能
│   ├── jest-guide/
│   └── ...
├── documentation/            # 文档类技能
│   ├── zh-product-doc-generator/
│   ├── docx/
│   └── ...
├── devops/                   # 运维类技能
│   ├── jenkins-guide/
│   └── ...
├── database/                 # 数据库类技能
│   ├── mysql-guide/
│   └── ...
└── cloud/                    # 云平台类技能
    ├── aws/
    ├── azure/
    ├── aliyun/
    ├── tencent/
    └── huawei/
```

---

## 四、实施优先级

### P0（高优先级 - 立即实施）
1. **开发类技能**（用户明确提到的）：
   - vue2-guide
   - vue3-guide
   - vite-guide
   - uniapp-project-creater
   - uniapp-project-guide
   - uniappx-project-creater
   - uniappx-project-guide
   - spring-boot-guide
   - spring-cloud-guide
   - spring-cloud-alibaba-guide
   - spring-ai-guide
   - spring-ai-alibaba-guide

### P1（中优先级 - 近期实施）
2. **设计类技能**：Figma、AI 设计工具
3. **测试类技能**：Jest、Cypress、Playwright
4. **文档类技能**：完善现有文档技能

### P2（低优先级 - 后续实施）
5. **架构类技能**：DDD、微服务架构
6. **运维类技能**：CI/CD、容器化
7. **数据库类技能**：MySQL、Redis
8. **云平台类技能**：各云平台使用技能

---

## 五、下一步行动

1. **确认规划**：与用户确认新的组织方式是否符合预期
2. **迁移现有技能**：将现有的通用技能迁移到新的目录结构
3. **创建新技能**：开始创建用户提到的具体工具技能（vue3-guide、spring-boot-guide 等）
4. **更新 marketplace.json**：按新的技能类别组织 plugin

---

**规划日期**：2024年  
**状态**：待确认
