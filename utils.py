"""
Utility functions for the Hospital Urgency System UI.

This module provides helper functions for console output formatting,
screen management, and patient information display. These utilities
create a consistent and professional user interface experience.

Functions:
    clear_screen(): Clears the terminal screen (cross-platform).
    print_header(title): Prints a centered header with decorative borders.
    print_separator(): Prints a horizontal separator line.
    print_patient_info(patient): Displays formatted patient information.
    print_waiting_queue(queue): Displays the formatted waiting queue.

Example:
    >>> import utils
    >>> utils.print_header("WELCOME")
    >>> print("System ready")
    >>> utils.print_separator()
"""


def clear_screen():
    """
    Clear the console screen in a cross-platform manner.
    
    Uses the appropriate system command based on the operating system:
    - Unix/Linux/MacOS: 'clear'
    - Windows: 'cls'
    
    Time Complexity:
        O(1) - Single system call.
    
    Example:
        >>> import utils
        >>> utils.clear_screen()
        # Terminal screen is cleared
    
    Note:
        This function performs a system call and may not work in all
        environments (e.g., some IDEs' integrated terminals).
    """
    import os
    # Use 'clear' for Unix-like systems, 'cls' for Windows
    os.system('clear' if os.name != 'nt' else 'cls')


def print_header(title):
    """
    Print a formatted header with centered title.
    
    Creates a visually distinct header section with:
    - Top border of equals signs (60 characters)
    - Centered title text
    - Bottom border of equals signs (60 characters)
    
    Args:
        title (str): The text to display in the header.
    
    Example:
        >>> print_header("MAIN MENU")
        
        ============================================================
                              MAIN MENU
        ============================================================
    
    Note:
        Header width is fixed at 60 characters for consistency.
    """
    # Blank line for spacing
    print("\n" + "=" * 60)
    
    # Center title with 2-space left padding, total width 60
    print(f"  {title}".center(60))
    
    # Bottom border
    print("=" * 60)


def print_separator():
    """
    Print a horizontal separator line.
    
    Prints a line of dashes (60 characters) used to visually
    separate sections of output.
    
    Example:
        >>> print_separator()
        ------------------------------------------------------------
    
    Note:
        Separator width matches header width (60 characters).
    """
    print("-" * 60)


def print_patient_info(patient):
    """
    Print formatted patient information.
    
    Displays the patient's name and urgency level in a
    clean, readable format.
    
    Args:
        patient (Patient): The patient object to display.
    
    Example:
        >>> patient = Patient("María García", 1)
        >>> print_patient_info(patient)
        Name: María García
        Urgency Level: 1
    
    Note:
        This displays the numeric urgency level. Use
        patient.get_urgency_name() to display the color code.
    """
    print(f"Name: {patient.name}")
    print(f"Urgency Level: {patient.urgency_level}")


def print_waiting_queue(queue):
    """
    Print the complete waiting queue in formatted layout.
    
    Displays all patients in the queue with:
    - Header section
    - Numbered list of patients
    - Name and urgency level for each
    - Footer separator
    
    Args:
        queue (list): List of Patient objects to display.
    
    Example:
        >>> patients = [Patient("Patient A", 1), Patient("Patient B", 3)]
        >>> print_waiting_queue(patients)
        
        ============================================================
                            WAITING QUEUE
        ============================================================
        1. Patient A - Urgency Level: 1
        2. Patient B - Urgency Level: 3
        ------------------------------------------------------------
    
    Note:
        Queue should be pre-sorted by priority before calling
        this function for correct display order.
    """
    # Display header
    print_header("WAITING QUEUE")
    
    # Iterate through patients with index numbers starting at 1
    for idx, patient in enumerate(queue, start=1):
        # Display patient number, name, and urgency level
        print(f"{idx}. {patient.name} - Urgency Level: {patient.urgency_level}")
    
    # Display footer separator
    print_separator()
