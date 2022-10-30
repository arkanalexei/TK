from django.urls import path
from leaderboard.views import *

app_name='leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='leaderboard'),
    path('json/', json_leaderboard, name='json_leaderboard'),
    path('json/comments/', json_feedback, name='json_feedback'),
    path('submit/', submit_form, name='submit_form')
]