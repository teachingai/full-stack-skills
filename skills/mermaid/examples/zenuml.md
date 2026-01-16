## Instructions

ZenUML provides a simplified way to create sequence diagrams with a more concise syntax than the original Sequence Diagram in Mermaid. A sequence diagram is an interaction diagram that shows how processes operate with one another and in what order.

### Syntax

- Use `zenuml` keyword
- Participants: Defined implicitly by order of appearance, or explicitly with `participant Name`
- Annotators: Use symbols instead of rectangles (e.g., `@Actor`, `@User`, `@Database`)
- Aliases: `participant Alias as "Label"`
- Messages:
  - Sync message: `Participant1.method() -> Participant2` (blocking)
  - Async message: `Participant1.method() => Participant2` (non-blocking)
  - Creation message: `new Participant()` (creates new object)
  - Reply message: `Participant2.result() -> Participant1` or `@return` or `return`
- Nesting: Sync and Creation messages are naturally nestable with `{}`
- Comments: `// comment` (Markdown supported)
- Control structures:
  - Loops: `while(condition)`, `for(condition)`, `forEach(condition)`, `loop(condition)`
  - Alt: `if(condition) { } else if(condition) { } else { }`
  - Opt: `opt { }`
  - Parallel: `par { statement1 statement2 }`
  - Try/Catch/Finally: `try { } catch { } finally { }`

Reference: [Mermaid ZenUML Documentation](https://mermaid.ai/open-source/syntax/zenuml.html)

### Example (Basic Sequence)

```mermaid
zenuml
    User.login() -> System
    System.validate() -> Database
    Database.query() -> System
    System.response() -> User
```

### Example (With Participants)

```mermaid
zenuml
    participant User
    participant System
    participant Database

    User.login() -> System
    System.validate() -> Database
    Database.query() -> System
    System.response() -> User
```

### Example (Sync and Async Messages)

```mermaid
zenuml
    participant Client
    participant Server

    Client.sendRequest() -> Server
    Server.process() -> Database
    Server.notify() => Client
    Server.response() -> Client
```

### Example (With Nesting)

```mermaid
zenuml
    User.login() -> System {
        System.validate() -> Database
        Database.check() -> System
    }
    System.response() -> User
```

### Example (With Loops)

```mermaid
zenuml
    participant User
    participant System

    User.request() -> System
    while(hasMoreData) {
        System.fetch() -> Database
        Database.result() -> System
        System.send() -> User
    }
    System.complete() -> User
```

### Example (With Alt - Alternative Paths)

```mermaid
zenuml
    User.login() -> System
    if(valid) {
        System.success() -> User
    } else {
        System.error() -> User
    }
```

### Example (With Opt - Optional)

```mermaid
zenuml
    User.request() -> System
    opt(cacheAvailable) {
        System.getFromCache() -> Cache
        Cache.data() -> System
    }
    System.response() -> User
```

### Example (With Parallel)

```mermaid
zenuml
    User.request() -> System
    par {
        System.process1() -> Service1
        System.process2() -> Service2
        System.process3() -> Service3
    }
    System.combine() -> User
```

### Example (With Try/Catch/Finally)

```mermaid
zenuml
    User.request() -> System
    try {
        System.process() -> Database
        Database.result() -> System
    } catch {
        System.error() -> User
    } finally {
        System.cleanup()
    }
```

### Example (With Annotators)

```mermaid
zenuml
    @Actor User
    @System API
    @Database DB

    User.login() -> API
    API.validate() -> DB
    DB.query() -> API
    API.response() -> User
```

### Example (With Comments)

```mermaid
zenuml
    // User authentication flow
    User.login() -> System
    // Validate credentials
    System.validate() -> Database
    Database.check() -> System
    // Return result
    System.response() -> User
```

### Alternative (Standard Sequence Diagram - compatible with all Mermaid versions)

If ZenUML is not supported, use the standard sequence diagram:

```mermaid
sequenceDiagram
    participant U as User
    participant S as System
    participant D as Database

    U->>S: Login Request
    activate S
    S->>D: Query User
    activate D
    D-->>S: User Data
    deactivate D
    S-->>U: Login Success
    deactivate S
```
