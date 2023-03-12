from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
import json

#Importaciones de modelos
from user.models import CustomUser

#Importaciones de serializadores
from user.serializers import CustomUserDetailsSerializer

# Create your views here.
class UserList(APIView):
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
        queryset=CustomUser.objects.all()
        print(queryset)
        # serializer = ProcesoCreateUpdateSerializer(queryset,many=True,context={'request':request})
        return Response(self.custom_response("Success", queryset, status=status.HTTP_200_OK))
    