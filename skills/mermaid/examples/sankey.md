## Instructions

Sankey diagrams visualize flow and relationships between entities, showing the magnitude of flows between nodes.

### Syntax

- Use `sankey` keyword (requires Mermaid v10.3.0+, experimental feature 🔥)
- Format: CSV style with exactly **3 columns**: `Source,Target,Value`
- Each line represents one flow: `source,target,value`
- **Empty lines are allowed** (for visual separation, without comma separators)
- Node names with **commas** must be wrapped in quotes: `"Node, Name"`
- Node names with **double quotes** use two quotes: `"He said ""Hello"""`
- Values should be numeric
- Multiple flows can originate from or target the same node
- **Important**: Do NOT use arrow syntax (`-->|Value|`). Use CSV format instead.
- **Important**: If your environment doesn't support sankey, use the flowchart alternative below

Reference: [Mermaid Sankey Documentation](https://mermaid.ai/open-source/syntax/sankey.html)

### Example (Sankey - requires Mermaid v10.3.0+)

```mermaid
sankey
Energy Production,Electricity,100
Energy Production,Heat,30

Electricity,Residential,80
Electricity,Industrial,20

Heat,Residential,25
Heat,Industrial,5
```

### Example with Special Characters

```mermaid
sankey
Source A,Target B,50
"Source, with comma","Target with ""quotes""",30
Source C,Target D,20
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If sankey is not supported, use this flowchart alternative:

```mermaid
flowchart LR
    EP[Energy Production]
    E[Electricity]
    H[Heat]
    R[Residential]
    I[Industrial]

    EP -->|100| E
    EP -->|30| H
    E -->|80| R
    E -->|20| I
    H -->|25| R
    H -->|5| I

    style EP fill:#e1f5ff
    style E fill:#b3e5fc
    style H fill:#b3e5fc
    style R fill:#c8e6c9
    style I fill:#c8e6c9
```
