from django.forms import ModelForm, Form , CharField
from django import forms
from appflux.models import Entrepreneur, Fichier

class EntrepreneurForm(ModelForm):
    class Meta:
       model = Entrepreneur
       fields = '__all__'


class EntrepreneurFiltre(Form):
    nom = CharField(max_length=100, required=False)
    prenom = CharField(max_length=100, required=False)
    structure = CharField(max_length=100, required=False)



class FichierForm(forms.ModelForm):
    class Meta:
        model = Fichier
        fields = ['nom', 'fichier']