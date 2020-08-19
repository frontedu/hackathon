from django.urls import path
from .views import home,teste,novaEmpresa

urlpatterns = [
    path('',home,name='home'),
    path('teste/',teste, name='teste'),
    path('cad/',novaEmpresa,name='cad'),
]