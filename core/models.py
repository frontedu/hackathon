from django.db import models

class Categoria(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class Endereco(models.Model):
    rua = models.CharField(max_length=25)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=15)
    cep = models.IntegerField()
    
    def __str__(self):
        return self.cidade




class Empresa(models.Model):
    nome = models.CharField(max_length=25)
    responsavel = models.CharField(max_length=50)
    telFixo = models.IntegerField()
    movel = models.IntegerField()
    cpf = models.IntegerField(blank=False,unique=True)
    cnpj = models.IntegerField()
    tipo = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    local = models.ForeignKey(Endereco,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome