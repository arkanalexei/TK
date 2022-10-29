from django.urls import path
from deposit.views import *

app_name='deposit'

urlpatterns = [
     path('', deposit_sampah, name='deposit_sampah'),
     path('json/', get_user_deposits, name='get_user_deposits'),
     path('json/achiever/', get_achiever, name='get_achiever'),
     path('submit/', submit_form, name='submit_form'),
     path('view/<int:id>', show_deposit_by_id, name='show_deposit_by_id')
]