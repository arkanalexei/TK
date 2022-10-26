from ast import Mod
from django.forms import Form, ModelForm
from banksampah.models import *

class DepositForm(ModelForm):
    class Meta:
        model = WasteDeposit
        fields = ['type', 'description', 'mass']

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description']