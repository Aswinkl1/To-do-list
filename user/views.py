from django.shortcuts import render,redirect
from .forms import signUpForm,loginForm
from django.contrib.auth import login as auth_login,authenticate,logout

# Create your views here.

def signUp(request):
    if request.POST:
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = signUpForm()
            
    return render(request,'user/signup.html',{'form':form})

def login(request):
    if request.POST:
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user  = authenticate(username = user_name,password = password)
        if user:
            auth_login(request,user)
            return redirect('/')
    else:
        form = loginForm()
    return render(request,'user/login.html',{'form':form})
