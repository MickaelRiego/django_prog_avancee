from django.urls import path
from . import views

urlpatterns = [
    path ("home/<param>", views.home, name="home"),
    path ("home/", views.home, name="home"),
    path ("contact_us", views.contact_us, name="contact us"),
    path ("about_us", views.about_us, name="about us"),
    path ("list_produits", views.list_produits, name="list produit"),
    path ("list_categories", views.list_categories, name="list categorie"),
    path ("list_status", views.list_status, name="list statut"),
]

