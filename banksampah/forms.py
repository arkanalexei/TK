from ast import Mod
from django.forms import Form, ModelForm
from banksampah.models import WasteDeposit

class DepositForm(ModelForm):
    class Meta:
        model = WasteDeposit
        fields = ['type', 'description', 'mass']