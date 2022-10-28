from django import forms
from django.forms import Form, ModelForm
from deposit.models import WasteDeposit
from banksampah.models import News

class DepositForm(ModelForm):
    class Meta:
        model = WasteDeposit
        fields = ['type', 'mass', 'description']
        widgets = {
            'type': forms.Select(),
            'mass': forms.NumberInput(attrs={'placeholder': '0.15'}),
            'description': forms.TextInput(attrs={'placeholder': 'Plastic bottles!'})
        }
        labels = {
            'type': 'Type',
            'mass': 'Mass (kg)',
            'description': 'Description'
        }