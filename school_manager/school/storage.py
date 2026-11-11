# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
import json
import logging
from dataclasses import asdict
from school.models import Student


def save_students(students: list[Student], filename: str) -> None:
    data = [asdict(s) for s in students]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    logging.info("Saved %d students to %s", len(students), filename)


def load_students(filename: str) -> list[Student]:
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        logging.info("%s not found, starting with an empty list", filename)
        return []
    except json.JSONDecodeError:
        logging.warning("%s is damaged, starting with an empty list", filename)
        return []
    students = [Student(**d) for d in data]
    logging.info("Loaded %d students from %s", len(students), filename)
    return students
