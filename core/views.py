
from django.shortcuts import render,redirect
from .forms import EmpresaForm
def home(request):

    return render(request,'homepage/home.html')


def teste(resquest):
    return render(resquest,'teste/teste.html')

def novaEmpresa(request):
    form = EmpresaForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'cadastroForm/cadastro.html',{'form':form})