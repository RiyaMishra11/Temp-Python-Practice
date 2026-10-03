"""98 - Inventory Manager"""
import json
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class Product:
    product_id: int
    name: str
    quantity: int
    price: float

class Inventory:
    def __init__(self, filename="inventory.json"):
        self.filename = Path(filename)
        self.products = self.load()

    def load(self):
        if not self.filename.exists():
            return []
        try:
            data = json.loads(self.filename.read_text(encoding="utf-8"))
            return [Product(**item) for item in data]
        except (json.JSONDecodeError, OSError, TypeError):
            return []

    def save(self):
        self.filename.write_text(
            json.dumps([asdict(p) for p in self.products], indent=2),
            encoding="utf-8"
        )

    def add_product(self, name, quantity, price):
        new_id = max((p.product_id for p in self.products), default=0) + 1
        self.products.append(Product(new_id, name, quantity, price))
        self.save()
        return new_id

    def update_stock(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = quantity
                self.save()
                return True
        return False

    def total_value(self):
        return sum(p.quantity * p.price for p in self.products)

def main():
    inventory = Inventory()
    inventory.add_product("Keyboard", 10, 1200)
    inventory.add_product("Mouse", 15, 600)
    print("Products:", inventory.products)
    print("Total value:", inventory.total_value())

if __name__ == "__main__":
    main()
