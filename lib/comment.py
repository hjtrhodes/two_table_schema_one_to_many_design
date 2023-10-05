class Comment:
    def __init__(self, id, content, post_id):
        self.id = id
        self.content = content
        self.post_id = post_id

    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.id == other.id and self.content == other.content and self.post_id == other.post_id
        return False
    
    def __repr__(self):
        return f"Comment({self.id}, {self.content}, {self.post_id})"