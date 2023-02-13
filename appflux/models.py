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

    def __str__(self):
        return f'{self.nom} nom'

