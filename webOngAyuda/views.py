from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def Cachulo(request):
    return render(request, "Cachulo.html")

def Flaca(request):
    return render(request, "Flaca.html")

def gato(request):
    return render(request, "gato.html")

def Ginger(request):
    return render(request, "Ginger.html")

def Lucifer(request):
    return render(request, "Lucifer.html")
    
def Niña(request):
    return render(request, "Niña.html")
    
def Perro(request):
    return render(request, "Perro.html")

def Tommy(request):
    return render(request, "Tommy.html")