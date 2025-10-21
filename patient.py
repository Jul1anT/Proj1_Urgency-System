"""
Module defining the Patient class with urgency levels.

This module contains the Patient class which represents a patient in the
hospital urgency system. Each patient has a name and an urgency level
that determines their priority in the medical triage system.

Classes:
    Patient: Represents a patient with urgency-based priority.
"""


class Patient:
    """
    Represents a patient in the hospital urgency system.
    
    The Patient class encapsulates patient information and implements
    comparison operators for priority queue ordering. Lower urgency
    levels indicate higher priority (1 = highest, 5 = lowest).
    
    Attributes:
        name (str): The full name of the patient.
        urgency_level (int): Medical urgency level (1-5).
        URGENCY_LEVELS (dict): Class constant mapping levels to color codes.
    
    Constants:
        URGENCY_LEVELS: Dictionary mapping urgency levels to color names:
            1: "RED"    - Life-threatening emergency
            2: "ORANGE" - Emergency
            3: "YELLOW" - Urgency
            4: "GREEN"  - Minor urgency
            5: "BLUE"   - Non-urgent
    
    Example:
        >>> patient = Patient("María García", 1)
        >>> print(patient.get_urgency_name())
        RED
        >>> patient.urgency_level
        1
    """

    # Urgency levels constants - Maps numeric levels to color codes
    # Following standard medical triage color system
    URGENCY_LEVELS = {
        1: "RED",      # Critical/Life-threatening
        2: "ORANGE",   # Emergency
        3: "YELLOW",   # Urgent
        4: "GREEN",    # Semi-urgent
        5: "BLUE"      # Non-urgent
    }

    def __init__(self, name, urgency_level):
        """
        Initialize a new Patient instance.
        
        Args:
            name (str): The patient's full name. Should not be empty.
            urgency_level (int): Urgency level from 1-5, where:
                1 = Highest priority (RED - Life-threatening)
                5 = Lowest priority (BLUE - Non-urgent)
        
        Example:
            >>> patient = Patient("John Doe", 3)
            >>> patient.name
            'John Doe'
            >>> patient.urgency_level
            3
        """
        self.name = name
        self.urgency_level = urgency_level

    def get_urgency_name(self):
        """
        Get the color name corresponding to the patient's urgency level.
        
        Returns:
            str: The urgency color name (RED, ORANGE, YELLOW, GREEN, BLUE),
                 or "UNKNOWN" if the urgency level is invalid.
        
        Example:
            >>> patient = Patient("Ana López", 2)
            >>> patient.get_urgency_name()
            'ORANGE'
        """
        return self.URGENCY_LEVELS.get(self.urgency_level, "UNKNOWN")

    # Comparison methods for priority queue ordering
    
    def __lt__(self, other):
        """
        Less-than comparison operator for priority ordering.
        
        This method enables the Patient class to be used in heapq operations.
        Patients with lower urgency_level values have higher priority.
        
        Args:
            other (Patient): Another Patient instance to compare against.
        
        Returns:
            bool: True if self has higher priority (lower urgency_level)
                  than other, False otherwise.
        
        Note:
            This is used by heapq to maintain the min-heap property.
            Lower urgency_level = Higher priority = Attended first
        
        Example:
            >>> red_patient = Patient("Emergency", 1)
            >>> blue_patient = Patient("Routine", 5)
            >>> red_patient < blue_patient  # RED has higher priority
            True
        """
        return self.urgency_level < other.urgency_level
