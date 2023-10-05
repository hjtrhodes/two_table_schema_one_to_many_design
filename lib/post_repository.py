from lib.post import Post
from lib.comment import Comment

class PostRepository:
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        posts = []
        for row in rows:
            post = Post(row["id"], row["title"])
            posts.append(post)
        return posts

    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            "SELECT posts.id AS post_id, posts.title, comments.id, comments.content FROM posts JOIN comments ON posts.id = comments.post_id WHERE posts.id = %s", [post_id])
        comments = []
        for row in rows:
            comment = Comment(row["post_id"], row["title"], row["content"])
            comments.append(comment)
        return comments