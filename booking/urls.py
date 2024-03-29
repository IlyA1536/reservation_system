from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name = 'home'),
    path('rooms-list/', get_rooms_list, name = 'get_rooms_list'),
    path('users/', get_users_list, name = 'get_users_list'),
    path('room/<int:pk>', room_detail, name = 'room_detail'),
    path('booking-detail/<int:pk>', booking_detail, name = 'booking_detail'),
    path('booking/', booking_form, name = 'booking_form'),
]
