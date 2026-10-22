"""
Student Management System
-------------------------
Features:
  - Stores student data (roll number, name, marks) in a CSV file
  - Add, delete and search students (plus view all)
  - Every change is saved to the file immediately, so data is permanent
"""

import csv
import os

# The CSV file is created in the same folder as this script
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")
FIELDS = ["roll_number", "name", "marks"]


def load_students():
    """Read all students from the CSV file. Returns a list of dictionaries."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_students(students):
    """Write the full list of students to the CSV file (saves changes permanently)."""
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def find_student(students, roll_number):
    """Return the student with this roll number, or None if not found."""
    for student in students:
        if student["roll_number"].lower() == roll_number.lower():
            return student
    return None


def add_student():
    """Add a new student after checking the input."""
    students = load_students()

    roll_number = input("Enter roll number: ").strip()
    if not roll_number:
        print("Roll number cannot be empty.")
        return
    if find_student(students, roll_number):
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))
    except ValueError:
        print("Invalid marks. Please enter a number.")
        return
    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students.append({"roll_number": roll_number, "name": name, "marks": marks})
    save_students(students)
    print(f"Student '{name}' added successfully.")


def delete_student():
    """Delete a student by roll number."""
    students = load_students()
    roll_number = input("Enter roll number to delete: ").strip()

    student = find_student(students, roll_number)
    if student is None:
        print("No student found with that roll number.")
        return

    students.remove(student)
    save_students(students)
    print(f"Student '{student['name']}' deleted successfully.")


def search_student():
    """Search by roll number (exact) or by name (partial match)."""
    students = load_students()
    keyword = input("Enter roll number or name to search: ").strip().lower()
    if not keyword:
        print("Search cannot be empty.")
        return

    results = [
        s for s in students
        if keyword == s["roll_number"].lower() or keyword in s["name"].lower()
    ]
    if not results:
        print("No matching student found.")
        return

    print(f"\nFound {len(results)} student(s):")
    print_table(results)


def view_all_students():
    """Show every student in a table."""
    students = load_students()
    if not students:
        print("No students found. Add some first.")
        return
    print_table(students)


def print_table(students):
    """Print a list of students as a neat table."""
    print(f"\n{'Roll No':<12}{'Name':<25}{'Marks':<8}")
    print("-" * 45)
    for s in students:
        print(f"{s['roll_number']:<12}{s['name']:<25}{s['marks']:<8}")


def show_menu():
    """Print the main menu."""
    print("\n------ STUDENT MANAGEMENT SYSTEM ------")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. View All Students")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Goodbye! All changes are saved in students.csv")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
