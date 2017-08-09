from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, 'FrikerApp/index.html', {})


def llogin(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username1 = request.POST.get('username', None)
        password1 = request.POST.get('password', None)

        if action == 'signup':
            user2 = User.objects.create_user(username=username1,
                                             password=password1)
            user2.save()
        elif action == 'login':
            user1 = authenticate(username=username1,
                                 password=password1)
            if user1 is not None:
                login(request, user1)
                redirect('/')
            else:
                redirect('index')

    return render(request, 'FrikerApp/login.html', {})
