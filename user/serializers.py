from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from proyectos.models import ProyectosModel

from role.models import RoleModel

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    id_role = serializers.ListField()
    id_project = serializers.ListField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        
        projects=self.validated_data.get('id_project')
        list_projects=[]
        for id_aux in projects:
            try:
                project = ProyectosModel.objects.get(id=id_aux)
                list_projects.append(project)
            except RoleModel.DoesNotExist:
                print(f'El proyecto con id:{id_aux} no existe')
        
        
        roles=self.validated_data.get('id_role')
        list_roles=[]
        for id_aux in roles:
            try:
                role = RoleModel.objects.get(id=id_aux)
                list_roles.append(role)
            except RoleModel.DoesNotExist:
                print(f'El rol con id:{id_aux} no existe')
                

        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'email': self.validated_data.get('email', ''),
            'id_role': list_roles,
            'id_project': list_projects,
        }

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ('is_superuser','is_staff','id_role','id_project')
        read_only_fields = ('username','email','first_name','last_name')