from django.db import models

# Create your models here.
class ProyectosModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    