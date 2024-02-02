
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('',views.home),
    path('add-task/',views.add_Task,name='add-task'),
    path('category/',views.show_category,name='category'),
    path('add-category/',views.add_category,name='add-category'),
    path('edit_category',views.edit_category,name='edit_category'),
    path('<int:pk>/delete-category/',views.delete_category,name='delete-category'),
    path('<int:pk>/delete-task/',views.delete_task,name='delete-task'),
    path('edit-task/',views.edit_task,name='edit-task')

    
]