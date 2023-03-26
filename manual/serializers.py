from rest_framework import serializers
from manual.models import ManualModel

class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualModel
        fields = ('__all__')