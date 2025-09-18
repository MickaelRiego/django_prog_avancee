from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    # path ("home", views.home, name="home"),
    path ("contact_us", views.ContactView.as_view(), name="contact us"),
    path ("about_us", views.AboutView.as_view(), name="about us"),
    # path ("list_produits", views.list_produits, name="list produit"),
    # path ("list_categories", views.list_categories, name="list categorie"),
    path ("list_status", views.list_status, name="list statut"),
    path ("home/", views.HomeView.as_view()),
    path ("home/<param>", views.HomeView.as_view()),
    path ("produits/", views.ProduitListView.as_view(), name="liste_produits"),
    path("produit/<pk>/",views.ProduitDetailView.as_view(), name="detail_produit"),
    path ("categories/", views.CategorieListView.as_view(), name="liste_categories"),
]

