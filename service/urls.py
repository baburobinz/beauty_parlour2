
from django.urls import path
from .views import *

urlpatterns = [
   
    path('',show_home,name="show_home"),
    path('service',show_services,name="show_services"),
    path('price',show_pricing,name="show_pricing"),
    path('today_offer',show_offer,name="show_offer")
   
]
