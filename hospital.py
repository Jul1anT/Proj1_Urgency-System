import heapq
from patient import Patient

class Hospital:
    def __init__(self, hospital_name="HOSPITAL URGENCY SYSTEM"):
        self.hospital_name = hospital_name

        # Data Structures
        self._priority_queue = [] # Priority Queue for managing patients by priority
        self._attended_stack = [] # Stack for managing attended patients
        self._all_patients = [] # List for managing all patients

    def add_patient(self, patient):
        heapq.heappush(self._priority_queue, patient)
        self._all_patients.append(patient)

    def attend_patient(self):
        if self._priority_queue:
            patient = heapq.heappop(self._priority_queue)
            self._attended_stack.append(patient)
            return patient
        return None

    def get_attended_patients(self):
        return self._attended_stack

    def get_all_patients(self):
        return self._all_patients



    


