from rest_framework import serializers
from proyectos.models import ProyectosModel

class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectosModel
        fields = ('__all__')

