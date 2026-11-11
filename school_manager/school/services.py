# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
from school.models import Student


def add_student(students: list[Student], name: str, roll_number: int) -> Student:
    if name.strip() == "":
        raise ValueError("Name cannot be empty")
    if roll_number <= 0:
        raise ValueError("Roll number must be more than 0")
    if find_student(students, roll_number) is not None:
        raise ValueError("This roll number already exists")
    student = Student(name.strip(), roll_number)
    students.append(student)
    return student


def find_student(students: list[Student], roll_number: int) -> Student | None:
    for student in students:
        if student.roll_number == roll_number:
            return student
    return None


def add_marks(student: Student, marks: list[float]) -> None:
    # check all marks first, so nothing is added if one of them is wrong
    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")
    student.marks.extend(marks)


def get_grade(avg: float) -> str:
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    else:
        return "Fail"


def report_card(student: Student) -> str:
    if len(student.marks) == 0:
        return f"{student.name} (Roll {student.roll_number}): no marks yet"
    avg = student.average()
    return (f"Name   : {student.name}\n"
            f"Roll   : {student.roll_number}\n"
            f"Marks  : {student.marks}\n"
            f"Average: {avg:.2f}\n"
            f"Grade  : {get_grade(avg)}")


def class_ranking(students: list[Student]) -> list[Student]:
    # highest average first
    return sorted(students, key=lambda s: s.average(), reverse=True)


def make_comment(student: Student) -> str:
    # bonus: simple rules, no AI needed
    if len(student.marks) == 0:
        return "No marks yet."
    if min(student.marks) >= 80:
        return "Excellent in all subjects, keep it up."
    if min(student.marks) < 33:
        return "Failing in at least one subject, needs extra practice."
    if student.average() >= 60:
        return "Good work, try to improve the weaker subjects."
    return "Needs more hard work. Please revise daily."
