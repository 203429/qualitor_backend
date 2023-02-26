from django.db import models

class Phase(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    id_phase = models.IntegerField(null=True)
    
    

    def __str__(self):
        return f'{self.id} Phase'