from django.db import models

class Serie(models.Model) :
    nom  = models.CharField(max_length=25)
    langue = models.CharField(max_length=25)
    nbSaison=models.IntegerField()
    dateDiffusion = models.DateField()
    type=models.ForeignKey('Type',on_delete=models.CASCADE,)
    def __str__(self) -> str:
        return self.nom

class Type(models.Model):
    nomType= models.TextField()
    description=models.TextField()
    def __str__(self) -> str:
        return self.nomType
