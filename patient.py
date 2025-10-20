"""Module defining the Patient class with urgency levels."""

class Patient:

    # Urgency levels constants
    URGENCY_LEVELS = {
        1: "RED",
        2: "ORANGE",
        3: "YELLOW",
        4: "GREEN",
        5: "BLUE"
    }

    def __init__(self, name, urgency_level):
        self.name = name
        self.urgency_level = urgency_level

    def get_urgency_name(self):
        return self.URGENCY_LEVELS.get(self.urgency_level, "UNKNOWN")

    # Comparison methods for priority queue
    def __lt__(self, other):
        return self.urgency_level < other.urgency_level

        