from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_leaderboard(request):
    # context = {
    #     'username': request.user.username,
    #     'task_list': Task.objects.filter(user=request.user),
    # }
    return render(request, "leaderboard.html")