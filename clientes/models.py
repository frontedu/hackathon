from django.db import models
from django.contrib.auth.models import User

'''provavelmente usarei p/ cadastro de empresas'''
class Clientes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sobrenome = models.CharField(max_length=15)
    eml = models.EmailField(verbose_name="Seu email aqui")
    begin_date = models.DateTimeField(auto_now_add=True)
