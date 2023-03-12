from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from proyectos.models import ProyectosModel

from role.models import RoleModel

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    id_role = serializers.IntegerField()
    id_project = serializers.IntegerField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        try:
            role = RoleModel.objects.get(id=self.validated_data.get('id_role'))
            project = ProyectosModel.objects.get(id=self.validated_data.get('id_project'))
        except RoleModel.DoesNotExist:
            role = None
            project = None
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'email': self.validated_data.get('email', ''),
            'id_role': role,
            'id_project': project,
        }

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ('is_superuser','is_staff','id_role','id_project')
        read_only_fields = ('username','email','first_name','last_name')