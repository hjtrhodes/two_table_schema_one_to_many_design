from lib.comment import Comment

'''Constructs with fields'''
def test_comment_constructs():
    comment = Comment(1, 'Test Comment', 1)
    assert comment.id == 1
    assert comment.content == 'Test Comment'
    assert comment.post_id == 1

'''Construct with equality'''
def test_comments_are_equal():
    comment1 = Comment(1, 'Test Comment', 3)
    comment2 = Comment(1, 'Test Comment', 3)
    
    assert comment1 == comment2
    
    
'''Constructs so it looks pretty'''
def test_comments_format_nicely():
    comment = Comment(1, 'Test Comment', 3)
    assert str(comment) == "Comment(1, Test Comment, 3)"