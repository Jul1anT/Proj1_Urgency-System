"""
Main module for the Hospital Urgency System application.

This is the main entry point for the Hospital Urgency System, a console-based
application that simulates a medical triage system. It demonstrates the
practical application of three fundamental data structures:
    - Priority Queue (heapq) for patient ordering by urgency
    - Stack (list) for attendance history tracking
    - Dynamic Array (list) for complete patient registry

The application provides an interactive menu system allowing users to:
    - Register patients with urgency levels (1-5)
    - Attend patients in priority order
    - View waiting queue and attendance history
    - Undo accidental attendances

Modules:
    hospital: Contains Hospital class for patient management
    patient: Contains Patient class with urgency levels
    utils: Contains UI utility functions

Author: Julian T
Date: October 2025
Course: Data Structures
"""

from hospital import Hospital
from patient import Patient
import utils


def display_main_menu():
    """
    Display the main menu with all available system options.
    
    Clears the screen and shows a formatted menu with 6 options:
    1. Register New Patient
    2. Attend Next Patient
    3. View Waiting Queue
    4. View Attended Patients
    5. Undo Last Attendance
    6. Exit
    
    Side Effects:
        Clears the terminal screen and prints formatted menu.
    
    Example:
        >>> display_main_menu()
        # Displays formatted main menu
    """
    utils.clear_screen()
    utils.print_header("HOSPITAL WAITING SYSTEM")
    print("1. Register New Patient")
    print("2. Attend Next Patient")
    print("3. View Waiting Queue")
    print("4. View Attended Patients")
    print("5. Undo Last Attendance")
    print("6. Exit")
    utils.print_separator()


def display_patient_registration_menu():
    """
    Display the patient registration menu with urgency level options.
    
    Shows a formatted menu explaining each urgency level (1-5) with
    color codes and descriptions to help users choose appropriately.
    
    Urgency Levels:
        1 - RED: Life-threatening emergency
        2 - ORANGE: Emergency
        3 - YELLOW: Urgency
        4 - GREEN: Minor urgency
        5 - BLUE: Non-urgent
    
    Side Effects:
        Clears the terminal screen and prints registration menu.
    
    Example:
        >>> display_patient_registration_menu()
        # Displays urgency level selection menu
    """
    utils.clear_screen()
    utils.print_header("REGISTER NEW PATIENT")
    print("Select Patient Urgency Level:")
    print("1. RED: Life-threatening emergency")
    print("2. ORANGE: Emergency")
    print("3. YELLOW: Urgency")
    print("4. GREEN: Minor urgency")
    print("5. BLUE: Non-urgent")
    utils.print_separator()


def register_patient(hospital):
    """
    Handle the patient registration workflow.
    
    Guides the user through registering a new patient by:
    1. Displaying the registration menu
    2. Prompting for urgency level (1-5)
    3. Validating urgency level input
    4. Prompting for patient name
    5. Validating name (non-empty)
    6. Creating Patient object
    7. Adding to hospital system
    8. Displaying confirmation
    
    Args:
        hospital (Hospital): The hospital instance to add the patient to.
    
    User Input:
        urgency_level (int): Must be 1-5
        name (str): Must be non-empty
    
    Validation:
        - Urgency level must be integer 1-5
        - Name must be non-empty string
        - Non-numeric input for urgency is caught
    
    Side Effects:
        - Adds patient to hospital's data structures
        - Prints status messages and confirmations
    
    Example:
        >>> hospital = Hospital()
        >>> register_patient(hospital)
        # User interactive session:
        # Enter urgency level (1-5): 1
        # Enter patient name: María García
        # Patient 'María García' registered successfully!
        # Urgency Level: RED
    """
    display_patient_registration_menu()

    try:
        # Get urgency level from user - must be integer 1-5
        urgency_level = int(input("\nEnter urgency level (1-5): "))
        
        # Validate urgency level is within acceptable range
        if urgency_level not in range(1, 6):
            print("Invalid urgency level! Please enter a number between 1 and 5.")
            return

        # Get patient name and remove leading/trailing whitespace
        name = input("Enter patient name: ").strip()
        
        # Validate name is not empty
        if not name:
            print("Patient name cannot be empty!")
            return

        # Create new Patient object with validated inputs
        patient = Patient(name, urgency_level)
        
        # Add patient to hospital system (priority queue + registry)
        hospital.add_patient(patient)

        # Display success confirmation with urgency color code
        print(f"\nPatient '{name}' registered successfully!")
        print(f"  Urgency Level: {Patient.URGENCY_LEVELS[urgency_level]}")

    except ValueError:
        # Handle non-numeric input for urgency level
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Error registering patient: {e}")


