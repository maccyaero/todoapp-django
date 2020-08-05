from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todoapp-login')
    else:
        form = CreateUserForm()

    context = {'forms':form}
    return render(request, 'register/register.html',context)



def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("passwd")
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect('todoapp_home')
        
    context = {}
    return render(request, 'register/login.html',context)
    
    