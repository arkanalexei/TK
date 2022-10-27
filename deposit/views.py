from deposit.models import WasteDeposit
from deposit.forms import DepositForm
from django.shortcuts import render, redirect
from django.forms import Form
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime as dt

@login_required(login_url='banksampah:login')
def get_user_deposits(request):    
    current_user = request.user
    data = WasteDeposit.objects.filter(user=current_user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def deposit_sampah(request):
    # if user is logged in, allow to see deposit history
    if request.user.is_authenticated:
        username = request.COOKIES['username']
        request.session['is_logged_in'] = True
        
    # if user is not logged in
    else:
        username = "None"
        request.session['is_logged_in'] = False
        
    is_logged_in = request.session['is_logged_in']
    context = { 'form': DepositForm, 
                'username': username,
                'is_logged_in' : is_logged_in}
    return render(request, "deposit.html", context = context)
    
@require_http_methods(["POST"])
def submit_form(request):
    # if user is logged in, allow them to submit new deposit
    if request.method == "POST":
        form = Form(request.POST)
        if request.session['is_logged_in'] and form.is_valid():
            new_deposit = WasteDeposit()
            new_deposit.user = request.user
            new_deposit.date_time = dt.now()
            new_deposit.description = form.data['description']
            new_deposit.type = form.data['type']
            new_deposit.mass = form.data['mass']
            new_deposit.save()
            
            messages.add_message(request, messages.SUCCESS, "Deposit submitted successfully")
            response = HttpResponseRedirect(reverse("deposit:deposit_sampah"))
            return response
            
        else: # if user is not logged in
            return redirect('banksampah:login')
    
    else: # wrong request method
        return redirect('deposit:deposit_sampah')