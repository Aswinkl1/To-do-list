from django.urls import path,include
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/',views.signUp,name='signup'),
    path('login/',views.login,name='login')

]