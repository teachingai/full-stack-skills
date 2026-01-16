## Instructions

Block diagrams are an intuitive way to represent complex systems, processes, or architectures visually. They are composed of blocks and connectors, where blocks represent fundamental components or functions, and connectors show relationships or flow between components. Unlike flowcharts, block diagrams give the author full control over where shapes are positioned.

### Syntax

- Use `block-beta` keyword
- Basic blocks: `block BlockName` or just `BlockName`
- Columns: Specify number of columns to organize blocks
- Block width: Blocks can span multiple columns
- Composite blocks: Nested blocks within parent blocks
- Connections: `Block1 --> Block2` or `Block1 --- Block2`
- Labels: `Block1 -->|Label| Block2`
- Block shapes: rectangle (default), circle, round, diamond, hexagon, square, double-circle, asymmetric, rhombus, parallelogram, trapezoid
- Space blocks: `space` or `space:num` for intentional spacing
- Styling: `style BlockName fill:#color,stroke:#color,stroke-width:2px`

Reference: [Mermaid Block Diagram Documentation](https://mermaid.ai/open-source/syntax/block.html)

### Example (Simple Block Diagram)

```mermaid
block-beta
    a b c
```

### Example (Multi-Column Layout)

```mermaid
block-beta columns 3
    a b c d
```

### Example (Block Spanning Multiple Columns)

```mermaid
block-beta columns 3
    A:1 b:2 c:2 d:1
```

### Example (Composite Blocks - Nested)

```mermaid
block-beta
    A B C
    D
        D E
        D F
```

### Example (Basic Connections)

```mermaid
block-beta
    A B C
    A --> B
    B --> C
```

### Example (Connections with Labels)

```mermaid
block-beta
    A B C
    A -->|Data| B
    B -->|Result| C
```

### Example (Different Block Shapes)

```mermaid
block-beta
    A["Rectangle"]
    B(("Circle"))
    C(["Round"])
    D{"Diamond"}
    E{{"Hexagon"}}
    E1["Square"]
    E2(("Double Circle"))
    E3>"Asymmetric"]
    E4{"Rhombus"}
    E5[/"Parallelogram"/]
    E6[/"Trapezoid"\]
```

### Example (Space Blocks)

```mermaid
block-beta
    A space B
    C space:2 D
```

### Example (System Architecture with Styling)

```mermaid
block-beta
    Frontend Backend Database
    Frontend -->|HTTP| Backend
    Backend -->|Query| Database

    style Frontend fill:#e1f5,stroke:#333,stroke-width:2px
    style Backend fill:#fff4e1,stroke:#333,stroke-width:2px
    style Database fill:#e1f5ff,stroke:#333,stroke-width:2px
```

### Example (Business Process Flow)

```mermaid
block-beta
    Start{"Start"}
    Process1["Process 1"]
    Decision{"Decision?"}
    Process2["Process 2"]
    End["End"]

    Start --> Process1
    Process1 --> Decision
    Decision -->|Yes| Process2
    Decision -->|No| End
    Process2 --> End
```
