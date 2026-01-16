## Instructions

Quadrant charts display items in a 2x2 grid based on two criteria, useful for prioritization and analysis. A quadrant chart is a visual representation of data that is divided into four quadrants. It is used to plot data points on a two-dimensional grid, with one variable represented on the x-axis and another variable represented on the y-axis. The quadrants are determined by dividing the chart into four equal parts based on a set of criteria that is specific to the data being analyzed.

### Syntax

- Use `quadrantChart` keyword
- Title: `title Chart Title` (optional)
- X-axis: `x-axis Left Label --> Right Label` or `x-axis Left Label` (only left)
- Y-axis: `y-axis Bottom Label --> Top Label` or `y-axis Bottom Label` (only bottom)
- Quadrants: `quadrant-1 Label`, `quadrant-2 Label`, `quadrant-3 Label`, `quadrant-4 Label`
  - `quadrant-1`: Top right quadrant
  - `quadrant-2`: Top left quadrant
  - `quadrant-3`: Bottom left quadrant
  - `quadrant-4`: Bottom right quadrant
- Points: `Point Name: [x, y]` where x and y values are in the range 0-1
- Point styling: `Point Name: [x, y] radius: 12, color: #ff3300, stroke-color: #10f0f0, stroke-width: 5px`
- Class styling: `Point Name:::className: [x, y]` with `classDef className color: #109060, radius: 10`

Reference: [Mermaid Quadrant Chart Documentation](https://mermaid.ai/open-source/syntax/quadrantChart.html)

### Example (Basic Quadrant Chart)

```mermaid
quadrantChart
    title Product Prioritization
    x-axis Low Effort --> High Effort
    y-axis Low Impact --> High Impact
    quadrant-1 Should Do
    quadrant-2 Must Do
    quadrant-3 Won't Do
    quadrant-4 Nice to Have
    Feature A: [0.3, 0.8]
    Feature B: [0.7, 0.9]
    Feature C: [0.2, 0.3]
    Feature D: [0.8, 0.2]
```

### Example (With Single Axis Labels)

```mermaid
quadrantChart
    title Risk vs Reward
    x-axis Low Risk
    y-axis Low Reward
    quadrant-1 High Risk, High Reward
    quadrant-2 Low Risk, High Reward
    quadrant-3 Low Risk, Low Reward
    quadrant-4 High Risk, Low Reward
    Investment A: [0.8, 0.9]
    Investment B: [0.2, 0.7]
    Investment C: [0.3, 0.2]
```

### Example (With Point Styling)

```mermaid
quadrantChart
    title Performance vs Cost
    x-axis Low Cost --> High Cost
    y-axis Low Performance --> High Performance
    quadrant-1 High Cost, High Performance
    quadrant-2 Low Cost, High Performance
    quadrant-3 Low Cost, Low Performance
    quadrant-4 High Cost, Low Performance
    Product A: [0.9, 0.0] radius: 12
    Product B: [0.8, 0.1] color: #ff3300, radius: 10
    Product C: [0.7, 0.2] radius: 25, color: #00ff33, stroke-color: #10f0f0
    Product D: [0.6, 0.3] radius: 15, stroke-color: #00ff0f, stroke-width: 5px, color: #ff33f0
```

### Example (With Class Styling)

```mermaid
quadrantChart
    title Feature Analysis
    x-axis Low Priority --> High Priority
    y-axis Low Value --> High Value
    quadrant-1 High Priority, High Value
    quadrant-2 Low Priority, High Value
    quadrant-3 Low Priority, Low Value
    quadrant-4 High Priority, Low Value
    Feature A:::highValue: [0.3, 0.9]
    Feature B:::mediumValue: [0.7, 0.6]
    Feature C:::lowValue: [0.2, 0.2]
    Feature D:::highValue: [0.8, 0.8]

    classDef highValue color: #109060, radius: 10
    classDef mediumValue color: #908342, radius: 8, stroke-color: #310085, stroke-width: 3px
    classDef lowValue color: #f00fff, radius: 6
```

### Example (Business Strategy)

```mermaid
quadrantChart
    title Market Analysis
    x-axis Low Market Share --> High Market Share
    y-axis Low Growth --> High Growth
    quadrant-1 Stars
    quadrant-2 Question Marks
    quadrant-3 Dogs
    quadrant-4 Cash Cows
    Product A: [0.8, 0.9]
    Product B: [0.3, 0.7]
    Product C: [0.2, 0.2]
    Product D: [0.7, 0.3]
```

### Example (Team Skills Assessment)

```mermaid
quadrantChart
    title Team Skills Matrix
    x-axis Low Experience --> High Experience
    y-axis Low Performance --> High Performance
    quadrant-1 High Experience, High Performance
    quadrant-2 Low Experience, High Performance
    quadrant-3 Low Experience, Low Performance
    quadrant-4 High Experience, Low Performance
    Developer A: [0.9, 0.85]
    Developer B: [0.6, 0.9]
    Developer C: [0.3, 0.4]
    Developer D: [0.8, 0.5]
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If quadrant charts are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    subgraph Q1["Quadrant 1<br>High X, High Y"]
        A[Feature A]
    end
    subgraph Q2["Quadrant 2<br>Low X, High Y"]
        B[Feature B]
    end
    subgraph Q3["Quadrant 3<br>Low X, Low Y"]
        C[Feature C]
    end
    subgraph Q4["Quadrant 4<br>High X, Low Y"]
        D[Feature D]
    end
```
