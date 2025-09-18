from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse

from monApp.models import Categorie, Produit, Statut
from django.views.generic import *


def accueil(request, param="Anon"):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def ma_vue(request):
    return JsonResponse({'foo':'bar'})

# def contact_us(request):
#     return render(request, "monApp/contact.html")

# def about_us(request):
#     return render(request, "monApp/about.html")

# def list_produits(request):
#     prdts = Produit.objects.all()
#     return render(request, "monApp/list_produit.html", {'prdts': prdts})

def list_categories(request):
    categs = Categorie.objects.all()
    return render(request, "monApp/list_categorie.html", {'categs': categs})

def list_status(request):
    status = Statut.objects.all()
    return render(request, "monApp/list_statut.html", {'status': status})

        
class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        param = self.kwargs.get('param')
        if param != None and param != None and param != "":
            context['name'] = param 
            context['titreh1'] = "Hello " + param
        else:
            context['titreh1'] = "Hello DJANGO"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..." 
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class ContactView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "Nous Contacter"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"

    def get_queryset(self ) :
        return Produit.objects.order_by("prixUnitaireProd")
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
    
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categorie.html"
    context_object_name = "categ"
    
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Categories"
        return context

class CategorieDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_categorie.html"
    context_object_name = "categ"

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context