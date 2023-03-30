from rest_framework import serializers
from phases.serializers import PhaseCreateUpdateSerializer
from proyectos.models import ProyectosModel

class ProyectosSerializer(serializers.ModelSerializer):
    phases_list = PhaseCreateUpdateSerializer(many=True, read_only=True)
    class Meta:
        model = ProyectosModel
        fields = ('id','name','phases_list')

