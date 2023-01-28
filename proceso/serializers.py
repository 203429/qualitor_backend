from rest_framework import serializers
from proceso.models import ProcesoModel

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcesoModel
        fields = ('__all__')
