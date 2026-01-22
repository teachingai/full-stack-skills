# Java 编程规范 - 文档化要求

## 概述

本文档基于《JAVA 编程规范》，说明 Java 代码注释的规范要求。根据规范第10节"文档化"的要求，必须用 javadoc 来为类生成文档，这是被各种 Java 编译器都认可的标准方法。

## 核心要求

### 1. 必须使用 JavaDoc

- **必须用 javadoc 来为类生成文档**，不仅因为它是标准，这也是被各种 Java 编译器都认可的方法
- 程序中类的描述要求符合 Javadoc 的规范

### 2. JavaDoc 注释格式

根据规范，JavaDoc 注释的标准格式如下：

```java
/**
 * <p>向缓冲池中增加一个属性和相应的字符串值</p>
 *
 * @return int
 * @param attribute java.lang.String
 * @param data java.lang.String
 * @exception java.lang.Exception
 */
```

### 3. 格式要求

1. **描述信息使用 `<p> </p>` 括起来**
   - 类、方法、字段的描述都应该使用 `<p>` 标签包裹
   - 这是规范要求的格式

2. **必须声明返回参数**
   - 使用 `@return` 标签
   - 说明返回值的类型和含义

3. **必须声明传入参数**
   - 使用 `@param` 标签
   - 格式：`@param 参数名 参数类型 参数说明`
   - 例如：`@param attribute java.lang.String`

4. **必须声明异常处理**
   - 使用 `@exception` 或 `@throws` 标签
   - 格式：`@exception 异常类型 异常说明`
   - 例如：`@exception java.lang.Exception`

## 类注释规范

### 基本格式

```java
/**
 * <p>类描述信息</p>
 *
 * <p>类的详细说明，包括主要功能、职责等</p>
 *
 * @author 作者名
 * @since 版本号或日期
 */
public class MyClass {
}
```

### 示例

```java
/**
 * <p>用户管理服务类</p>
 *
 * <p>提供用户相关的业务逻辑处理，包括用户的创建、查询、更新和删除操作。
 * 本服务遵循领域驱动设计（DDD）原则，封装用户领域的核心业务逻辑。</p>
 *
 * @author System
 * @since 1.0.0
 */
public class UserService {
}
```

## 方法注释规范

### 基本格式

```java
/**
 * <p>方法描述信息</p>
 *
 * <p>方法的详细说明，包括功能、处理流程等</p>
 *
 * @param 参数名 参数类型 参数说明
 * @return 返回类型 返回值说明
 * @exception 异常类型 异常说明
 */
public ReturnType methodName(ParamType param) {
}
```

### 示例

```java
/**
 * <p>向缓冲池中增加一个属性和相应的字符串值</p>
 *
 * <p>该方法用于向系统缓冲池中添加新的属性配置，包括属性名称和对应的字符串值。
 * 如果属性已存在，则更新其值；如果不存在，则创建新的属性项。</p>
 *
 * @param attribute java.lang.String 属性名称，不能为空
 * @param data java.lang.String 属性对应的字符串值
 * @return int 返回操作结果，0表示成功，-1表示失败
 * @exception java.lang.Exception 当属性名称为空或缓冲池操作失败时抛出
 */
public int addAttribute(String attribute, String data) throws Exception {
}
```

### 多个参数示例

```java
/**
 * <p>创建新用户</p>
 *
 * <p>根据用户创建请求创建新用户，包括数据验证、密码加密等处理。</p>
 *
 * @param username java.lang.String 用户名，长度3-20个字符
 * @param email java.lang.String 邮箱地址，必须符合邮箱格式
 * @param password java.lang.String 密码，长度至少8个字符
 * @return com.example.dto.UserDTO 创建成功的用户信息DTO
 * @exception java.lang.IllegalArgumentException 当请求参数不合法时抛出
 * @exception com.example.exception.BusinessException 当用户名或邮箱已存在时抛出
 */
public UserDTO createUser(String username, String email, String password) 
    throws IllegalArgumentException, BusinessException {
}
```

## 字段注释规范

### 基本格式

```java
/**
 * <p>字段描述信息</p>
 *
 * <p>字段的详细说明，包括用途、约束等</p>
 */
private FieldType fieldName;
```

### 示例

```java
/**
 * <p>用户数据访问对象</p>
 *
 * <p>用于执行用户相关的数据库操作，由Spring容器注入</p>
 */
private final UserMapper userMapper;
```

## 标签使用规范

### @param 标签

