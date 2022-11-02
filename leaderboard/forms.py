from django import forms
from django.forms import Form, ModelForm
from leaderboard.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
    comment = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": 'form-control validate mb-3 col-12 required',
            "id": 'comment_text',
        }
    ), label='', max_length=100)
