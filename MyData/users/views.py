from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def singup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        vefirpass = request.POST['paswd_conf']
        if password != vefirpass:
            return render(request, 'users/singup.html', {'error':'La contraseña debe coinicidir!!'})
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password = password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect('login_view')
    return render(request, 'users/singup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return redirect('Dashboard')
        else:
            return render(request,'users/login.html',{'error':'Usuario o Contraseña no válido'})

    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')

def prueba(request):
    return render(request, 'block.html')