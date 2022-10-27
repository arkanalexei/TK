from django import forms
from django.forms import Form, ModelForm
from deposit.models import WasteDeposit
from banksampah.models import News

class DepositForm(ModelForm):
    class Meta:
        model = WasteDeposit
        fields = ['type', 'mass']
    description = forms.CharField(widget=forms.TextInput)