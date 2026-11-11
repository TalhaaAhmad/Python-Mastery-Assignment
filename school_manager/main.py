# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# School Manager - run with:  python main.py
import logging
import os
from school.storage import load_students
from school.cli import run_menu

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "school.json")


def main() -> None:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    students = load_students(DATA_FILE)
    run_menu(students, DATA_FILE)


if __name__ == "__main__":
    main()
