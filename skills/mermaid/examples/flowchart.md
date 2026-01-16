## Instructions

Flowcharts are composed of nodes (geometric shapes) and edges (arrows or lines). The Mermaid code defines how nodes and edges are made and accommodates different arrow types, multi-directional arrows, and any linking to and from subgraphs.

### Syntax

- Use `flowchart` or `graph` keyword
- Direction: `TD`/`TB` (Top to Bottom), `BT` (Bottom to Top), `RL` (Right to Left), `LR` (Left to Right)
- Node shapes:
  - Default: `A` or `A["Text"]`
  - Round edges: `A("Text")`
  - Stadium: `A(["Text"])`
  - Subroutine: `A[["Text"]]`
  - Cylindrical: `A[("Text")]`
  - Circle: `A(("Text"))`
  - Asymmetric: `A>"Text"]`
  - Rhombus: `A{"Text"}`
  - Hexagon: `A{{"Text"}}`
  - Parallelogram: `A[/"Text"/]` or `A[\"Text"/]`
  - Parallelogram alt: `A[/"Text"\]` or `A[\"Text"\`
  - Trapezoid: `A[/"Text"\]` or `A[\"Text"\`
  - Trapezoid alt: `A[/"Text"/]` or `A[\"Text"/]`
  - Double circle: `A((("Text")))`
  - New shapes (v11.3.0+): `A@{ shape: shapeName }` (e.g., `bang`, `cloud`, `diamond`, `cylinder`, etc.)
- Edges:
  - `A --> B` - Arrow with arrowhead
  - `A --- B` - Open link
  - `A -->|label| B` - Link with label
  - `A -.-> B` - Dotted link
  - `A -.->|label| B` - Dotted link with label
  - `A ==> B` - Thick link
  - `A ==|label|==> B` - Thick link with label
- Subgraphs: `subgraph id ["Title"] ... end`
- Styling: `style A fill:#color,stroke:#color` or `classDef className fill:#color` and `class A className` or `A:::className`
- Links: `linkStyle 0 stroke:#color` (0-based index)
- Comments: `%% comment` (on separate line)
- FontAwesome icons: `A[fa:fa-icon-name]`
- Custom icons: `A[fak:fa-custom-icon-name]` (requires FontAwesome kit)
- Click events: `click A callback "tooltip"` or `click A href "url" "tooltip"`
- Line curves: `curve: basis|bumpX|bumpY|cardinal|catmullRom|linear|monotoneX|monotoneY|natural|step|stepAfter|stepBefore`
- Edge IDs (v11.10.0+): `A -->|label|e1[ID] B` then `e1.curve = "stepBefore"`

**Warnings:**
- If using "end" in a node, capitalize it (e.g., "End" or "END")
- If using "o" or "x" as first letter, add space or capitalize (e.g., "dev--- ops" or "dev---Ops")

Reference: [Mermaid Flowchart Documentation](https://mermaid.ai/open-source/syntax/flowchart.html)

### Example (Basic Flowchart)

```mermaid
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Process]
    B -->|No| D[End]
    C --> D
```

### Example (With Different Directions)

```mermaid
flowchart LR
    A[Start] --> B[Process] --> C[End]
```

### Example (With Node Shapes)

```mermaid
flowchart TD
    A[Rectangle]
    B("Rounded")
    C(["Stadium"])
    D[["Subroutine"]]
    E[("Cylindrical")]
    F(("Circle"))
    G>"Asymmetric"]
    H{"Diamond"}
    I{{"Hexagon"}}
    J[/"Parallelogram"/]
    K[\"Parallelogram Alt"\]
    L[/"Trapezoid"\]
    M[\"Trapezoid Alt"/]
    N((("Double Circle")))
```

### Example (With Labels on Edges)

```mermaid
flowchart TD
    A[Start] -->|Step 1| B[Process 1]
    B -->|Step 2| C[Process 2]
    C -->|Step 3| D[End]
```

### Example (With Subgraphs)

```mermaid
flowchart TD
    A[Start] --> B[Process]
    B --> C[End]

    subgraph SG1 ["Subgraph 1"]
        D[Node D]
        E[Node E]
        D --> E
    end

    subgraph SG2 ["Subgraph 2"]
        F[Node F]
        G[Node G]
        F --> G
    end

    B --> D
    E --> F
    G --> C
```

### Example (With Styling)

```mermaid
flowchart TD
    A[Start] --> B[Process]
    B --> C[End]

    style A fill:#e1f5,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
```

### Example (With Class Definitions)

```mermaid
flowchart TD
    A[Start] --> B[Process]
    B --> C[End]

    classDef startEnd fill:#e1f5,stroke:#333,stroke-width:2px
    classDef process fill:#bbf,stroke:#333,stroke-width:2px

    class A,C startEnd
    class B process
```

### Example (With Class Shorthand)

```mermaid
flowchart TD
    A[Start]:::startClass --> B[Process]:::processClass
    B --> C[End]:::endClass

    classDef startClass fill:#e1f5,stroke:#333
    classDef processClass fill:#bbf,stroke:#333
    classDef endClass fill:#bfb,stroke:#333
```

### Example (With Dotted Links)

```mermaid
flowchart TD
    A[Start] --> B[Process]
    A -.-> C[Alternative]
    B -.->|Optional| D[End]
    C -.-> D
```

### Example (With Thick Links)

```mermaid
flowchart TD
    A[Start] ==> B[Important Process]
    B ==>|Critical| C[End]
```

### Example (With FontAwesome Icons)

```mermaid
flowchart TD
    A[fa:fa-user Start]
    B[fa:fa-cog Process]
    C[fa:fa-check End]

    A --> B --> C
```

### Example (Complex Flowchart)

```mermaid
flowchart TD
    Start([Start]) --> Input{Input Data?}
    Input -->|Yes| Validate[Validate Data]
    Input -->|No| End([End])

    Validate --> Check{Valid?}
    Check -->|Yes| Process[Process Data]
    Check -->|No| Error[Error Handler]

    Process --> Save[Save Results]
    Save --> End
    Error --> End

    style Start fill:#e1f5,stroke:#333
    style End fill:#e1f5,stroke:#333
    style Process fill:#bbf,stroke:#333
    style Error fill:#fbb,stroke:#333
```

### Example (With Multiple Paths)

```mermaid
flowchart TD
    A[Start] --> B{Decision 1}
    B -->|Path 1| C[Process 1]
    B -->|Path 2| D[Process 2]
    B -->|Path 3| E[Process 3]

    C --> F[Converge]
    D --> F
    E --> F
    F --> G[End]
```

### Example (With Comments)

```mermaid
flowchart TD
    A[Start] --> B[Process]
    %% This is a comment
    B --> C[End]
```

### Example (With Edge Styling)

```mermaid
flowchart TD
    A[Start] --> B[Process 1]
    B --> C[Process 2]
    C --> D[End]

    linkStyle 0 stroke:#ff3,stroke-width:4px
    linkStyle 1 stroke:#3f3,stroke-width:2px
    linkStyle 2 stroke:#33f,stroke-width:3px
```

### Example (With New Shapes - v11.3.0+)

```mermaid
flowchart TD
    A@{ shape: cloud, label: "Cloud" }
    B@{ shape: diam, label: "Decision" }
    C@{ shape: cyl, label: "Database" }
    D@{ shape: bang, label: "Event" }

    A --> B
    B --> C
    C --> D
```

### Example (With Edge IDs and Curve Styles - v11.10.0+)

```mermaid
flowchart LR
    A[Start]
    B[Process]
    C[End]
    A -->|Step 1|e1[ID] B
    B -->|Step 2|e2[ID] C

    e1.curve = "stepBefore"
    e2.curve = "stepAfter"
```
