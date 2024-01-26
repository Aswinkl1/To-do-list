from django.urls import path,include

from . import views

app_name = 'user'

urlpatterns = [
    # path('signup/',views.signUp,name='signup'),
#     url(r'^signup/$', views.signup, name='signup'),
#    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#          views.activate, name='activate'),
    path('signup/', views.signUp, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('login/',views.login,name='login'),
    path('logout/',views.user_logout,name='logout'),

]