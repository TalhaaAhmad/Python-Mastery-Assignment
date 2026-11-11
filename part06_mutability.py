# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 6 - References and mutability
import copy

# ---------- Warm-up: Predict, then run ----------
print("--- Warm-up ---")
a = [1, 2, 3]
b = a
b.append(4)
# prediction: [1, 2, 3, 4]  (a and b are the same list)
print(a)

c = a.copy()
c.append(5)
# prediction: [1, 2, 3, 4] [1, 2, 3, 4, 5]  (c is a separate copy)
print(a, c)
# prediction: True False True
print(a is b, a is c, a == a[:])
# Explanation: "b = a" does not copy the list, both names point to the same
# list, so changing b also changed a. ".copy()" makes a new list, so c is
# separate. "a == a[:]" is True because the values are equal, but they are
# not the same object.


# ---------- Build: Fix the cart bug ----------
print("\n--- Build: cart bug ---")


def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("With the bug:")
print(add_item_bug("milk"))    # customer 1
print(add_item_bug("bread"))   # customer 2 - wrongly also sees milk!


def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print("After the fix:")
print(add_item("milk"))
print(add_item("bread"))

# ---------- Challenge: Safe class copy ----------
print("\n--- Challenge: shallow and deep copy ---")
classes = {"A": ["Ali", "Sara"]}
shallow = copy.copy(classes)
deep = copy.deepcopy(classes)

shallow["A"].append("Ahmed")
deep["A"].append("Hina")

print("Original:", classes)
print("Shallow :", shallow)
print("Deep    :", deep)
# The shallow copy still shares the inner list with the original, so Ahmed
# shows up in both. The deep copy has its own inner list, so Hina is only there.
