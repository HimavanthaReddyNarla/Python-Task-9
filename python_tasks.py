"""File-handling exercises and student record helpers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).resolve().parent
WELCOME_FILE = DATA_DIR / "welcome.txt"
NAMES_FILE = DATA_DIR / "student_names.txt"
LINES_FILE = DATA_DIR / "sample_lines.txt"
STUDENTS_FILE = DATA_DIR / "students.txt"
SIMPLE_STUDENTS_FILE = DATA_DIR / "task11_students.txt"
RECORDS_FILE = DATA_DIR / "record_students.txt"


def ensure_sample_files() -> None:
    """Create the exercise files once without replacing existing user data."""
    samples = {
        WELCOME_FILE: "Welcome to Python\nI am learning File Handling\n",
        NAMES_FILE: "Aarav\nMeera\nIshaan\nDiya\nKabir\n",
        LINES_FILE: "Python makes files useful.\nRead one line at a time.\nUse loops to process text.\nKeep student records safely.\nPractice a little every day.\n",
        STUDENTS_FILE: "Aarav | 88\nMeera | 94\nIshaan | 79\n",
    }
    for path, content in samples.items():
        if not path.exists():
            with open(path, "w", encoding="utf-8") as file:
                file.write(content)


def write_welcome() -> str:
    with open(WELCOME_FILE, "w", encoding="utf-8") as file:
        file.write("Welcome to Python\nI am learning File Handling\n")
    return f"Created {WELCOME_FILE.name}."


def save_student_details(name: str, age: str, course: str, marks: str) -> str:
    with open(DATA_DIR / "student.txt", "w", encoding="utf-8") as file:
        file.write(f"Name: {name}\nAge: {age}\nCourse: {course}\nMarks: {marks}\n")
    return "Student details saved to student.txt."


def read_file_lines(path: Path) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]


def append_student_name(name: str) -> str:
    with open(STUDENTS_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name.strip()}\n")
    return f"Added {name.strip()} to {STUDENTS_FILE.name}."


def count_file_lines(path: Path) -> int:
    with open(path, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)


def count_file_words(path: Path) -> int:
    with open(path, "r", encoding="utf-8") as file:
        return len(file.read().split())


def read_requested_file(filename: str) -> str:
    path = (DATA_DIR / filename).resolve()
    if path.parent != DATA_DIR.resolve():
        return "Please enter a filename from this project folder."
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


def divide_numbers(first: str, second: str) -> str:
    try:
        result = float(first) / float(second)
        return f"Result: {result:g}"
    except ValueError:
        return "Invalid input. Please enter numbers."
    except ZeroDivisionError:
        return "Cannot divide by zero."


def calculate_square(value: str) -> str:
    try:
        number = float(value)
        result = f"Square: {number * number:g}"
    except ValueError:
        result = "Invalid input. Please enter a number."
    finally:
        result += "\nProgram completed."
    return result


def add_simple_student(name: str, marks: str) -> str:
    try:
        marks_number = float(marks)
    except ValueError:
        return "Marks must be a number."
    with open(SIMPLE_STUDENTS_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name.strip()} | {marks_number:g}\n")
    return "Student added."


def view_students(path: Path) -> str:
    try:
        rows = read_file_lines(path)
    except FileNotFoundError:
        return "No student file found yet. Add a student first."
    if not rows:
        return "No students found."
    return "\n".join(rows)


def validate_and_save_student(name: str, age: str, marks: str) -> str:
    try:
        age_number = int(age)
    except ValueError:
        return "Age must be an integer."
    try:
        marks_number = float(marks)
    except ValueError:
        return "Marks must be a number."
    if not 0 <= marks_number <= 100:
        return "Marks must be between 0 and 100."
    with open(DATA_DIR / "validated_students.txt", "a", encoding="utf-8") as file:
        file.write(f"{name.strip()} | {age_number} | {marks_number:g}\n")
    return "Valid student data saved."


def search_student(path: Path, name: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                fields = next(csv.reader([line], delimiter="|"))
                if fields and fields[0].strip().casefold() == name.strip().casefold():
                    return f"Student found\n{line.strip()}"
    except FileNotFoundError:
        return "Student not found"
    return "Student not found"


def add_record(path: Path, name: str, age: str, course: str, marks: str) -> str:
    age_number = int(age)
    marks_number = float(marks)
    if not name.strip() or not course.strip():
        raise ValueError("Name and course cannot be empty.")
    if not 0 <= marks_number <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="|")
        writer.writerow([name.strip(), age_number, course.strip(), f"{marks_number:g}"])
    return "Student record added."


def add_multiple_records(path: Path, lines: str) -> str:
    added = 0
    for entry in lines.splitlines():
        if not entry.strip():
            continue
        fields = [field.strip() for field in entry.split(",")]
        if len(fields) != 4:
            raise ValueError("Enter each student as: Name, Age, Course, Marks.")
        add_record(path, *fields)
        added += 1
    if not added:
        return "Enter at least one student record."
    return f"Added {added} student record(s)."


def read_student_records(path: Path) -> str:
    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            rows = list(csv.reader(file, delimiter="|"))
    except FileNotFoundError:
        return "No student file found yet. Add a student first."
    if not rows:
        return "No students found."
    output = []
    for row in rows:
        if not row:
            continue
        if len(row) == 1:
            output.append(f"Name: {row[0].strip()}")
        elif len(row) == 2:
            output.append(f"Name: {row[0].strip()} | Marks: {row[1].strip()}")
        else:
            output.append(
                f"Name: {row[0].strip()} | Age: {row[1].strip()} | "
                f"Course: {row[2].strip()} | Marks: {row[3].strip()}"
            )
    return "\n".join(output) or "No students found."


def execute_task(task_id: int, data: Any = None) -> str:
    """Run one exercise with supplied values; used by both Flask and the CLI."""
    values = data or {}
    get = values.get
    action = get("action", "")
    if task_id == 1:
        return write_welcome()
    if task_id == 2:
        return save_student_details(get("name", ""), get("age", ""), get("course", ""), get("marks", ""))
    if task_id == 3:
        return "\n".join(read_file_lines(NAMES_FILE))
    if task_id == 4:
        return "\n".join(read_file_lines(LINES_FILE))
    if task_id == 5:
        return append_student_name(get("name", ""))
    if task_id == 6:
        return f"Total lines: {count_file_lines(LINES_FILE)}"
    if task_id == 7:
        return f"Total words: {count_file_words(LINES_FILE)}"
    if task_id == 8:
        return read_requested_file(get("filename", ""))
    if task_id == 9:
        return divide_numbers(get("first", ""), get("second", ""))
    if task_id == 10:
        return calculate_square(get("number", ""))
    if task_id == 11:
        if action == "add":
            return add_simple_student(get("name", ""), get("marks", ""))
        if action == "view":
            return view_students(SIMPLE_STUDENTS_FILE)
        return "Choose Add Student or View Students."
    if task_id == 12:
        return validate_and_save_student(get("name", ""), get("age", ""), get("marks", ""))
    if task_id == 13:
        return search_student(STUDENTS_FILE, get("name", ""))
    if task_id == 14:
        if action == "add":
            return add_record(RECORDS_FILE, get("name", ""), get("age", ""), get("course", ""), get("marks", ""))
        if action == "view":
            return read_student_records(RECORDS_FILE)
        if action == "search":
            return search_student(RECORDS_FILE, get("name", ""))
        return "Choose Add Student, View Students, or Search Student."
    if task_id == 15:
        if action == "add":
            return add_record(STUDENTS_FILE, get("name", ""), get("age", ""), get("course", ""), get("marks", ""))
        if action == "add_more":
            return add_multiple_records(STUDENTS_FILE, get("records", ""))
        if action == "view":
            return read_student_records(STUDENTS_FILE)
        if action == "search":
            return search_student(STUDENTS_FILE, get("name", ""))
        return "Choose Add Student, View Students, Search Student, or Add More Students."
    raise ValueError("Choose a task from 1 to 15.")


TASK_TITLES = [
    "Create a file", "Write student data", "Read student names", "Read line by line",
    "Append student", "Count lines", "Count words", "Handle missing file",
    "Handle invalid input", "Use finally", "Student data management",
    "Validate student marks", "Search student", "Student record system",
    "Mini student management system",
]


def prompt_for_task(task_id: int, action: str = "") -> dict[str, str]:
    if task_id == 2:
        return {"name": input("Name: "), "age": input("Age: "), "course": input("Course: "), "marks": input("Marks: ")}
    if task_id == 5:
        return {"name": input("Student name: ")}
    if task_id == 8:
        return {"filename": input("Filename: ").strip()}
    if task_id == 9:
        return {"first": input("First number: "), "second": input("Second number: ")}
    if task_id == 10:
        return {"number": input("Number: ")}
    if task_id == 11 and action == "add":
        return {"name": input("Name: "), "marks": input("Marks: ")}
    if task_id == 12:
        return {"name": input("Name: "), "age": input("Age: "), "marks": input("Marks: ")}
    if task_id in (13, 14, 15) and action == "search":
        return {"name": input("Student name: ")}
    if task_id in (14, 15) and action == "add":
        return {"name": input("Name: "), "age": input("Age: "), "course": input("Course: "), "marks": input("Marks: ")}
    if task_id == 15 and action == "add_more":
        entries = []
        count = int(input("How many students? "))
        for _ in range(count):
            entries.append(",".join(input(f"{label}: ") for label in ("Name", "Age", "Course", "Marks")))
        return {"records": "\n".join(entries)}
    return {}


def run_cli() -> None:
    ensure_sample_files()
    while True:
        print("\n--- Python File Handling Tasks ---")
        for number, title in enumerate(TASK_TITLES, start=1):
            print(f"{number}. {title}")
        print("0. Exit")
        selection = -1
        try:
            selection = int(input("Select a task: "))
            if selection == 0:
                print("Goodbye.")
                break
            if not 1 <= selection <= 15:
                print("Choose a number from 1 to 15.")
                continue
            if selection in (11, 14, 15):
                while True:
                    options = "1. Add Student\n2. View Students"
                    if selection != 11:
                        options += "\n3. Search Student"
                    if selection == 15:
                        options += "\n4. Add More Students"
                    print(f"\n{options}\n0. Back")
                    choice = input("Select an option: ").strip()
                    if choice == "0":
                        break
                    action = {"1": "add", "2": "view", "3": "search", "4": "add_more"}.get(choice, "")
                    if not action or (selection == 11 and action not in ("add", "view")) or (selection == 14 and action == "add_more"):
                        print("Invalid option.")
                        continue
                    data = prompt_for_task(selection, action)
                    data["action"] = action
                    print(execute_task(selection, data))
            else:
                print(execute_task(selection, prompt_for_task(selection)))
        except (ValueError, FileNotFoundError, ZeroDivisionError) as error:
            print(f"Input or file error: {error}")


if __name__ == "__main__":
    ensure_sample_files()
    run_cli()