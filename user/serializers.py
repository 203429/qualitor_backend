from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'id_role': self.validate_data.get('role', ''),
            'is_superuser': self.validate_data.get('isSuperUser', ''),
            'id_project': self.validate_data.get('idProject', ''),
        }

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ('is_superuser','is_staff')
        read_only_fields = ('username','email','first_name','last_name')