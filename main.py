"""
Hospital Urgency System - Medical triage application.

Console-based triage system demonstrating three data structures:
    - Priority Queue (heapq): O(log n) patient ordering by urgency
    - Stack (list): LIFO attendance history
    - Dynamic Array (list): Complete patient registry
"""

from hospital import Hospital
from patient import Patient
import utils


def display_main_menu():
    """Display main menu with all system options."""
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
    """Display urgency level selection menu for patient registration."""
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
    Handle patient registration with input validation.

    Validates urgency level (1-5) and non-empty name before
    adding patient to hospital system.
    """
    display_patient_registration_menu()

    try:
        urgency_level = int(input("\nEnter urgency level (1-5): "))

        if urgency_level not in range(1, 6):
            print("Invalid urgency level! Please enter a number between 1 and 5.")
            return

        name = input("Enter patient name: ").strip()
        if not name:
            print("Patient name cannot be empty!")
            return

        patient = Patient(name, urgency_level)
        hospital.add_patient(patient)

        print(f"\nPatient '{name}' registered successfully!")
        print(f"  Urgency Level: {Patient.URGENCY_LEVELS[urgency_level]}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"Error registering patient: {e}")


def attend_next_patient(hospital):
    """Attend highest priority patient from queue."""
    utils.print_header("ATTEND NEXT PATIENT")

    patient = hospital.attend_patient()

    if patient:
        print(f"\nNow attending: {patient.name}")
        print(
            f"  Urgency Level: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
    else:
        print("\nNo patients in the waiting queue.")

    utils.print_separator()


def view_waiting_queue(hospital):
    """Display all waiting patients sorted by priority."""
    utils.print_header("WAITING QUEUE")

    queue = sorted(hospital._priority_queue)

    if not queue:
        print("\nNo patients in the waiting queue.")
    else:
        print(f"\nTotal patients waiting: {len(queue)}\n")
        for idx, patient in enumerate(queue, start=1):
            print(f"{idx}. {patient.name}")
            print(
                f"   Urgency: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
            print()

    utils.print_separator()


def view_attended_patients(hospital):
    """Display attendance history (most recent first - LIFO)."""
    utils.print_header("ATTENDED PATIENTS")

    attended = hospital.get_attended_patients()

    if not attended:
        print("\nNo patients have been attended yet.")
    else:
        print(f"\nTotal patients attended: {len(attended)}\n")
        # Reverse order to show most recent first (stack behavior)
        for idx, patient in enumerate(reversed(attended), start=1):
            print(f"{idx}. {patient.name}")
            print(
                f"   Urgency: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
            print()

    utils.print_separator()


def main():
    """
    Main application loop.

    Runs interactive menu system with error handling for invalid
    input and keyboard interrupts (Ctrl+C).
    """
    hospital = Hospital("HOSPITAL URGENCY SYSTEM")

    utils.clear_screen()
    utils.print_header(f"Welcome to {hospital.hospital_name}")

    while True:
        display_main_menu()

        try:
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == '1':
                register_patient(hospital)

            elif choice == '2':
                attend_next_patient(hospital)

            elif choice == '3':
                view_waiting_queue(hospital)

            elif choice == '4':
                view_attended_patients(hospital)

            elif choice == '5':
                # Undo feature: return last attended patient to queue
                undone = hospital.undo_last_attendance()
                if undone:
                    print(f"\nLast attendance undone. Patient '{undone.name}' "
                          f"re-added to the waiting queue.")
                else:
                    print("\nNo attended patients to undo.")

            elif choice == '6':
                print("\n" + "=" * 60)
                print("Thank you for using Hospital Urgency System!".center(60))
                print("=" * 60 + "\n")
                break

            else:
                print("\nInvalid choice! Please enter a number between 1 and 6.")

            input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            print("\n\nExiting system...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
