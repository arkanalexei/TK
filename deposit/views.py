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
from django.http import JsonResponse
from django.views.decorators import csrf
import json

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
        try:
            username = request.COOKIES['username']
        except:
            print("A logged-in user tried to access /deposit/ without valid cookies. Setting cookie manually.")
            request.COOKIES['username'] = request.user.username
        
        if Achiever.objects.filter(user=request.user): # if user already has points, proceed
            achiever = Achiever.objects.filter(user=request.user).get()
        else: # if user has no points, create new Achiever object to store user's points
            achiever = Achiever()
            achiever.user = request.user
            achiever.name = request.user.username
            achiever.points = 0
            achiever.save()
            
        # new cookie request for flutter support
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
@csrf.csrf_exempt    
def submit_form(request):
    ''' Submit a new deposit. '''
    
    # --- if user is logged in, allow them to submit new deposit ---
    if request.method == "POST":
        print("Form submitted! With cookies: ", request.COOKIES)
        
        # --- session & form validation ---
        if request.COOKIES['sessionid'] != None: # validation
            # Save form data as new WasteDeposit object
            try:
                # flutter request sends data in body
                data = json.loads(request.body)
            except:
                # django sends html form (old fashioned way)
                data = Form(request.POST).data
            desc, type, mass = data['description'], data['type'], data['mass']
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
            
            # new JSON response (for flutter support)
            response = JsonResponse({
                'status': 'success',
                'message': 'Deposit successfully saved!'
            })
            response.status_code = 201
            return response
            
        else: # if user is not logged in
            # new JSON response (for flutter support)
            response = JsonResponse({
                'status': 'error',
                'message': 'User not logged in or form invalid. Deposit not saved.'
            })
            response.status_code = 400
            return response
        
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