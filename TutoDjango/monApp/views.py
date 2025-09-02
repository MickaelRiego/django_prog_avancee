from django.shortcuts import render
from django.http import HttpResponse

def home(request, param=None):
    if param != None:
        return HttpResponse("<h1>Bonjour "+param+" !</h1>")
    else:
        return HttpResponse("<h1>Asalamalaykum !</h1>")
    
def contact_us(request):
    return HttpResponse("<p>Ici un formulaire</p>")

def about_us(request):
    return HttpResponse("<p>Ici le about us</p>")
