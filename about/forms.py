from django import forms
from django.forms.models import ModelForm
from about.models import Feedback
from django.utils.safestring import mark_safe

class FeedbackForm(forms.ModelForm):
    CHOICES=[('1','1'),
         ('2','2'),
         ('3','3'),
         ('4','4'),
         ('5','5')]
    ratings = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}))
    class Meta:
        model = Feedback
        fields =['pengirim','message','ratings']
        widgets = {'ratings':forms.RadioSelect}
        
form = FeedbackForm()