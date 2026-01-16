## Instructions

Gantt charts display project schedules, showing tasks, their durations, and dependencies over time. A Gantt chart is a type of bar chart that illustrates a project schedule and the amount of time it would take for any one project to finish. Gantt charts illustrate number of days between the start and finish dates of the terminal elements and summary elements of a project.

### Syntax

- Use `gantt` keyword
- Date format: `dateFormat YYYY-MM-DD` (required)
- Title: `title Project Title` (optional)
- Sections: `section Section Name` (required for grouping tasks)
- Tasks: `Task Name :[tags], [taskID], [startDate], [endDate|duration]`
- Tags: `active`, `done`, `crit`, `milestone` (optional, must be first)
- Task metadata syntax:
  - `Task Name :[tags], taskID, startDate, endDate`
  - `Task Name :[tags], taskID, startDate, duration`
  - `Task Name :[tags], taskID, after otherTaskID, endDate`
  - `Task Name :[tags], taskID, after otherTaskID, duration`
  - `Task Name :[tags], startDate, endDate` (no ID)
  - `Task Name :[tags], startDate, duration` (no ID)
  - `Task Name :[tags], after otherTaskID, endDate` (no ID)
  - `Task Name :[tags], endDate` (no ID, sequential)
  - `Task Name :[tags], duration` (no ID, sequential)
- Excludes: `excludes dates` (optional) - excludes specific dates, days, or weekends
- Weekend: `weekend friday` or `weekend saturday` (v11.0.0+, optional)
- Milestones: Use `milestone` tag
- Comments: `%% comment` (on separate line)
- Tick interval: `tickInterval 1day|1week|1month` (v10.3.0+)
- Weekday: `weekday sunday|monday|...` (for week-based intervals)

Reference: [Mermaid Gantt Chart Documentation](https://mermaid.ai/open-source/syntax/gantt.html)

### Example (Basic Gantt Chart)

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section Phase 1
    Design :done, des1, 2024-01-01, 2024-01-15
    Development :active, dev1, 2024-01-16, 2024-02-15
    section Phase 2
    Testing :test1, after dev1, 10d
    Deployment :milestone, deploy1, after test1, 1d
```

### Example (With Task IDs and Dependencies)

```mermaid
gantt
    title Project Schedule
    dateFormat YYYY-MM-DD
    section Design
    Requirements :req1, 2024-01-01, 2024-01-10
    Design Phase :des1, after req1, 2024-01-25
    section Development
    Frontend :front1, after des1, 20d
    Backend :back1, after des1, 25d
    section Testing
    Integration Testing :test1, after front1 back1, 10d
    Deployment :milestone, deploy1, after test1, 1d
```

### Example (With Tags)

```mermaid
gantt
    title Project with Tags
    dateFormat YYYY-MM-DD
    section Tasks
    Completed Task :done, task1, 2024-01-01, 2024-01-10
    Active Task :active, task2, 2024-01-11, 2024-01-25
    Critical Task :crit, task3, 2024-01-26, 2024-02-10
    Milestone :milestone, milestone1, 2024-02-11, 0d
```

### Example (With Excludes)

```mermaid
gantt
    title Project with Exclusions
    dateFormat YYYY-MM-DD
    excludes weekends
    section Development
    Task 1 :task1, 2024-01-01, 10d
    Task 2 :task2, after task1, 10d
```

### Example (With Weekend Configuration)

```mermaid
gantt
    title Project with Custom Weekend
    dateFormat YYYY-MM-DD
    excludes weekends
    weekend friday
    section Development
    Task 1 :task1, 2024-01-01, 10d
    Task 2 :task2, after task1, 10d
```

### Example (With Tick Interval)

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    tickInterval 1week
    weekday monday
    section Phase 1
    Design :des1, 2024-01-01, 2024-01-15
    Development :dev1, after des1, 20d
```

### Example (Sequential Tasks)

```mermaid
gantt
    title Sequential Tasks
    dateFormat YYYY-MM-DD
    section Phase 1
    Task A :2024-01-01, 5d
    Task B :5d
    Task C :10d
    section Phase 2
    Task D :after Task C, 7d
```

### Example (Complex Project)

```mermaid
gantt
    title Software Development Project
    dateFormat YYYY-MM-DD
    excludes weekends
    section Planning
    Requirements Gathering :done, req1, 2024-01-01, 2024-01-10
    System Design :done, des1, after req1, 2024-01-20
    section Development
    Frontend Development :active, front1, after des1, 30d
    Backend Development :active, back1, after des1, 35d
    Database Setup :db1, after des1, 10d
    section Testing
    Unit Testing :test1, after front1 back1, 15d
    Integration Testing :test2, after test1, 10d
    section Deployment
    Production Deployment :milestone, deploy1, after test2, 1d
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If Gantt charts are not supported, use this flowchart alternative:

```mermaid
flowchart LR
    Start[Project Start] --> Phase1[Phase 1: Design]
    Phase1 --> Phase2[Phase 2: Development]
    Phase2 --> Phase3[Phase 3: Testing]
    Phase3 --> End[Deployment]
```
