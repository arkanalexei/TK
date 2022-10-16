from django.urls import path
from banksampah.views import *

app_name='banksampah'

urlpatterns = [
     path('', home, name=''),
     path('deposit', deposit_sampah, name='deposit')
]