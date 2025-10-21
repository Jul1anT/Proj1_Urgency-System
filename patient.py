"""
Patient class with medical triage urgency levels.

This module implements the Patient entity for a hospital triage system,
where lower urgency numbers indicate higher priority (1=RED, 5=BLUE).
"""


class Patient:
    """
    Patient with urgency-based priority for medical triage.
    
    Attributes:
        name (str): Patient's full name.
        urgency_level (int): Priority level (1-5, lower = higher priority).
    """

    # Medical triage color codes (1=highest priority, 5=lowest)
    URGENCY_LEVELS = {
        1: "RED",      # Life-threatening
        2: "ORANGE",   # Emergency
        3: "YELLOW",   # Urgent
        4: "GREEN",    # Semi-urgent
        5: "BLUE"      # Non-urgent
    }

    def __init__(self, name, urgency_level):
        """Initialize patient with name and urgency level (1-5)."""
        self.name = name
        self.urgency_level = urgency_level

    def get_urgency_name(self):
        """Return color name for urgency level (e.g., 'RED', 'ORANGE')."""
        return self.URGENCY_LEVELS.get(self.urgency_level, "UNKNOWN")

    def __lt__(self, other):
        """
        Compare patients by priority for heap ordering.
        
        Required by heapq - lower urgency_level = higher priority.
        """
        return self.urgency_level < other.urgency_level
