"""
Module for Hospital patient management system.

This module implements the Hospital class which manages patients using a
medical triage system. It utilizes three fundamental data structures to
efficiently handle patient flow:
    - Priority Queue (heapq): For managing waiting patients by urgency
    - Stack (list): For tracking attended patients history (LIFO)
    - Dynamic Array (list): For maintaining complete patient registry

Classes:
    Hospital: Main class for hospital patient management.

Example:
    >>> hospital = Hospital("City Hospital")
    >>> patient = Patient("John Doe", 1)
    >>> hospital.add_patient(patient)
    >>> next_patient = hospital.attend_patient()
"""

import heapq    # Import heapq for efficient priority queue management

from patient import Patient


class Hospital:
    """
    Manages hospital triage system with multiple data structures.
    
    The Hospital class implements a complete patient management system
    using three data structures to demonstrate their practical applications:
    
    1. Priority Queue (_priority_queue): Min-heap for urgent patient ordering
    2. Stack (_attended_stack): LIFO structure for attendance history
    3. Dynamic Array (_all_patients): Complete patient registry
    
    Attributes:
        hospital_name (str): Name of the hospital facility.
        _priority_queue (list): Heap-based priority queue of waiting patients.
        _attended_stack (list): Stack of attended patients (most recent last).
        _all_patients (list): Complete list of all registered patients.
    
    Example:
        >>> hospital = Hospital()
        >>> patient1 = Patient("María", 1)  # RED urgency
        >>> patient2 = Patient("Juan", 3)   # YELLOW urgency
        >>> hospital.add_patient(patient1)
        >>> hospital.add_patient(patient2)
        >>> next_up = hospital.attend_patient()
        >>> print(next_up.name)
        María
    """
    
    def __init__(self, hospital_name="HOSPITAL URGENCY SYSTEM"):
        """
        Initialize a new Hospital instance with empty data structures.
        
        Args:
            hospital_name (str, optional): Name of the hospital.
                Defaults to "HOSPITAL URGENCY SYSTEM".
        
        Example:
            >>> hospital = Hospital("General Hospital")
            >>> hospital.hospital_name
            'General Hospital'
        """
        self.hospital_name = hospital_name

        # Data Structures - Core of the triage system
        
        # Priority Queue: Min-heap for O(log n) insertion and extraction
        # Patients with lower urgency_level (higher priority) are at the front
        self._priority_queue = []
        
        # Stack: LIFO structure for attendance history
        # Most recently attended patient is at the end (top of stack)
        self._attended_stack = []
        
        # Dynamic Array: Complete registry maintaining insertion order
        # Never removes patients - provides historical record
        self._all_patients = []

    def add_patient(self, patient):
        """
        Register a new patient in the hospital system.
        
        Adds the patient to both the priority queue (for triage ordering)
        and the all_patients list (for historical tracking).
        
        Args:
            patient (Patient): The patient object to register.
        
        Time Complexity:
            O(log n) where n is the number of waiting patients.
        
        Side Effects:
            - Adds patient to priority queue (heappush)
            - Adds patient to complete registry (append)
        
        Example:
            >>> hospital = Hospital()
            >>> patient = Patient("Ana López", 2)
            >>> hospital.add_patient(patient)
            >>> len(hospital._priority_queue)
            1
        """
        # Add to priority queue - O(log n) operation
        # heappush maintains min-heap property automatically
        heapq.heappush(self._priority_queue, patient)
        
        # Add to complete patient registry - O(1) operation
        self._all_patients.append(patient)

    def waiting_patients(self):
        """
        Return sorted copy of waiting patients without modifying the heap.
        
        Creates a sorted list of waiting patients for display purposes
        without disturbing the internal heap structure.
        
        Returns:
            list: Sorted list of Patient objects in priority order
                  (highest priority first).
        
        Time Complexity:
            O(n log n) where n is the number of waiting patients.
        
        Note:
            Returns a copy - does not modify the original priority queue.
        
        Example:
            >>> hospital = Hospital()
            >>> hospital.add_patient(Patient("Patient A", 3))
            >>> hospital.add_patient(Patient("Patient B", 1))
            >>> waiting = hospital.waiting_patients()
            >>> waiting[0].urgency_level
            1
        """
        return sorted(self._priority_queue)

    def attend_patient(self):
        """
        Attend the next highest priority patient.
        
        Removes the patient with the highest priority (lowest urgency_level)
        from the waiting queue and adds them to the attended history stack.
        
        Returns:
            Patient: The attended patient object, or None if queue is empty.
        
        Time Complexity:
            O(log n) where n is the number of waiting patients.
        
        Side Effects:
            - Removes patient from priority queue (heappop)
            - Adds patient to attended stack (append)
        
        Example:
            >>> hospital = Hospital()
            >>> hospital.add_patient(Patient("Emergency", 1))
            >>> patient = hospital.attend_patient()
            >>> patient.name
            'Emergency'
            >>> patient = hospital.attend_patient()
            >>> patient is None
            True
        """
        # Check if any patients are waiting
        if self._priority_queue:
            # Remove and return highest priority patient - O(log n)
            # heappop automatically maintains heap property
            patient = heapq.heappop(self._priority_queue)
            
            # Add to attended history stack - O(1)
            # Most recent attendance is at the end (top of stack)
            self._attended_stack.append(patient)
            
            return patient
        
        # Return None if no patients waiting
        return None

    def undo_last_attendance(self):
        """
        Undo the last patient attendance (return patient to queue).
        
        Removes the most recently attended patient from the attended stack
        and returns them to the priority queue. Useful for correcting mistakes.
        
        Returns:
            Patient: The patient returned to queue, or None if no attended
                     patients exist.
        
        Time Complexity:
            O(log n) where n is the number of waiting patients.
        
        Side Effects:
            - Removes patient from attended stack (pop)
            - Re-adds patient to priority queue (heappush)
        
        Example:
            >>> hospital = Hospital()
            >>> hospital.add_patient(Patient("Patient", 1))
            >>> attended = hospital.attend_patient()
            >>> undone = hospital.undo_last_attendance()
            >>> undone.name
            'Patient'
            >>> len(hospital._priority_queue)
            1
        """
        # Check if any patients have been attended
        if self._attended_stack:
            # Remove most recent from stack (LIFO) - O(1)
            patient = self._attended_stack.pop()
            
            # Re-add to priority queue - O(log n)
            heapq.heappush(self._priority_queue, patient)
            
            return patient
        
        # Return None if no attended patients to undo
        return None

    def get_attended_patients(self):
        """
        Get the list of attended patients.
        
        Returns the attended patients stack in attendance order
        (first attended at index 0, most recent at the end).
        
        Returns:
            list: List of attended Patient objects in attendance order.
        
        Time Complexity:
            O(1) - Direct reference return.
        
        Note:
            Returns reference to internal list, not a copy.
        
        Example:
            >>> hospital = Hospital()
            >>> # ... add and attend patients ...
            >>> attended = hospital.get_attended_patients()
            >>> most_recent = attended[-1] if attended else None
        """
        return self._attended_stack

    def get_all_patients(self):
        """
        Get the complete registry of all patients.
        
        Returns all patients ever registered, regardless of whether
        they're waiting or have been attended.
        
        Returns:
            list: List of all registered Patient objects in
                  registration order.
        
        Time Complexity:
            O(1) - Direct reference return.
        
        Note:
            This list is never modified after patients are added,
            providing a complete historical record.
        
        Example:
            >>> hospital = Hospital()
            >>> hospital.add_patient(Patient("Patient 1", 1))
            >>> hospital.add_patient(Patient("Patient 2", 2))
            >>> all_patients = hospital.get_all_patients()
            >>> len(all_patients)
            2
        """
        return self._all_patients
