from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from leaderboard.models import Achiever, Comment
from django.contrib.auth.decorators import login_required
from django.core import serializers
from leaderboard.forms import CommentForm


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
        'form' : CommentForm,
        'username': request.user.username,
        'users': Achiever.objects.all().order_by('-points')
    }
    return render(request, "leaderboard.html", context)

# form
def get_comment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        comment = request.POST['comment']
        if comment.is_valid():
            comment.save()
            return redirect('leaderboard:leaderboard')
    # if a GET (or any other method) we'll create a blank form
    else:
        comment = CommentForm()
    
    return render(request, 'leaderboard.html', {'comment': comment})