from django.db import models
from django.contrib.auth.models import User

class RoleModel(models.Model):
    name = models.CharField(null= True, max_length=200)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)