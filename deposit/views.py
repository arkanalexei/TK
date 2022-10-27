from deposit.models import WasteDeposit
from banksampah.models import News
from banksampah.forms import DepositForm
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

@login_required(login_url='banksampah:login')
def get_user_deposits(request):    
    current_user = request.user
    data = WasteDeposit.objects.filter(user=current_user) # TODO: reverse this queryset
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def deposit_sampah(request):
    # if user is logged in, allow to see deposit history
    if request.user.is_authenticated:
        username = request.COOKIES['username']
        request.session['is_logged_in'] = True
        is_logged_in = True
        
    # if user is not logged in
    else:
        username = "None"
        is_logged_in = False
        
    context = { 'form': DepositForm, 
                'username': username,
                'is_logged_in' : is_logged_in,
                'action_button_label' : 'Make Deposit' if is_logged_in else 'Login to Make Deposit'}
    return render(request, "deposit.html", context = context)
    
def submit_form(request):
    # if user is logged in, allow them to submit new deposit
    print(request.session.items())
    
    if request.method == "POST":
        form = Form(request.POST)
        if request.user.is_authenticated and form.is_valid():
            new_deposit = WasteDeposit()
            new_deposit.user = request.user
            new_deposit.date_time = dt.now()
            new_deposit.description = form.data['description']
            new_deposit.type = form.data['type']
            new_deposit.mass = form.data['mass']
            new_deposit.save()
            
            response = HttpResponseRedirect(reverse("deposit:deposit_sampah"))
            return response
            
        else: # if user is not logged in
            return redirect('banksampah:login')
    
    else: # wrong request method
        return redirect('deposit:deposit_sampah')