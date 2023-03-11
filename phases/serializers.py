from rest_framework import serializers
from proceso.serializers import ProcesoCreateUpdateSerializer
from .models import Phase

class PhaseCreateUpdateSerializer(serializers.ModelSerializer):
    process_list = ProcesoCreateUpdateSerializer(many=True, read_only=True)
    class Meta:
        model = Phase
        fields =  ('id','nombre','id_proyecto','process_list')
