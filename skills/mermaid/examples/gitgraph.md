## Instructions

Git graphs visualize Git branching structures and commit history, showing how branches diverge and merge. A Git Graph is a pictorial representation of git commits and git actions (commands) on various branches. These diagrams are particularly helpful to developers and devops teams to share their Git branching strategies.

### Syntax

- Use `gitGraph` keyword
- Default branch: `main` (formerly `master`) - initialized automatically
- Commits: `commit id: "message"` or `commit` (auto-generated ID)
- Commit types: `NORMAL` (default), `REVERSE`, `HIGHLIGHT`
- Commit attributes: `id: "custom_id"`, `type: HIGHLIGHT`, `tag: "v1.0"`
- Branches: `branch branchName` (creates and switches to new branch)
- Checkout: `checkout branchName` or `switch branchName` (switches to existing branch)
- Merge: `merge branchName` (merges branch into current branch)
- Cherry-pick: `cherry-pick commitId` (applies commit to current branch)
- Orientation: `LR:` (Left-to-Right, default), `TB:` (Top-to-Bottom), `BT:` (Bottom-to-Top, v11.0.0+)
- Options: `mainBranchName`, `mainBranchOrder`, `parallelCommits`

Reference: [Mermaid GitGraph Documentation](https://mermaid.ai/open-source/syntax/gitgraph.html)

### Example (Basic GitGraph)

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Add feature A"
    commit id: "Add feature B"
```

### Example (With Branches)

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Update README"
    branch develop
    checkout develop
    commit id: "Add feature A"
    commit id: "Add feature B"
    checkout main
    commit id: "Fix bug"
    merge develop
    commit id: "Release v1.0"
```

### Example (With Commit Types)

```mermaid
gitGraph
    commit id: "Initial commit" type: NORMAL
    commit id: "Add feature" type: HIGHLIGHT
    commit id: "Revert change" type: REVERSE
    commit id: "Final commit" type: NORMAL
```

### Example (With Tags)

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Add feature A" tag: "v0.1"
    commit id: "Add feature B"
    commit id: "Release" tag: "v1.0"
```

### Example (Complex Branching)

```mermaid
gitGraph
    commit id: "Initial commit"
    branch develop
    checkout develop
    commit id: "Add feature A"
    branch feature-branch
    checkout feature-branch
    commit id: "Work on feature"
    checkout develop
    commit id: "Add feature B"
    checkout main
    commit id: "Update docs"
    merge develop
    commit id: "Release v1.0"
    checkout feature-branch
    commit id: "Complete feature"
    checkout develop
    merge feature-branch
```

### Example (With Cherry-pick)

```mermaid
gitGraph
    commit id: "Initial commit"
    branch develop
    checkout develop
    commit id: "Add feature A"
    commit id: "Add feature B"
    checkout main
    commit id: "Hotfix"
    cherry-pick "Add feature A"
    commit id: "Release"
```

### Example (Top-to-Bottom Orientation)

```mermaid
gitGraph TB:
    commit id: "Initial commit"
    branch develop
    checkout develop
    commit id: "Add feature A"
    checkout main
    merge develop
```

### Example (Bottom-to-Top Orientation - v11.0.0+)

```mermaid
gitGraph BT:
    commit id: "Initial commit"
    branch develop
    checkout develop
    commit id: "Add feature A"
    checkout main
    merge develop
```

### Example (With Custom Main Branch Name)

```mermaid
gitGraph:
    options:
        mainBranchName: "production"
    commit id: "Initial commit"
    branch develop
    checkout develop
    commit id: "Add feature"
```

### Example (Git Flow Strategy)

```mermaid
gitGraph
    commit id: "Initial commit"
    branch develop
    checkout develop
    commit id: "Setup project"
    branch feature/login
    checkout feature/login
    commit id: "Add login form"
    commit id: "Add validation"
    checkout develop
    merge feature/login
    commit id: "Merge login feature"
    branch release/v1.0
    checkout release/v1.0
    commit id: "Prepare release"
    checkout main
    merge release/v1.0
    commit id: "Release v1.0" tag: "v1.0"
    checkout develop
    merge release/v1.0
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If GitGraph diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    C1[Initial commit] --> C2[Add feature A]
    C2 --> C3[Add feature B]
    C3 --> C4[Release v1.0]
```
