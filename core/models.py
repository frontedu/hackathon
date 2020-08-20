
import uuid
from django.db import models
import pycep_correios



class Categoria(models.Model):
    tipo = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.tipo

class Estados(models.Model):
    sigla = models.CharField(max_length=15)

    def __str__(self):
        return self.sigla




class Conteudo(models.Model):
    titulo = models.CharField(max_length=25)
    imagem = models.ImageField()
    tel = models.IntegerField(null=True)
    descricao = models.TextField(max_length=240)
    cep = models.CharField(max_length=8)



    def endereco(cep):
        stringCep=str(cep)
        endereco = pycep_correios.get_address_from_cep(stringCep)
        return (endereco)



    def __str__(self):
        return self.titulo




