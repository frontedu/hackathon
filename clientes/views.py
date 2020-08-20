from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model,login,authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.views import generic
from django.db import models
from django.shortcuts import render,redirect
from .forms import SignUpForm
from .tokens import account_activation_token


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

def activation_sent_view(request):
    return render(request,'activation/activation_sent.html')



def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        #usuario nao pode logar até confirmar o link
        user.is_active = True
        user.save()
        current_site = get_current_site(request)
        subject = 'Por favor ative sua conta'

        message = render_to_string('activation/activations_request.html',{
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject,message)
        return redirect('activation/activation_sent.html')
    else:
        form = SignUpForm()
    return render(request,'signup/signup.html', {'form': form})

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_encode(uidb64))
        user = User.objtects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.profile.signup_confirmation = True
        user.save()
        login(request,user)
        return redirect('/')
    else:
        return render(request,'activations_invalid.html')










