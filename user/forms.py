from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
class signUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class loginForm(AuthenticationForm):
    username = forms.CharField()
    password  = forms.PasswordInput()
    
    