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
import datetime

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
        self.created_at = datetime.datetime.now

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

# v = Validator(nonworking)
# print(v.content, v.tags, v.title)

# Create a BlogManager class that:

# Stores all valid blog posts in a list.

# Automatically attaches a UTC timestamp to each post on insertion.

# Provide a method add_post(blog_data: dict) that:

# Validates and stores the post if valid.

# Returns errors if invalid.

# Provide a method get_all_posts() that:

# Returns a list of all blog posts sorted in reverse chronological order.

# Example stored blog post structure:
# {
#   "title": "My Blog Title",
#   "content": "...",
#   "tags": ["python", "api"],
#   "created_at": "2025-06-23T03:42:11Z"
# }

class BlogManager:
    def __init__(self) -> None:
        # ordered DS for posts
        self.posts = []


    def add_post(self, blog_data: dict):
        # validated
        try:
            v = Validator(blog_data)
        except KeyError as e:
            print(e)
            return
        
        self.posts.append(v)
        return
    
    def get_all_posts(self):
        # returns posts in reverse chronological order
        return list(reversed(self.posts))


b = BlogManager()

working = {
  "title": "string",
  "content": "strinjasldjflasdjfjasd;gfj;asdgoias fgioasjgoifpnads;lfcnaepsoincfiopascoahsdocmfsadlmcfgiasdfjasdhflkadhsfghadsgfhadsfaasdnhopfiasdhpogxfhnsqopughxg",
  "tags": ["string", "asdfasd", "uasdgiouhasdg", "fanfic"]
}

working1 = {
  "title": "string1",
  "content": "strinjasldjflasdjfjasd;gfj;asdgoias fgioasjgoifpnads;lfcnaepsoincfiopascoahsdocmfsadlmcfgiasdfjasdhflkadhsfghadsgfhadsfaasdnhopfiasdhpogxfhnsqopughxg",
  "tags": ["string", "uasdgiouhasdg", "fanfic"]
}

working2 = {
  "title": "string2",
  "content": "strinjasldjflasdjfjasd;gfj;asdgoias fgioasjgoifpnads;lfcnaepsoincfiopascoahsdocmfsadlmcfgiasdfjasdhflkadhsfghadsgfhadsfaasdnhopfiasdhpogxfhnsqopughxg",
  "tags": ["string", "asdfasd", "uasdgiouhasdg", "fanfic"]
}

working3 = {
  "title": "string3",
  "content": "strinjasldjflasdjfjasd;gfj;asdgoias fgioasjgoifpnads;lfcnaepsoincfiopascoahsdocmfsadlmcfgiasdfjasdhflkadhsfghadsgfhadsfaasdnhopfiasdhpogxfhnsqopughxg",
  "tags": ["string", "asdfasd", "uasdgiouhasdg", "fanfic"]
}


b.add_post(working)
b.add_post(working1)
b.add_post(working2)
b.add_post(working3)
print(b.get_all_posts())
