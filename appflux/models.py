from django.db import models
from PIL import Image
from django.core.validators import RegexValidator
from authentification.models import User


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
    STRUCTURE = (
    ('Impulsions', 'Impulsions'),
    ('Eclosion', 'Eclosions')

)
    nom = models.CharField (max_length=30,)
    prenom = models.CharField(max_length=30, verbose_name="prénom")
    matricule = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(default='avatar.jpg', upload_to='entrepreneur_avatars', blank=True,)
    telephone = models.CharField(max_length=15 ,blank=True, verbose_name="téléphone")
    structure = models.CharField(max_length=40, choices=STRUCTURE)
    email =  models.EmailField()
    nationalite = models.CharField(max_length=150, verbose_name="nationalité")
    naissance = models.CharField(max_length=100, verbose_name="pays de naissance",)
    numero = models.CharField( max_length=15 ,verbose_name="numéro de téléphone professionel", blank=True)
    adresse_postal = models.CharField(max_length=200, verbose_name="Code")
    adresse = models.CharField(max_length=200, blank=True, null=True)
    securite_social = models.CharField(max_length=240, blank=True, verbose_name=" Numéro de sécurité social")
    date_naissance = models.DateField(verbose_name="date de naissance")
    ville = models.CharField(max_length=120, verbose_name="lieu de résidence", blank=True )
    fonction = models.CharField(max_length=240, blank=True,)
    date_entree = models.DateField(blank=True, null= True, verbose_name="date d'entrée dans la CAE")
    debut = models.DateField(blank=True, null=True, verbose_name="date du début du contrat")
    motif = models.CharField(max_length=240, blank=True, verbose_name=' Contrat de travail', choices=TRAVAIL)
    activite = models.CharField(max_length=40, blank=True, verbose_name="type de activité", choices=ACTIVITE)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.nom} {self.prenom}'
    

class Fichier(models.Model):
    nom = models.CharField(max_length=100)
    fichier = models.FileField(upload_to= "fichiers/")
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
    

NATURE =  [
    ('RDV conseil', 'Rendez-vous conseil'),
    ('RDV gestion', ' Rendez-vous gestion'),
    ('RDV administration', ' Rendez-vous admin',),
    ('RDV Ressources Humaines', 'Rendez vous RH'), 
    ('RDV comptabilité', 'Rendez-vous comptabilité'),
    ('RDV hebdomadaire', ' Rendez-vous hebdomadaire')

]

PRESENCE = [
    ('Present', 'Present'),
    ('Absent', 'Absent'),
    ('Attendu', 'Attendu'),
    ('Excusé', 'Excusé')
]

LIEU = [
    ('presentiel', 'Presentiel'),
    ('a distance', 'A distance'),
]

class RendezVous(models.Model):
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    sujet = models.CharField(max_length=20)
    date = models.DateField()
    heure = models.TimeField()
    nature = models.CharField(max_length=240, verbose_name=' Nature du rendez vous', choices=NATURE, blank=True)
    lieu = models.CharField(max_length=100, choices=LIEU, verbose_name='Mode d\'entretien', blank=True)
    objectifs = models.TextField(blank=True)
    personne = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.TextField(max_length=1000, verbose_name='Point qui ont été abordés', blank=True)
    notes = models.TextField(blank=True)
    #nouveau champ a ajouter apres

    def __str__(self):
        return f"Rendez-vous avec {self.entrepreneur} le {self.date} à {self.heure}"

class Evenement(models.Model):
    titre = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    date = models.DateField()
    heure = models.TimeField()
    entrepreneurs = models.ManyToManyField(Entrepreneur)
    compte_rendu = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titre
