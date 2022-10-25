from django.urls import path
from banksampah.views import *

app_name='banksampah'

urlpatterns = [
     path('', home, name='home'),
     path('deposit', deposit_sampah, name='deposit'),
     path('register/', register, name='register'),
     path('login/', login_user, name='login'),
     path('logout/', logout_user, name='logout'),
     path('json/', get_user_deposits, name='get_user_deposits')
]