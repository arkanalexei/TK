from django.shortcuts import render
from banksampah.models import WasteDeposit

# Create your views here.

def home(request):
    return render(request, "home.html")

# @login_required(...)
def deposit_sampah(request):
    context = {}
    return render(request, "deposit.html", context=context)