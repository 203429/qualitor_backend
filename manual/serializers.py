from rest_framework import serializers
from manual.models import ManualModel

class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualModel
        fields = 'historia', 'alcance', 'vision', 'mision', 'organizacion_empresa', 'organigrama', 'vocabulario', 'funciones_puestos', 'politicas'