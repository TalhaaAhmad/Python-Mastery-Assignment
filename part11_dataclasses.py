# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 11 - Type hints and dataclasses
import json
from dataclasses import dataclass, field, asdict

# ---------- Warm-up ----------
# I added type hints to all functions in part05_functions.py
# and ran:  mypy part05_functions.py
# mypy first complained that I passed list[int] where list[float] was
# expected. I changed the marks to 80.0, 72.0 ... and then it said:
# Success: no issues found in 1 source file


# ---------- Build: Product dataclass ----------
# compare=False means only the price is used when sorting (order=True)
@dataclass(order=True)
class Product:
    name: str = field(compare=False)
    price: float
    stock: int = field(compare=False)
    tags: list[str] = field(default_factory=list, compare=False)

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative")


products = [
    Product("Pen", 20.0, 100, ["stationery"]),
    Product("Notebook", 150.0, 0, ["stationery", "paper"]),
    Product("Bag", 1800.0, 5),
    Product("Calculator", 900.0, 0, ["electronics"]),
    Product("Ruler", 40.0, 30),
]

print("--- Build: out of stock products ---")
for p in products:
    if p.stock == 0:
        print(p.name, "is out of stock")

try:
    bad = Product("Broken", -5.0, 1)
except ValueError as error:
    print("Error:", error)

# ---------- Challenge: Save and load ----------
print("\n--- Challenge: save, load, sort ---")
data = [asdict(p) for p in products]
with open("products.json", "w") as file:
    json.dump(data, file, indent=4)
print("Saved products.json")

with open("products.json", "r") as file:
    loaded_data = json.load(file)
loaded_products = [Product(**d) for d in loaded_data]

for p in sorted(loaded_products):
    print(p.name, "- Rs", p.price)
