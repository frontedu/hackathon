from django.shortcuts import render

def home(request):

    return render(request,'homepage/home.html')


def teste(resquest):
    return render(resquest,'teste/teste.html')