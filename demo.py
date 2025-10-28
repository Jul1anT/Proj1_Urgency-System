"""
Hospital Urgency System - Compact Demonstration Script

This demo showcases all system functionalities in a concise flow,
perfect for video recording demonstrations (3-4 minutes).

Author: GitHub Copilot
Date: October 28, 2025
"""

from hospital import Hospital
from patient import Patient
import utils


def press_enter_to_continue():
    """Wait for user to press Enter before continuing."""
    input("\n[Press Enter to continue...]\n")


def demo_step(step_number, description):
    """Display demo step header."""
    utils.clear_screen()
    utils.print_header(f"STEP {step_number}: {description}")
    print()


def main():
    """
    Demostración compacta del Sistema de Urgencias Hospitalarias.
    
    Demuestra las tres estructuras de datos:
        - Cola de Prioridad: Ordenamiento de pacientes por urgencia
        - Pila: Historial de atenciones y funcionalidad UNDO
        - Arreglo Dinámico: Registro completo de pacientes
    """
    
    hospital = Hospital("CENTRO MÉDICO DE EMERGENCIAS")
    
    # Welcome screen
    utils.clear_screen()
    utils.print_header("HOSPITAL URGENCY SYSTEM - DEMO")
    print("\nThis demonstration will show:")
    print("  ✓ Patient Registration")
    print("  ✓ Priority Queue")
    print("  ✓ Patient Attendance")
    print("  ✓ History and UNDO Functionality")
    press_enter_to_continue()
    
    
    # ========== STEP 1: Register 3 patients ==========
    demo_step(1, "Register Patients")
    print("Registering 3 patients with different urgency levels:\n")
    
    patient1 = Patient("María López", 1)  # RED
    patient2 = Patient("Juan Pérez", 5)   # BLUE
    patient3 = Patient("Ana Martínez", 2) # ORANGE
    
    hospital.add_patient(patient1)
    print(f"✓ {patient1.name} - {patient1.get_urgency_name()} (Cardiac arrest)")
    
    hospital.add_patient(patient2)
    print(f"✓ {patient2.name} - {patient2.get_urgency_name()} (Minor cold)")
    
    hospital.add_patient(patient3)
    print(f"✓ {patient3.name} - {patient3.get_urgency_name()} (Chest pain)")
    
    print("\n→ Data Structures: PRIORITY QUEUE + DYNAMIC ARRAY")
    press_enter_to_continue()
    
    
    # ========== STEP 2: View waiting queue ==========
    demo_step(2, "View Waiting Queue (Priority Queue)")
    print("Priority Queue automatically sorts by urgency:\n")
    
    utils.print_separator()
    queue = hospital.waiting_patients()
    print(f"Patients waiting: {len(queue)}\n")
    
    for idx, patient in enumerate(queue, start=1):
        print(f"{idx}. {patient.name} - {patient.get_urgency_name()} ({patient.urgency_level})")
        if idx == 1:
            print("   ⚠️  HIGHEST PRIORITY - Will be attended first")
        print()
    
    utils.print_separator()
    print("→ Automatic O(log n) sorting")
    press_enter_to_continue()
    
    
    # ========== STEP 3: Attend first patient ==========
    demo_step(3, "Attend Highest Priority Patient")
    print("Attending most urgent patient...\n")
    
    utils.print_separator()
    attended1 = hospital.attend_patient()
    
    if attended1:
        print(f"✓ NOW ATTENDING: {attended1.name}")
        print(f"  Urgency: {attended1.get_urgency_name()}")
        print(f"\n  → Removed from PRIORITY QUEUE")
        print(f"  → Added to STACK of attended patients")
    
    utils.print_separator()
    press_enter_to_continue()
    
    
    # ========== STEP 4: View updated queue ==========
    demo_step(4, "Updated Queue")
    print(f"{attended1.name} has been attended.\n")
    
    utils.print_separator()
    queue = hospital.waiting_patients()
    print(f"Patients waiting: {len(queue)}\n")
    
    for idx, patient in enumerate(queue, start=1):
        print(f"{idx}. {patient.name} - {patient.get_urgency_name()}")
    
    utils.print_separator()
    press_enter_to_continue()
    
    
    # ========== STEP 5: Attend second patient ==========
    demo_step(5, "Attend Next Patient")
    
    attended2 = hospital.attend_patient()
    
    if attended2:
        print(f"✓ NOW ATTENDING: {attended2.name} - {attended2.get_urgency_name()}\n")
    
    press_enter_to_continue()
    
    
    # ========== STEP 6: View attendance history ==========
    demo_step(6, "Attendance History (Stack - LIFO)")
    print("The STACK shows patients in reverse order (LIFO):\n")
    
    utils.print_separator()
    attended_list = hospital.get_attended_patients()
    print(f"Attended patients: {len(attended_list)}\n")
    
    for idx, patient in enumerate(reversed(attended_list), start=1):
        print(f"{idx}. {patient.name} - {patient.get_urgency_name()}")
        if idx == 1:
            print("   📌 MOST RECENT (Top of Stack)")
        print()
    
    utils.print_separator()
    press_enter_to_continue()
    
    
    # ========== STEP 7: UNDO last attendance ==========
    demo_step(7, "UNDO Last Attendance (Stack Pop)")
    print("Demonstrating UNDO functionality using STACK (LIFO):\n")
    
    utils.print_separator()
    undone = hospital.undo_last_attendance()
    
    if undone:
        print(f"✓ UNDO SUCCESSFUL!")
        print(f"  Patient: {undone.name}")
        print(f"\n  → Removed from top of STACK")
        print(f"  → Re-added to PRIORITY QUEUE")
    
    utils.print_separator()
    press_enter_to_continue()
    
    
    # ========== STEP 8: Final summary ==========
    demo_step(8, "Final Summary")
    print("Current system state:\n")
    
    utils.print_separator()
    
    queue = hospital.waiting_patients()
    print(f"📋 Waiting Queue: {len(queue)} patients")
    for patient in queue:
        print(f"   - {patient.name} - {patient.get_urgency_name()}")
    print()
    
    attended_list = hospital.get_attended_patients()
    print(f"✓ Attended Patients: {len(attended_list)} patient(s)")
    for patient in reversed(attended_list):
        print(f"   - {patient.name} - {patient.get_urgency_name()}")
    print()
    
    all_patients = hospital.get_all_patients()
    print(f"📁 Complete Registry: {len(all_patients)} total records")
    
    utils.print_separator()
    
    print("\n🎯 DATA STRUCTURES DEMONSTRATED:")
    print("   1. PRIORITY QUEUE (heapq) - Efficient O(log n) sorting")
    print("   2. STACK (list) - LIFO history with UNDO")
    print("   3. DYNAMIC ARRAY (list) - Permanent registry")
    
    print("\n✓ Demonstration complete!")
    utils.print_separator()
    
    press_enter_to_continue()
    
    # Final screen
    utils.clear_screen()
    utils.print_header("DEMONSTRATION COMPLETE")
    print("\nThank you for watching the Hospital Urgency System demo!")
    print("\nFunctionalities shown:")
    print("  ✓ Patient registration")
    print("  ✓ Automatic priority queue")
    print("  ✓ Attendance by urgency")
    print("  ✓ Attendance history")
    print("  ✓ UNDO functionality")
    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
