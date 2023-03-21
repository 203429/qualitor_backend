import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','qualitor_backend.settings')

django.setup()

from role.models import RoleModel

def generate_roles():
    roles = ["Gestor de calidad", "Scrum master", "Product owner", "Analista de requerimientos", "Analista/tester", "Arquitecto de software", "Jefe de programacion",
            "DevOps", "Programador backend", "Programador Frontend", "Programador Fullstack", "Jefe de programacion"]
    
    for role in roles:
        RoleModel.objects.create(
            name = role
        )
    
if __name__ == '__main__':
    print("Generando roles...")
    generate_roles()
    print("Se generaron los roles")

# Ejecutar !python create_roles.py