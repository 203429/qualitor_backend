from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
import json

#Importaciones de modelos
from proyectos.models import ProyectosModel

#Importaciones de serializadores
from proyectos.serializers import ProyectosSerializer

# Create your views here.
class ProyectoView(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response
    def get(self,request):
        queryset=ProyectosModel.objects.all()
        serializer=ProyectosSerializer(queryset,many=True,context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    def post(self, request):
        serializer = ProyectosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

class ProyectoDetail(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def get_object(self, pk):
        try:
            return ProyectosModel.objects.get(pk = pk)  
        except ProyectosModel.DoesNotExist:   
            return 0

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = ProyectosSerializer(idResponse)
            return Response(self.custom_response("Success", idResponse.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", "serializer.errors", status=status.HTTP_400_BAD_REQUEST))
    
    def patch(self, request, pk, format = None):
        id_response = self.get_object(pk)
        serializer = ProyectosSerializer(id_response, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CrearProyecto(APIView):
    serializer_class = ProyectosSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EliminarProyecto(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response
    def delete(self, request, id_users):
        proyecto=ProyectosModel.objects.get(pk=id_users)
        proyecto.delete()
        proyecto=ProyectosModel.objects.all()
        
        serializer = ProyectosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))