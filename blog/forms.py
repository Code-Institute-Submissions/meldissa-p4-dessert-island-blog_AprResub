from .models import Comment
from django import forms


"""
Please note code was used from the Code Institute I Think Therefore I Blog
tutorial to help create this project.
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
