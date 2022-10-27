from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from leaderboard.models import Achiever, Feedback
from django.contrib.auth.decorators import login_required
from django.core import serializers



# Create your views here.

@login_required(login_url='banksampah:login')
def json_leaderboard(request):    
    current_user = request.user
    data = Achiever.objects.filter(user=current_user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='banksampah:login')
def json_feedback(request):    
    current_user = request.user
    # data = Feedback.objects.filter(user=current_user)
    data = Achiever.objects.filter(user=current_user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json-fb")

def show_leaderboard(request):
    context = {
        'username': request.user.username,
        'users': Achiever.objects.all().order_by('-points')
    }
    return render(request, "leaderboard.html", context)
