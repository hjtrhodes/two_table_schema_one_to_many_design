# Test-drive an AlbumRepository class that has a method all that returns a list of Album objects.
from lib.post_repository import PostRepository
from lib.database_connection import DatabaseConnection
from lib.comment import Comment

"""
Test find by Tag returns correct output
"""
def test_get_post_from_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository

    posts = repository.find_with_comments(1)

    # Assert on the results
    assert posts == [
        Comment(1, "How to use Git", "I am a Git pro now!"),
        Comment(1, "How to use Git", "You are da bomb!")
    ]
