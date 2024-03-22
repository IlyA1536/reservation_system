from django.shortcuts import render, redirect
from hotel.models import *
from django.http import HttpResponse
from auth_system.models import CustomUser


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
    users = CustomUser.objects.all()

    context = {
        "users" : users
    }

    return render(
        request,
        "hotel/users_list.html",
        context,
    )

def room_detail(request, pk:int):
    room = Room.objects.get(id=pk)

    context = {
        "room" : room
    }

    return render(
        request,
        "hotel/room_detail.html",
        context,
    )

def booking_detail(request, pk:int):
    booking = Booking.objects.get(id=pk)

    context = {
        "booking" : booking
    }

    return render(
        request,
        "hotel/booking_detail.html",
        context,
    )

def booking_form(request):
    if request.method == 'GET':
        return render(request, 'hotel/booking_form.html')
    else:
        room_number = request.POST.get('room_number')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        try:
            room = Room.objects.get(number = room_number)
        except ValueError:
            return HttpResponse("Wrong room number", status=400)
        except Room.DoesNotExist:
            return HttpResponse("Room does not exist", status=404)
        booking = Booking.objects.create(
            room = room,
            user = request.user,
            start_time = start_time,
            end_time = end_time,
        )

        return redirect("booking_detail", pk = booking.id)
