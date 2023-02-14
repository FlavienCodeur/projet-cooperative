from django.db import models
from PIL import Image
from django.core.validators import RegexValidator
from authentification.models import User

ROLES = (
    ('Monsieur', 'Monsieur'),
    ('Madame', 'Madame'),
    ('Non defini', 'Non defini')
)

STRUCTURE = (
    ('Impulsions', 'Impulsions'),
    ('Eclosion', 'Eclosions')

)

TRAVAIL = (
    ('CDI', 'Contrat à duree indéterminée'),
    ('CDD', 'Contrat à duree determinée'),
    ('Apprentissage', 'Apprentissage'),
    ('Professionalisation', 'Contrat de Professionalisation'),
)

ACTIVITE = (
    ('Temps Plein', 'Temps Plein'),
    ('Temps Partiel', 'Temps Partiel'),
    ('Autre', 'Autre')
)

class Entrepreneur(models.Model):
    nom = models.CharField (max_length=30,)
    prenom = models.CharField(max_length=30,)
    matricule = models.CharField(max_length=30, blank=True)
    civilite = models.CharField(max_length=20, choices=ROLES)
    photo = models.ImageField(default='avatar.jpg', upload_to='entrepreneur_avatars', blank=True,)
    telephone = models.CharField(max_length=10 ,blank=True, )
    structure = models.CharField(max_length=40, choices=STRUCTURE,)
    email = models.CharField(max_length=150,)
    nationalite = models.CharField(max_length=150,)
    naissance = models.CharField(max_length=100, verbose_name="pays de naissance",)
    numero = models.CharField( max_length=10 ,verbose_name="numero de telephone professionel", blank=True)
    adresse_postal = models.CharField( max_length=200)
    securite_social = models.CharField(max_length=240, blank=True,)
    date_naissance = models.DateField()
    ville = models.CharField(max_length=120, verbose_name="lieu de residence", blank=True )
    fonction = models.CharField(max_length=240, blank=True,)
    date_entree = models.DateField(blank=True, null= True)
    debut = models.DateField(blank=True, null=True, verbose_name="date du debut du contrat")
    motif = models.CharField(max_length=240, blank=True, verbose_name=' Contrat de travail', choices=TRAVAIL)
    activite = models.CharField(max_length=40, blank=True, verbose_name="type de activité", choices=ACTIVITE)
    manager = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.nom} nom'

