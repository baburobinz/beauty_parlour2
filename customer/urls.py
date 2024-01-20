from django.urls import path
from .views import *

urlpatterns = [
   path('authentication',user_registraion_and_login,name="user_registraion_and_login"),
   path('logout',user_logout,name="user_logout")
]
