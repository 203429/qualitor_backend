from rest_framework import serializers
from documento.models import DocumentoModel

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoModel
        fields = ('__all__')

