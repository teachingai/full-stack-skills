## Instructions

User journey diagrams visualize the experience of a user as they interact with a system or service, showing different stages and touchpoints. User journeys describe at a high level of detail exactly what steps different users take to complete a specific task within a system, application or website. This technique shows the current (as-is) user workflow, and reveals areas of improvement for the to-be workflow.

### Syntax

- Use `journey` keyword
- Title: `title Title Text` (optional)
- Sections: `section Section Name` (groups steps into stages)
- Steps: `Step Name: Score: Actor1, Actor2`
- Score: Number between 1 and 5 (inclusive) - represents satisfaction level
- Actors: Comma-separated list of actors who perform the step

Reference: [Mermaid User Journey Documentation](https://mermaid.ai/open-source/syntax/userJourney.html)

### Example (Basic User Journey)

```mermaid
journey
    title User Shopping Journey
    section Browse
      Visit Website: 5: User
      Search Products: 4: User
      View Product Details: 5: User
    section Purchase
      Add to Cart: 4: User
      Checkout: 3: User
      Payment: 4: User, Payment System
    section Delivery
      Order Confirmation: 5: System
      Shipping: 4: Logistics
      Receive Product: 5: User
```

### Example (Simple Journey)

```mermaid
journey
    title Daily Workflow
    section Morning
      Wake Up: 3: User
      Breakfast: 4: User
      Commute: 2: User
    section Work
      Check Email: 3: User
      Meetings: 4: User, Team
      Lunch: 5: User
    section Evening
      Exercise: 5: User
      Dinner: 5: User
      Sleep: 4: User
```

### Example (Product Onboarding)

```mermaid
journey
    title New User Onboarding
    section Sign Up
      Create Account: 4: User
      Verify Email: 3: User, System
      Complete Profile: 3: User
    section First Use
      Tutorial: 4: User, System
      First Task: 4: User
      Get Help: 3: User, Support
    section Engagement
      Daily Usage: 5: User
      Share with Friends: 4: User
      Upgrade Plan: 3: User, Sales
```

### Example (Customer Support Journey)

```mermaid
journey
    title Customer Support Experience
    section Issue Discovery
      Notice Problem: 2: Customer
      Search Help: 3: Customer
      Contact Support: 3: Customer
    section Resolution
      Describe Issue: 3: Customer, Support Agent
      Troubleshooting: 4: Customer, Support Agent
      Solution Provided: 5: Support Agent
    section Follow-up
      Issue Resolved: 5: Customer
      Feedback: 4: Customer
      Close Ticket: 5: Support Agent
```

### Example (E-commerce Purchase)

```mermaid
journey
    title Online Shopping Experience
    section Discovery
      Browse Catalog: 5: Customer
      Search Product: 4: Customer
      Compare Options: 4: Customer
    section Decision
      Read Reviews: 5: Customer
      Check Price: 4: Customer
      Add to Wishlist: 4: Customer
    section Purchase
      Add to Cart: 4: Customer
      Apply Discount: 5: Customer
      Checkout: 3: Customer
      Payment: 4: Customer, Payment Gateway
    section Post-Purchase
      Order Confirmation: 5: System
      Track Shipment: 4: Customer
      Receive Product: 5: Customer
      Leave Review: 4: Customer
```

### Example (App Installation)

```mermaid
journey
    title Mobile App Installation
    section Discovery
      Find App: 4: User
      Read Description: 3: User
      Check Reviews: 5: User
    section Installation
      Download: 4: User, App Store
      Install: 3: User, Device
      Open App: 4: User
    section Setup
      Permissions: 2: User, Device
      Account Creation: 3: User
      Initial Configuration: 4: User
    section Usage
      First Use: 4: User
      Explore Features: 5: User
      Regular Usage: 5: User
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If user journey diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Start[Start] --> Browse[Browse Products]
    Browse --> Select[Select Product]
    Select --> Cart[Add to Cart]
    Cart --> Checkout[Checkout]
    Checkout --> Payment[Payment]
    Payment --> Confirm[Order Confirmation]
    Confirm --> End[End]
```
