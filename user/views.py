from django.shortcuts import render,redirect
from .forms import signUpForm,loginForm
from django.contrib.auth import login as auth_login,authenticate,logout

from django.contrib.auth.forms import PasswordChangeForm

# email verification 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.

def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request,"Please confirm your email address to complete the registration")
            return redirect('user:login1')
    else:
        form = signUpForm()
    return render(request, 'user/signup.html', {'form': form})


# activating the verified emai
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        messages.success(request,"Thank you for your email confirmation. Now you can login your account.")
        return redirect("user:login1")
    else:
        return HttpResponse('Activation link is invalid!')


# def signUp(request):
#     if request.POST:
#         form = signUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login')
#     else:
#         form = signUpForm()
            
#     return render(request,'user/signup.html',{'form':form})

def login(request):
    form = loginForm(request.POST or None)
    errors = None
    if request.POST:
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user  = authenticate(username = user_name,password = password)
        if user:
            auth_login(request,user)
            return redirect('/')
        else:
            errors = "invalid cridentials"

    return render(request,'user/login.html',{'form':form,'errors':errors})


def user_logout(request):
    """
    user logout
    """
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("user:login1")

def password_change(request):
    form = PasswordChangeForm(request.user)
    return render(request,'core/password_reset.html',{'form':form})