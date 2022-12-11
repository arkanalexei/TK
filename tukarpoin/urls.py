from django.urls import path
from tukarpoin.views import tukar_poin, tambah_perk, tukar_poin_json, redeem

app_name = 'tukarpoin'

urlpatterns = [
    path('', tukar_poin, name='tukar_poin'),
    path('tambah/', tambah_perk, name='tambah_perk'),
    path('json/', tukar_poin_json, name='tukar_poin_json'),
    path('redeem/<str:perk_id>/', redeem, name='redeem')
]