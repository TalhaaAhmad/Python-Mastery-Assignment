# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 5 - Functions and comprehensions
# (type hints were added later for Part 11)
import math


# ---------- Warm-up: Small helpers ----------
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


print("--- Warm-up: Small helpers ---")
print(area_of_circle(1))
print(area_of_circle(2.5))
print(area_of_circle(10))
print(is_even(4))
print(is_even(7))
print(is_even(0))
print(greet("Ali"))
print(greet("Sara", "ur"))
print(greet("Ahmed", "en"))


# ---------- Build: Marks toolkit ----------
def average(marks: list[float]) -> float:
    if len(marks) == 0:
        raise ValueError("No marks given")
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
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


print("\n--- Build: Marks toolkit ---")
print(report("Ali", [80.0, 72.0, 91.0]))
print(report("Sara", [95.0, 88.0, 90.0]))
print(report("Ahmed", [30.0, 55.0, 20.0]))

# ---------- Challenge: Comprehensions ----------
print("\n--- Challenge: Comprehensions ---")
results = {
    "Ali": [80.0, 72.0, 91.0],
    "Sara": [95.0, 88.0, 90.0],
    "Ahmed": [30.0, 55.0, 70.0],
    "Hina": [65.0, 78.0, 81.0],
    "Usman": [20.0, 35.0, 30.0],
}
names = ["Ali", "Sara", "Ahmed", "Hina", "Usman"]

squares = [n * n for n in range(1, 11)]
long_names = [n for n in names if len(n) > 4]
averages = {name: average(marks) for name, marks in results.items()}
passing = [name for name, avg in averages.items() if avg >= 33]

print("Squares:", squares)
print("Names longer than 4 letters:", long_names)
print("Averages:", averages)
print("Passing students:", passing)
