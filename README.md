# Hospital Urgency System �

## Project Overview

This program simulates a hospital emergency triage system where patients are managed through priority queues based on medical urgency levels, with complete tracking of attended patients.

### **Data Structures Implemented**

1. **Priority Queue (heapq)** - Manages waiting patients by medical urgency:
   - 🔴 **RED** - Life-threatening emergency (Highest Priority - Level 1)
   - 🟠 **ORANGE** - Emergency (High Priority - Level 2)
   - 🟡 **YELLOW** - Urgency (Medium Priority - Level 3)
   - 🟢 **GREEN** - Minor urgency (Low Priority - Level 4)
   - 🔵 **BLUE** - Non-urgent (Lowest Priority - Level 5)

2. **Stack (list)** - Stores history of attended patients (LIFO - Last In First Out)

3. **Dynamic Array (list)** - Maintains complete registry of all patients

---

## 📋 Menu Options

### 1. **Register New Patient**
- Add a new patient to the hospital system
- Choose urgency level (1-5):
  - **1 - RED**: Life-threatening emergency
  - **2 - ORANGE**: Emergency
  - **3 - YELLOW**: Urgency
  - **4 - GREEN**: Minor urgency
  - **5 - BLUE**: Non-urgent
- Enter patient name
- Added to priority queue based on urgency level

### 2. **Attend Next Patient**
- Calls the next patient from the priority queue
- Highest urgency patients (RED) are attended first
- Lower urgency levels attended in order
- Displays patient name and urgency level
- Moves attended patient to history stack

### 3. **View Waiting Queue**
- Displays all patients currently waiting
- Organized by urgency level (sorted)
- Shows patient names and their urgency levels
- Total count of waiting patients

### 4. **View Attended Patients**
- Displays recently attended patients from the stack
- Shows most recent first (LIFO order)
- Displays patient name and urgency level
- Total count of attended patients

### 5. **Exit**
- Displays farewell message
- Safely exits the system

---

## Key Features

- Medical Triage Priority Management
- Professional Interface
- Robust Implementation

---

## Project Structure

```
Proj1_Urgency-System/
│
├── main.py          # Main program with menu system
├── hospital.py      # Hospital class with data structures
├── patient.py       # Patient class definition
├── utils.py         # Helper functions and formatting
└── _README.md       # This file
```

---

## Example Usage

### Typical Workflow

1. **Start the program**
   ```bash
   python3 main.py
   ```

2. **Register some patients**
   - Add urgency level 1 (RED): "María García" - Heart attack
   - Add urgency level 5 (BLUE): "Juan Pérez" - Minor cold
   - Add urgency level 2 (ORANGE): "Ana López" - Broken bone

3. **View the waiting queue (Option 3)**
   ```
   WAITING QUEUE
   Total patients waiting: 3
   
   1. María García
      Urgency: RED
   
   2. Ana López
      Urgency: ORANGE
   
   3. Juan Pérez
      Urgency: BLUE
   ```

4. **Attend patients (Option 2)**
   - María is attended first (RED - highest priority)
   - Ana is attended second (ORANGE)
   - Juan is attended last (BLUE - lowest priority)

5. **Check attended history (Option 4)**
   - View recently attended patients in reverse order (stack)
   - Juan appears first (most recent)
   - Ana second
   - María last (first attended)

---

## Technical Details

### Priority Queue Implementation
Uses Python's `heapq` module:
- `heappush()` - O(log n) insertion
- `heappop()` - O(log n) removal
- Automatically maintains min-heap property

### Stack Implementation
Uses Python list:
- `append()` - O(1) push
- `[-n:]` slicing - O(k) access to last k elements
- Maintains insertion order

### Time Complexity
- Register patient: O(log n)
- Attend patient: O(log n)
- View queues: O(n)
- View history: O(1) to O(k)
- Statistics: O(n)

---

## Notes

- The system uses medical triage urgency levels (1-5)
- Priority queue ensures critical patients are seen first
- The system maintains data in memory (not persisted to disk)
- Can be extended with:
  - Time tracking for waiting times
  - Shift management
  - Database integration
  - GUI interface
  - Statistics and analytics

---

## ✅ Requirements Met

- ✅ Three linear data structures (Priority Queue, Stack, Dynamic Array)
- ✅ Text-based interactive interface
- ✅ Complete menu system with 5 options
- ✅ Patient attributes (name, urgency_level)
- ✅ Realistic medical triage flow simulation
- ✅ Object-oriented design
- ✅ Modular, clean code
- ✅ Professional documentation
- ✅ Input validation and error handling
