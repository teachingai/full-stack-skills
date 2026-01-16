## Instructions

State diagrams show the different states of an object and the transitions between them, useful for modeling state machines. A state diagram is a type of diagram used in computer science and related fields to describe the behavior of systems. State diagrams require that the system described is composed of a finite number of states; sometimes, this is indeed the case, while at other times this is a reasonable abstraction.

### Syntax

- Use `stateDiagram-v2` (recommended) or `stateDiagram` keyword
- States: `[StateName]` or `state StateName` or `StateId : State Description`
- Initial state: `[*]` (start state)
- Final state: `[*]` (end state)
- Transitions: `State1 --> State2 : Event` or `State1 --> State2`
- Composite states: `state StateName { [State1] [State2] }`
- Choice: `<<choice>>` (decision point)
- Fork/Join: `<<fork>>` and `<<join>>`
- Notes: `note right of StateName : Note text` or `note left of StateName : Note text`
- Concurrency: `--` (parallel states)
- Direction: `direction TB|BT|LR|RL` (default: TB)
- Comments: `%% comment` (on separate line)
- Styling: `classDef className fill:#color,stroke:#color` and `class StateName className` or `StateName:::className`
- Spaces in state names: Define state with id first, then reference it

Reference: [Mermaid State Diagram Documentation](https://mermaid.ai/open-source/syntax/stateDiagram.html)

### Example (Basic State Diagram)

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : Start
    Processing --> Completed : Success
    Processing --> Error : Failure
    Error --> Idle : Retry
    Completed --> [*]
```

### Example (With State Descriptions)

```mermaid
stateDiagram-v2
    [*] --> Still
    Still --> Moving : Start
    Moving --> Still : Stop
    Moving --> Crash : Error
    Crash --> [*]

    state Still {
        [*] --> Stationary
        Stationary --> [*]
    }
```

### Example (With Transitions and Labels)

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Running : Start Event
    Running --> Paused : Pause Event
    Paused --> Running : Resume Event
    Running --> Stopped : Stop Event
    Stopped --> [*]
```

### Example (Composite States)

```mermaid
stateDiagram-v2
    [*] --> First

    state First {
        [*] --> State1
        State1 --> State2
        State2 --> [*]
    }

    First --> Second

    state Second {
        [*] --> State3
        State3 --> State4
        State4 --> [*]
    }

    Second --> [*]
```

### Example (With Choice)

```mermaid
stateDiagram-v2
    [*] --> State1
    State1 --> Choice1 : Event1
    Choice1 --> State2 : Condition1
    Choice1 --> State3 : Condition2
    State2 --> [*]
    State3 --> [*]

    state Choice1 <<choice>>
```

### Example (With Fork and Join)

```mermaid
stateDiagram-v2
    [*] --> Fork1

    state Fork1 <<fork>>
    Fork1 --> State1
    Fork1 --> State2
    Fork1 --> State3

    State1 --> Join1
    State2 --> Join1
    State3 --> Join1

    state Join1 <<join>>
    Join1 --> [*]
```

### Example (With Notes)

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : Start
    Processing --> Completed : Success
    Completed --> [*]

    note right of Processing : This is a critical state
    note left of Idle : Initial state
```

### Example (With Concurrency)

```mermaid
stateDiagram-v2
    [*] --> State1
    State1 --> State2
    State2 --> State3

    State2 --> Parallel1
    State2 --> Parallel2

    Parallel1 --> State4
    Parallel2 --> State5

    State4 --> State3
    State5 --> State3
    State3 --> [*]
```

### Example (With Direction - Left to Right)

```mermaid
stateDiagram-v2
    direction LR
    [*] --> State1
    State1 --> State2 : Event
    State2 --> [*]
```

### Example (With Styling)

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : Start
    Processing --> Error : Failure
    Error --> Idle : Retry
    Processing --> Completed : Success
    Completed --> [*]

    classDef errorState fill:#ff6b6b,stroke:#333,stroke-width:3px
    classDef successState fill:#4ecdc4,stroke:#333,stroke-width:2px

    class Error errorState
    class Completed successState
```

### Example (With Spaces in State Names)

```mermaid
stateDiagram-v2
    [*] --> yswsii
    yswsii --> YetAnotherState

    state yswsii : Your state with spaces in it
    YetAnotherState --> [*]

    classDef spacedState fill:#ffe66d,stroke:#333,stroke-width:2px
    class yswsii spacedState
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If state diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Start([Start]) --> Idle[Idle]
    Idle -->|Start| Processing[Processing]
    Processing -->|Success| Completed[Completed]
    Processing -->|Failure| Error[Error]
    Error -->|Retry| Idle
    Completed --> End([End])
```
