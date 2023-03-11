from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class RoleModel(models.Model):
    name = models.CharField(null= True, max_length=200)
    # id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)