from django import forms
from banksampah.models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description']