from urllib import request
from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse_lazy

from monApp.forms import CategorieForm, ContactUsForm, ContenirForm, ProduitForm, RayonForm
from monApp.models import Categorie, Contenir, Produit, Rayon, Statut
from django.views.generic import *
from django.contrib.auth.views import *
from django.core.mail import *
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
    
from django.shortcuts import redirect
    
def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monprojet.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form})

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"

    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Produit.objects.filter(intituleProd__icontains=query).select_related('categorie').select_related('status')
            # Si aucun terme de recherche, retourner tous les produits
            # Charge les catégories en même temps
        return Produit.objects.select_related('categorie').select_related('status')
    
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
    context_object_name = "ctgrs"

    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Categorie.objects.filter(nomCat__icontains=query).annotate(nb_produits=Count('produit'))
        # Si aucun terme de recherche, retourner tous les produits
        # Charge les catégories en même temps
        return Categorie.objects.annotate(nb_produits=Count('produit'))
    
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Categories"
        return context

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "ctgr"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produit'))

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = Produit.objects.filter(categorie=self.object)
        return context
    
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statut.html"
    context_object_name = "status"
    
    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Statut.objects.filter(libelleStatus__icontains=query).annotate(nb_produits=Count('produit'))
        # Si aucun terme de recherche, retourner tous les produits
        # Charge les catégories en même temps
        return Statut.objects.annotate(nb_produits=Count('produit'))

    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes statut"
        return context

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "statut"

    def get_queryset(self):
        # Annoter chaque statut avec le nombre de produits liés
        return Statut.objects.annotate(nb_produits=Count('produit'))

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        context['prdts'] = Produit.objects.filter(status=self.object)
        return context
    
class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayon.html"
    context_object_name = "rayons"

    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Rayon.objects.filter(nomRayon__icontains=query).prefetch_related(
        Prefetch("contenir_rayon", queryset=Contenir.objects.select_related("produits"))
        )
        # Si aucun terme de recherche, retourner tous les produits
        # Charge les catégories en même temps
        return Rayon.objects.prefetch_related(
        Prefetch("contenir_rayon", queryset=Contenir.objects.select_related("produits"))
        )
    

    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        ryns_dt = []
        for rayon in context['rayons']:
            total = 0
            for contenir in rayon.contenir_rayon.all():
                total += contenir.produits.prixUnitaireProd * contenir.qte
                ryns_dt.append({'rayon': rayon,'total_stock': total})
                
        context['ryns_dt'] = ryns_dt
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0
        for contenir in self.object.contenir_rayon.all():
            total_produit = contenir.produits.prixUnitaireProd * contenir.qte
            prdts_dt.append({ 'produit': contenir.produits,
                'qte': contenir.qte,
                'prix_unitaire': contenir.produits.prixUnitaireProd,
                'total_produit': total_produit,
            })
            total_rayon += total_produit
            total_nb_produit += contenir.qte

        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit

        return context
    
class ConnectView(LoginView):

    template_name = 'monApp/page_login.html'

    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')
        
class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
        
class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
    
class EmailSentView(TemplateView):
    template_name = 'monApp/email_sent.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)
    
# def ProduitCreate(request):
#     if request.method == 'POST':
#         form = ProduitForm(request.POST)
#         if form.is_valid():
#             prdt = form.save()
#             return redirect('prdt-dtl', prdt.refProd)
#     else:
#         form = ProduitForm()
#         return render(request, "monApp/create_produit.html", {'form': form})
    
@method_decorator(login_required, name='dispatch')
class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/create_produit.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect("prdt-dtl", prdt.refProd)
    

@method_decorator(login_required, name='dispatch')
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('prdt-dtl', prdt.refProd)
    
@method_decorator(login_required, name='dispatch')
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"

    success_url = reverse_lazy('liste_produits')


# def ProduitUpdate(request, pk):
#     prdt = Produit.objects.get(refProd=pk)
#     if request.method == 'POST':
#         if form.is_valid():
#             # mettre à jour le produit existant dans la base de données
#             form.save()
#             # rediriger vers la page détaillée du produit que nous venons de mettre à jour
#             return redirect('prdt-dtl', prdt.refProd)
#         else:
#             form = ProduitForm(instance=prdt)
#         return render(request,'monApp/update_produit.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/create_categorie.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        categ = form.save()
        return redirect("categ-dtl", categ.idCat)

@method_decorator(login_required, name='dispatch')
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_categorie.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        categ = form.save()
        return redirect('categ-dtl', categ.idCat)
    
@method_decorator(login_required, name='dispatch')
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"

    success_url = reverse_lazy('lst-ctgrs')

@method_decorator(login_required, name='dispatch')
class RayonCreateView(CreateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/create_rayon.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect("liste_rayons")

@method_decorator(login_required, name='dispatch')
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class= RayonForm
    template_name = "monApp/update_rayon.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect("rayon-dtl", rayon.idRayon)
    
@method_decorator(login_required, name='dispatch')
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"

    success_url = reverse_lazy('liste_rayons')

@method_decorator(login_required, name='dispatch')
class ContenirCreateView(TemplateView):
    template_name = "monApp/create_contenir.html"

    def get(self, request, **kwargs):
        form = ContenirForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        rayon_id = self.kwargs.get('pk')
        form = ContenirForm(request.POST)
        
        if form.is_valid():
            try:
                rayon = Rayon.objects.get(pk=rayon_id)
            except Rayon.DoesNotExist:
                # Gérer l'erreur si le rayon n'existe pas
                return HttpResponseNotFound("Rayon non trouvé")
            
            produit = form.cleaned_data['produits']
            qte = form.cleaned_data['qte']
            contenir, created = Contenir.objects.get_or_create(rayons=rayon, produits=produit)
            if not created:
                contenir.qte += qte
            else:
                contenir.qte = qte
            contenir.save()
            return redirect('rayon-dtl', rayon.idRayon)
        return render(request, self.template_name, {'form': form})
    
class ContenirUpdateView(UpdateView):
    model = Contenir
    form_class=ContenirForm
    template_name = "monApp/update_contenir.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        contenir = form.save()
        return redirect('rayon-dtl', contenir.rayons.idRayon)
    
class ContenirDeleteView(DeleteView):
    model = Contenir
    template_name = "monApp/delete_contenir.html"

    def get_success_url(self) -> str:
        contenir = self.get_object()
        return reverse_lazy('rayon-dtl', kwargs={'pk': contenir.rayons.idRayon})
    
    