# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
import logging
from school.models import Student
from school.services import (add_student, find_student, add_marks,
                             report_card, class_ranking, make_comment)
from school.storage import save_students


def ask_roll_number() -> int:
    while True:
        try:
            return int(input("Roll number: "))
        except ValueError:
            print("Roll number must be a whole number.")


def ask_student(students: list[Student]) -> Student | None:
    roll_number = ask_roll_number()
    student = find_student(students, roll_number)
    if student is None:
        print("No student with that roll number.")
    return student


def show_menu() -> None:
    print("\n===== SCHOOL MANAGER =====")
    print("1. Add student")
    print("2. Add marks")
    print("3. Show report card")
    print("4. Class ranking")
    print("5. Save and exit")
    print("6. Write comment")


def menu_add_student(students: list[Student]) -> None:
    name = input("Student name: ")
    roll_number = ask_roll_number()
    try:
        add_student(students, name, roll_number)
        print("Student added.")
    except ValueError as error:
        print("Error:", error)


def menu_add_marks(students: list[Student]) -> None:
    student = ask_student(students)
    if student is None:
        return
    text = input("Enter marks separated by commas (e.g. 80,75,90): ")
    try:
        marks = [float(m) for m in text.split(",")]
        add_marks(student, marks)
        print("Marks added.")
    except ValueError:
        print("Error: type numbers between 0 and 100 only.")


def menu_report(students: list[Student]) -> None:
    student = ask_student(students)
    if student is not None:
        print(report_card(student))


def menu_ranking(students: list[Student]) -> None:
    ranked = class_ranking(students)
    if len(ranked) == 0:
        print("No students yet.")
    for position, student in enumerate(ranked, 1):
        print(f"{position}. {student.name} - {student.average():.2f}")


def menu_comment(students: list[Student]) -> None:
    student = ask_student(students)
    if student is not None:
        print(make_comment(student))


def run_menu(students: list[Student], filename: str) -> None:
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        logging.info("Menu choice: %s", choice)
        if choice == "1":
            menu_add_student(students)
        elif choice == "2":
            menu_add_marks(students)
        elif choice == "3":
            menu_report(students)
        elif choice == "4":
            menu_ranking(students)
        elif choice == "5":
            save_students(students, filename)
            print("Saved. Goodbye!")
            break
        elif choice == "6":
            menu_comment(students)
        else:
            print("Please choose a number from 1 to 6.")
