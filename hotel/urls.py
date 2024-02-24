from django.urls import path
from .views import *

urlpatterns = [
    path('', get_rooms_list),
    path('users/', get_users_list),
]
