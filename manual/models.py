from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class ManualModel(models.Model):
    nombre = models.CharField(max_length=100)
    id_manual = models.CharField(max_length=50)
    historia=models.CharField(max_length=300)
    alcance = models.CharField(max_length=300)
    vision = models.CharField(max_length=300)
    mision=models.CharField(max_length=100)
    organizacion_empresa = models.FileField(upload_to = 'resources',  blank = True, null=True)
    organigrama = models.FileField(upload_to = 'resources',  blank = True, null=True)
    vocabulario = models.FileField(upload_to = 'resources',  blank = True, null=True)
    politicas = models.ArrayField(models.CharField(max_length=150))
    