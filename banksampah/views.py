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


def news_add(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST)
        data = request.POST['data']
        data2 = ast.literal_eval(data)

        new_news = News()
        new_news.user = request.user
        new_news.date = timezone.now().strftime("%Y-%m-%d")
        new_news.description = data2['description']
        new_news.title = data2['title']
        new_news.save()

        return HttpResponseRedirect(reverse("banksampah:news"))
    else:
        return redirect('banksampah:news')

    # if request.method == "POST":
    #     data = json.loads(request.POST['data'])

    #     new_news = News(title=data["title"], description=data["description"], user=request.user)
    #     new_news.save()

    #     return HttpResponse(serializers.serialize("json", [new_news]), content_type="application/json")

    # return HttpResponse()

@csrf_exempt
def news_delete(request, news_id):
    if request.method == "POST":
        news = get_object_or_404(News, pk=news_id, user=request.user)
        news.delete()

    return HttpResponse()

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
        'total_mass': sum(mass),
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
        new_total.append(num)

    net_footprint = (new_total[0] * 249 + new_total[1] * -454 + new_total[2] * -2088 + new_total[3] * -3247) / 1000
    new_total.append(net_footprint)
    return new_total

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('banksampah:login')
    
    context = {'form':form, 'user':request.user}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("banksampah:home")) # membuat response
            response.set_cookie('username', username)
            response.set_cookie('last_login', timezone.now().strftime("%b. %d, %Y %H:%M:%S")) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('banksampah:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('username')
    return redirect('banksampah:login')
