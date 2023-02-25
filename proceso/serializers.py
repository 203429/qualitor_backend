from rest_framework import serializers
from .models import Proceso, Proceso_Media

class Proceso_Media_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso_Media
        fields =  ('__all__')

# Story  Serializer
class ProcesoCreateUpdateSerializer(serializers.ModelSerializer):
    # story_media = Story_Media_Serializer(many=True, required = False)
    proceso_media = Proceso_Media_Serializer(many = True, required = False)

    class Meta:
        model = Proceso
        fields =  ('__all__')

    def create(self, validated_data):
        # Story  contains images
        if 'proceso_media' in validated_data:
            proceso_media = validated_data.pop('proceso_media')
            proceso_instance = Proceso.objects.create(**validated_data)
            for img in proceso_media:
                Proceso_Media.objects.create(**img, proceso=proceso_instance)
            return proceso_instance

        # Story  is not containing images
        if 'proceso_media'not in validated_data:
            proceso_instance = Proceso.objects.create(**validated_data)
            return proceso_instance