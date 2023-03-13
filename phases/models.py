from django.db import models
from proyectos.models import ProyectosModel

class Phase(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    id_proyecto = models.ForeignKey(ProyectosModel, on_delete=models.CASCADE, null=True, related_name = 'phases_list', related_query_name = 'phases_list')