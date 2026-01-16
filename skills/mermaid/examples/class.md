## Instructions

Class diagrams represent the structure of a system by showing classes, their attributes, methods, and relationships. In software engineering, a class diagram in the Unified Modeling Language (UML) is a type of static structure diagram that describes the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects.

### Syntax

- Use `classDiagram` keyword
- Class definition: `class ClassName` or via relationship `Vehicle <|-- Car`
- Members: `ClassName : +attribute` or `ClassName { +attribute +method() }`
- Visibility: `+` (Public), `-` (Private), `#` (Protected), `~` (Package/Internal)
- Methods: Identified by `()` parentheses
- Return types: `method() ReturnType` (space between `)` and return type)
- Generic types: `ClassName~Type~` (enclosed in `~` tilde)
- Classifiers: `*` (Abstract), `$` (Static)
- Relationships:
  - `<|--` - Inheritance
  - `*--` - Composition
  - `o--` - Aggregation
  - `-->` - Association
  - `--` - Link (Solid)
  - `..>` - Dependency
  - `..|>` - Realization
  - `..` - Link (Dashed)
- Labels: `ClassA --> ClassB : LabelText`
- Cardinality: `"1" ClassA --> "0..1" ClassB : LabelText`
- Annotations: `<<Interface>>`, `<<Abstract>>`, `<<Service>>`, `<<Enumeration>>`
- Interfaces: `ClassA ..|> InterfaceName` or lollipop syntax
- Namespaces: `namespace NamespaceName { Class1 Class2 }`
- Direction: `direction TB|BT|LR|RL` (default: TB)
- Comments: `%% comment` (on separate line)
- Notes: `note for ClassName "note text"`
- Styling: `style ClassName fill:#color,stroke:#color` or `classDef className fill:#color` and `cssClass "ClassName" className` or `ClassName:::className`

Reference: [Mermaid Class Diagram Documentation](https://mermaid.ai/open-source/syntax/classDiagram.html)

### Example (Basic Class Diagram)

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +eat()
        +sleep()
    }
    class Dog {
        +String breed
        +bark()
    }
    class Cat {
        +meow()
    }

    Animal <|-- Dog
    Animal <|-- Cat
```

### Example (With Visibility and Methods)

```mermaid
classDiagram
    class BankAccount {
        -double balance
        +deposit(amount)
        +withdraw(amount) double
        +getBalance() double
    }
    class Customer {
        +String name
        +String email
        +openAccount() BankAccount
    }

    Customer --> BankAccount : owns
```

### Example (With Return Types)

```mermaid
classDiagram
    class Calculator {
        +add(a, b) int
        +subtract(a, b) int
        +multiply(a, b) int
        +divide(a, b) double
    }
```

### Example (With Generic Types)

```mermaid
classDiagram
    class List~T~ {
        +add(item T)
        +get(index) T
        +size() int
    }
    class Map~K,V~ {
        +put(key K, value V)
        +get(key K) V
    }
```

### Example (With Relationships)

```mermaid
classDiagram
    class Vehicle {
        +String brand
        +start()
    }
    class Car {
        +int doors
    }
    class Engine {
        +int horsepower
    }
    class Wheel {
        +int size
    }

    Vehicle <|-- Car
    Car *-- Engine
    Car o-- Wheel
```

### Example (With Labels and Cardinality)

```mermaid
classDiagram
    class Company {
        +String name
    }
    class Employee {
        +String name
        +String position
    }

    Company "1" --> "1..*" Employee : employs
```

### Example (With Interfaces)

```mermaid
classDiagram
    class Shape {
        <<interface>>
        +area() double
        +perimeter() double
    }
    class Circle {
        +double radius
        +area() double
        +perimeter() double
    }
    class Rectangle {
        +double width
        +double height
        +area() double
        +perimeter() double
    }

    Shape <|.. Circle
    Shape <|.. Rectangle
```

### Example (With Annotations)

```mermaid
classDiagram
    class UserService {
        <<Service>>
        +createUser()
        +deleteUser()
    }
    class AbstractRepository {
        <<Abstract>>
        +save()
        +find()*
    }
    class Status {
        <<Enumeration>>
        ACTIVE
        INACTIVE
        PENDING
    }
```

### Example (With Namespaces)

```mermaid
classDiagram
    namespace Core {
        class User
        class Product
    }
    namespace Services {
        class UserService
        class ProductService
    }

    User --> UserService
    Product --> ProductService
```

### Example (With Direction - Left to Right)

```mermaid
classDiagram
    direction LR
    class Animal {
        +String name
        +eat()
    }
    class Dog {
        +bark()
    }
    Animal <|-- Dog
```

### Example (With Styling)

```mermaid
classDiagram
    class User {
        +String name
        +String email
    }
    class Admin {
        +String role
    }
    User <|-- Admin

    classDef userClass fill:#e1f5ff,stroke:#333,stroke-width:2px
    classDef adminClass fill:#ff6b6b,stroke:#333,stroke-width:3px

    class User userClass
    class Admin adminClass
```

### Example (Complex Class Diagram)

```mermaid
classDiagram
    class Person {
        +String name
        +int age
        +walk()
    }
    class Student {
        +int studentId
        +study()
    }
    class Teacher {
        +String subject
        +teach()
    }
    class Course {
        +String title
        +int credits
    }
    class Enrollment {
        +date enrolledDate
        +String grade
    }

    Person <|-- Student
    Person <|-- Teacher
    Student "1..*" --> "0..*" Course : enrolls
    Course "1" --> "0..*" Enrollment : has
    Student "1" --> "0..*" Enrollment : receives
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If class diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Animal[Animal]
    Dog[Dog]
    Cat[Cat]

    Animal -->|inherits| Dog
    Animal -->|inherits| Cat
```
