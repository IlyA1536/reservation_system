from django.urls import path
from .views import register, log_in


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
]
