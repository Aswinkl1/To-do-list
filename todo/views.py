from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import category,Task
from . forms import addTask,addCategory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:login1')
def home(request):
    task = addTask()

    main_task = Task.objects.filter(created_by = request.user)
    print(main_task)
    return render(request,'core/index.html',{'task':task,'main_task':main_task})

def delete_task(request,pk):
    Task.objects.get(pk=pk).delete()
    messages.success(request,"Task deleted successfully ")
    return redirect('/')



def add_Task(request):
    """Returns a page to add task"""
    print('i am here')
    if request.POST:
        print(request.POST)
        task = addTask(request.POST)
        
        if task.is_valid():
            print('its valid')
            task = task.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request,"Task added successfuly")
            return redirect('/')
        else:
            print(task.errors)

    return redirect('/')

def edit_task(request):
    if request.POST:
        
        mutable_post = request.POST.copy()

        pk1 = mutable_post.get('pk')
        

        task_instance = get_object_or_404(Task,pk=pk1)
        mutable_post.pop('pk',None)

        mutable_post['created_by'] = request.user.id
        form = addTask(mutable_post, instance=task_instance)
        if form.is_valid():
            form.save()
        messages.success(request,"successfully edited the Task")

    return redirect('/')


def show_category(request):
    "Shows all category"
    form = addCategory()
    categories = category.objects.filter(created_by = request.user.id)
    
    return render(request,'core/category.html',{'categories':categories,'form':form})

def add_category(request):
    print("i am on categories")
    if request.POST:
        form = addCategory(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            messages.success(request,"successfully added the category")

    # print(request.POST.get('name'))
    # category.objects.create(name =request.POST.get('name'),created_by=request.user )
    return redirect('core:category')

def edit_category(request):
    if request.POST:
        # Make a mutable copy of the QueryDict
        mutable_post = request.POST.copy()
        
        pk1 = mutable_post.get('pk')
        category_instance = get_object_or_404(category, pk=pk1)

        # Remove 'pk' from the copy
        mutable_post.pop('pk', None)

        # Set 'created_by' in the copy
        mutable_post['created_by'] = request.user.id

        form = addCategory(mutable_post, instance=category_instance)
        if form.is_valid():
            form.save()
        messages.success(request,"successfully edited the category")

    return redirect('core:category')

def delete_category(request,pk):
    category.objects.get(pk=pk).delete()
    messages.success(request,"category deleted successfully ")
    return redirect('core:category')





