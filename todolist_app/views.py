

from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from todolist_app.models import TaskList
from todolist_app.forms import TaskListForm

from django.contrib import messages                     # display messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage             # Pagination

from todolist_app.utils import paginateProjects

from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'todolist_app/index.html')


@login_required(login_url="login")
def todolist(request):
    message="New Task Added Sucessfully!"               # success message
    # profile = request.user.profile

    if request.method=='POST':
        form=TaskListForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.owner=request.user
            instance.save()
        messages.success(request, message)
        return redirect('todolist')

    all_tasks=TaskList.objects.filter(owner=request.user)
    custom_range, all_tasks= paginateProjects(request, all_tasks, 10)    # 'paginateProject' mentioned in utils.py

    context={'all_tasks':all_tasks, 'custom_range':custom_range}
    return render(request, 'todolist_app/todolist.html', context)


@login_required(login_url="login")
def delete_task(request, id):
    task=TaskList.objects.get(pk=id)
    if task.owner==request.user:
        task.delete()
    return redirect('todolist')


@login_required(login_url="login")
def update_task(request, id):
    message="Task Edited Successfully!"
    task=TaskList.objects.get(pk=id)

    if request.method=="POST":
        form=TaskListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect('todolist')

    context={'task':task}
    return render(request, 'todolist_app/edit.html', context)


@login_required(login_url="login")
def completed_task(request, id):
    task=TaskList.objects.get(pk=id)
    if task.owner==request.user:
        task.done=True
        task.save()
    return redirect('todolist')


@login_required(login_url="login")
def pending_task(request, id):
    task=TaskList.objects.get(pk=id)
    if task.owner==request.user:
        task.done=False
        task.save()
    return redirect('todolist')


@login_required(login_url="login")
def contact_us(request):
    message="This is contact us page"
    context={'message': message}
    return render(request, 'todolist_app/contact_us.html', context)


@login_required(login_url="login")
def about_us(request):
    message="This is about us page"
    context={'message': message}
    return render(request, 'todolist_app/about_us.html', context)