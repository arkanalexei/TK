from django.urls import path
from banksampah.views import home

app_name='banksampah'

urlpatterns = [
     path('', home, name=''),
]