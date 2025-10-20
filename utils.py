"""Utility functions for displaying information in the urgency system."""


def clear_screen():  # Clear the console screen
    import os
    os.system('clear' if os.name != 'nt' else 'cls')


def print_header(title):  # Print a formatted header
    print("\n" + "=" * 60)
    print(f"  {title}".center(60))
    print("=" * 60)


def print_separator():  # Print a separator line
    print("-" * 60)


def print_patient_info(patient):  # Print patient information
    print(f"Name: {patient.name}")
    print(f"Urgency Level: {patient.urgency_level}")


def print_waiting_queue(queue):  # Print waiting queue information
    print_header("WAITING QUEUE")
    for idx, patient in enumerate(queue, start=1):  # Enumerate patients
        print(f"{idx}. {patient.name} - Urgency Level: {patient.urgency_level}")
        # Print additional patient information if needed
    print_separator()
