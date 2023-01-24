from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def admin_login_view(request):
    if request.method == 'POST':
        submitted_username = request.POST['username']
        submitted_password = request.POST['password']
        admin = authenticate(request, username=submitted_username, password=submitted_password)
        if admin is not None:
            login(request, admin)
            return redirect('web/templates/management.html')
        else:
            return render(request, 'web/templates/admin_login.html', {'error': 'Invalid login credentials'})
    return render(request, 'web/templates/admin_login.html')


def user_login_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'web/templates/login.html')


def home(request):
    return render(request, 'home.html')
