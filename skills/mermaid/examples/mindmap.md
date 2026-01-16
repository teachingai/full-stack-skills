## Instructions

Mindmaps visualize hierarchical information, showing relationships between concepts in a tree-like structure. A mind map is a diagram used to visually organize information into a hierarchy, showing relationships among pieces of the whole. It is often created around a single concept, drawn as an image in the center of a blank page, to which associated representations of ideas such as images, words and parts of words are added.

**Note**: This is an experimental diagram type. The syntax and properties can change in future releases. The syntax is stable except for the icon integration which is the experimental part.

### Syntax

- Use `mindmap` keyword
- Root: `root((Root Node))` or just `Root` (text at root level)
- Nodes: Defined by indentation (spaces or tabs determine hierarchy)
- Shapes: Similar to flowchart nodes:
  - Square: `id["Label"]`
  - Rounded square: `id("Label")`
  - Circle: `id(("Label"))`
  - Bang: `id))Label((`
  - Cloud: `id))Label(("
  - Hexagon: `id{{"Label"}}`
  - Default: Just text (no shape delimiters)
- Icons: `::icon(fa:fa-icon-name)` (experimental, requires icon fonts)
- Classes: `:::class1 class2` (triple colon followed by CSS classes)
- Markdown strings: Supports **bold** and *italics*, auto-wraps text

Reference: [Mermaid Mindmap Documentation](https://mermaid.ai/open-source/syntax/mindmap.html)

### Example (Basic Mindmap)

```mermaid
mindmap
    root((Mermaid))
        Flowcharts
            Basic Flowchart
            Subgraph
            Styling
        Sequence Diagrams
            Participants
            Messages
            Activations
        Class Diagrams
            Classes
            Relationships
            Interfaces
        Other Diagrams
            State Diagrams
            ER Diagrams
            Gantt Charts
```

### Example (With Different Shapes)

```mermaid
mindmap
    root((Project))
        Planning["Planning"]
            Requirements("Requirements")
            Design(("Design"))
            Timeline))Timeline((
        Development{{"Development"}}
            Frontend
            Backend
            Database
        Testing
            Unit Tests
            Integration Tests
```

### Example (With Markdown Formatting)

```mermaid
mindmap
    root((**Mermaid**))
        *Flowcharts*
            **Basic** Flowchart
            *Subgraph*
            Styling
        Sequence Diagrams
            **Participants**
            Messages
            *Activations*
```

### Example (Simple Hierarchy)

```mermaid
mindmap
    Root
        A
            B
            C
        D
            E
            F
```

### Example (Technology Stack)

```mermaid
mindmap
    root((Tech Stack))
        Frontend
            React
            Vue
            Angular
        Backend
            Node.js
            Python
            Java
        Database
            PostgreSQL
            MongoDB
            Redis
        DevOps
            Docker
            Kubernetes
            CI/CD
```

### Example (Project Planning)

```mermaid
mindmap
    root((Project))
        Planning
            Requirements
            Design
            Timeline
        Development
            Frontend
            Backend
            Testing
        Deployment
            Staging
            Production
            Monitoring
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If mindmap diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Root((Root))
    A[Node A]
    B[Node B]
    C[Node C]
    D[Node D]

    Root --> A
    Root --> B
    A --> C
    A --> D
```
