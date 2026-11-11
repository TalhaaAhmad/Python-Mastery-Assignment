# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 3 - Loops (for / while)
import random

# ---------- Warm-up: Times table ----------
print("--- Warm-up: Times table ---")
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please type a whole number.")

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# ---------- Build: ATM PIN check ----------
print("\n--- Build: ATM PIN check ---")
correct_pin = "4321"
tries_left = 3
while tries_left > 0:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Welcome")
        break
    tries_left = tries_left - 1
    if tries_left > 0:
        print("Wrong PIN. Tries left:", tries_left)
if tries_left == 0:
    print("Card blocked")

# ---------- Challenge: Number guessing game ----------
print("\n--- Challenge: Number guessing game ---")
play = "y"
while play == "y":
    secret = random.randint(1, 50)
    guesses = 0
    while True:
        try:
            guess = int(input("Guess the number (1 to 50): "))
        except ValueError:
            print("Please type a whole number.")
            continue
        guesses = guesses + 1
        if guess > secret:
            print("Too high")
        elif guess < secret:
            print("Too low")
        else:
            print(f"Got it in {guesses} guesses!")
            break
    play = input("Play again? (y/n): ").lower()
    while play != "y" and play != "n":
        play = input("Please type y or n: ").lower()

# ---------- Extra practice ----------
print("\n--- Extra practice ---")
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()

total = 0
for n in range(1, 101):
    if n % 2 == 0:
        total = total + n
print("Sum of even numbers from 1 to 100:", total)
