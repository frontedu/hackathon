from django.forms import ModelForm
from .models import Conteudo


class EmpresaForm(ModelForm):
    class Meta:
        model = Conteudo
        fields = ['titulo','imagem','tel','descricao','cep']