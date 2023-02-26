from django.db import models
from django.contrib.postgres.fields import ArrayField
from proyectos.models import ProyectosModel

# Create your models here.

class ManualModel(models.Model):
    historia=models.CharField(max_length=300)
    alcance = models.CharField(max_length=300)
    vision = models.CharField(max_length=300)
    mision=models.CharField(max_length=100)
    organizacion_empresa = models.FileField(upload_to = 'resources',  blank = True, null=True)
    organigrama = models.FileField(upload_to = 'resources',  blank = True, null=True)
    vocabulario = models.FileField(upload_to = 'resources',  blank = True, null=True)
    funciones_puestos = models.FileField(upload_to = 'resources',  blank = True, null=True)
    politicas = ArrayField(models.CharField(max_length=150))
    id_proyecto = models.ForeignKey(ProyectosModel, on_delete=models.CASCADE, null=False, blank=False, related_name='proyecto')
    