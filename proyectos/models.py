from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class ProyectosModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    # id_users = models.CharField(max_length=50)
    #manual = models.FileField(upload_to = 'resources',  blank = True, null=True)
    