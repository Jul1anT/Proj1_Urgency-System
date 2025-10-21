"""UI utility functions for console formatting and display."""


def clear_screen():
    """Clear terminal screen (cross-platform: Unix/Windows)."""
    import os
    # Use 'cls' for Windows and 'clear' for Unix/Linux/Mac
    os.system('clear' if os.name != 'nt' else 'cls')


def print_header(title):
    """Print centered header with decorative borders (60 chars width)."""
    print("\n" + "=" * 60)
    print(f"  {title}".center(60))
    print("=" * 60)


def print_separator():
    """Print horizontal separator line."""
    print("-" * 60)


def print_patient_info(patient):
    """Display patient name and urgency level."""
    print(f"Name: {patient.name}")
    print(f"Urgency Level: {patient.urgency_level}")


def print_waiting_queue(queue):
    """Display formatted waiting queue with header and numbered list."""
    print_header("WAITING QUEUE")

    for idx, patient in enumerate(queue, start=1):
        print(f"{idx}. {patient.name} - Urgency Level: {patient.urgency_level}")
    print_separator()
