from django.shortcuts import render
from banksampah.models import WasteDeposit
from banksampah.forms import DepositForm

# Create your views here.

def home(request):
    return render(request, "home.html")

# @login_required(...)
def deposit_sampah(request):
    context = {'form': DepositForm()}
    return render(request, "deposit.html", context=context)