from hashlib import new
from deposit.models import WasteDeposit
from banksampah.models import News
from deposit.forms import DepositForm
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import Form
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime as dt
from django.contrib.admin.views.decorators import staff_member_required
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from banksampah.forms import NewsForm
import ast
from leaderboard.models import Achiever
from django.http import JsonResponse

# Create your views here.

def read_more(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {
        'news': news
    }
    return render(request, "read_more.html", context)

@login_required(login_url="/login")
def news(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    form = NewsForm()

    context = {
        'num_visits': num_visits,
        'form': form
    }

    return render(request, "news.html", context)


@csrf_exempt
def news_add(request):
    if request.method == "POST":
        print(request.POST.dict())
        data = request.POST.dict()
        # print(json.loads(request.POST['data']))
        # data = json.loads(request.POST['data'])

        new_news = News(title=data["title"], description=data["description"], user=request.user)
        new_news.save()

        return JsonResponse({
            "status": True,
            "message": "Successfully Added News!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        # return HttpResponse(serializers.serialize("json", [new_news]), content_type="application/json")
    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to add news, check your input."
            }, status=401)
    # return HttpResponse()

@csrf_exempt
def news_delete(request, news_id):
    if request.method == "POST":
        news = get_object_or_404(News, pk=news_id, user=request.user)
        news.delete()

        return JsonResponse({
            "status": True,
            "message": "Successfully Deleted News!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)

    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to delete news, check your permission."
            }, status=401)

    # return HttpResponse()

def news_json(request):
    news = News.objects.all()
    return HttpResponse(serializers.serialize("json", news), content_type="application/json")

def home(request):
    mass = [0,0,0,0,0]
    is_logged_in = request.user.is_authenticated
    if is_logged_in:
        mass = get_mass(request)

    context = {
        'is_logged_in': is_logged_in,
        'mass_plastik': mass[0],
        'mass_kaca': mass[1],
        'mass_kertas': mass[2],
        'mass_organik': mass[3],
        'total_mass': mass[0]+mass[1]+mass[2]+mass[3],
        'net_footprint':mass[4]
    }

    return render(request, "home.html", context)

def get_mass(request):
    current_user = request.user
    data = WasteDeposit.objects.filter(user=current_user)

    total_plastik = 0
    total_kaca = 0
    total_kertas = 0
    total_organik = 0

    data_plastik = data.filter(type="PLASTIK")
    data_kaca = data.filter(type="KACA")
    data_kertas = data.filter(type="KERTAS")
    data_organik = data.filter(type="ETC")
    
    for data in data_plastik:
        total_plastik += data.mass

    for data in data_kaca:
        total_kaca += data.mass
    
    for data in data_kertas:
        total_kertas += data.mass

    for data in data_organik:
        total_organik += data.mass

    total = [total_plastik, total_kaca, total_kertas, total_organik]
    new_total = []
    for num in total:
        if str(num).endswith('.0'):
            num = int(num)
        else:
            num = round(num, 2)
        new_total.append(num)

    net_footprint = (new_total[0] * 249 + new_total[1] * -454 + new_total[2] * -2088 + new_total[3] * -3247) / 1000
    new_total.append(net_footprint)
    total_mass = new_total[0] + new_total[1] + new_total[2] + new_total[3]
    new_total.append(total_mass)
    return new_total

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            # return redirect('banksampah:login')
            return JsonResponse({
            "status": True,
            "message": "Successfully Registered User!",
            "success": True,
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to register, check your input.",
            }, status=401)
    
    context = {'form':form, 'user':request.user}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            admin = False
            if user.is_superuser:
                admin = True

            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("banksampah:home")) # membuat response
            response.set_cookie('username', username)
            response.set_cookie('last_login', timezone.now().strftime("%b. %d, %Y %H:%M:%S")) # membuat cookie last_login dan menambahkannya ke dalam response
            
            mass = get_mass(request)


            if Achiever.objects.filter(user=request.user): # if user already has points, proceed
                achiever = Achiever.objects.filter(user=request.user).get()
            else: # if user has no points, create new Achiever object to store user's points
                achiever = Achiever()
                achiever.user = request.user
                achiever.name = request.user.username
                achiever.points = 0
                achiever.save()

            
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!",
            "admin": admin,
            "username": username,
            'mass': mass,
            'points': achiever.points
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            messages.info(request, 'Username atau Password salah!')
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
            }, status=401)
    context = {}
    return render(request, 'login.html', context)


@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('banksampah:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('username')

    return JsonResponse({
            "status": True,
            "message": "Successfully Logged Out!",
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
    # return redirect('banksampah:login')
