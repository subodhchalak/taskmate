from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http.response import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from userApp.forms import CustomRegisterForm

from django.contrib.auth import views as auth_views

# Create your views here.


def register(request):
    form=CustomRegisterForm()
    message="New user crearted successfully! Login to get started."

    if request.method=="POST":
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect('login')

    context={'form':form}
    return render(request, 'userApp/register.html', context)