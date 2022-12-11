from django.urls import path
from about.views import *
from about.views import show_xml
from about.views import show_xml_by_id  
from about.views import show_json 
from about.views import show_json_by_id 

app_name='about'

urlpatterns = [
    path('', about_us, name='about_us'),
    path('edit_feedback', edit_feedback, name='edit_feedback'),
    path('delete_feedback', delete_feedback, name='delete_feedback'),
    path('get-data/',get_data ,name='get_data'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>', show_xml_by_id, name="show_xml_by_id"),
    path('json/', show_json, name='show_json'), 
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]