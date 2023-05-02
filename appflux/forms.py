from django.forms import ModelForm, Form , CharField
from django import forms
from appflux.models import Entrepreneur, Fichier, RendezVous, Evenement, Question, Answer

class EntrepreneurForm(ModelForm):
    class Meta:
       model = Entrepreneur
       fields = '__all__'


class EntrepreneurFiltre(Form):
    nom = CharField(max_length=100, required=False)
    prénom = CharField(max_length=100, required=False)
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
    entrepreneur = forms.ModelChoiceField(queryset=Entrepreneur.objects.order_by('nom'))

    class Meta:
        model = RendezVous
        fields = ['entrepreneur','sujet', 'date', 'heure','nature','lieu','objectifs', 'personne','points','notes']


class RendezVousFiltre(forms.Form):
    nom = forms.CharField(required=False)
    prénom = forms.CharField(required=False)
    date_minimum = forms.DateField(required=False)
    date_maximum = forms.DateField(required=False)


class EvenementForm(forms.ModelForm):
    entrepreneurs = forms.ModelMultipleChoiceField(
        queryset=Entrepreneur.objects.all().order_by("nom"),
        
    )

    class Meta:
        model = Evenement
        fields = ('titre', 'description', 'date', 'heure', 'entrepreneurs', 'compte_rendu')


class EvenementFiltre(forms.Form):
    titre = forms.CharField(required=False)
    date_minimum = forms.DateField(required=False)
    date_maximum = forms.DateField(required=False)


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'content')


class AnswerCreateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)