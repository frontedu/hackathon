from django.urls import path
from .views import SignUp,signup_view,activate,activation_sent_view



urlpatterns = [

    path('signup/',signup_view,name='signup'),
    path('sent/',activation_sent_view,name='activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/',activate,name='activate'),

]

#path('register/',SignUp.as_view(),name='register'),
#<a class="btn btn-success" href="{% url 'register' %}">Registre-ser</a>