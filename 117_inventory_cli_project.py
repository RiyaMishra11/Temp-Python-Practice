# 117 Inventory CLI-Style Mini Project
from dataclasses import dataclass, asdict
import json

# 1 Product model
@dataclass
class Product:
    name: str
    price: float
    quantity: int

product = Product("Keyboard", 1500, 10)
print("1.", product)

# 2 Add product
inventory = {}

def add_product(product):
    inventory[product.name] = product

add_product(product)
print("2.", inventory)

# 3 Add multiple products
add_product(Product("Mouse", 500, 20))
add_product(Product("Monitor", 12000, 5))
print("3.", list(inventory))

# 4 Search product
def find_product(name):
    return inventory.get(name)

print("4.", find_product("Mouse"))

# 5 Update stock
def update_stock(name, amount):
    item = find_product(name)
    if item is None or item.quantity + amount < 0:
        return False
    item.quantity += amount
    return True

update_stock("Mouse", 5)
print("5.", find_product("Mouse"))

# 6 Sell product
def sell_product(name, amount):
    item = find_product(name)
    if item is None or item.quantity < amount:
        return False
    item.quantity -= amount
    return True

print("6.", sell_product("Keyboard", 3), find_product("Keyboard"))

# 7 Inventory value
def inventory_value():
    return sum(item.price * item.quantity for item in inventory.values())

print("7.", inventory_value())

# 8 Low-stock products
def low_stock(limit=5):
    return [item for item in inventory.values() if item.quantity <= limit]

print("8.", low_stock())

# 9 Sort by price
print("9.", sorted(inventory.values(), key=lambda item: item.price))

# 10 Save inventory
filename = "/mnt/data/inventory_117.json"
with open(filename, "w", encoding="utf-8") as file:
    json.dump([asdict(item) for item in inventory.values()], file, indent=2)

print("10. Saved:", filename)

# 11 Complete inventory report
def inventory_report():
    items = list(inventory.values())
    return {
        "products": len(items),
        "total_units": sum(item.quantity for item in items),
        "inventory_value": inventory_value(),
        "low_stock": [item.name for item in low_stock()],
        "most_expensive": max(items, key=lambda item: item.price).name,
    }

print("11.", inventory_report())
