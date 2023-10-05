class Post:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.id == other.id and self.title == other.title
        return False

    def __repr__(self):
        return f"Post({self.id}, {self.title})"