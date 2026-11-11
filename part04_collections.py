# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 4 - Lists, dictionaries, tuples and sets

# ---------- Warm-up: Shopping list ----------
print("--- Warm-up: Shopping list ---")
items = ["milk", "bread", "eggs"]
items.append("tea")
items.remove("bread")
items.sort()
for number, item in enumerate(items, 1):
    print(number, item)

# ---------- Build: Phone book ----------
print("\n--- Build: Phone book ---")
contacts = {
    "Ali": "0300-1111111",
    "Sara": "0311-2222222",
    "Ahmed": "0321-3333333",
    "Hina": "0333-4444444",
    "Usman": "0345-5555555",
}

while True:
    print("\n1) Add  2) Search  3) Delete  4) Show all  5) Exit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Name: ").strip().title()
        number = input("Phone number: ").strip()
        if name == "" or number == "":
            print("Name and number cannot be empty.")
        else:
            contacts[name] = number
            print("Saved.")
    elif choice == "2":
        name = input("Name to search: ").strip().title()
        print(contacts.get(name, "Not found"))
    elif choice == "3":
        name = input("Name to delete: ").strip().title()
        if name in contacts:
            del contacts[name]
            print("Deleted.")
        else:
            print("Not found")
    elif choice == "4":
        for name in contacts:
            print(name, ":", contacts[name])
    elif choice == "5":
        break
    else:
        print("Please choose 1 to 5.")

# ---------- Challenge: Class result sheet ----------
print("\n--- Challenge: Class result sheet ---")
results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [30, 55, 70],
    "Hina": [65, 78, 81],
    "Usman": [20, 35, 30],
}

topper = ""
best_total = 0
weak_students = set()

for name in results:
    marks = results[name]
    total = sum(marks)
    average = total / len(marks)
    print(f"{name}: total = {total}, average = {average:.2f}")
    if total > best_total:
        best_total = total
        topper = name
    for m in marks:
        if m < 40:
            weak_students.add(name)

print("Class topper:", topper)
print("Students below 40 in any subject:", weak_students)

# a tuple is for fixed data, for example a location
location = (34.0151, 71.5249)
print("Fixed location (tuple):", location)
