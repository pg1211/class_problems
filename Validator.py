# Requirements:
# Create a class to parse and store the input.

# Validation logic:

# title must be non-empty and under 100 characters.

# content must be at least 50 characters.

# tags must be a list of strings, each alphanumeric and lowercase.

# Error messages:

# "Title cannot be empty or longer than 100 characters."

# "Content must be at least 50 characters."

# "Tags must be lowercase, alphanumeric strings."

# input_format = {
#   "title": "string",
#   "content": "string",
#   "tags": ["string", ...]
# }
import json

class Validator:
    # parse data
    def __init__(self, input) -> None:
        my_dict = input if isinstance(input, dict) else json.loads(input)
        for key in ["title", "content", "tags"]:
            if key not in my_dict:
                raise KeyError(f"missing input: {key}")

        # assign data to class members
        self.title = my_dict["title"]
        self.content = my_dict["content"]
        self.tags = my_dict["tags"]

        # validate data
        if not self.title or len(self.title) >= 100:
            raise KeyError("Title cannot be empty or longer than 100 characters.")

        if len(self.content) < 50:
            raise KeyError("Content must be at least 50 characters.")

        if isinstance(self.tags, list):
            for tag in self.tags:
                if not tag == tag.lower() or not tag.isalnum():
                    raise KeyError("Tags must be lowercase, alphanumeric strings.")

working = {
  "title": "string",
  "content": "strinjasldjflasdjfjasd;gfj;asdgoias fgioasjgoifpnads;lfcnaepsoincfiopascoahsdocmfsadlmcfgiasdfjasdhflkadhsfghadsgfhadsfaasdnhopfiasdhpogxfhnsqopughxg",
  "tags": ["string", "asdfasd", "uasdgiouhasdg", "fanfic"]
}

nonworking = {
  "title": "asdfas",
  "content": "strinjasldjflasdjfjasd;gfj;asdgoias fgioasjgoifpnads;lfcnaepsoincfiopascoahsdocmfsadlmcfgiasdfjasdhflkadhsfghadsgfhadsfaasdnhopfiasdhpogxfhnsqopughxg",
  "tags": ["string", "asdi", "uasdgiouha/sdg", "fanfic"]
}

v = Validator(nonworking)
print(v.content, v.tags, v.title)
