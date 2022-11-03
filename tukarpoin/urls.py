from django.urls import path
from tukarpoin.views import *
from tukarpoin.views import show_tukarpoin

app_name='tukarpoin'

urlpatterns = [
    path('', show_tukarpoin, name='show_tukarpoin'),
]