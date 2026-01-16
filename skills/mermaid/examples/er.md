## Instructions

Entity Relationship (ER) diagrams represent the structure of a database, showing entities, their attributes, and relationships between them. An entity–relationship model (or ER model) describes interrelated things of interest in a specific domain of knowledge. A basic ER model is composed of entity types (which classify the things of interest) and specifies relationships that can exist between entities (instances of those entity types).

### Syntax

- Use `erDiagram` keyword
- Entities: `ENTITY_NAME { }` or `ENTITY_NAME { type name }` (with attributes)
- Relationships: `<first-entity> [<relationship> <second-entity> : <relationship-label>]`
- Cardinality markers:
  - `||` - Exactly one
  - `|o` - Zero or one
  - `}|` - One or more
  - `}o` - Zero or more
- Relationship types:
  - `--` - Identifying relationship (solid line)
  - `..` - Non-identifying relationship (dashed line)
- Aliases: `one or zero`, `zero or one`, `one or more`, `one or many`, `many(1)`, `1+`, `zero or more`, `zero or many`, `many(0)`, `0+`, `only one`, `1`, `to`, `optionally to`
- Attributes: `type name` or `*type name` (asterisk for primary key)
- Attribute keys: `PK` (Primary Key), `FK` (Foreign Key), `UK` (Unique Key)
- Comments: Double quotes at the end of attribute: `type name "comment"`
- Entity aliases: `ENTITY_NAME[alias]` (alias shown instead of entity name)
- Direction: `direction TB|BT|LR|RL` (default: TB)
- Styling: `style entityId fill:#color,stroke:#color` or `classDef className fill:#color`
- Unicode and Markdown: Supported in entity names, relationships, and attributes

Reference: [Mermaid Entity Relationship Diagram Documentation](https://mermaid.ai/open-source/syntax/entityRelationshipDiagram.html)

### Example (Basic ER Diagram)

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    PRODUCT ||--|{ LINE-ITEM : "ordered in"
```

### Example (With Attributes)

```mermaid
erDiagram
    CUSTOMER {
        int id PK
        string name
        string email UK
        string phone
    }
    ORDER {
        int id PK
        date orderDate
        decimal total
        int customerId FK
    }
    PRODUCT {
        int id PK
        string name
        decimal price
        int stock
    }
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    PRODUCT ||--|{ LINE-ITEM : "ordered in"
```

### Example (With Relationship Labels)

```mermaid
erDiagram
    PROPERTY ||--|{ ROOM : contains
    ROOM ||--o{ WINDOW : has
    BUILDING ||--o{ PROPERTY : "located in"
```

### Example (Identifying vs Non-identifying)

```mermaid
erDiagram
    PERSON }|..|{ CAR : "driver"
    PERSON ||--o{ NAMED-DRIVER : "is"
    CAR ||--o{ NAMED-DRIVER : "drives"
```

### Example (With Aliases)

```mermaid
erDiagram
    CUSTOMER[Cust] {
        int id PK
        string name
    }
    ORDER[Ord] {
        int id PK
        date orderDate
    }
    LINE_ITEM[Item] {
        int id PK
        int quantity
    }
    PRODUCT[Prod] {
        int id PK
        string name
    }
    
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    PRODUCT ||--|{ LINE_ITEM : "ordered in"
```

### Example (With Attribute Comments)

```mermaid
erDiagram
    USER {
        int id PK "Unique identifier"
        string username UK "Login name"
        string email "Contact email"
        date createdAt "Account creation date"
    }
    POST {
        int id PK
        string title
        text content
        int userId FK "Author reference"
        date publishedAt
    }
    USER ||--o{ POST : "writes"
```

### Example (With Direction - Left to Right)

```mermaid
erDiagram
    direction LR
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    PRODUCT ||--|{ LINE-ITEM : "ordered in"
```

### Example (With Styling)

```mermaid
erDiagram
    CUSTOMER {
        int id PK
        string name
        string email
    }
    ORDER {
        int id PK
        date orderDate
        decimal total
    }
    CUSTOMER ||--o{ ORDER : places

    style CUSTOMER fill:#e1f5,stroke:#333,stroke-width:2px
    style ORDER fill:#fff4e1,stroke:#333,stroke-width:2px
```

### Example (With Class Definitions)

```mermaid
erDiagram
    CUSTOMER {
        int id PK
        string name
    }
    ORDER {
        int id PK
        date orderDate
    }
    CUSTOMER ||--o{ ORDER : places

    classDef customerClass fill:#e1f5,stroke:#333,stroke-width:2px
    classDef orderClass fill:#fff4e1,stroke:#333,stroke-width:2px

    class CUSTOMER customerClass
    class ORDER orderClass
```

### Example (Complex Database Schema)

```mermaid
erDiagram
    USER {
        int id PK
        string username UK
        string email
        date createdAt
    }
    POST {
        int id PK
        string title
        text content
        int authorId FK
        date publishedAt
    }
    COMMENT {
        int id PK
        text content
        int postId FK
        int userId FK
        date createdAt
    }
    CATEGORY {
        int id PK
        string name
        string slug UK
    }
    USER ||--o{ POST : "writes"
    POST ||--o{ COMMENT : "has"
    USER ||--o{ COMMENT : "makes"
    CATEGORY ||--o{ POST : "categorizes"
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If ER diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    CUSTOMER[Customer]
    ORDER[Order]
    PRODUCT[Product]
    LINE_ITEM[Line Item]

    CUSTOMER -->|places| ORDER
    ORDER -->|contains| LINE_ITEM
    PRODUCT -->|ordered in| LINE_ITEM
```
