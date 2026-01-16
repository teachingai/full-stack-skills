## Instructions

Architecture diagrams are used to show the relationship between services and resources commonly found within the Cloud or CI/CD deployments. In an architecture diagram, services (nodes) are connected by edges. Related services can be placed within groups to better illustrate how they are organized.

**⚠️ Important Compatibility Note**: `architecture-beta` requires Mermaid v11.1.0 or higher. If your rendering environment doesn't support this diagram type (you'll see "No diagram type detected" error), please use the **Flowchart alternatives** provided below each example, which are compatible with all Mermaid versions.

### Syntax

- Use `architecture-beta` keyword (requires Mermaid v11.1.0+)
- **If your environment doesn't support `architecture-beta`**: Each example below includes a flowchart alternative that works with all Mermaid versions
- Building blocks: `groups`, `services`, `edges`, and `junctions`
- Icons: Declared by surrounding the icon name with `()`
- Labels: Declared by surrounding the text with `[]`
- Groups: `group {group id}({icon name})[{title}] (in {parent id})?`
- Services: `service {service id}({icon name})[{title}] (in {parent id})?`
- Edges: `{serviceId}{{group}}?:{T|B|L|R} -- {T|B|L|R}:{serviceId}{{group}}?` (use `--` not `-->`)
- Junctions: `junction {junction id} (in {parent id})?`
- Default icons: `cloud`, `database`, `disk`, `internet`, `server`
- Custom icons: Can use 200,000+ icons from iconify.design by registering an icon pack

Reference: [Mermaid Architecture Diagram Documentation](https://mermaid.ai/open-source/syntax/architecture.html)

### Example (Basic Architecture)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group public_api(cloud)[Public API]
    group private_api(cloud)[Private API] in public_api
    service database1(database)[My Database] in private_api
    service server1(server)[Web Server] in public_api
    server1:L -- R:database1
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph PublicAPI["Public API"]
        subgraph PrivateAPI["Private API"]
            Database[(My Database)]
        end
        Server[Web Server]
    end
    Server --> Database
```

### Example (With Edges and Directions)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    service db(database)[Database]
    service server(server)[Server]
    service gateway(internet)[Gateway]

    db:L -- R:server
    server:T -- B:gateway
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart LR
    DB[(Database)]
    Server[Server]
    Gateway[Gateway]

    DB --> Server
    Server --> Gateway
```

### Example (Groups and Nested Services)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group frontend(cloud)[Frontend]
    group backend(cloud)[Backend]

    service web(server)[Web Server] in frontend
    service api(server)[API Server] in backend
    service db(database)[Database] in backend

    web:L -- R:api
    api:L -- R:db
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph Frontend["Frontend"]
        Web[Web Server]
    end
    subgraph Backend["Backend"]
        API[API Server]
        DB[(Database)]
    end
    Web --> API
    API --> DB
```

### Example (With Junctions)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    service db1(database)[Database 1]
    service db2(database)[Database 2]
    service server(server)[Server]
    junction j1

    server:B -- T:j1
    j1:L -- R:db1
    j1:R -- L:db2
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    Server[Server]
    DB1[(Database 1)]
    DB2[(Database 2)]

    Server --> DB1
    Server --> DB2
```

### Example (Edge from Group to Group)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group groupOne(cloud)[Group One]
    group groupTwo(cloud)[Group Two]

    service server[Server] in groupOne
    service subnet[Subnet] in groupTwo

    server{group}:B -- T:subnet{group}
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph GroupOne["Group One"]
        Server[Server]
    end
    subgraph GroupTwo["Group Two"]
        Subnet[Subnet]
    end
    Server --> Subnet
```

### Example (Complex Cloud Architecture)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group public(cloud)[Public Cloud]
    group private(cloud)[Private Cloud]

    service gateway(internet)[Internet Gateway] in public
    service loadbalancer(server)[Load Balancer] in public
    service app1(server)[App Server 1] in private
    service app2(server)[App Server 2] in private
    service db(database)[Database] in private
    service storage(disk)[Storage] in private

    gateway:L -- R:loadbalancer
    loadbalancer:B -- T:app1
    loadbalancer:B -- T:app2
    app1:L -- R:db
    app2:L -- R:db
    db:B -- T:storage
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph Public["Public Cloud"]
        Gateway[Internet Gateway]
        LB[Load Balancer]
    end
    subgraph Private["Private Cloud"]
        App1[App Server 1]
        App2[App Server 2]
        DB[(Database)]
        Storage[(Storage)]
    end

    Gateway --> LB
    LB --> App1
    LB --> App2
    App1 --> DB
    App2 --> DB
    DB --> Storage
```
