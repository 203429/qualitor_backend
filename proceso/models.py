from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class ProcesoModel(models.Model):
    nombre = models.CharField(max_length=100)
    id_proceso = models.CharField(max_length=50)
    proposito=models.CharField(max_length=300)
    objetivo = ArrayField( models.TextField(blank=True))
    descripcion = ArrayField( models.TextField(blank=True))
    responsable=models.CharField(max_length=100)
    categoria=models.CharField(max_length=50)
    participantes=ArrayField(models.CharField(max_length=100))
    procesoRelacionado=models.CharField(max_length=100)
    frecuencia= models.CharField(max_length=100)