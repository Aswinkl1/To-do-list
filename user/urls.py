from django.urls import path,include
from django.contrib.auth import views as auth_views 
from django.urls import reverse_lazy
from . import views

app_name = 'user'

urlpatterns = [
#   path('signup/',views.signUp,name='signup'),
    path('signup/', views.signUp, name='signup1'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('login/',views.login,name='login1'),
    path('logout/',views.user_logout,name='logout1'),
    # path('password-change/',views.password_change,name="password-change"),
    # path('accounts/password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user:password_change_done')), name='password_change'),
    # path("accounts/", include("django.contrib.auth.urls")),


]