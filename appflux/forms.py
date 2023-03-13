from django.forms import ModelForm, Form , CharField
from django import forms
from appflux.models import Entrepreneur, Fichier, RendezVous, Evenement

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


class RendezVousAnnuaire(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = '__all__'


class RendezVousFiltre(forms.Form):
    nom = forms.CharField(required=False)
    prenom = forms.CharField(required=False)
    date_min = forms.DateField(required=False)
    date_max = forms.DateField(required=False)


class EvenementForm(forms.ModelForm):
    entrepreneurs = forms.ModelMultipleChoiceField(
        queryset=Entrepreneur.objects.all().order_by("nom"),
        
    )

    class Meta:
        model = Evenement
        fields = ('titre', 'description', 'date', 'heure', 'entrepreneurs', 'compte_rendu')


class EvenementFiltre(forms.Form):
    titre = forms.CharField(required=False)
    date_min = forms.DateField(required=False)
    date_max = forms.DateField(required=False)