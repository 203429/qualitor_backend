from rest_framework import serializers
from .models import Phase

class PhaseCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields =  ('__all__')
