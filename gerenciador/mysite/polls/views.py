from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):

    return render(request, 'index.html')


def login(request):
    return HttpResponse("Hello, its the login page")

def createTask(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('view-tasks')

    context = {'form':form}

    return render(request, 'create-task.html',context=context)

def viewTasks(request):

    tasks  = Task.objects.all()

    context = {'tasks':tasks}

    return render(request, 'view-tasks.html',context=context)

def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('view-tasks')

    context = {'form':form}

    return render(request, 'update-task.html',context=context)
