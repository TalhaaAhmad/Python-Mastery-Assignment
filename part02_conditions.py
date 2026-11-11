# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 2 - Conditions (if / elif / else)

# ---------- Warm-up: Even, odd and sign ----------
print("--- Warm-up: Even, odd and sign ---")
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("That is not a whole number. Try again.")

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# ---------- Build: Grade calculator ----------
print("\n--- Build: Grade calculator ---")
try:
    marks = float(input("Enter marks out of 100: "))
except ValueError:
    marks = -1   # letters are treated as invalid marks

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: Fail")

# ---------- Challenge: Electricity bill ----------
print("\n--- Challenge: Electricity bill ---")
while True:
    try:
        units = int(input("Units used: "))
        if units < 0:
            print("Units cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Please type a whole number. Try again.")

if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = 100 * 10 + (units - 100) * 15
else:
    bill = 100 * 10 + 100 * 15 + (units - 200) * 20

bill = bill + 50   # fixed charges
print("Total bill: Rs", bill)
