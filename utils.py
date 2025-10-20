def clear_screen():
    import os
    os.system('clear' if os.name != 'nt' else 'cls')

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  {title}".center(60))
    print("=" * 60)

def print_separator():
    print("-" * 60)

def print_patient_info(patient):
    print(f"Name: {patient.name}")
    print(f"Urgency Level: {patient.urgency_level}")

def print_waiting_queue(queue):
    print_header("WAITING QUEUE")
    for idx, patient in enumerate(queue, start=1):
        print(f"{idx}. {patient.name} - Urgency Level: {patient.urgency_level}")
    print_separator()