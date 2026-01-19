#!/usr/bin/env python3
"""
批量更新 SKILL.md 文件的 description，使其符合 Anthropic Skills 规范
"""

import os
import re
import json
from pathlib import Path

# 技能描述模板映射
SKILL_DESCRIPTIONS = {
    # Vue 生态
    "vue2": "Provides comprehensive guidance for Vue 2.x development including Options API, components, directives, lifecycle hooks, computed properties, watchers, Vuex state management, and Vue Router. Use when the user asks about Vue 2, needs to create Vue 2 components, implement reactive data binding, handle component communication, or work with Vue 2 ecosystem tools.",
    "vue3": "Provides comprehensive guidance for Vue 3.x development including Composition API, Setup Script, reactivity system, single-file components, template syntax, component development, routing, and state management. Use when the user asks about Vue 3, needs to create Vue 3 applications, implement Composition API patterns, work with Pinia or Vuex, or build reactive user interfaces.",
    "vite": "Provides comprehensive guidance for Vite build tool usage including project creation, configuration, dev server, HMR, plugins, static assets, environment variables, build optimization, and deployment. Use when the user asks about Vite, needs to set up a Vite project, configure build options, optimize bundle size, or work with Vite plugins.",
    "vue-router": "Provides comprehensive guidance for Vue Router including route configuration, navigation, dynamic routes, nested routes, route guards, programmatic navigation, and route meta. Use when the user asks about Vue Router, needs to set up routing, implement navigation guards, handle route parameters, or manage route transitions.",
    "pinia": "Provides comprehensive guidance for Pinia state management including stores, state, getters, actions, plugins, and TypeScript support. Use when the user asks about Pinia, needs to manage application state, create stores, implement state persistence, or migrate from Vuex.",
    "vuex": "Provides comprehensive guidance for Vuex state management including state, mutations, actions, getters, modules, and plugins. Use when the user asks about Vuex, needs to manage application state, implement centralized state management, or work with Vuex modules.",
    "vuex-vue2": "Provides comprehensive guidance for Vuex 2.x state management in Vue 2 applications including state, mutations, actions, getters, modules, and plugins. Use when the user asks about Vuex for Vue 2, needs to manage state in Vue 2 applications, or implement Vuex patterns.",
    
    # React 生态
    "react": "Provides comprehensive guidance for React development including components, JSX, props, state, hooks, context, performance optimization, and best practices. Use when the user asks about React, needs to create React components, implement hooks, manage component state, or build React applications.",
    "react-hooks": "Provides comprehensive guidance for React Hooks including useState, useEffect, useContext, useReducer, useMemo, useCallback, custom hooks, and hook patterns. Use when the user asks about React Hooks, needs to use hooks in functional components, create custom hooks, or optimize hook performance.",
    "nextjs": "Provides comprehensive guidance for Next.js framework including App Router, Pages Router, routing, data fetching, server components, API routes, middleware, image optimization, and deployment. Use when the user asks about Next.js, needs to create Next.js applications, implement SSR or SSG, set up API routes, or optimize Next.js performance.",
    "redux": "Provides comprehensive guidance for Redux state management including stores, actions, reducers, middleware, selectors, and Redux Toolkit. Use when the user asks about Redux, needs to manage global state, implement Redux patterns, or work with Redux middleware.",
    
    # 构建工具
    "webpack": "Provides comprehensive guidance for Webpack bundler including configuration, loaders, plugins, code splitting, optimization, and development setup. Use when the user asks about Webpack, needs to configure Webpack, set up build pipelines, optimize bundles, or work with Webpack plugins.",
    "rollup": "Provides comprehensive guidance for Rollup bundler including configuration, plugins, code splitting, tree shaking, and library bundling. Use when the user asks about Rollup, needs to bundle libraries, optimize output, or configure Rollup for production builds.",
    "parcel": "Provides comprehensive guidance for Parcel bundler including zero-configuration setup, asset handling, hot module replacement, and production builds. Use when the user asks about Parcel, needs to set up a build tool quickly, or work with Parcel's automatic configuration.",
    "rspack": "Provides comprehensive guidance for Rspack bundler including configuration, plugins, loaders, optimization, and Webpack compatibility. Use when the user asks about Rspack, needs to configure Rspack, optimize build performance, or migrate from Webpack.",
    
    # UI 框架
    "element-plus": "Provides comprehensive guidance for Element Plus Vue 3 component library including components, themes, internationalization, and best practices. Use when the user asks about Element Plus, needs to use Element Plus components, customize themes, or implement UI layouts.",
    "element-plus-vue3": "Provides comprehensive guidance for Element Plus Vue 3 component library including installation, components, themes, internationalization, and API reference. Use when the user asks about Element Plus for Vue 3, needs to build Vue 3 applications with Element Plus, or customize component styles.",
    "ant-design-vue": "Provides comprehensive guidance for Ant Design Vue component library including components, design principles, themes, and best practices. Use when the user asks about Ant Design Vue, needs to use Ant Design components, implement enterprise UI, or customize design tokens.",
    "ant-design-react": "Provides comprehensive guidance for Ant Design React component library including components, design system, themes, and TypeScript support. Use when the user asks about Ant Design for React, needs to build React applications with Ant Design, or implement design system patterns.",
    "ant-design-mobile": "Provides comprehensive guidance for Ant Design Mobile component library including mobile components, themes, and platform adaptations. Use when the user asks about Ant Design Mobile, needs to build mobile applications, or implement mobile UI components.",
    "ant-design-mini": "Provides comprehensive guidance for Ant Design Mini component library for mini-programs including components, themes, and platform support. Use when the user asks about Ant Design Mini, needs to build mini-program applications, or use mini-program components.",
    "bootstrap-vue3": "Provides comprehensive guidance for Bootstrap Vue 3 component library including Bootstrap components, grid system, utilities, and Vue 3 integration. Use when the user asks about Bootstrap Vue 3, needs to use Bootstrap components in Vue 3, or implement responsive layouts.",
    "vant-vue3": "Provides comprehensive guidance for Vant Vue 3 mobile component library including mobile components, themes, and best practices. Use when the user asks about Vant, needs to build mobile applications with Vue 3, or implement mobile UI components.",
    "uview-vue2": "Provides comprehensive guidance for uView Vue 2 component library including components, tools, and layouts. Use when the user asks about uView for Vue 2, needs to build Vue 2 applications with uView, or use uView components.",
    "uview-pro-vue3": "Provides comprehensive guidance for uView Pro Vue 3 component library including components, tools, layouts, and templates. Use when the user asks about uView Pro, needs to build Vue 3 applications with uView Pro, or implement mobile-first UI components.",
    "layui-vue": "Provides comprehensive guidance for Layui Vue component library including components, layer dialogs, and utilities. Use when the user asks about Layui Vue, needs to use Layui components in Vue, or implement UI components.",
    "avue": "Provides comprehensive guidance for Avue framework including CRUD operations, form components, and data management. Use when the user asks about Avue, needs to build admin interfaces, implement CRUD operations, or work with Avue components.",
    "avue-crud": "Provides comprehensive guidance for Avue CRUD component including table operations, form handling, and data management. Use when the user asks about Avue CRUD, needs to implement table CRUD operations, or build data management interfaces.",
    "avue-form": "Provides comprehensive guidance for Avue Form component including form configuration, validation, and dynamic forms. Use when the user asks about Avue Form, needs to create dynamic forms, implement form validation, or work with form configurations.",
    
    # 后端框架
    "spring-boot": "Provides comprehensive guidance for Spring Boot development including project creation, auto-configuration, dependency injection, web development, data access, security, testing, and deployment. Use when the user asks about Spring Boot, needs to create Spring Boot applications, configure Spring Boot, or implement Spring Boot features.",
    "spring-cloud": "Provides comprehensive guidance for Spring Cloud microservices including service discovery, configuration management, load balancing, circuit breakers, API gateways, and distributed tracing. Use when the user asks about Spring Cloud, needs to build microservices, implement service discovery, or work with Spring Cloud components.",
    "spring-cloud-alibaba": "Provides comprehensive guidance for Spring Cloud Alibaba including Nacos, Sentinel, RocketMQ, and Alibaba Cloud integration. Use when the user asks about Spring Cloud Alibaba, needs to use Alibaba Cloud services, implement service discovery with Nacos, or work with Spring Cloud Alibaba components.",
    "spring-ai": "Provides comprehensive guidance for Spring AI including AI model integration, prompt templates, vector stores, and AI applications. Use when the user asks about Spring AI, needs to integrate AI models, implement RAG applications, or work with AI services in Spring.",
    "spring-ai-alibaba": "Provides comprehensive guidance for Spring AI Alibaba including Alibaba Cloud AI services integration, model APIs, and AI application development. Use when the user asks about Spring AI Alibaba, needs to use Alibaba Cloud AI services, or integrate AI capabilities in Spring applications.",
    "spring-security": "Provides comprehensive guidance for Spring Security including authentication, authorization, OAuth2, JWT, and security best practices. Use when the user asks about Spring Security, needs to implement security in Spring applications, configure authentication, or work with security features.",
    "spring-data-jpa": "Provides comprehensive guidance for Spring Data JPA including repositories, entity management, query methods, and database operations. Use when the user asks about Spring Data JPA, needs to work with JPA repositories, implement data access layers, or configure JPA in Spring.",
    "express": "Provides comprehensive guidance for Express.js framework including routing, middleware, request handling, templating, and API development. Use when the user asks about Express, needs to create Express applications, set up routes, implement middleware, or build REST APIs.",
    "nestjs": "Provides comprehensive guidance for NestJS framework including modules, controllers, providers, dependency injection, decorators, and microservices. Use when the user asks about NestJS, needs to create NestJS applications, implement modules and controllers, or build scalable Node.js applications.",
    "koa": "Provides comprehensive guidance for Koa.js framework including middleware, context, async/await patterns, and application structure. Use when the user asks about Koa, needs to create Koa applications, implement middleware, or build Node.js web applications.",
    "fastify": "Provides comprehensive guidance for Fastify framework including routing, plugins, schemas, hooks, and performance optimization. Use when the user asks about Fastify, needs to create high-performance Node.js applications, implement Fastify plugins, or optimize API performance.",
    "django": "Provides comprehensive guidance for Django framework including models, views, templates, forms, admin, REST framework, and deployment. Use when the user asks about Django, needs to create Django applications, implement models and views, or build Django REST APIs.",
    "fastapi": "Provides comprehensive guidance for FastAPI framework including routing, request validation, dependency injection, async operations, OpenAPI documentation, and database integration. Use when the user asks about FastAPI, needs to create FastAPI applications, implement REST APIs, or build high-performance Python web services.",
    "flask": "Provides comprehensive guidance for Flask framework including routing, templates, forms, database integration, extensions, and deployment. Use when the user asks about Flask, needs to create Flask applications, implement web routes, or build Python web applications.",
    "gin": "Provides comprehensive guidance for Gin Go framework including routing, middleware, request handling, JSON binding, and API development. Use when the user asks about Gin, needs to create Gin applications, implement REST APIs, or build Go web services.",
    "gin-gonic": "Provides comprehensive guidance for Gin-Gonic framework including routing, middleware, validation, and best practices. Use when the user asks about Gin-Gonic, needs to create Go web applications, or implement Gin patterns.",
    
    # 数据库
    "mysql": "Provides comprehensive guidance for MySQL database including SQL syntax, data types, indexes, transactions, stored procedures, and optimization. Use when the user asks about MySQL, needs to write SQL queries, design database schemas, optimize MySQL performance, or work with MySQL features.",
    "postgresql": "Provides comprehensive guidance for PostgreSQL database including SQL syntax, advanced features, JSON support, full-text search, and performance tuning. Use when the user asks about PostgreSQL, needs to work with PostgreSQL features, write complex queries, or optimize PostgreSQL databases.",
    "oracle": "Provides comprehensive guidance for Oracle database including SQL, PL/SQL, database administration, and Oracle-specific features. Use when the user asks about Oracle, needs to write Oracle SQL, work with PL/SQL, or manage Oracle databases.",
    "mongodb": "Provides comprehensive guidance for MongoDB database including document operations, queries, aggregation, indexes, and best practices. Use when the user asks about MongoDB, needs to work with MongoDB collections, write queries, or design MongoDB schemas.",
    "redis": "Provides comprehensive guidance for Redis including data structures, commands, pub/sub, persistence, clustering, and caching patterns. Use when the user asks about Redis, needs to use Redis for caching, implement Redis data structures, or work with Redis features.",
    "elasticsearch": "Provides comprehensive guidance for Elasticsearch including indexing, searching, aggregations, mappings, and cluster management. Use when the user asks about Elasticsearch, needs to implement search functionality, work with Elasticsearch queries, or manage Elasticsearch clusters.",
    
    # 测试
    "jest": "Provides comprehensive guidance for Jest testing framework including test writing, matchers, async testing, mocking, snapshots, configuration, and CLI. Use when the user asks about Jest, needs to write JavaScript/TypeScript tests, mock dependencies, or configure Jest for projects.",
    "vitest": "Provides comprehensive guidance for Vitest testing framework including fast test execution, Vite integration, component testing, mocking, and configuration. Use when the user asks about Vitest, needs to write fast unit tests, test Vue/React components, or configure Vitest with Vite projects.",
    "pytest": "Provides comprehensive guidance for pytest testing framework including test writing, fixtures, parametrization, mocking, and plugins. Use when the user asks about pytest, needs to write Python tests, use pytest fixtures, or configure pytest for Python projects.",
    "junit": "Provides comprehensive guidance for JUnit testing framework including test annotations, assertions, test lifecycle, and best practices. Use when the user asks about JUnit, needs to write Java unit tests, use JUnit annotations, or configure JUnit for Java projects.",
    "cypress": "Provides comprehensive guidance for Cypress end-to-end testing including test writing, commands, assertions, component testing, and best practices. Use when the user asks about Cypress, needs to write E2E tests, test web applications, or implement Cypress test suites.",
    "playwright": "Provides comprehensive guidance for Playwright testing including browser automation, test writing, page objects, and cross-browser testing. Use when the user asks about Playwright, needs to write E2E tests, automate browsers, or test web applications across browsers.",
    "selenium": "Provides comprehensive guidance for Selenium WebDriver including browser automation, element location, waits, and test frameworks. Use when the user asks about Selenium, needs to automate web browsers, write Selenium tests, or work with Selenium WebDriver.",
    "appium": "Provides comprehensive guidance for Appium mobile testing including mobile app automation, element location, gestures, and cross-platform testing. Use when the user asks about Appium, needs to test mobile applications, automate mobile apps, or write Appium test scripts.",
    "detox": "Provides comprehensive guidance for Detox mobile testing framework including React Native testing, E2E testing, and test synchronization. Use when the user asks about Detox, needs to test React Native applications, write E2E tests for mobile apps, or configure Detox.",
    
    # DevOps
    "jenkins": "Provides comprehensive guidance for Jenkins CI/CD including pipeline creation, job configuration, plugins, and automation. Use when the user asks about Jenkins, needs to set up CI/CD pipelines, configure Jenkins jobs, or automate build and deployment processes.",
    "gitlab-ci": "Provides comprehensive guidance for GitLab CI/CD including pipeline configuration, jobs, stages, and GitLab Runner. Use when the user asks about GitLab CI, needs to create CI/CD pipelines, configure GitLab CI jobs, or automate GitLab workflows.",
    "github-actions": "Provides comprehensive guidance for GitHub Actions including workflow creation, actions, secrets, and automation. Use when the user asks about GitHub Actions, needs to create GitHub workflows, automate GitHub processes, or configure CI/CD with GitHub Actions.",
    "docker": "Provides comprehensive guidance for Docker including container creation, images, Dockerfile, docker-compose, and container management. Use when the user asks about Docker, needs to create Docker containers, build Docker images, or manage containerized applications.",
    "kubernetes": "Provides comprehensive guidance for Kubernetes including pods, services, deployments, ingress, and cluster management. Use when the user asks about Kubernetes, needs to deploy applications to Kubernetes, configure Kubernetes resources, or manage Kubernetes clusters.",
    "docker-compose": "Provides comprehensive guidance for Docker Compose including multi-container applications, service definition, networking, and volumes. Use when the user asks about Docker Compose, needs to orchestrate multiple containers, define docker-compose services, or manage multi-container applications.",
    "terraform": "Provides comprehensive guidance for Terraform infrastructure as code including resource definition, state management, modules, and cloud provider integration. Use when the user asks about Terraform, needs to define infrastructure as code, manage cloud resources, or work with Terraform modules.",
    "ansible": "Provides comprehensive guidance for Ansible automation including playbooks, roles, inventory, and module usage. Use when the user asks about Ansible, needs to automate IT tasks, create Ansible playbooks, or manage infrastructure with Ansible.",
    "cloudformation": "Provides comprehensive guidance for AWS CloudFormation including template creation, stack management, resources, and best practices. Use when the user asks about CloudFormation, needs to define AWS infrastructure, create CloudFormation templates, or manage AWS resources as code.",
    
    # 设计工具
    "figma": "Provides comprehensive guidance for Figma design tool including design creation, components, prototyping, collaboration, and design systems. Use when the user asks about Figma, needs to create designs, work with Figma components, or collaborate on design projects.",
    "figma-ai": "Provides comprehensive guidance for Figma AI features including AI-powered design tools, automation, and AI-assisted design workflows. Use when the user asks about Figma AI, needs to use AI features in Figma, or automate design tasks with AI.",
    "sketch": "Provides comprehensive guidance for Sketch design tool including artboards, symbols, styles, and prototyping. Use when the user asks about Sketch, needs to create designs in Sketch, work with Sketch symbols, or export designs from Sketch.",
    "adobe-xd": "Provides comprehensive guidance for Adobe XD including design creation, prototyping, components, and collaboration. Use when the user asks about Adobe XD, needs to create UI/UX designs, build prototypes, or work with Adobe XD components.",
    "axure": "Provides comprehensive guidance for Axure prototyping tool including wireframing, interactions, dynamic panels, and prototyping. Use when the user asks about Axure, needs to create interactive prototypes, design wireframes, or build complex interactions.",
    "modao": "Provides comprehensive guidance for Modao prototyping tool including rapid prototyping, component libraries, and collaboration. Use when the user asks about Modao, needs to create quick prototypes, or work with Modao components.",
    "framer": "Provides comprehensive guidance for Framer design tool including interactive design, code components, and prototyping. Use when the user asks about Framer, needs to create interactive designs, build prototypes, or work with Framer code components.",
    
    # AI 设计工具
    "midjourney": "Provides comprehensive guidance for Midjourney AI image generation including prompt engineering, image generation, parameters, and best practices. Use when the user asks about Midjourney, needs to generate AI images, create prompts, or work with Midjourney features.",
    "dalle": "Provides comprehensive guidance for DALL-E AI image generation including prompt creation, image generation, variations, and editing. Use when the user asks about DALL-E, needs to generate AI images, create image variations, or work with DALL-E API.",
    "stable-diffusion": "Provides comprehensive guidance for Stable Diffusion AI image generation including model usage, prompt engineering, parameters, and image generation. Use when the user asks about Stable Diffusion, needs to generate AI images, configure models, or work with Stable Diffusion.",
    "uizard": "Provides comprehensive guidance for Uizard AI design tool including AI-powered design generation, wireframing, and design automation. Use when the user asks about Uizard, needs to generate designs with AI, create wireframes, or automate design tasks.",
    "galileo-ai": "Provides comprehensive guidance for Galileo AI design tool including AI-assisted design, component generation, and design automation. Use when the user asks about Galileo AI, needs to use AI for design, generate design components, or automate design workflows.",
    "runway-ml": "Provides comprehensive guidance for Runway ML including AI video generation, image editing, and creative AI tools. Use when the user asks about Runway ML, needs to generate AI videos, edit images with AI, or work with creative AI tools.",
    
    # 架构
    "ddd": "Provides comprehensive guidance for Domain-Driven Design including bounded contexts, entities, value objects, aggregates, domain services, and strategic patterns. Use when the user asks about DDD, needs to design domain models, implement DDD patterns, or structure applications with DDD principles.",
    "ddd-cola": "Provides comprehensive guidance for COLA architecture including adapter layer, application layer, domain layer, and infrastructure layer. Use when the user asks about COLA, needs to implement COLA architecture, structure applications with COLA, or work with COLA patterns.",
    "ddd-microservices": "Provides comprehensive guidance for DDD in microservices including bounded contexts, service boundaries, event-driven architecture, and microservice patterns. Use when the user asks about DDD microservices, needs to design microservices with DDD, or implement microservice architectures.",
    "ddd-event-driven": "Provides comprehensive guidance for event-driven architecture including domain events, event sourcing, CQRS, and event patterns. Use when the user asks about event-driven architecture, needs to implement event-driven systems, or work with domain events.",
    "ddd-hexagonal-architecture": "Provides comprehensive guidance for hexagonal architecture including ports and adapters, domain isolation, and dependency inversion. Use when the user asks about hexagonal architecture, needs to implement ports and adapters pattern, or structure applications with hexagonal architecture.",
    "ddd-clean-architecture": "Provides comprehensive guidance for clean architecture including layer separation, dependency rules, and architectural patterns. Use when the user asks about clean architecture, needs to implement clean architecture principles, or structure applications with clean architecture.",
    "c4-model": "Provides comprehensive guidance for C4 model including context diagrams, container diagrams, component diagrams, and code diagrams. Use when the user asks about C4 model, needs to create architecture diagrams, document system architecture, or visualize software architecture.",
    "plantuml": "Provides comprehensive guidance for PlantUML including diagram syntax, UML diagrams, sequence diagrams, and code generation. Use when the user asks about PlantUML, needs to create UML diagrams, generate diagrams from code, or document software design.",
    "drawio-architecture": "Provides comprehensive guidance for draw.io architecture diagrams including diagram creation, shapes, templates, and collaboration. Use when the user asks about draw.io architecture, needs to create architecture diagrams, design system diagrams, or collaborate on diagrams.",
    "drawio-flowchart": "Provides comprehensive guidance for draw.io flowcharts including flowchart creation, shapes, connectors, and diagramming. Use when the user asks about draw.io flowcharts, needs to create flowcharts, design process diagrams, or visualize workflows.",
    "processon-mindmap": "Provides comprehensive guidance for ProcessOn mind mapping including mind map creation, node management, and collaboration. Use when the user asks about ProcessOn mind maps, needs to create mind maps, organize ideas, or collaborate on mind maps.",
    
    # 移动开发
    "uniapp-project-creator": "Provides one-command project creation for uni-app including project initialization, configuration, and template generation. Use when the user asks about creating uni-app projects, needs to initialize a new uni-app project, or generate uni-app project structure.",
    "uniapp-project": "Provides comprehensive guidance for uni-app development including components, APIs, platform compatibility, and best practices. Use when the user asks about uni-app, needs to develop cross-platform applications, use uni-app components, or work with uni-app APIs.",
    "uniappx-project-creator": "Provides one-command project creation for uni-app-x including Vue 3 + TypeScript + Vite setup, configuration, and template generation. Use when the user asks about creating uni-app-x projects, needs to initialize a new uni-app-x project, or generate uni-app-x project structure.",
    "uniappx-project": "Provides comprehensive guidance for uni-app-x development including components, APIs, Vue 3 integration, and TypeScript support. Use when the user asks about uni-app-x, needs to develop uni-app-x applications, use uni-app-x components, or work with uni-app-x APIs.",
    
    # 游戏引擎
    "cocos2d-x": "Provides comprehensive guidance for Cocos2d-x v4 game engine including scene graph, nodes, sprites, actions, animations, physics, rendering, shaders, and platform deployment. Use when the user asks about Cocos2d-x, needs to create games, implement game features, set up development environments, or deploy games to multiple platforms.",
    
    # 其他前端框架
    "angular": "Provides comprehensive guidance for Angular framework including components, modules, services, dependency injection, routing, forms, and TypeScript integration. Use when the user asks about Angular, needs to create Angular applications, implement Angular components, or work with Angular features.",
    "svelte": "Provides comprehensive guidance for Svelte framework including components, reactivity, stores, transitions, and compilation. Use when the user asks about Svelte, needs to create Svelte applications, implement Svelte components, or work with Svelte features.",
    
    # Vue Router 版本
    "vue-router-v3": "Provides comprehensive guidance for Vue Router v3 including route configuration, navigation, nested routes, route guards, dynamic routes, and Vue 2 integration. Use when the user asks about Vue Router v3, needs to set up routing for Vue 2 applications, implement navigation guards, or work with Vue Router v3 features.",
    "vue-router-v4": "Provides comprehensive guidance for Vue Router v4 including route configuration, navigation, nested routes, route guards, and Vue 3 integration. Use when the user asks about Vue Router v4, needs to set up routing for Vue 3 applications, implement navigation guards, or work with Vue Router v4 features.",
    
    # 移动开发
    "react-native": "Provides comprehensive guidance for React Native development including components, navigation, native modules, platform-specific code, and mobile app development. Use when the user asks about React Native, needs to create mobile applications, implement React Native components, or work with React Native features.",
    "react-native-project-creater": "Provides one-command project creation for React Native including project initialization, configuration, and template generation. Use when the user asks about creating React Native projects, needs to initialize a new React Native project, or generate React Native project structure.",
    "flutter": "Provides comprehensive guidance for Flutter development including widgets, state management, navigation, platform channels, and mobile app development. Use when the user asks about Flutter, needs to create Flutter applications, implement Flutter widgets, or work with Flutter features.",
    "flutter-project-creater": "Provides one-command project creation for Flutter including project initialization, configuration, and template generation. Use when the user asks about creating Flutter projects, needs to initialize a new Flutter project, or generate Flutter project structure.",
    "android-kotlin": "Provides comprehensive guidance for Android development with Kotlin including activities, fragments, views, lifecycle, navigation, and Android app development. Use when the user asks about Android Kotlin, needs to create Android applications, implement Android components, or work with Kotlin in Android.",
    "ios-swift": "Provides comprehensive guidance for iOS development with Swift including view controllers, views, navigation, lifecycle, and iOS app development. Use when the user asks about iOS Swift, needs to create iOS applications, implement iOS components, or work with Swift in iOS.",
    
    # 云平台
    "cloud-aws-ec2": "Provides comprehensive guidance for AWS EC2 including instance creation, configuration, security groups, and EC2 management. Use when the user asks about AWS EC2, needs to create EC2 instances, configure EC2, or manage AWS compute resources.",
    "cloud-aws-s3": "Provides comprehensive guidance for AWS S3 including bucket creation, object storage, access control, and S3 management. Use when the user asks about AWS S3, needs to store files in S3, configure S3 buckets, or work with S3 storage.",
    "cloud-aws-rds": "Provides comprehensive guidance for AWS RDS including database creation, configuration, backups, and RDS management. Use when the user asks about AWS RDS, needs to create RDS databases, configure RDS, or manage AWS database services.",
    "cloud-aws-lambda": "Provides comprehensive guidance for AWS Lambda including function creation, triggers, configuration, and serverless development. Use when the user asks about AWS Lambda, needs to create Lambda functions, implement serverless functions, or work with AWS serverless computing.",
    "cloud-azure-vm": "Provides comprehensive guidance for Azure Virtual Machines including VM creation, configuration, networking, and Azure VM management. Use when the user asks about Azure VMs, needs to create Azure VMs, configure Azure compute, or manage Azure virtual machines.",
    "cloud-azure-storage": "Provides comprehensive guidance for Azure Storage including blob storage, file shares, queues, and storage account management. Use when the user asks about Azure Storage, needs to store data in Azure, configure Azure Storage, or work with Azure storage services.",
    "cloud-azure-sql": "Provides comprehensive guidance for Azure SQL Database including database creation, configuration, security, and Azure SQL management. Use when the user asks about Azure SQL, needs to create Azure SQL databases, configure Azure SQL, or manage Azure database services.",
    "cloud-aliyun-ecs": "Provides comprehensive guidance for Alibaba Cloud ECS including instance creation, configuration, security groups, and ECS management. Use when the user asks about Alibaba Cloud ECS, needs to create ECS instances, configure ECS, or manage Alibaba Cloud compute resources.",
    "cloud-aliyun-oss": "Provides comprehensive guidance for Alibaba Cloud OSS including bucket creation, object storage, access control, and OSS management. Use when the user asks about Alibaba Cloud OSS, needs to store files in OSS, configure OSS buckets, or work with Alibaba Cloud storage.",
    "cloud-aliyun-rds": "Provides comprehensive guidance for Alibaba Cloud RDS including database creation, configuration, backups, and RDS management. Use when the user asks about Alibaba Cloud RDS, needs to create RDS databases, configure RDS, or manage Alibaba Cloud database services.",
    "cloud-tencent-cvm": "Provides comprehensive guidance for Tencent Cloud CVM including instance creation, configuration, security groups, and CVM management. Use when the user asks about Tencent Cloud CVM, needs to create CVM instances, configure CVM, or manage Tencent Cloud compute resources.",
    "cloud-tencent-cos": "Provides comprehensive guidance for Tencent Cloud COS including bucket creation, object storage, access control, and COS management. Use when the user asks about Tencent Cloud COS, needs to store files in COS, configure COS buckets, or work with Tencent Cloud storage.",
    "cloud-tencent-cdb": "Provides comprehensive guidance for Tencent Cloud CDB including database creation, configuration, backups, and CDB management. Use when the user asks about Tencent Cloud CDB, needs to create CDB databases, configure CDB, or manage Tencent Cloud database services.",
    "cloud-huawei-ecs": "Provides comprehensive guidance for Huawei Cloud ECS including instance creation, configuration, security groups, and ECS management. Use when the user asks about Huawei Cloud ECS, needs to create ECS instances, configure ECS, or manage Huawei Cloud compute resources.",
    "cloud-huawei-obs": "Provides comprehensive guidance for Huawei Cloud OBS including bucket creation, object storage, access control, and OBS management. Use when the user asks about Huawei Cloud OBS, needs to store files in OBS, configure OBS buckets, or work with Huawei Cloud storage.",
    "cloud-huawei-rds": "Provides comprehensive guidance for Huawei Cloud RDS including database creation, configuration, backups, and RDS management. Use when the user asks about Huawei Cloud RDS, needs to create RDS databases, configure RDS, or manage Huawei Cloud database services.",
    
    # 数据库工具
    "navicat": "Provides comprehensive guidance for Navicat database management tool including database connection, query execution, data management, and database administration. Use when the user asks about Navicat, needs to manage databases with Navicat, execute SQL queries, or work with Navicat features.",
    "dbeaver": "Provides comprehensive guidance for DBeaver database tool including database connection, SQL editor, data management, and database administration. Use when the user asks about DBeaver, needs to manage databases with DBeaver, execute SQL queries, or work with DBeaver features.",
    
    # 工具和生成器
    "code-generator": "Provides comprehensive guidance for code generation including template-based generation, code scaffolding, and automated code creation. Use when the user asks about code generation, needs to generate code from templates, create code scaffolds, or automate code creation.",
    "test-writer": "Provides comprehensive guidance for writing tests including test case creation, test structure, and testing best practices. Use when the user asks about writing tests, needs to create test cases, structure tests, or implement testing strategies.",
    "documentation-builder": "Provides comprehensive guidance for building documentation including documentation generation, formatting, and documentation best practices. Use when the user asks about building documentation, needs to generate documentation, format documentation, or create documentation structures.",
    "api-doc-generator": "Provides comprehensive guidance for API documentation generation including API documentation creation, formatting, and API documentation best practices. Use when the user asks about API documentation, needs to generate API docs, format API documentation, or create API documentation structures.",
    "full-stack-doc": "Provides comprehensive guidance for Chinese product documentation generation including product documentation creation, formatting, and documentation best practices. Use when the user asks about product documentation in Chinese, needs to generate product docs, or create Chinese documentation.",
    
    # 教学工具
    "course-designer": "Provides comprehensive guidance for course design including curriculum development, learning objectives, and course structure. Use when the user asks about course design, needs to design courses, create learning objectives, or structure educational content.",
    "learning-assessor": "Provides comprehensive guidance for learning assessment including assessment creation, evaluation methods, and assessment best practices. Use when the user asks about learning assessment, needs to create assessments, evaluate learning, or implement assessment strategies.",
    "teaching-resource-generator": "Provides comprehensive guidance for teaching resource generation including resource creation, formatting, and educational content development. Use when the user asks about teaching resources, needs to generate teaching materials, create educational content, or develop teaching resources.",
    
    # UniApp
    "uniapp-project": "Provides comprehensive guidance for uni-app development including components, APIs, platform compatibility, and cross-platform development. Use when the user asks about uni-app, needs to develop cross-platform applications, use uni-app components, or work with uni-app APIs.",
    "upgradeLink": "Provides comprehensive guidance for upgrade link management including upgrade link creation, configuration, and upgrade link best practices. Use when the user asks about upgrade links, needs to create upgrade links, configure upgrade processes, or manage upgrade links.",
    
    # 其他
    "mermaid": "Provides comprehensive guidance for creating Mermaid diagrams including flowcharts, sequence diagrams, class diagrams, state diagrams, Gantt charts, and all other Mermaid diagram types. Use when the user requests to create, draw, or visualize any diagram, flowchart, or structured chart using Mermaid syntax.",
    "nvm": "Provides comprehensive guidance for Node Version Manager (nvm) including installation, version management, switching Node.js versions, and environment configuration. Use when the user asks about nvm, needs to manage Node.js versions, switch between Node versions, or configure Node.js environments.",
    "dart-sass": "Provides comprehensive guidance for Dart Sass including Sass syntax, compilation, mixins, functions, and best practices. Use when the user asks about Dart Sass, needs to compile Sass to CSS, use Sass features, or work with Sass in projects.",
    "electron": "Provides comprehensive guidance for Electron framework including main process, renderer process, IPC communication, window management, and desktop app development. Use when the user asks about Electron, needs to create desktop applications, implement Electron features, or build cross-platform desktop apps.",
    "electron-egg": "Provides comprehensive guidance for Electron EGG framework including project structure, main/renderer processes, IPC, window management, and desktop app development. Use when the user asks about Electron EGG, needs to create Electron applications with EGG, or work with Electron EGG patterns.",
    "tauri": "Provides comprehensive guidance for Tauri framework including Rust backend, frontend integration, window management, and desktop app development. Use when the user asks about Tauri, needs to create Tauri applications, implement Tauri features, or build lightweight desktop apps.",
    "ucharts": "Provides comprehensive guidance for uCharts chart library including chart types, data formats, chart configuration, and platform support. Use when the user asks about uCharts, needs to create charts, configure chart options, or work with uCharts in applications.",
    "lime-echart": "Provides comprehensive guidance for Lime ECharts including chart creation, configuration, data visualization, and interactive charts. Use when the user asks about Lime ECharts, needs to create charts, visualize data, or work with ECharts features.",
}

