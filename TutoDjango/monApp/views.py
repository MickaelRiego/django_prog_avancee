from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse

from monApp.models import Categorie, Produit, Statut

def home(request, param=None):
    if request.GET and request.GET['test']:
        raise Http404
    return HttpResponse("Hello World!")

def accueil(request, param="Anon"):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def ma_vue(request):
    return JsonResponse({'foo':'bar'})

    
def contact_us(request):
    return HttpResponse("<p>Ici un formulaire</p>")

def about_us(request):
    return HttpResponse("<p>Ici le about us</p>")

def list_produits(request):
    prdts = Produit.objects.all()
    return render(request, "monApp/list_produit.html", {'prdts': prdts})

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
        