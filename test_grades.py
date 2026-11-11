# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 12 Build - tests for the grade function
import pytest
from school_tools import grade


@pytest.mark.parametrize("marks, expected", [
    (0, "Fail"),
    (32, "Fail"),
    (33, "D"),
    (59, "D"),
    (60, "C"),
    (69, "C"),
    (70, "B"),
    (79, "B"),
    (80, "A"),
    (100, "A"),
])
def test_grade(marks, expected):
    assert grade(marks) == expected


def test_marks_above_100():
    with pytest.raises(ValueError):
        grade(101)


def test_marks_below_0():
    with pytest.raises(ValueError):
        grade(-1)
