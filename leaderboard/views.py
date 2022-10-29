from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import redirect, render
from leaderboard.models import Achiever, Comment
from django.contrib.auth.decorators import login_required
from django.core import serializers
from leaderboard.forms import CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime as dt

# Create your views here.

@login_required(login_url='banksampah:login')
def json_leaderboard(request):    
    current_user = request.user
    data = Achiever.objects.all().order_by('-points')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='banksampah:login')
def json_feedback(request):    
    data = Comment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_leaderboard(request):
    context = {
        'form' : CommentForm,
        'username': request.user.username,
        'users': Achiever.objects.all().order_by('-points')
    }
    return render(request, "leaderboard.html", context)


@require_http_methods(["POST"])
def submit_form(request):
    # if user is logged in, allow them to submit new deposit
    if request.method == "POST":
        form = Form(request.POST)
        if request.session['is_logged_in'] and form.is_valid(): # validation
            # Save form data as new WasteDeposit object
            comment = form.data['comment']
            new_comment = Comment()
            new_comment.comment = comment
            new_comment.user = request.user
            new_comment.date_added = dt.now()
            new_comment.save()

            
            response = HttpResponseRedirect(reverse("leaderboard:leaderboard"))
            return response
            
        else: # if user is not logged in
            return redirect('banksampah:login')

# comment view ajax
# def comment_view(request):
