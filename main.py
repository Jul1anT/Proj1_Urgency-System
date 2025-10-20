""""Main module for the Hospital Urgency System application."""

from hospital import Hospital
from patient import Patient

import utils

def display_main_menu():
    utils.clear_screen()
    utils.print_header("HOSPITAL WAITING SYSTEM")
    print("1. Register New Patient")
    print("2. Attend Next Patient")
    print("3. View Waiting Queue")
    print("4. View Attended Patients")
    print("5. Exit")
    utils.print_separator()
    
def display_patient_registration_menu():
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
    display_patient_registration_menu()
    
    try:
        # Get urgency level and patient name
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
    utils.print_header("ATTEND NEXT PATIENT")
    
    patient = hospital.attend_patient()
    if patient:  # If a patient was attended
        print(f"\nNow attending: {patient.name}")
        print(f"  Urgency Level: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
    else:
        print("\nNo patients in the waiting queue.")
    
    utils.print_separator()

def view_waiting_queue(hospital):
    utils.print_header("WAITING QUEUE")
    
    queue = sorted(hospital._priority_queue)  # Get sorted list of waiting patients

    if not queue:  # If no patients are waiting
        print("\nNo patients in the waiting queue.")
    else:
        print(f"\nTotal patients waiting: {len(queue)}\n")
        for idx, patient in enumerate(queue, start=1):  # Enumerate patients
            print(f"{idx}. {patient.name}")
            print(f"   Urgency: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
            print()
    
    utils.print_separator()

def view_attended_patients(hospital):
    utils.print_header("ATTENDED PATIENTS")
    
    attended = hospital.get_attended_patients()
    
    if not attended:
        print("\nNo patients have been attended yet.")
    else:
        print(f"\nTotal patients attended: {len(attended)}\n")
        for idx, patient in enumerate(reversed(attended), start=1):
            print(f"{idx}. {patient.name}")
            print(f"   Urgency: {Patient.URGENCY_LEVELS[patient.urgency_level]}")
            print()
    
    utils.print_separator()

def main():
    hospital = Hospital("HOSPITAL URGENCY SYSTEM")

    utils.clear_screen()
    utils.print_header(f"Welcome to {hospital.hospital_name}")
    
    # Main application loop
    while True:
        display_main_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                register_patient(hospital)
            elif choice == '2':
                attend_next_patient(hospital)
            elif choice == '3':
                view_waiting_queue(hospital)
            elif choice == '4':
                view_attended_patients(hospital)
            elif choice == '5':
                print("\n" + "=" * 60)
                print("Thank you for using Hospital Urgency System!".center(60))
                print("=" * 60 + "\n")
                break
            else:
                print("\nInvalid choice! Please enter a number between 1 and 5.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:  # Handle Ctrl+C gracefully
            print("\n\nExiting system...")
            break
        except Exception as e:  # Handle other exceptions
            print(f"\nAn error occurred: {e}")
            input("\nPress Enter to continue...")

# Run the main application
if __name__ == "__main__":
    main()


