from django.shortcuts import render
from banksampah.models import WasteDeposit
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from banksampah.forms import DepositForm

# Create your views here.

def home(request):
    return render(request, "home.html")

# @login_required(...)
def deposit_sampah(request):
    context = {'form': DepositForm()}
    return render(request, "deposit.html", context=context)



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
            response.set_cookie('last_login', timezone.now.strftime("%b. %d, %Y %H:%M:%S")) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('banksampah:login'))
    response.delete_cookie('last_login')
    return redirect('banksampah:login')
