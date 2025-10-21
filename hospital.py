"""
Hospital management system with three data structures.

Demonstrates practical application of:
    - Priority Queue (heapq): O(log n) patient triage by urgency
    - Stack (list): LIFO attendance history
    - Dynamic Array (list): Complete patient registry
"""

import heapq
from patient import Patient


class Hospital:
    """
    Hospital triage system managing patients by urgency.
    
    Uses three data structures for different purposes:
        _priority_queue: Min-heap for urgent patient ordering
        _attended_stack: LIFO attendance history
        _all_patients: Complete registration record
    """
    
    def __init__(self, hospital_name="HOSPITAL URGENCY SYSTEM"):
        """Initialize hospital with empty data structures."""
        self.hospital_name = hospital_name
        self._priority_queue = []  # Min-heap: O(log n) operations
        self._attended_stack = []  # Stack: LIFO history
        self._all_patients = []    # Registry: never removes patients

    def add_patient(self, patient):
        """
        Register patient in system.
        
        Time Complexity: O(log n) due to heappush.
        """
        heapq.heappush(self._priority_queue, patient)
        self._all_patients.append(patient)

    def waiting_patients(self):
        """Return sorted copy of waiting patients without modifying heap."""
        return sorted(self._priority_queue)

    def attend_patient(self):
        """
        Attend highest priority patient.
        
        Returns None if queue is empty. Time Complexity: O(log n).
        """
        if self._priority_queue:
            patient = heapq.heappop(self._priority_queue)
            self._attended_stack.append(patient)
            return patient
        return None

    def undo_last_attendance(self):
        """
        Return most recently attended patient to queue.
        
        Useful for correcting mistakes. Returns None if no attended patients.
        """
        if self._attended_stack:
            patient = self._attended_stack.pop()
            heapq.heappush(self._priority_queue, patient)
            return patient
        return None

    def get_attended_patients(self):
        """Return list of attended patients in attendance order."""
        return self._attended_stack

    def get_all_patients(self):
        """Return complete registry of all registered patients."""
        return self._all_patients
