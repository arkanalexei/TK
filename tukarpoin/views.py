from django.shortcuts import render

from deposit.views import get_user_deposits
from tukarpoin.models import Tukarpoin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def show_tukarpoin(request):
    tukar_poin = Tukarpoin.objects.all()
    context = { #context blm lengkap
        'tampung_poin': tukar_poin,
    }
    return render(request, "tukarpoin.html", context)


