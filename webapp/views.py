from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('signup')

        else:
            return render(request, "signup.html", {'form': form})

    else:
        form = UserCreationForm()
        return render(request, "signup.html", {'form': form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

        else:
            return render(request, "signin.html", {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, "signin.html", {'form': form})


def secondpage(request):
    return render(request, 'secondpage.html')


def thirdpage(request):
    return render(request, 'thirdpage.html')


def static(request):
    return render(request, 'static.css')


