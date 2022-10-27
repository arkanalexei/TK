from django.forms import Form, ModelForm
from deposit.models import WasteDeposit
from banksampah.models import News

class DepositForm(ModelForm):
    class Meta:
        model = WasteDeposit
        fields = ['type', 'description', 'mass']

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description']