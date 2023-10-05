from lib.post import Post

'''Constructs with fields'''
def test_post_constructs():
    post = Post(1, 'How to make great cakes')
    assert post.id == 1
    assert post.title == 'How to make great cakes'


'''Construct with equality'''
def test_posts_are_equal():
    post1 = Post(1, 'Test Post')
    post2 = Post(1, 'Test Post')
    
    assert post1 == post2
    
    
'''Constructs so it looks pretty'''
def test_posts_format_nicely():
    post = Post(1, 'Test Post')
    assert str(post) == "Post(1, Test Post)"