## Instructions

Pie charts display proportional data, showing how parts relate to a whole. A pie chart (or a circle chart) is a circular statistical graphic, which is divided into slices to illustrate numerical proportion. In a pie chart, the arc length of each slice (and consequently its central angle and area), is proportional to the quantity it represents.

### Syntax

- Use `pie` keyword to begin the diagram
- Show data: `showData` (optional) - renders the actual data values after the legend text
- Title: `title "Chart Title"` (optional) - gives a title to the pie chart
- Data format: `"Label" : Value` (quotes around label, colon separator, positive numeric value)
- Values: Must be positive numbers greater than zero (supported up to two decimal places)
- Negative values are not allowed and will result in an error
- Pie slices will be ordered clockwise in the same order as the labels

Reference: [Mermaid Pie Chart Documentation](https://mermaid.ai/open-source/syntax/pie.html)

### Example (Basic Pie Chart)

```mermaid
pie title Sales by Product
    "Product A" : 42.5
    "Product B" : 30.2
    "Product C" : 15.8
    "Product D" : 11.5
```

### Example (With showData)

```mermaid
pie showData title Sales by Product
    "Product A" : 42.5
    "Product B" : 30.2
    "Product C" : 15.8
    "Product D" : 11.5
```

### Example (Budget Allocation)

```mermaid
pie title Budget Allocation
    "Development" : 40
    "Marketing" : 25
    "Operations" : 20
    "Support" : 10
    "Other" : 5
```

### Example (Market Share)

```mermaid
pie title Market Share
    "Company A" : 35.5
    "Company B" : 28.3
    "Company C" : 20.1
    "Company D" : 10.2
    "Others" : 5.9
```

### Example (Team Distribution)

```mermaid
pie showData title Team Distribution
    "Frontend" : 30
    "Backend" : 35
    "DevOps" : 15
    "QA" : 12
    "Design" : 8
```

### Example (Revenue Sources)

```mermaid
pie title Revenue Sources
    "Product Sales" : 55.5
    "Services" : 25.3
    "Subscriptions" : 12.7
    "Licensing" : 4.2
    "Other" : 2.3
```

### Example (With Decimal Values)

```mermaid
pie title Survey Results
    "Very Satisfied" : 45.75
    "Satisfied" : 32.50
    "Neutral" : 12.25
    "Dissatisfied" : 7.50
    "Very Dissatisfied" : 2.00
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If pie charts are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    subgraph Chart["Sales by Product"]
        A[Product A: 42.5%]
        B[Product B: 30.2%]
        C[Product C: 15.8%]
        D[Product D: 11.5%]
    end
```
