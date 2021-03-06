from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_post_status_defaults_to_draft(self):
        user = User.objects.create(username='testname')
        recipe = Post.objects.create(
            title='recipe1',
            author=user
        )
        self.assertFalse(recipe.status)

    def test_comment_approved_defaults_to_false(self):
        user = User.objects.create(username='testname')
        recipe = Post.objects.create(
            title='recipe1',
            author=user
        )
        comment = Comment.objects.create(
            post=recipe,
            body='recipe comment',
        )
        self.assertFalse(comment.approved)

    def test_post_string_method_returns_title(self):
        user = User.objects.create(username='testname')
        recipe = Post.objects.create(
            title='recipe1',
            author=user
        )
        self.assertEquals(str(recipe), 'recipe1')

    def test_comment_string_method_returns_comment(self):
        user = User.objects.create(username='testname')
        recipe = Post.objects.create(
            title='recipe1',
            author=user
        )
        comment = Comment.objects.create(
            post=recipe,
            name=user,
            body='recipe comment',
        )
        self.assertEquals(str(comment), 'Comment recipe comment by testname')
