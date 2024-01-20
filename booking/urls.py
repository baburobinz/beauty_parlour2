
from django.urls import path
from .views import *

urlpatterns = [
    path('my_bookings',show_bookings,name="show_bookings")
]