def attend_next_patient(hospital):
    """
    Attend the next highest priority patient in the queue.
    
    Retrieves and attends the patient with the lowest urgency_level
    (highest priority) from the waiting queue. Displays patient
    information or notifies if queue is empty.
    
    Args:
        hospital (Hospital): The hospital instance to attend from.
    
    Side Effects:
        - Removes patient from priority queue
        - Adds patient to attended history stack
        - Prints patient information or empty queue message
    
    Example:
        >>> hospital = Hospital()
        >>> hospital.add_patient(Patient("María", 1))
        >>> attend_next_patient(hospital)
        # Displays:
        # Now attending: María
        # Urgency Level: RED
    """
    utils.print_header("ATTEND NEXT PATIENT")

    # Attempt to attend next patient (returns None if queue empty)
    patient = hospital.attend_patient()
    
    if patient:  # If a patient was successfully attended
        # Display patient information
        print(f"\nNow attending: {patient.name}")
        print(f"  Urgency Level: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
    else:
        # Queue is empty - no patients waiting
        print("\nNo patients in the waiting queue.")

    utils.print_separator()


def view_waiting_queue(hospital):
    """
    Display all patients currently in the waiting queue.
    
    Shows a formatted list of all waiting patients sorted by priority
    (highest priority first). Displays total count and individual
    patient details including name and urgency level.
    
    Args:
        hospital (Hospital): The hospital instance to query.
    
    Display Format:
        - Header section
        - Total patient count
        - Numbered list of patients with urgency colors
        - Footer separator
    
    Time Complexity:
        O(n log n) due to sorting, where n = number of waiting patients.
    
    Example:
        >>> hospital = Hospital()
        >>> hospital.add_patient(Patient("María", 1))
        >>> hospital.add_patient(Patient("Juan", 3))
        >>> view_waiting_queue(hospital)
        # Displays sorted queue with María first (RED), Juan second (YELLOW)
    """
    utils.print_header("WAITING QUEUE")

    # Get sorted copy of waiting patients (highest priority first)
    # Uses Patient.__lt__ for comparison
    queue = sorted(hospital._priority_queue)

    if not queue:  # Check if queue is empty
        print("\nNo patients in the waiting queue.")
    else:
        # Display total count
        print(f"\nTotal patients waiting: {len(queue)}\n")
        
        # Iterate through sorted queue with numbered list
        for idx, patient in enumerate(queue, start=1):
            # Display patient number and name
            print(f"{idx}. {patient.name}")
            
            # Display urgency level with color code
            print(f"   Urgency: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
            
            # Blank line for readability
            print()

    utils.print_separator()


def view_attended_patients(hospital):
    """
    Display all patients who have been attended (history).
    
    Shows the attendance history with most recently attended patients
    first (reverse chronological order). This demonstrates the Stack
    (LIFO) data structure behavior.
    
    Args:
        hospital (Hospital): The hospital instance to query.
    
    Display Format:
        - Header section
        - Total attended count
        - Numbered list (most recent first) with urgency levels
        - Footer separator
    
    Note:
        Patients are displayed in reverse order (LIFO - Last In First Out)
        to show most recent attendances first, typical of stack behavior.
    
    Example:
        >>> hospital = Hospital()
        >>> hospital.add_patient(Patient("First", 1))
        >>> hospital.add_patient(Patient("Second", 2))
        >>> hospital.attend_patient()  # Attends First
        >>> hospital.attend_patient()  # Attends Second
        >>> view_attended_patients(hospital)
        # Displays Second first, then First (reverse order)
    """
    utils.print_header("ATTENDED PATIENTS")

    # Get attended patients stack from hospital
    attended = hospital.get_attended_patients()

    if not attended:
        # No patients have been attended yet
        print("\nNo patients have been attended yet.")
    else:
        # Display total attended count
        print(f"\nTotal patients attended: {len(attended)}\n")
        
        # Iterate in reverse order (LIFO - most recent first)
        for idx, patient in enumerate(reversed(attended), start=1):
            # Display patient number and name
            print(f"{idx}. {patient.name}")
            
            # Display urgency level with color code
            print(f"   Urgency: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
            
            # Blank line for readability
            print()

    utils.print_separator()


def main():
    """
    Main application loop for the Hospital Urgency System.
    
    Initializes the hospital system and runs the interactive menu loop,
    allowing users to manage patients through various operations. Handles
    user input, menu navigation, and graceful error handling.
    
    Menu Options:
        1. Register New Patient - Add patient to system
        2. Attend Next Patient - Process highest priority patient
        3. View Waiting Queue - Display all waiting patients
        4. View Attended Patients - Display attendance history
        5. Undo Last Attendance - Return patient to queue
        6. Exit - Terminate program
    
    Features:
        - Input validation for menu choices
        - Exception handling for errors
        - Keyboard interrupt (Ctrl+C) handling
        - Pause after each operation for user review
    
    Flow:
        1. Initialize Hospital instance
        2. Display welcome message
        3. Loop: Display menu -> Get choice -> Execute action -> Pause
        4. Exit gracefully on user request or interrupt
    
    Example:
        >>> main()
        # Runs interactive hospital management system
    """
    # Initialize hospital with default name
    hospital = Hospital("HOSPITAL URGENCY SYSTEM")
    
    # Not used but available for future enhancements
    queue = hospital.waiting_patients()

    # Display welcome screen
    utils.clear_screen()
    utils.print_header(f"Welcome to {hospital.hospital_name}")

    # Main application loop - runs until user exits
    while True:
        # Display main menu options
        display_main_menu()

        try:
            # Get user's menu choice and remove whitespace
            choice = input("\nEnter your choice (1-6): ").strip()

            # Process user's choice
            if choice == '1':
                # Option 1: Register new patient
                register_patient(hospital)
                
            elif choice == '2':
                # Option 2: Attend next highest priority patient
                attend_next_patient(hospital)
                
            elif choice == '3':
                # Option 3: View all waiting patients
                view_waiting_queue(hospital)
                
            elif choice == '4':
                # Option 4: View attendance history
                view_attended_patients(hospital)
                
            elif choice == '5':
                # Option 5: Undo last attendance (error correction)
                undo_last_attendance = hospital.undo_last_attendance()
                
                if undo_last_attendance:
                    # Successfully undone - patient returned to queue
                    print(f"\nLast attendance undone. Patient '{undo_last_attendance.name}' "
                          f"re-added to the waiting queue.")
                else:
                    # No attended patients to undo
                    print("\nNo attended patients to undo.")
                    
            elif choice == '6':
                # Option 6: Exit program gracefully
                print("\n" + "=" * 60)
                print("Thank you for using Hospital Urgency System!".center(60))
                print("=" * 60 + "\n")
                break  # Exit the while loop
                
            else:
                # Invalid menu choice
                print("\nInvalid choice! Please enter a number between 1 and 6.")

            # Pause to let user review results before returning to menu
            input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully (user interrupt)
            print("\n\nExiting system...")
            break  # Exit the while loop
            
        except Exception as e:
            # Catch any other unexpected errors
            print(f"\nAn error occurred: {e}")
            # Pause before continuing to let user see error
            input("\nPress Enter to continue...")


# Entry point - runs main() if script is executed directly
if __name__ == "__main__":
    main()
