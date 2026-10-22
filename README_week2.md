# Student Management System (Python)

A command-line Student Management System built as a Week 2 mini project. It stores student records (roll number, name, marks) in a CSV file and supports add, delete and search operations. All changes are saved permanently to the file.

## Features

- Store student data (roll number, name, marks) in a CSV file
- Add a student (with duplicate roll number check and marks validation)
- Delete a student by roll number
- Search a student by roll number or by name (partial match works)
- View all students in a neat table
- Changes are saved to `students.csv` immediately, so data stays after the program closes

## Project Structure

| Function | Purpose |
|---|---|
| `load_students()` | Reads all records from the CSV file |
| `save_students()` | Writes all records back to the CSV file |
| `find_student()` | Finds a student by roll number |
| `add_student()` | Adds a new student |
| `delete_student()` | Deletes a student by roll number |
| `search_student()` | Searches by roll number or name |
| `view_all_students()` | Shows every student |
| `print_table()` | Prints students as a table |
| `show_menu()` / `main()` | Menu and program loop |

## How to Run

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Download `student_management.py`.
3. Open a terminal in the same folder and run:

```
python student_management.py
```

The file `students.csv` is created automatically when you add the first student.

## Sample CSV (students.csv)

```
roll_number,name,marks
101,Anshika,88.5
102,Rahul,72.0
```

## Concepts Used

- File handling (reading and writing files)
- The `csv` module (`DictReader` and `DictWriter`)
- CRUD logic (Create, Read, Delete, Search)
- Functions, loops and input validation

## Possible Improvements

- Add an update/edit option for marks
- Sort students by marks
- Show the class average and topper

## Author

Anshika Khewariya
