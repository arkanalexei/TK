from deposit.forms import DepositForm
from deposit.models import WasteDeposit
from deposit.wastes import *
from leaderboard.models import Achiever

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
    ''' Retrieve user's deposit history in JSON form'''
    current_user = request.user
    data = WasteDeposit.objects.filter(user=current_user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='banksampah:login')
def get_achiever(request):    
    ''' Retrieve user's points (Achiever model from Leaderboard app) in JSON form.'''
    current_user = request.user
    data = Achiever.objects.filter(user=current_user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def deposit_sampah(request):
    ''' Show the main /deposit/ page. '''
    # ------- See deposit history if logged in -------
    if request.user.is_authenticated:
        if Achiever.objects.filter(user=request.user): # if user already has points, proceed
            achiever = Achiever.objects.filter(user=request.user).get()
        else: # if user has no points, create new Achiever object to store user's points
            achiever = Achiever()
            achiever.user = request.user
            achiever.name = request.user.username
            achiever.points = 0
            achiever.save()
            
        username = request.COOKIES['username']
        request.session['is_logged_in'] = True
    
    # ------- Limit page display if not logged in -------
    else:
        username = "None"
        request.session['is_logged_in'] = False
        
    is_logged_in = request.session['is_logged_in']
    context = { 'deposit_form': DepositForm(auto_id=False), 
                'username': username,
                'is_logged_in' : is_logged_in
                }
    return render(request, "deposit.html", context=context)

    
@require_http_methods(["POST"])
def submit_form(request):
    ''' Submit a new deposit. '''
    
    # --- if user is logged in, allow them to submit new deposit ---
    if request.method == "POST":
        form = Form(request.POST)
        print("Form submitted!\n")
        
        # --- session & form validation ---
        if request.session['is_logged_in'] and form.is_valid(): # validation
            # Save form data as new WasteDeposit object
            desc, type, mass = form.data['description'], form.data['type'], form.data['mass']
            if (float(mass) > 0 and type != ""):
                new_deposit = WasteDeposit()
                new_deposit.user = request.user
                new_deposit.date_time = dt.now()
                new_deposit.description = desc
                new_deposit.type = type
                new_deposit.mass = mass
                new_deposit.save()
            
                # increment points to existing Achiever object
                achiever = Achiever.objects.filter(user=request.user).get()
                achiever.points += int(float(mass) * get_waste_points(type))
                achiever.save()
            
            messages.add_message(request, messages.SUCCESS, "Deposit submitted successfully") # todo
            response = HttpResponseRedirect(reverse("deposit:deposit_sampah"))
            return response
            
        else: # if user is not logged in
            return redirect('banksampah:login')
        
def show_deposit_by_id(request, id):
    ''' Show complete information of a single deposit'''
    data = WasteDeposit.objects.filter(user=request.user, pk=id)
    if data: # if deposit exists AND was made by the user
        data = data.get()
        is_data_exist = True
    else:   # do not show data
        data = "ERROR"
        is_data_exist = False
        
    context = {
        'is_display': request.session['is_logged_in'] and is_data_exist,
        'data': data,
    }
    return render(request, "single_deposit.html", context=context)