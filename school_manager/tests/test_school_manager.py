# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
import pytest
from school.models import Student
from school.services import (add_student, add_marks, get_grade,
                             report_card, class_ranking, make_comment)
from school.storage import save_students, load_students


def test_average():
    student = Student("Ali", 1, [80, 90])
    assert student.average() == 85


def test_add_student_and_duplicate_roll():
    students = []
    add_student(students, "Ali", 1)
    assert len(students) == 1
    with pytest.raises(ValueError):
        add_student(students, "Sara", 1)


def test_empty_name_is_rejected():
    with pytest.raises(ValueError):
        add_student([], "   ", 5)


def test_wrong_marks_add_nothing():
    student = Student("Ali", 1)
    with pytest.raises(ValueError):
        add_marks(student, [50, 101])
    assert student.marks == []


@pytest.mark.parametrize("avg, expected", [
    (95, "A"), (75, "B"), (65, "C"), (40, "D"), (10, "Fail"),
])
def test_grades(avg, expected):
    assert get_grade(avg) == expected


def test_report_card():
    text = report_card(Student("Ali", 1, [80, 90]))
    assert "85.00" in text
    assert "A" in text


def test_ranking_highest_first():
    ali = Student("Ali", 1, [60])
    sara = Student("Sara", 2, [90])
    hina = Student("Hina", 3, [75])
    ranked = class_ranking([ali, sara, hina])
    assert [s.name for s in ranked] == ["Sara", "Hina", "Ali"]


def test_save_and_load(tmp_path):
    filename = str(tmp_path / "school.json")
    save_students([Student("Ali", 1, [80, 90])], filename)
    loaded = load_students(filename)
    assert loaded == [Student("Ali", 1, [80, 90])]


def test_missing_file_gives_empty_list(tmp_path):
    assert load_students(str(tmp_path / "nothing.json")) == []


def test_comment():
    assert make_comment(Student("Ali", 1, [90, 85])) == "Excellent in all subjects, keep it up."
