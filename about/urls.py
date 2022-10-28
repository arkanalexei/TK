from django.urls import path
from about.views import *

app_name='about'

urlpatterns = [
    path('', about_us, name='about_us'),
    path('edit_feedback', edit_feedback, name='edit_feedback'),
    path('delete_feedback', delete_feedback, name='delete_feedback'),
    path('get-data/',get_data,name='get_data'),
]