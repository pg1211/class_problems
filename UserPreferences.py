"""
part1 time w/ testing/debugging: 6:50

part2 time: 4:07
part2 debugging/testing time: 2:31
"""

"""
Part 1: User Preferences Validator

Design a class `UserPreferences` to validate configuration settings submitted by users.

Each preference entry has the following fields:

{
  "theme": "string",
  "notifications_enabled": boolean,
  "font_size": integer
}

Validation Rules:
1. theme must be one of the following strings: "light", "dark", "system"
2. notifications_enabled must be a boolean
3. font_size must be an integer between 10 and 30 inclusive

If validation fails, raise a `ValueError` with one of these messages:
- "Theme must be 'light', 'dark', or 'system'."
- "Notifications_enabled must be a boolean."
- "Font size must be between 10 and 30."
"""
import json

# Start your implementation here
class UserPreferences:
    def __init__(self, input) -> None:
        # parse data into member fields
        store = input if isinstance(input, dict) else json.loads(input)

        for key in ["theme", "notifications_enabled", "font_size"]:
            if key not in store:
                raise KeyError(f"missing key: {key}")

        # validate data with error handling
        self.theme = store["theme"]
        self.notifications_enabled = store["notifications_enabled"]
        self.font_size = store["font_size"]


        # - "Theme must be 'light', 'dark', or 'system'."
        # - "Notifications_enabled must be a boolean."
        # - "Font size must be between 10 and 30."
        if not isinstance(self.theme, str) or self.theme  not in {"light", "dark", "system"}:
            raise KeyError("Theme must be 'light', 'dark', or 'system'.")
        
        if not isinstance(self.notifications_enabled, bool):
            raise KeyError("Notifications_enabled must be a boolean.")
        
        if not isinstance(self.font_size, int) or not 10 <= self.font_size <= 30:
            raise KeyError("Font size must be between 10 and 30.")

working = {
    "theme": "light",
    "notifications_enabled": True,
    "font_size": 25
}

nonworking = {
    "theme": "light",
    "notifications_enabled": True,
    "font_size": 25
}

up = UserPreferences(nonworking)

print(up.theme, up.notifications_enabled, up.font_size)


"""
Part 2: PreferencesManager

Create a class `PreferencesManager` to manage preferences for multiple users.

Each user is identified by a `user_id` (string).

Implement the following methods:

- set_preferences(user_id: str, data: dict) -> None
  - Validates and stores preferences for the user.
  - Raises ValueError if validation fails or if user_id is empty.

- get_preferences(user_id: str) -> dict
  - Returns the stored preferences for the given user_id.
  - Raises ValueError("User not found.") if not found.

Store each user’s preferences in the format:
{
  "theme": "dark",
  "notifications_enabled": True,
  "font_size": 14,
  "updated_at": "2025-06-23T04:10:00Z"
}
"""
# Start your implementation here
class PreferencesManager:
    def __init__(self) -> None:
        self.users = {}

    def set_preferences(self, user_id: str, data: dict) -> None:
        if not user_id:
            raise ValueError("user_id empty!")

        try:
            u = UserPreferences(data)
        except KeyError as e:
            raise ValueError(e)
        
        self.users[user_id] = u
    
    def get_preferences(self, user_id: str) -> dict:
        if user_id not in self.users:
            raise ValueError("User not found.")

        return self.users[user_id]

pm = PreferencesManager()
pm.set_preferences("w", working)
print(pm.get_preferences("w").theme)
print(pm.set_preferences("ooops", nonworking))
print(pm.set_preferences("w", nonworking))
print(pm.get_preferences("w").theme)
