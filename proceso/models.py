from django.db import models
from django.contrib.postgres.fields import ArrayField

class Proceso(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    id_proceso = models.IntegerField(null=True)
    proposito=models.CharField(max_length=300, null=True)
    objetivo = ArrayField(models.TextField(blank=True), null=True)
    descripcion = ArrayField(models.TextField(blank=True), null=True)
    responsable = models.CharField(max_length=100, null=True)
    categoria = models.CharField(max_length=50, null=True)
    participantes = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    proceso_relacionado = models.CharField(max_length=100, null=True)
    frecuencia = models.CharField(max_length=100, null=True)
    status = models.BooleanField(null=True)
    metrica = models.FileField(upload_to='proceso_media/', null=True)

    def __str__(self):
        return f'{self.id} Proceso'

class Proceso_Media(models.Model):
    proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE, null=True, related_name = 'proceso_media', related_query_name = 'proceso_media')
    nombre = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to='proceso_media/', null=True)
    tipo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.id} Media'