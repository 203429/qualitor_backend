from rest_framework import serializers
from role.models import RoleModel

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = ('__all__')