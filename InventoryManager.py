# COMPLETED PART 1 in 8:45
# P2 in 5:50
# TESTING P2 in 2:22

"""
Part 1: Product Entry Validation

Design a class called `Product` to validate a product entry submitted via a JSON-based API.

Each product entry is expected to have the following fields:

{
  "product_id": "string",
  "price": float,
  "in_stock": boolean
}

Validation Rules:
1. product_id must be a non-empty alphanumeric string.
2. price must be a non-negative float or integer.
3. in_stock must be a boolean.

If validation fails, raise a `ValueError` with one of these messages:
- "Product ID must be a non-empty alphanumeric string."
- "Price must be a non-negative number."
- "In-stock must be a boolean value."
"""
import json
import datetime
from pickle import decode_long

# Start your implementation here
class Product:
    def __init__(self, input) -> None:
        # parse data
        # dict or string
        info_dict = input if isinstance(input, dict) else json.loads(input)
        for key in ["product_id", "price", "in_stock"]:
            if key not in info_dict:
                raise KeyError(f"missing key: {key}")

        # fields are included
        # add to member fields
        self.product_id = info_dict["product_id"]
        self.price = info_dict["price"]
        self.in_stock = info_dict["in_stock"]
        self.date = datetime.datetime.now()
        

        # validate data
        # 1. product_id must be a non-empty alphanumeric string.
        if not isinstance(self.product_id, str) or len(self.product_id) == 0 or not self.product_id.isalnum():
            raise KeyError("product_id is incompatible!")
        # 2. price must be a non-negative float or integer.
        if not isinstance(self.price, (float, int)) or self.price < 0:
            raise KeyError("price is incompatible!")
        # 3. in_stock must be a boolean.
        if not isinstance(self.in_stock, bool):
            raise KeyError("in_stock is incompatible!")

works = {
    "product_id": "98123423qr",
    "price": float(12312.000),
    "in_stock": False
}

p = Product(works)

print(p.in_stock, p.price, p.product_id)

"""
Part 2: Inventory Manager

Create a class `InventoryManager` to store and manage multiple validated `Product` entries.

Requirements:
1. Store products in a dictionary keyed by product_id.
2. Add a timestamp (UTC ISO format) for when the product was added.

Implement the following methods:

- add_product(data: dict) -> None
  - Validates and stores the product.
  - Raises ValueError("Product ID already exists.") if duplicate.

- update_product(product_id: str, updates: dict) -> None
  - Allows updating price and/or in_stock.
  - Re-validates updated fields.
  - Raises ValueError("Product not found.") if the product_id doesn't exist.

- delete_product(product_id: str) -> None
  - Removes the product.
  - Raises ValueError("Product not found.") if missing.

Each stored product should be a dictionary of:
{
  "product_id": str,
  "price": float,
  "in_stock": bool,
  "added_at": "2025-06-23T03:48:00Z"
}
"""
# Start your implementation here

class InventoryManager:
    def __init__(self) -> None:
        self.store = {}

    def add_product(self, data: dict) -> None:
        try:
            p = Product(data)
        except KeyError as e:
            print(e)
            return

        if p.product_id not in self.store:
            self.store[p.product_id] = p
            return
        else:
            raise KeyError("product_id taken!")

    def update_product(self, product_id: str, updates: dict) -> None:
        self.delete_product(product_id)
        self.add_product(updates)

    def delete_product(self, product_id: str) -> None:
        if product_id not in self.store:
            raise KeyError("product not found!")

        self.store.pop(product_id)


im = InventoryManager()


works = {
    "product_id": "98123423qr",
    "price": float(12312.000),
    "in_stock": False
}

works2 = {
    "product_id": "works2",
    "price": float(12312.000),
    "in_stock": False
}

updatedworks = {
    "product_id": "updated",
    "price": float(12312.000),
    "in_stock": False
}

im.add_product(works)
im.add_product(works2)
im.update_product("98123423qr", updatedworks)
print(im.store)
im.delete_product("works2")
print(im.store)
