from django import forms
from django.forms import Form, ModelForm
from tukarpoin.models import Perks

class TukarPoinForm(ModelForm):
    class Meta:
        model = Perks
        fields = ['nama', 'deskripsi', 'harga']
        labels = {
            'nama': 'Nama',
            'deskripsi': 'Deskripsi',
            'harga': 'Harga'
        }