from django.forms import Form, ModelForm
from deposit.models import WasteDeposit
from banksampah.models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description']