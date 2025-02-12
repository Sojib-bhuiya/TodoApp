from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

@login_required
def home(request):
    tasks = Task.objects.all()
    return render(request, 'task/index.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')

        if title and due_date and due_time:
            task = Task.objects.create(title=title, description=description, due_date=due_date, due_time=due_time)
            task.save()
            return redirect('home')
        else :
            return render(request, 'task/add_task.html')
    return render(request, 'task/add_task.html')

@login_required
def remaining_tasks(request):
    remaining_task = Task.objects.filter(completed=False)
    return render(request, 'task/remaining.html', {'task': remaining_task})

@login_required
def completedTask(request):
    task = Task.objects.filter(completed=True)
    return render(request, 'task/completed.html', {
        'task': task
    })

@login_required
def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task/task_detail.html', {'task': task})

@login_required
def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task/delete.html', {'task': task})

@login_required
def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('home')
    return redirect('home')

@login_required
def removeTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3 :
            messages.error(request, 'Password must be at least 3 characters long.')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)

        if get_all_users_by_username:
            messages.error(request, 'Username already exists.')
            return redirect('register')

        new_user = User.objects.create(username=username, password=password, email=email)
        new_user.save()
        messages.success(request, 'New user created successfully')
        return redirect('login')
    return render(request, 'register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        valid_user = authenticate(username=username, password=password)
        if valid_user is not None:
            login(request, valid_user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid user details.')
            return redirect('login')
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


