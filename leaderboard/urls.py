from django.urls import path
from leaderboard.views import *

app_name='leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='leaderboard'),
]