# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 10 - Iterators, generators and decorators
import time
from functools import wraps


# ---------- Warm-up: Countdown generator ----------
def countdown(n):
    while n > 0:
        yield n
        n = n - 1


def evens(limit):
    for i in range(0, limit + 1, 2):
        yield i


print("--- Warm-up ---")
for number in countdown(5):
    print(number)
print(list(evens(10)))

# ---------- Build: Big file reader ----------
print("\n--- Build: file reader ---")
# make a log file with 60 lines, every 6th line has ERROR
with open("log.txt", "w") as file:
    for i in range(1, 61):
        if i % 6 == 0:
            file.write(f"Line {i}: ERROR something went wrong\n")
        else:
            file.write(f"Line {i}: all ok\n")


def read_lines(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()


def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line


count = 0
for line in only_errors(read_lines("log.txt")):
    count = count + 1
print("Number of error lines:", count)


# ---------- Challenge: Your own decorators ----------
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, "took", round(end - start, 4), "seconds")
        return result
    return wrapper


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__, "with", args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@timer
@log_calls
def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


print("\n--- Challenge: decorators ---")
print("Sum:", sum_to(1000000))
