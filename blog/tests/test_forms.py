from django.test import SimpleTestCase
from blog.forms import CommentForm


class TestForms(SimpleTestCase):

    def test_comment_form_valid(self):
        form = CommentForm(data={
            "body": "Great Recipe!"
        })
        self.assertTrue(form.is_valid())
    
    def test_comment_form_invalid(self):
        form = CommentForm(data={
            "body": "Great Recipe!"
        })
        self.assertFalse(form.is_valid)

