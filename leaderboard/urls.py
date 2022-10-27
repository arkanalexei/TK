from django.urls import path
from leaderboard.views import *

app_name='leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='leaderboard'),
    path('json/', json_leaderboard, name='json_leaderboard'),
    path('json-fb/', json_feedback, name='json_feedback'),
]