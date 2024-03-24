from django.urls import path
from .views import signup, log_in


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
]