def update_description(skill_dir):
    """更新单个 skill 的 description"""
    skill_md = Path(skill_dir) / "SKILL.md"
    if not skill_md.exists():
        return False
    
    # 读取文件
    content = skill_md.read_text(encoding='utf-8')
    
    # 提取 skill name
    name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
    if not name_match:
        return False
    
    skill_name = name_match.group(1).strip()
    
    # 获取新的 description
    new_description = SKILL_DESCRIPTIONS.get(skill_name)
    if not new_description:
        # 如果没有预定义的描述，尝试从现有内容生成
        return False
    
    # 替换 description（支持中文和英文）
    pattern = r'^description:\s*.+$'
    replacement = f'description: {new_description}'
    
    new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    if new_content != content:
        skill_md.write_text(new_content, encoding='utf-8')
        return True
    
    return False

def main():
    """主函数"""
    base_dir = Path(__file__).parent.parent
    skills_dir = base_dir / "skills"
    
    if not skills_dir.exists():
        print(f"Skills directory not found: {skills_dir}")
        return
    
    updated_count = 0
    skipped_count = 0
    
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        
        if update_description(skill_dir):
            print(f"✅ Updated: {skill_dir.name}")
            updated_count += 1
        else:
            skill_name = skill_dir.name
            if skill_name in SKILL_DESCRIPTIONS:
                print(f"⚠️  Skipped (already correct or error): {skill_name}")
            skipped_count += 1
    
    print(f"\n=== Summary ===")
    print(f"Updated: {updated_count}")
    print(f"Skipped: {skipped_count}")
    print(f"Total: {updated_count + skipped_count}")

if __name__ == "__main__":
    main()
