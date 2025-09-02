from django.urls import path
from . import views

urlpatterns = [
    path ("home/<param>", views.home, name="home"),
    path ("home/", views.home, name="home"),
    path ("contact_us", views.contact_us, name="contact us"),
    path ("about_us", views.about_us, name="about us"),
]

