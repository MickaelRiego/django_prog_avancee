from django.test import TestCase
from monApp.forms import CategorieForm
from monApp.models import Categorie

class CategorieFormTest(TestCase):
    def test_form_valid_data(self):
        form = CategorieForm(data = {'nomCat': 'CategoriePourTest'})
        self.assertTrue(form.is_valid())
    
    def test_form_valid_data_too_long(self):
        form = CategorieForm(data = {'nomCat': 'CategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTest'})
        self.assertFalse(form.is_valid())
        self.assertIn('nomCat', form.errors)
        self.assertEqual(form.errors['nomCat'], ['Assurez-vous que cette valeur comporte au plus 100 caractères (actuellement 102).'])

    def test_form_valid_data_missed(self):
        form = CategorieForm(data = {'nomCat': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('nomCat', form.errors)
        self.assertEqual(form.errors['nomCat'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        form = CategorieForm(data = {'nomCat': 'CategoriePourTest'})
        self.assertTrue(form.is_valid())
        ctgr = form.save()
        self.assertEqual(ctgr.nomCat, 'CategoriePourTest')
        self.assertEqual(ctgr.idCat, 1)

    