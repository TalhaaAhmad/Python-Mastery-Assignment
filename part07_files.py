# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 7 - Exceptions and files
import csv
import json
import datetime

# ---------- Warm-up: Safe division ----------
print("--- Warm-up: Safe division ---")
while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        answer = a / b
        print("Answer:", answer)
        break
    except ValueError:
        print("That is not a number. Try again.")
    except ZeroDivisionError:
        print("You cannot divide by zero. Try again.")

# ---------- Build: Daily diary ----------
print("\n--- Build: Daily diary ---")
while True:
    print("\n1) Write today's note  2) Read old entries  3) Exit")
    choice = input("Choose: ")
    if choice == "1":
        note = input("Today's note: ")
        file = open("diary.txt", "a")
        file.write(str(datetime.date.today()) + " : " + note + "\n")
        file.close()
        print("Saved.")
    elif choice == "2":
        try:
            file = open("diary.txt", "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No entries yet")
    elif choice == "3":
        break
    else:
        print("Please choose 1, 2 or 3.")

# ---------- Challenge: CSV result sheet ----------
print("\n--- Challenge: CSV and JSON ---")
results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [30, 55, 70],
    "Hina": [65, 78, 81],
    "Usman": [20, 35, 30],
}

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "mark1", "mark2", "mark3", "average"])
    for name in results:
        marks = results[name]
        average = round(sum(marks) / len(marks), 2)
        writer.writerow([name, marks[0], marks[1], marks[2], average])
print("Saved results.csv")

# the same data as JSON
data = {}
for name in results:
    marks = results[name]
    data[name] = {"marks": marks, "average": round(sum(marks) / len(marks), 2)}
with open("results.json", "w") as file:
    json.dump(data, file, indent=4)
print("Saved results.json")
print("Now run part07_read_results.py to read the CSV back.")
