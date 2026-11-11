# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 8 Warm-up - Standard library tour
import math
import random
import datetime
import statistics

# math
print("Square root of 144:", math.sqrt(144))

# random
students = ["Ali", "Sara", "Ahmed", "Hina", "Usman"]
print("Random student:", random.choice(students))

# datetime
today = datetime.date.today()
new_year_eve = datetime.date(today.year, 12, 31)
print("Days left until 31 December:", (new_year_eve - today).days)

# statistics
marks = [80, 72, 91, 65, 88]
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
