from django.db import models

# Create your models here.
class Patient(models.Model):
    nom = models.CharField (max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Praticien(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    addresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class CentreDeSante(models.Model):
    nom = models.CharField(max_length=100)
    addresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom
              