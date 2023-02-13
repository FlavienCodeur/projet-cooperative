from django.db import models
from PIL import Image
from django.core.validators import RegexValidator

ROLES = (
    ('Monsieur', 'Monsieur'),
    ('Madame', 'Madame'),
    ('Non defini', 'Non defini')
)

STRUCTURE = (
    ('Impulsions', 'Impulsions'),
    ('Eclosion', 'Eclosions')

)


class Entrepreneur(models.Model):
    nom = models.CharField (max_length=30)
    prenom = models.CharField(max_length=30)
    matricule = models.CharField(max_length=30, blank=True)
    civilite = models.CharField(max_length=20, choices=ROLES)
    photo = models.ImageField(null=True, blank=True)
    telephone = models.IntegerField(blank=True, null=True)
    structure = models.CharField(max_length=40, choices=STRUCTURE, blank=True, null=True)
    email = models.CharField(max_length=150)
    nationalite = models.CharField(max_length=150, blank=True, null=True)
    naissance = models.CharField(max_length=100, verbose_name="pays de naissance", null=True, blank=True)
    numero = models.IntegerField(blank=True, null=True, verbose_name="numero de telephone professionel")
    adresse_postal = models.CharField(blank=True, null=True, max_length=200)
    securite_social = models.CharField(blank=True, null=True, max_length=240)
    date_naissance = models.DateField(blank=True, null=True)
    ville = models.CharField(max_length=120, verbose_name="lieu de residence", blank=True, null=True)

    def __str__(self):
        return f'{self.nom} nom'

