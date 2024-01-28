from django.shortcuts import render,HttpResponse,redirect
from .models import category
from . forms import addTask
# Create your views here.

def home(request):
    task = addTask()
    # categories = category.objects.all()
    return render(request,'core/index.html',{'task':task})

def add_Task(request):
    """Returns a page to add task"""
    print('i am here')
    if request.POST:
        print(request.POST)
        task = addTask(request.POST)
        print(task)
        if task.is_valid():
            print('its valid')
            task.save()
            return redirect('/')
        else:
            print(task.errors)

    return render(request,'core/add-task.html')




