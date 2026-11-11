# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 1 - Variables, data types, input and output

# ---------- Warm-up: Student ID card ----------
print("--- Warm-up: Student ID card ---")
name = input("Enter name: ")
while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Age must be a whole number. Try again.")
class_name = input("Enter class: ")
city = input("Enter city: ")

print("======== STUDENT CARD ========")
print("Name :", name)
print("Age  :", age)
print("Class:", class_name)
print("City :", city)
print("==============================")
print("Type of name :", type(name))
print("Type of age  :", type(age))
print("Type of class:", type(class_name))
print("Type of city :", type(city))

# ---------- Build: Shop bill ----------
print("\n--- Build: Shop bill ---")
item = input("Item name: ")
while True:
    try:
        price = float(input("Price of one item: "))
        quantity = int(input("Quantity: "))
        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Please type numbers only. Try again.")

subtotal = price * quantity
discount = subtotal * 0.05
after_discount = subtotal - discount
tax = after_discount * 0.17
total = after_discount + tax

print("Item         :", item)
print("Subtotal     :", f"Rs {round(subtotal, 2):.2f}")
print("Discount (5%):", f"Rs {round(discount, 2):.2f}")
print("Tax (17%)    :", f"Rs {round(tax, 2):.2f}")
print("Final total  :", f"Rs {round(total, 2):.2f}")

# ---------- Challenge: Unit converter ----------
print("\n--- Challenge: Unit converter ---")
while True:
    try:
        celsius = float(input("Temperature in Celsius: "))
        km = float(input("Distance in kilometres: "))
        break
    except ValueError:
        print("Please type numbers only. Try again.")

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
miles = km * 0.621371
metres = km * 1000

print(f"Fahrenheit: {fahrenheit:.1f}")
print(f"Kelvin    : {kelvin:.1f}")
print(f"Miles     : {miles:.1f}")
print(f"Metres    : {metres:.1f}")
