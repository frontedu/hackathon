import uuid
from django.db import models



class Categoria(models.Model):
    tipo = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.tipo

class Estados(models.Model):
    sigla = models.CharField(max_length=15)



    def __str__(self):
        return self.sigla


class Cadastro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=25, null=True, blank=True)
    responsavel = models.CharField(max_length=50, null=True, blank=True)
    telFixo = models.IntegerField(null=True, blank=True)
    movel = models.IntegerField(null=True, blank=True)
    cpf = models.IntegerField(blank=False,unique=True)
    cnpj = models.IntegerField(null=True,blank=True)
    tipo = models.ManyToManyField(Categoria)
    rua = models.CharField(max_length=25,null=True, blank=True)
    bairro = models.CharField(max_length=25,null=True, blank=True)
    cidade = models.CharField(max_length=15,null=True, blank=True)
    estado = models.ManyToManyField(Estados)
    cep = models.IntegerField(null=True,blank=True)



    def __str__(self):
        return self.nome