**格式**：`@param 参数名 参数类型 参数说明`

**要求**：
- 必须包含参数类型（完整类名或简单类型）
- 参数说明要清晰，包括约束条件

**示例**：
```java
/**
 * @param userId java.lang.Long 用户唯一标识符，不能为null
 * @param username java.lang.String 用户名，长度3-20个字符
 */
```

### @return 标签

**格式**：`@return 返回类型 返回值说明`

**要求**：
- 必须包含返回类型（完整类名或简单类型）
- 说明返回值的含义和可能的值

**示例**：
```java
/**
 * @return int 返回操作结果，0表示成功，-1表示失败
 * @return com.example.dto.UserDTO 用户信息DTO，如果用户不存在则返回null
 */
```

### @exception / @throws 标签

**格式**：`@exception 异常类型 异常说明` 或 `@throws 异常类型 异常说明`

**要求**：
- 必须包含完整的异常类型（包括包名）
- 说明什么情况下会抛出该异常

**示例**：
```java
/**
 * @exception java.lang.IllegalArgumentException 当请求参数不合法时抛出
 * @exception com.example.exception.BusinessException 当业务规则违反时抛出
 * @exception java.lang.Exception 当系统发生未知错误时抛出
 */
```

## 完整示例

### 类注释完整示例

```java
/**
 * <p>用户管理控制器</p>
 *
 * <p>提供用户相关的REST API接口，包括用户的创建、查询、更新和删除操作。
 * 本控制器遵循RESTful设计规范，使用标准的HTTP方法进行资源操作。</p>
 *
 * <p>主要功能：
 * <ul>
 *   <li>创建新用户</li>
 *   <li>根据ID查询用户信息</li>
 *   <li>更新用户信息</li>
 *   <li>删除用户</li>
 * </ul>
 * </p>
 *
 * @author System
 * @since 1.0.0
 */
@RestController
@RequestMapping("/api/users")
public class UserController {
}
```

### 方法注释完整示例

```java
/**
 * <p>根据用户ID查询用户信息</p>
 *
 * <p>根据提供的用户ID从数据库查询对应的用户详细信息。
 * 如果用户不存在，将抛出ResourceNotFoundException异常。</p>
 *
 * @param id java.lang.Long 用户唯一标识符，不能为null
 * @return com.example.dto.UserDTO 用户信息DTO，包含用户的基本信息
 * @exception com.example.exception.ResourceNotFoundException 当用户不存在时抛出
 * @exception java.lang.IllegalArgumentException 当id为null时抛出
 */
@GetMapping("/{id}")
public UserDTO getUserById(@PathVariable Long id) {
    // 实现代码
}
```

## 规范要点总结

1. **必须使用 `<p>` 标签包裹描述信息**
   - 类描述：`<p>类描述</p>`
   - 方法描述：`<p>方法描述</p>`
   - 字段描述：`<p>字段描述</p>`

2. **必须声明所有参数**
   - 格式：`@param 参数名 参数类型 参数说明`
   - 参数类型使用完整类名（如 `java.lang.String`）或简单类型（如 `int`）

3. **必须声明返回值**
   - 格式：`@return 返回类型 返回值说明`
   - 返回类型使用完整类名或简单类型

4. **必须声明异常**
   - 格式：`@exception 异常类型 异常说明` 或 `@throws 异常类型 异常说明`
   - 异常类型使用完整类名（包括包名）

5. **标签顺序**
   - 描述信息（`<p>` 标签）
   - `@param` 标签（按参数顺序）
   - `@return` 标签
   - `@exception` / `@throws` 标签
   - 其他标签（`@author`, `@since` 等）

## 与标准 JavaDoc 的区别

本规范基于《JAVA 编程规范》，与标准 JavaDoc 的主要区别：

1. **描述信息必须使用 `<p>` 标签包裹**
   - 标准 JavaDoc：可以直接写描述，不需要 `<p>` 标签
   - 本规范：描述信息必须使用 `<p> </p>` 括起来

2. **参数类型声明更明确**
   - 标准 JavaDoc：`@param paramName description`
   - 本规范：`@param paramName paramType description`（包含类型）

3. **返回值类型声明更明确**
   - 标准 JavaDoc：`@return description`
   - 本规范：`@return returnType description`（包含类型）

## 参考资料

- 《JAVA 编程规范》第10节 - 文档化
- Sun Microsystems, Inc. 《How to Write Doc Comments for the Javadoc(TM) Tool》
