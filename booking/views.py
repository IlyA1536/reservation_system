from datetime import datetime
from django.shortcuts import render, redirect
from .models import Room, Booking
from django.http import HttpResponse
from auth_system.models import CustomUser


def home(request):
    return render(request, 'hotel/home.html')

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
    elif request.method == 'POST':
        room = request.POST.get('room_number')
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')

        start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
        end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')

        if start_time >= end_time:
            return HttpResponse("Start time must be before end time", status=400)

        if Booking.objects.filter(room=room, start_time__lte=end_time, end_time__gte=start_time).exists():
            return HttpResponse("Room is already booked for selected dates", status=400)

        booking = Booking.objects.create(
            room=room,
            user=request.user,
            start_time=start_time,
            end_time=end_time,
        )
        return redirect("booking_detail", pk=booking.id)
