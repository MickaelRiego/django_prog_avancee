from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    # path ("home", views.home, name="home"),
    path ("contact/", views.ContactView, name="contact us"),
    path ("about_us", views.AboutView.as_view(), name="about us"),
    # path ("list_produits", views.list_produits, name="list produit"),
    # path ("list_categories", views.list_categories, name="list categorie"),
    path ("list_status", views.list_status, name="list statut"),
    path ("home/", views.HomeView.as_view()),
    path ("home/<param>", views.HomeView.as_view()),
    path ("produits/", views.ProduitListView.as_view(), name="liste_produits"),
    path ("produit/<pk>/",views.ProduitDetailView.as_view(), name="prdt-dtl"),
    path ("categories/", views.CategorieListView.as_view(), name="lst-ctgrs"),
    path ("categorie/<pk>", views.CategorieDetailView.as_view(), name="categ-dtl"),
    path ("statuts/", views.StatutListView.as_view(), name="liste_statut"),
    path ("statut/<pk>", views.StatutDetailView.as_view(), name="statut-dtl"),
    path ("rayons/", views.RayonListView.as_view(), name="liste_rayons"),
    path ("rayon/<pk>", views.RayonDetailView.as_view(), name="rayon-dtl"),
    path ('login/', views.ConnectView.as_view(), name='login'),
    path ('register/', views.RegisterView.as_view(), name='register'),
    path ('logout/', views.DisconnectView.as_view(), name='logout'),
    path ('email-sent/', views.EmailSentView.as_view(), name='email-sent'),

    path ("produit/", views.ProduitCreateView.as_view(), name="create_produit"),
    path ("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="prdt-chng"),
    path ("produit/<pk>/delete/", views.ProduitDeleteView.as_view(), name="prdt-dlt"),

    path ("categorie/", views.CategorieCreateView.as_view(), name="create_categorie"),
    path ("categorie/<pk>/update/", views.CategorieUpdateView.as_view(), name="ctgr-chng"),
    path ("categorie/<pk>/delete/", views.CategorieDeleteView.as_view(), name="ctgr-dlt"),

    path ("rayon/", views.RayonCreateView.as_view(), name="create_rayon"),
    path ("rayon/<pk>/update/", views.RayonUpdateView.as_view(), name="rayon-chng"),
    path ("rayon/<pk>/delete/", views.RayonDeleteView.as_view(), name="rayon-dlt"),

]

