## Instructions

Radar diagrams are a simple way to plot low-dimensional data in a circular format. They are also known as radar charts, spider charts, star charts, cobweb charts, polar charts, or Kiviat diagrams. This diagram type is particularly useful for developers, data scientists, and engineers who require a clear and concise way to represent data in a circular format. It is commonly used to graphically summarize and compare the performance of multiple entities across multiple dimensions.

### Syntax

- Use `radar-beta` keyword (requires Mermaid v11.6.0+)
- Title: `title Title of the Radar Diagram` (optional)
- Axis: `axis id1["Label1"]` or `axis id1, id2, id3` (multiple axes in one line)
- Curve: `curve id1["Label1"]{1, 2, 3}` or `curve id1{ axis1: 20, axis2: 30, axis3: 10 }` (key-value pairs)
- Options:
  - `showLegend true/false` - Show or hide legend (default: true)
  - `max value` - Maximum value for scaling (auto-calculated if not provided)
  - `min value` - Minimum value for scaling (default: 0)
  - `graticule circle/polygon` - Type of graticule (default: circle)
  - `ticks number` - Number of concentric circles/polygons (default: 5)

Reference: [Mermaid Radar Diagram Documentation](https://mermaid.ai/open-source/syntax/radar.html)

### Example (Basic Radar Diagram)

```mermaid
radar-beta
    axis Performance, Quality, Speed, Cost
    curve Product A[Product A]{80, 90, 70, 60}
    curve Product B[Product B]{70, 85, 90, 75}
```

### Example (With Title and Options)

```mermaid
radar-beta
    title Performance Comparison
    axis Performance, Quality, Speed, Cost
    curve Product A[Product A]{80, 90, 70, 60}
    curve Product B[Product B]{70, 85, 90, 75}
    showLegend true
    max 100
    min 0
    graticule circle
    ticks 5
```

### Example (Using Key-Value Pairs)

```mermaid
radar-beta
    axis Performance["Performance"], Quality["Quality"], Speed["Speed"], Cost["Cost"]
    curve Product A[Product A]{ Performance: 80, Quality: 90, Speed: 70, Cost: 60 }
    curve Product B[Product B]{ Performance: 70, Quality: 85, Speed: 90, Cost: 75 }
```

### Example (Multiple Curves)

```mermaid
radar-beta
    title Team Skills Assessment
    axis Frontend, Backend, DevOps, Testing, Design
    curve Developer1[Developer 1]{85, 70, 60, 75, 80}
    curve Developer2[Developer 2]{70, 90, 75, 80, 65}
    curve Developer3[Developer 3]{90, 75, 85, 70, 90}
    max 100
    graticule polygon
    ticks 4
```

### Example (Polygon Graticule)

```mermaid
radar-beta
    title Sales Performance
    axis Q1, Q2, Q3, Q4
    curve Region A[Region A]{100, 120, 110, 130}
    curve Region B[Region B]{90, 100, 115, 125}
    graticule polygon
    ticks 6
    max 150
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If radar diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    subgraph Performance["Performance Comparison"]
        A1[Product A: 80]
        A2[Product B: 70]
    end
    subgraph Quality["Quality"]
        B1[Product A: 90]
        B2[Product B: 85]
    end
    subgraph Speed["Speed"]
        C1[Product A: 70]
        C2[Product B: 90]
    end
    subgraph Cost["Cost"]
        D1[Product A: 60]
        D2[Product B: 75]
    end
```
