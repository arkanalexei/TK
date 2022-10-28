from django import forms
from django.forms import Form, ModelForm
from leaderboard.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
    comment = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": 'form-control validate mb-3',
            "id": 'comment',
        }
    ), label='', max_length=100)
