from django.forms import ModelForm, Form , CharField
from django import forms
from appflux.models import Entrepreneur, Fichier, RendezVous

class EntrepreneurForm(ModelForm):
    class Meta:
       model = Entrepreneur
       fields = '__all__'


class EntrepreneurFiltre(Form):
    nom = CharField(max_length=100, required=False)
    prenom = CharField(max_length=100, required=False)
    structure = forms.ChoiceField(choices=Entrepreneur.STRUCTURE, required=False)
    


class FichierForm(forms.ModelForm):
    class Meta:
        model = Fichier
        fields = ['nom', 'fichier']


class RendezVousForm (forms.ModelForm):
    class Meta : 
        model = RendezVous
        fields = ['sujet', 'date', 'heure','nature','lieu','objectifs', 'personne','points','notes']