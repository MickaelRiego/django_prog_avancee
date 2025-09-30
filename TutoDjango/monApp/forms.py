from django import forms

from monApp.models import Categorie, Produit, Rayon


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        exclude = ('categorie', 'status')
        # fields = '__all__'

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"

class RayonForm(forms.ModelForm):
    class Meta:
        model = Rayon
        fields = "__all__"