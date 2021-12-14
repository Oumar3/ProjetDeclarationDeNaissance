from django.db import models
# Create your models here.
class infoSurPersonnel(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    fonction=models.CharField(max_length=100)

    def __str__(self):
        return self.nom + ' ' + self.prenom

class infoEnfant(models.Model):
    infoSurPersonnel=models.ForeignKey(infoSurPersonnel,null=True,on_delete=models.SET_NULL)
    nom_enf=models.CharField(max_length=100)
    prenom_enf=models.CharField(max_length=100)
    Date_De_Naissance_enf=models.DateField(auto_now_add=True)
    lieu_De_Naissance_enf=models.CharField(max_length=100)
    nom_pere=models.CharField(max_length=100)
    Date_De_Naissance_pere=models.DateField()
    lieu_De_Naissance_pere=models.CharField(max_length=100)
    fonction_pere=models.CharField(max_length=100)
    nom_mere=models.CharField(max_length=100)
    Date_De_Naissance_mere=models.DateField()
    lieu_De_Naissance_mere=models.CharField(max_length=100)
    fonction_mere=models.CharField(max_length=100)
    def __str__(self):
        return self.nom_enf + ' ' + self.prenom_enf
