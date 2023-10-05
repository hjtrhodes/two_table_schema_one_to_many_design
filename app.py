from lib.post_repository import PostRepository
from lib.database_connection import DatabaseConnection
from lib.post import Post
from lib.comment import Comment

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/blog_posts_tags.sql")

    def run(self):
        user = input("Enter the post_id to see comments: ")
        post_repository = PostRepository(self._connection)
        posts = post_repository.find_with_comments(user)
        for post in posts:
            print(post)


if __name__ == '__main__':
    app = Application()
    app.run()
