from django.db import models
from django.contrib.postgres.fields import ArrayField
from proceso.models import ProcesoModel
# Create your models here.
class DocumentoModel(models.Model):
    proceso = models.ForeignKey(ProcesoModel, on_delete=models.CASCADE, null=False, blank=False, related_name='documentos')
    nombre = models.CharField(max_length=100)
    documento = models.FileField(upload_to = 'resources',  blank = True, null=True)
    tipo = models.CharField(max_length=50)