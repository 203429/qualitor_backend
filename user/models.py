from django.contrib.auth.models import AbstractUser
from django.db import models
from role.models import RoleModel
from proyectos.models import ProyectosModel

class CustomUser(AbstractUser):
    id_role = models.ManyToManyField(RoleModel)
    id_project = models.ManyToManyField(ProyectosModel)
    # id_role = models.ForeignKey(RoleModel, on_delete=models.CASCADE, null=True)
    # id_project = models.ForeignKey(ProyectosModel, on_delete=models.CASCADE, null=True)