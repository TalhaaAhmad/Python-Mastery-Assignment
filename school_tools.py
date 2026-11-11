# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 8 Build - my own module (Part 5 functions moved here, with type hints)
import math


def area_of_circle(r: float) -> float:
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r


def is_even(n: int) -> bool:
    return n % 2 == 0


def greet(name: str, lang: str = "en") -> str:
    if lang == "ur":
        return "Salaam " + name
    return "Hello " + name


def average(marks: list[float]) -> float:
    if len(marks) == 0:
        raise ValueError("No marks given")
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    # changed in Part 12: marks outside 0-100 now raise an error
    if avg < 0 or avg > 100:
        raise ValueError("Marks must be between 0 and 100")
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


def report(name: str, marks: list[float]) -> str:
    avg = average(marks)
    return f"{name}: average {avg:.1f}, grade {grade(avg)}"


# this block only runs when I run school_tools.py directly,
# it does NOT run when another file imports this module
if __name__ == "__main__":
    print("Testing school_tools.py directly")
    print(report("Ali", [80, 72, 91]))
    print(greet("Sara", "ur"))
    print(is_even(10))
