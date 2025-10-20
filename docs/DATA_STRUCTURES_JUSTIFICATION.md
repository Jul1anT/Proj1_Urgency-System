# Data Structures Justification

## 1. Priority Queue (heap-based Min-Heap)

### Chosen Data Strcture: **Binary Min-Heap (heapq)**

- **Medical triage** 
Requieres constant-time acces to the **highest-priority** patient while efficiently managing dynamic additions to the queue

- **Time Complexity**
    - Insertion (register patient: O(log n))
    - Removal (attend patient): O(log n)
    - Peek highest priority: O(1)

- **Space Complexity**
    O(n) where n is number of waiting patients

### Alternatives Considered:
- Sorted Array: Slow for insertion

### Uses Cases Demostrated:

Hospital emergency departments use priority queues (implemented as heaps) in their triage software because:

- Patients arrive unpredictably (dynamic insertions)
- Critical patients must be seen immediately
- System must scale to hundreds of patients

### Notes

Python's `heapq` implements a binary min-heap where the element with the lowest value has highest priority. Since lower urgency numbers higher priority (1-5), this naturally aligns with medical triage logic

- - -

## 2. Stack (Python List with LIFO Operations)

### Chosen Data Strcture: **Dynamic Array with Stack Operations**

- **Tracking recently attended patients** 
Requieres **Last-In-First-Out** access to support undo operations and recent history review.

- **Time Complexity**
    - Push (add attended patient): O(1)
    - Pop (undo last attendance): O(1)
    - Peek top: O(1)

- **Space Complexity**
    O(m) where m is number of attended patients

### Alternatives Considered:
- Queue: Use FIFO, which is not ideal for attender urgency room triage.

### Uses Cases Demostrated:

1. History Tracking
2. Undo Funtionality
3. Audit Trail

- - - 

## 3. Dynamic Array (Python List)

### Chosen Data Strcture: **Python List (Dynamic Array)**

- **Patient registry** 
Requieres **dynamic growth**, also needed for analytics and reporting.

- **Time Complexity**
    - Append: O(1) amortized
    - Access by index: O(1)
    - Interaction: O(n)

- **Space Complexity**
    O(n) total patients.

### Alternatives Considered:
- Heap: because this is not most suitable one for logs process 

### Uses Cases Demostrated:

- Statistical Analysis
- Historical Records
- Reporting

### Notes

Python lists are implemented as dynamic arrays with geometric growth (typically 1.125x when full). This is recomended for a continuosly growing patient registry. [mortized O(1)].

- - -

# Data Structures Justification

## 1. Priority Queue (heapq-based Min-Heap)

### Chosen Data Structure: **Binary Min-Heap (via `heapq`)**

### Why This Structure?

Medical triage requires **constant-time access to the highest-priority patient** while efficiently managing dynamic additions to the queue.

### Technical Justification:

- **Time Complexity:**
  - Insertion (register patient): O(log n)
  - Removal (attend patient): O(log n)
  - Peek highest priority: O(1)

- **Space Complexity:** O(n) where n is number of waiting patients

### Alternatives Considered:

| Data Structure | Insert | Remove Min | Why Not Chosen |
|----------------|--------|------------|----------------|
| Sorted Array   | O(n)   | O(1)       | Too slow for insertions |
| Unsorted Array | O(1)   | O(n)       | Too slow to find minimum |
| Balanced BST   | O(log n) | O(log n) | Unnecessary complexity, no key-value needs |

### Real-World Application:

Hospital emergency departments use priority queues (implemented as heaps) in their triage software because:
- Patients arrive unpredictably (dynamic insertions)
- Critical patients must be seen immediately
- System must scale to hundreds of patients

### Implementation Detail:

Python's `heapq` implements a binary min-heap where the element with the **lowest value** has highest priority. Since lower urgency numbers represent higher priority (1=RED, 5=BLUE), this naturally aligns with medical triage logic.

---

## 2. Stack (Python List with LIFO Operations)

### Chosen Data Structure: **Dynamic Array with Stack Operations**

### Why This Structure?

Tracking recently attended patients requires **Last-In-First-Out** access to support undo operations and recent history review.

### Technical Justification:

- **Time Complexity:**
  - Push (add attended patient): O(1)
  - Pop (undo last attendance): O(1)
  - Peek top: O(1)

- **Space Complexity:** O(m) where m is number of attended patients

### Use Cases Demonstrated:

1. **History Tracking:** View most recently attended patients first
2. **Undo Functionality:** Return last attended patient to waiting queue
3. **Audit Trail:** Maintain order of patient service

### Why Not a Queue?

A queue (FIFO) would show oldest attended patients first, which is less useful for:
- Reviewing recent decisions
- Implementing undo functionality
- Quick access to last patient attended

---

## 3. Dynamic Array (Python List)

### Chosen Data Structure: **Python List (Dynamic Array)**

### Why This Structure?

Complete patient registry requires **efficient random access** and **dynamic growth** for analytics and reporting.

### Technical Justification:

- **Time Complexity:**
  - Append: O(1) amortized
  - Access by index: O(1)
  - Iteration: O(n)

- **Space Complexity:** O(n) total patients

### Use Cases:

1. **Statistical Analysis:** Calculate urgency distributions (requires iteration over all patients)
2. **Historical Records:** Maintain complete patient database
3. **Reporting:** Generate summaries without modifying queue/stack

### Implementation Note:

Python lists are implemented as dynamic arrays with geometric growth (typically 1.125x when full), providing amortized O(1) append operations. This is perfect for a continuously growing patient registry.

---

## Data Structure Interaction Diagram
```
┌─────────────────────┐
│  Patient Arrives    │
└──────────┬──────────┘
           │
           ↓
    ┌──────────────┐
    │ Add to Array │ ←── Complete Registry
    │  O(1) append │
    └──────┬───────┘
           │
           ↓
  ┌────────────────────┐
  │ Push to Priority Q │ ←── Waiting Queue
  │   O(log n) insert  │
  └────────┬───────────┘
           │
           ↓
      [Wait for Turn]
           │
           ↓
  ┌────────────────────┐
  │ Pop from Priority Q│ ←── Attend Highest Priority
  │   O(log n) remove  │
  └────────┬───────────┘
           │
           ↓
   ┌───────────────┐
   │ Push to Stack │ ←── Attended History
   │  O(1) push    │
   └───────────────┘
```
