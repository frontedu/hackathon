from django.forms import ModelForm
from .models import Cadastro


class EmpresaForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome','responsavel','tipo','cpf','cnpj','telFixo',
                  'movel','cidade','estado','bairro','rua','cep']