"""
Module for Hospital patient management

This module implements the Hospital class which manages patients using triage system. 
"""

import heapq    # Import heapq for priority queue management

from patient import Patient


class Hospital:
    def __init__(self, hospital_name="HOSPITAL URGENCY SYSTEM"):
        self.hospital_name = hospital_name

        # Data Structures
        self._priority_queue = []  # Priority Queue for managing patients by priority
        self._attended_stack = []  # Stack for managing attended patients
        self._all_patients = []  # List for managing all patients

    def add_patient(self, patient):
        """Methods to manage patients in the hospital."""
        heapq.heappush(self._priority_queue, patient)  # Add to priority queue
        self._all_patients.append(patient)  # Add to all patients list

    def waiting_patients(self):
        """Return sorted copy of waiting patients without modifying heap."""
        return sorted(self._priority_queue)

    def attend_patient(self):
        if self._priority_queue:    # Attend to the highest priority patient
            # Remove from priority queue
            patient = heapq.heappop(self._priority_queue)
            self._attended_stack.append(patient)    # Add to attended stack
            return patient
        return None

    def undo_last_attendance(self):
        if self._attended_stack:    # Undo last attended patient
            patient = self._attended_stack.pop()  # Remove from attended stack
            # Re-add to priority queue
            heapq.heappush(self._priority_queue, patient)
            return patient
        return None

    def get_attended_patients(self):
        return self._attended_stack

    def get_all_patients(self):
        return self._all_patients
