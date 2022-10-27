from django.shortcuts import render, redirect
from django.forms import Form
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime as dt

def about_us(request):
    return render(request, "about.html")
