---
name: nestjs
description: Provides comprehensive guidance for NestJS framework including modules, controllers, providers, dependency injection, decorators, and microservices. Use when the user asks about NestJS, needs to create NestJS applications, implement modules and controllers, or build scalable Node.js applications.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build RESTful APIs with NestJS
- Create controllers, services, and modules
- Implement dependency injection
- Set up middleware, guards, interceptors, and filters
- Work with databases (TypeORM, Prisma, Mongoose)
- Implement authentication and authorization
- Use validation and transformation pipes
- Set up GraphQL APIs
- Implement WebSocket connections
- Build microservices
- Write unit and e2e tests
- Configure NestJS applications
- Use custom decorators and providers
- Implement dynamic modules
- Handle exceptions and errors
- Use caching and performance optimization
- Deploy NestJS applications

## How to use this skill

This skill is organized to match the NestJS official documentation structure (https://docs.nestjs.com/). When working with NestJS:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/fundamentals/getting-started.md`
   - Controllers/控制器 → `examples/fundamentals/controllers.md`
   - Providers/提供者 → `examples/fundamentals/providers.md`
   - Modules/模块 → `examples/fundamentals/modules.md`
   - Middleware/中间件 → `examples/fundamentals/middleware.md`
   - Guards/守卫 → `examples/fundamentals/guards.md`
   - Interceptors/拦截器 → `examples/fundamentals/interceptors.md`
   - Pipes/管道 → `examples/fundamentals/pipes.md`
   - Exception filters/异常过滤器 → `examples/fundamentals/exception-filters.md`
   - Custom decorators/自定义装饰器 → `examples/fundamentals/custom-decorators.md`
   - Database/数据库 → `examples/techniques/database.md`
   - Validation/验证 → `examples/techniques/validation.md`
   - Caching/缓存 → `examples/techniques/caching.md`
   - File upload/文件上传 → `examples/techniques/file-upload.md`
   - Security/安全 → `examples/security/authentication.md`
   - GraphQL → `examples/graphql/getting-started.md`
   - WebSockets → `examples/websockets/gateways.md`
   - Microservices → `examples/microservices/basics.md`
   - Testing/测试 → `examples/testing/unit-testing.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Fundamentals (基础) - `examples/fundamentals/`**:
   - `examples/fundamentals/getting-started.md` - Creating a NestJS application and project structure
   - `examples/fundamentals/controllers.md` - Creating controllers and handling routes
   - `examples/fundamentals/providers.md` - Creating providers and services
   - `examples/fundamentals/modules.md` - Creating and organizing modules
   - `examples/fundamentals/middleware.md` - Creating and using middleware
   - `examples/fundamentals/guards.md` - Creating and using guards
   - `examples/fundamentals/interceptors.md` - Creating and using interceptors
   - `examples/fundamentals/pipes.md` - Creating and using pipes
   - `examples/fundamentals/exception-filters.md` - Creating and using exception filters
   - `examples/fundamentals/custom-decorators.md` - Creating custom decorators
   - `examples/fundamentals/dependency-injection.md` - Dependency injection patterns
   - `examples/fundamentals/custom-providers.md` - Custom providers (useValue, useFactory, useClass)

   **Techniques (技术) - `examples/techniques/`**:
   - `examples/techniques/database.md` - Database integration (TypeORM, Prisma, Mongoose)
   - `examples/techniques/validation.md` - Validation with class-validator
   - `examples/techniques/caching.md` - Caching implementation
   - `examples/techniques/file-upload.md` - File upload handling
   - `examples/techniques/configuration.md` - Configuration management
   - `examples/techniques/logging.md` - Logging implementation
   - `examples/techniques/http-module.md` - HTTP client module
   - `examples/techniques/task-scheduling.md` - Task scheduling with cron

   **Security (安全) - `examples/security/`**:
   - `examples/security/authentication.md` - Authentication implementation
   - `examples/security/authorization.md` - Authorization with guards
   - `examples/security/encryption.md` - Encryption and hashing
   - `examples/security/helmet.md` - Security headers with Helmet

   **GraphQL - `examples/graphql/`**:
   - `examples/graphql/getting-started.md` - GraphQL setup and basics
   - `examples/graphql/resolvers.md` - GraphQL resolvers
   - `examples/graphql/schema-first.md` - Schema-first approach
   - `examples/graphql/code-first.md` - Code-first approach

   **WebSockets - `examples/websockets/`**:
   - `examples/websockets/gateways.md` - WebSocket gateways
   - `examples/websockets/adapters.md` - WebSocket adapters

   **Microservices - `examples/microservices/`**:
   - `examples/microservices/basics.md` - Microservices basics
   - `examples/microservices/transport.md` - Transport layer configuration
   - `examples/microservices/rabbitmq.md` - RabbitMQ integration
   - `examples/microservices/kafka.md` - Kafka integration

   **Testing - `examples/testing/`**:
   - `examples/testing/unit-testing.md` - Unit testing
   - `examples/testing/e2e-testing.md` - End-to-end testing
   - `examples/testing/mocking.md` - Mocking dependencies

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow NestJS conventions and best practices
   - Examples include both JavaScript and TypeScript versions where applicable
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/decorators.md` - All NestJS decorators reference
   - `api/modules-api.md` - Module API reference
   - `api/controllers-api.md` - Controller API reference
   - `api/providers-api.md` - Provider API reference
   - `api/middleware-api.md` - Middleware API reference
   - `api/guards-api.md` - Guards API reference
   - `api/interceptors-api.md` - Interceptors API reference
   - `api/pipes-api.md` - Pipes API reference

5. **Use templates** from the `templates/` directory:
   - `templates/project-structure.md` - Standard NestJS project organization
   - `templates/module-template.md` - Module template
   - `templates/controller-template.md` - Controller template
   - `templates/service-template.md` - Service template
   - `templates/dto-template.md` - DTO template

## Examples and Templates

This skill includes detailed examples organized to match the NestJS official documentation structure (https://docs.nestjs.com/). All examples are in the `examples/` directory, organized by topic:

### Fundamentals (基础) - `examples/fundamentals/`

- `examples/fundamentals/getting-started.md` - Creating a NestJS application, project structure, and CLI usage
- `examples/fundamentals/controllers.md` - Controllers, routing, request handling, and route parameters
- `examples/fundamentals/providers.md` - Providers, services, dependency injection, and custom providers
- `examples/fundamentals/modules.md` - Modules, feature modules, shared modules, and global modules
- `examples/fundamentals/middleware.md` - Middleware creation and usage
- `examples/fundamentals/guards.md` - Guards for authentication and authorization
- `examples/fundamentals/interceptors.md` - Interceptors for cross-cutting concerns
- `examples/fundamentals/pipes.md` - Pipes for validation and transformation
- `examples/fundamentals/exception-filters.md` - Exception filters for error handling
- `examples/fundamentals/custom-decorators.md` - Creating custom decorators
- `examples/fundamentals/dependency-injection.md` - Dependency injection patterns and best practices
- `examples/fundamentals/custom-providers.md` - Custom providers (useValue, useFactory, useClass, useExisting)

### Techniques (技术) - `examples/techniques/`

- `examples/techniques/database.md` - Database integration with TypeORM, Prisma, and Mongoose
- `examples/techniques/validation.md` - Validation with class-validator and class-transformer
- `examples/techniques/caching.md` - Caching implementation with Redis
- `examples/techniques/file-upload.md` - File upload handling with multer
- `examples/techniques/configuration.md` - Configuration management with @nestjs/config
- `examples/techniques/logging.md` - Logging implementation
- `examples/techniques/http-module.md` - HTTP client module usage
- `examples/techniques/task-scheduling.md` - Task scheduling with @nestjs/schedule

### Security (安全) - `examples/security/`

- `examples/security/authentication.md` - Authentication implementation with JWT and Passport
- `examples/security/authorization.md` - Authorization with guards and roles
- `examples/security/encryption.md` - Encryption and hashing
- `examples/security/helmet.md` - Security headers with Helmet

### GraphQL - `examples/graphql/`

- `examples/graphql/getting-started.md` - GraphQL setup and basics
- `examples/graphql/resolvers.md` - GraphQL resolvers and queries
- `examples/graphql/schema-first.md` - Schema-first approach
- `examples/graphql/code-first.md` - Code-first approach

### WebSockets - `examples/websockets/`

- `examples/websockets/gateways.md` - WebSocket gateways
- `examples/websockets/adapters.md` - WebSocket adapters

### Microservices - `examples/microservices/`

- `examples/microservices/basics.md` - Microservices basics and setup
- `examples/microservices/transport.md` - Transport layer configuration
- `examples/microservices/rabbitmq.md` - RabbitMQ integration
- `examples/microservices/kafka.md` - Kafka integration

### Testing - `examples/testing/`

- `examples/testing/unit-testing.md` - Unit testing with Jest
- `examples/testing/e2e-testing.md` - End-to-end testing
- `examples/testing/mocking.md` - Mocking dependencies

### Templates Directory (`templates/`)

- `templates/project-structure.md` - Standard NestJS project organization and structure
- `templates/module-template.md` - Module template
- `templates/controller-template.md` - Controller template
- `templates/service-template.md` - Service template
- `templates/dto-template.md` - DTO template

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/project-structure.md` for project organization
- Use module, controller, service, and DTO templates for quick setup
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official NestJS API documentation structure:

### Decorators API (`api/decorators.md`)
- Module decorators: `@Module()`
- Controller decorators: `@Controller()`, `@Get()`, `@Post()`, `@Put()`, `@Delete()`, `@Patch()`
- Parameter decorators: `@Param()`, `@Query()`, `@Body()`, `@Headers()`, `@Req()`, `@Res()`
- Provider decorators: `@Injectable()`, `@Inject()`
- Guard decorators: `@UseGuards()`
- Interceptor decorators: `@UseInterceptors()`
- Pipe decorators: `@UsePipes()`
- Exception filter decorators: `@UseFilters()`

### Modules API (`api/modules-api.md`)
- `@Module()` decorator properties
- Module imports, exports, and providers
- Dynamic modules

### Controllers API (`api/controllers-api.md`)
- `@Controller()` decorator
- Route decorators and parameters
- Request and response handling

### Providers API (`api/providers-api.md`)
- `@Injectable()` decorator
- Custom providers (useValue, useFactory, useClass, useExisting)
- Provider scopes

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use dependency injection**: Leverage NestJS DI container for loose coupling
2. **Organize by modules**: Group related functionality into feature modules
3. **Use DTOs**: Create Data Transfer Objects for request/response validation
4. **Implement guards**: Use guards for authentication and authorization
5. **Handle exceptions**: Use exception filters for consistent error handling
6. **Validate input**: Use validation pipes to validate incoming data
7. **Use interceptors**: Implement interceptors for cross-cutting concerns
8. **Write tests**: Write unit and e2e tests for your application
9. **Follow naming conventions**: Use consistent naming for files and classes
10. **Use configuration module**: Use @nestjs/config for environment configuration

## Resources

- **Official Documentation**: https://docs.nestjs.com/
- **GitHub Repository**: https://github.com/nestjs/nest
- **CLI Documentation**: https://docs.nestjs.com/cli/overview
- **Recipes**: https://docs.nestjs.com/recipes

## Keywords

NestJS, Nest, Node.js, TypeScript, framework, controller, provider, module, middleware, guard, interceptor, pipe, exception filter, dependency injection, decorator, REST API, GraphQL, WebSocket, microservice, testing, validation, database, TypeORM, Prisma, Mongoose, authentication, authorization, JWT, Passport, caching, logging, configuration, 控制器, 提供者, 模块, 中间件, 守卫, 拦截器, 管道, 异常过滤器, 依赖注入, 装饰器, 微服务, 测试, 验证, 数据库, 认证, 授权
