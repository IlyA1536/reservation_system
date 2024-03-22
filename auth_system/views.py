from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('get_rooms_list')
    else:
        form = CustomUserCreationForm()

    return render(
        request,
        'auth_system/register.html',
        context={'form' : form}
    )

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get(username)
            password = form.cleaned_data.get(password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.error(request, "User is not None")
                return redirect('get_rooms_list')
            else:
                messages.error(request, "Wrong login or password")
    else:
        form = AuthenticationForm()

    return render(
        request,
        'auth_system/login.html',
        context={'form' : form}
    )
