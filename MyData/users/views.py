from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def prueba(request):
    if request.method == 'POST':
        username = reques.POST['username']
        password = reques.POST['passwd']
        vefirpass = reques.POST['paswd_conf']
        first_name = reques.POST['first_name']
        last_name = reques.POST['last_name']
        email = reques.POST['email']
    return render(request, 'block.html')

def singup_view(request):
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
