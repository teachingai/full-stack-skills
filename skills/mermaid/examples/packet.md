## Instructions

Packet diagrams are visual representations used to illustrate the structure and contents of a network packet. Network packets are the fundamental units of data transferred over a network. This diagram type is particularly useful for developers, network engineers, educators, and students who require a clear and concise way to represent the structure of network packets.

### Syntax

- Use `packet` keyword (requires Mermaid v11.0.0+)
- Title: `title "Packet Title"` (optional)
- Fields:
  - `start-end: "Field Description"` - Multi-bit blocks (e.g., `0-15: "Field Name"`)
  - `start: "Field Description"` - Single-bit block (e.g., `0: "Flag"`)
- Bit Syntax (v11.7.0+): Use `+<count>` to set the number of bits, which starts from the end of the previous field automatically
  - `+1: "Block name"` - Single-bit block
  - `+8: "Block name"` - 8-bit block
  - You can mix and match: `9-15: "Manually set start and end"`
- Ranges: Each line after the title represents a different field in the packet. The range (e.g., `0-15`) indicates the bit positions in the packet.
- Field Description: A brief description of what the field represents, enclosed in quotes.

Reference: [Mermaid Packet Diagram Documentation](https://mermaid.ai/open-source/syntax/packet.html)

### Example (Ethernet Frame - Basic Syntax)

```mermaid
packet
    title "Ethernet Frame"
    0-47: "Destination MAC"
    48-95: "Source MAC"
    96-111: "Type/Length"
    112-: "Payload"
```

### Example (IPv4 Header - Basic Syntax)

```mermaid
packet
    title "IPv4 Header"
    0-3: "Version"
    4-7: "Header Length"
    8-15: "Type of Service"
    16-31: "Total Length"
    32-47: "Identification"
    48-63: "Flags & Fragment Offset"
    64-71: "Time to Live"
    72-79: "Protocol"
    80-95: "Header Checksum"
    96-127: "Source IP Address"
    128-159: "Destination IP Address"
    160-: "Options & Padding"
```

### Example (Using Bit Count Syntax - v11.7.0+)

```mermaid
packet
    title "TCP Header"
    +4: "Source Port"
    +4: "Destination Port"
    +8: "Sequence Number"
    +8: "Acknowledgment Number"
    32-35: "Data Offset"
    +4: "Reserved"
    +6: "Flags"
    +16: "Window Size"
    +16: "Checksum"
    +16: "Urgent Pointer"
```

### Example (Mixed Syntax)

```mermaid
packet
    title "Mixed Syntax Example"
    +8: "First Field (8 bits)"
    8-15: "Second Field (manually set)"
    +4: "Third Field (4 bits, auto-continues from 16)"
    20-31: "Fourth Field (manually set)"
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If packet diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    subgraph Packet["Packet Structure"]
        Field1["0-47: Destination MAC"]
        Field2["48-95: Source MAC"]
        Field3["96-111: Type/Length"]
        Field4["112-: Payload"]
    end
```
