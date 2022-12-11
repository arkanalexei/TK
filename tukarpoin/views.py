from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tukarpoin.forms import TukarPoinForm
from tukarpoin.models import Perks
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from leaderboard.models import Achiever
from django.shortcuts import get_object_or_404
# Create your views here.

def tukar_poin(request):
    if Achiever.objects.filter(user=request.user): # if user already has points, proceed
        achiever = Achiever.objects.filter(user=request.user).get()
    else: # if user has no points, create new Achiever object to store user's points
        achiever = Achiever()
        achiever.user = request.user
        achiever.name = request.user.username
        achiever.points = 0
        achiever.save()

    context = {
        'form_poin': TukarPoinForm(),
        'perks': Perks.objects.all(),
        'poinz': achiever.points,
    }
    return render(request, "tukar_poin.html", context)

@csrf_exempt
def redeem(request, perk_id):
    if request.method == "POST":
        perk = get_object_or_404(Perks, pk=perk_id)
        if Achiever.objects.filter(user=request.user) and perk:
            achiever = Achiever.objects.filter(user=request.user).get()
            achiever.points -= perk.harga
            perk.delete()
            achiever.save()

            return JsonResponse({
            "status": True,
            "message": "Berhasil ditukar"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": "Tidak berhasil ditukar"
            }, status=401)

def tukar_poin_json(request):
    perk = Perks.objects.all()
    return HttpResponse(serializers.serialize("json", perk), content_type="application/json")

@csrf_exempt
def tambah_perk(request):
    form = TukarPoinForm()
    if request.method == "POST":
        form = TukarPoinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perk berhasil dibuat')
            return JsonResponse({
                "status": True,
                "message": "Berhasil",
            }, status=200)
        
    else:
        return JsonResponse({
            "status": False,
            "message": "Tidak berhasil",
        }, status = 401)