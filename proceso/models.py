from django.db import models
from django.contrib.postgres.fields import ArrayField

class Proceso(models.Model):
    nombre = models.CharField(max_length=50)
    id_proceso = models.IntegerField()
    proposito=models.CharField(max_length=300)
    objetivo = ArrayField(models.TextField(blank=True))
    descripcion = ArrayField(models.TextField(blank=True))
    responsable = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    participantes = ArrayField(models.CharField(max_length=100))
    proceso_relacionado = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    status = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.id} Proceso'

class Proceso_Media(models.Model):
    proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE, null=True, related_name = 'proceso_media', related_query_name = 'proceso_media')
    nombre = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to='proceso_media/', null=True)
    tipo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.id} Media'