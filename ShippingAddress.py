"""
lap times:
q1: 6:44
q2: 9:38
q3: 7:27
"""

"""
Part 1: Address Submission Validator

Design a class `ShippingAddress` to validate an address submitted via a JSON-based API.

Each address entry includes:

{
  "street": "string",
  "zipcode": "string",
  "country": "string"
}

Validation Rules:
1. street must be a non-empty string.
2. zipcode must be a string of exactly 5 digits (e.g., "90210").
3. country must be one of: "USA", "Canada", "UK"

If validation fails, raise a `ValueError` with one of these messages:
- "Street cannot be empty."
- "Zipcode must be a 5-digit number."
- "Country must be one of: USA, Canada, UK."
"""
import json

# Start your implementation here
class ShippingAddress:
    def __init__(self, input) -> None:
        store = input if isinstance(input, dict) else json.loads(input)
        for key in ["street", "zipcode", "country"]:
            if key not in store:
                raise KeyError(f"{key} missing!")

        # add to members
        self.street = store["street"]
        self.zipcode = store["zipcode"]
        self.country = store["country"]

        # validate data!
        if not isinstance(self.street, str) or not self.street:
            raise KeyError("street is wrong!")

        if not isinstance(self.zipcode, str) or len(self.zipcode) != 5 or not self.zipcode.isnumeric():
            raise KeyError("zipcode is wrong!")

        if not isinstance(self.country, str) or self.country not in {"USA", "Canada", "UK"}:
            raise KeyError("country is wrong!")

working = {
    "street": "ajskdfhljkasdfh",
    "zipcode": "12398",
    "country": "USA"
}

broke = {
    "street": "ajskdfhljkasdfh",
    "zipcode": "1234",
    "country": "USA"
}

# sa = ShippingAddress(working)
# print(sa.country)
# broke = ShippingAddress(broke)


"""
Part 2: AddressBook Manager

Create a class `AddressBook` to manage shipping addresses for multiple users.

Each address is associated with a `user_id` (string), and each user can only have **one** shipping address at a time.

Implement the following methods:

- add_address(user_id: str, data: dict) -> None
  - Validates and stores the address for the user.
  - Raises ValueError("User ID must be a non-empty string.") if invalid.
  - Overwrites the existing address for the user if already present.

- get_address(user_id: str) -> dict
  - Returns the address for the user.
  - Raises ValueError("Address not found for user.") if not present.

Each stored address should include:
{
  "street": "...",
  "zipcode": "...",
  "country": "...",
  "saved_at": "2025-06-23T04:20:00Z"
}
"""
from collections import defaultdict

# Start your implementation here
class AddressBook:
    def __init__(self) -> None:
        self.users = {}
        self.zipcodes = defaultdict(set)
        self.countries = defaultdict(set)

    def add_address(self, user_id: str, data: dict) -> None:
        if user_id in self.users:
            raise KeyError("user already exists!")

        try:
            sa = ShippingAddress(data)
        except KeyError as e:
            raise Exception(e)

        self.countries[sa.country].add(user_id)
        self.zipcodes[sa.zipcode].add(user_id)

        self.users[user_id] = sa

        
    def get_address(self, user_id: str) -> set:
        if user_id not in self.users:
            raise KeyError("user no exist!")
        return self.users[user_id].__dict__


    def get_users_by_country(self, country: str) -> list[str]:

        return list(self.countries[country])

    def get_users_by_zipcode(self, zipcode: str) -> list[str]:

        return list(self.zipcodes[zipcode])



ab = AddressBook()
# ab.add_address("hi!", working)

# print(ab.get_address("hi"))

arr = [
    {
    "street": "boing",
    "zipcode": "12398",
    "country": "USA"
    },
    {
    "street": "mandem",
    "zipcode": "12398",
    "country": "UK"
    },
    {
    "street": "ute",
    "zipcode": "12398",
    "country": "Canada"
    },
    {
    "street": "texas",
    "zipcode": "12398",
    "country": "USA"
    },
]

for i, item in enumerate(arr):
    ab.add_address(f"{i}", item)

print(ab.get_users_by_country("USA"))
print(ab.get_users_by_country("UK"))
print(ab.get_users_by_zipcode("12398"))
"""
Part 3: Address Filtering and Search

Extend `AddressBook` with filtering capabilities.

Implement:

- get_users_by_country(country: str) -> List[str]
  - Returns a list of user_ids whose address is in the specified country.
  - Raise ValueError("Invalid country.") if not in ["USA", "Canada", "UK"].

- get_users_by_zipcode(zipcode: str) -> List[str]
  - Returns a list of user_ids who live in the given 5-digit zipcode.
  - Raise ValueError("Zipcode must be a 5-digit number.") if invalid.
"""
# Start your implementation here
