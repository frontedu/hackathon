from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register/register.html'


def login_user(request):
    return render(request,'login/login.html')

@csrf_protect
def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Usuarios e senha inválido')
    return redirect('home')



