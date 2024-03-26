from django.shortcuts import render, redirect
from . forms import SignUpForm
from django.contrib.auth import login
# Create your views here.

def home(request):
    return render(request, 'authenticate/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'authenticate/signup.html', {'form': form})


def dashboard(request):
    return render(request, 'authenticate/dashboard.html')