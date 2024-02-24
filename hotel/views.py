from django.shortcuts import render
from hotel.models import *


def get_rooms_list(request):
    rooms = Room.objects.all()

    context = {
        "rooms" : rooms
    }

    return render(
        request,
        "hotel/rooms_list.html",
        context,
    )


def get_users_list(request):
    users = User.objects.all()

    context = {
        "users" : users
    }

    return render(
        request,
        "hotel/users_list.html",
        context,
    )
