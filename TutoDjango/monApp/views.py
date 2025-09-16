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
    return render(request, "monApp/contact.html")

def about_us(request):
    return render(request, "monApp/about.html")

def list_produits(request):
    prdts = Produit.objects.all()
    return render(request, "monApp/list_produit.html", {'prdts': prdts})

def list_categories(request):
    categs = Categorie.objects.all()
    return render(request, "monApp/list_categorie.html", {'categs': categs})

def list_status(request):
    status = Statut.objects.all()
    return render(request, "monApp/list_statut.html", {'status': status})
        