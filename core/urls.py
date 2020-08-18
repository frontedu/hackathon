from django.urls import path
from .views import home,teste

urlpatterns = [

    path('',home,name='home'),
    path('teste/',teste, name='teste'),
]