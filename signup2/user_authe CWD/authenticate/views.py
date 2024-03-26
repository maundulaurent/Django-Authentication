from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'authenticate/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('my_login')
    

    context = {'resiterform': form}
    return render(request, 'authenticate/register.html', context=context)

def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            
    context = {'loginform': form}
            
    return render(request, 'authenticate/my_login.html', context=context)


@login_required(login_url="my_login")
def dashboard(request):
    return render(request, 'authenticate/dashboard.html')

def user_logout(request):
    auth.logout(request)

    return redirect("index")