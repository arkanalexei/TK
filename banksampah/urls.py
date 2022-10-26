from django.urls import path
from banksampah.views import *

app_name='banksampah'

urlpatterns = [
     path('', home, name='home'),
     path('deposit', deposit_sampah, name='deposit'),
     path('register/', register, name='register'),
     path('login/', login_user, name='login'),
     path('logout/', logout_user, name='logout'),
     path('json/', get_user_deposits, name='get_user_deposits'),
     path('news/', news, name='news'),
     path('news/read/<str:news_id>/', read_more, name='read_more'),
     path('news/add/', news_add, name='news_add'),
     path('news/json/', news_json, name='news_json'),
     path('news/delete/<str:news_id>/', news_delete, name='news_delete')
]