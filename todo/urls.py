
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('',views.home),
    path('add-task',views.add_Task,name='add-task')
    
]