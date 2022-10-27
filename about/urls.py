from django.urls import path
from about.views import *

app_name='about'

urlpatterns = [
     path('', about_us, name='about_us'),
]