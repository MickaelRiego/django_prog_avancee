from django.shortcuts import render
from django.http import HttpResponse

from monApp.models import Categorie, Produit, Statut

def home(request, param=None):
    if param != None:
        return HttpResponse("<h1>Bonjour "+param+" !</h1>")
    else:
        return HttpResponse("<h1>Asalamalaykum !</h1>")
    
def contact_us(request):
    return HttpResponse("<p>Ici un formulaire</p>")

def about_us(request):
    return HttpResponse("<p>Ici le about us</p>")

def list_produits(request):
    prdts = Produit.objects.all()
    page = "<ul>"
    for i in range(len(prdts)):
        page += f"<li>{prdts[i]}</li>"
    return HttpResponse(page+"</ul>")

def list_categories(request):
    cats = Categorie.objects.all()
    page = "<ul>"
    for i in range(len(cats)):
        page += f"<li>{cats[i]}</li>"
    return HttpResponse(page+"</ul>")

def list_status(request):
    stats = Statut.objects.all()
    page = "<ul>"
    for i in range(len(stats)):
        page += f"<li>{stats[i]}</li>"
    return HttpResponse(page+"</ul>")
        