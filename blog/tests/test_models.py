from django.test import TestCase
from blog.models import Post, Comment


class TestModels(TestCase):

    def test_post_status_defaults_to_draft(self):
        recipe = Post.objects.create(
            title='recipe1',
            author='user1'
        )
        self.assertFalse(recipe.status)
    
    def test_comment_approved_defaults_to_false(self):
        comment = Comment.objects.create(
            name='user1',
            body='recipe comment',
            post_id='1'
        )
        self.assertFalse(comment.approved)
