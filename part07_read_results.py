# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 7 Challenge - second program: read results.csv and print the topper
import csv

try:
    with open("results.csv", "r") as file:
        reader = csv.DictReader(file)
        topper = ""
        best = -1
        for row in reader:
            average = float(row["average"])
            print(row["name"], "->", average)
            if average > best:
                best = average
                topper = row["name"]
    print("Topper:", topper, "with average", best)
except FileNotFoundError:
    print("results.csv not found. Run part07_files.py first.")
