from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import category
from . forms import addTask,addCategory
from django.contrib import messages
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





