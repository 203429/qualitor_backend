from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

#Importaciones de modelos
from role.models import RoleModel

#Importaciones de serializadores
from role.serializers import RoleSerializer

# Create your views here.
class RoleList(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def get(self,request,format=None):
        queryset=RoleModel.objects.all()
        serializer = RoleSerializer(queryset,many=True,context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

class RoleDetail(APIView):
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
            return RoleModel.objects.get(pk = pk)  
        except RoleModel.DoesNotExist:   
            return 0

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = RoleSerializer(idResponse)
            return Response(self.custom_response("Success", idResponse.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", "serializer.errors", status=status.HTTP_400_BAD_REQUEST))