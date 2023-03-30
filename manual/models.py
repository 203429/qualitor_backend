from django.db import models
from django.contrib.postgres.fields import ArrayField
from proyectos.models import ProyectosModel

# Create your models here.

class ManualModel(models.Model):
    historia=models.CharField(max_length=300, null=True)
    alcance = models.CharField(max_length=300, null=True)
    vision = models.CharField(max_length=300, null=True)
    mision=models.CharField(max_length=100, null=True)
    organizacion_empresa = models.FileField(upload_to='proceso_media/',  blank = True, null=True)
    organigrama = models.FileField(upload_to='proceso_media/',  blank = True, null=True)
    vocabulario = models.FileField(upload_to='proceso_media/',  blank = True, null=True)
    funciones_puestos = models.FileField(upload_to='proceso_media/',  blank = True, null=True)
    politicas = ArrayField(models.CharField(max_length=150), null=True)
    proyecto = models.ForeignKey(ProyectosModel, on_delete=models.CASCADE, null=False, blank=False, related_name='proyecto')
    