from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
import json
# from django.contrib.auth.models import User
from .serializers import CustomUserDetailsSerializer

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
        serializer = CustomUserDetailsSerializer(queryset,many=True,context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    
class UserListDetail(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response
    
    def get_object(self, id_users):
        try:
            return CustomUser.objects.get(pk = id_users)  
        except CustomUser.DoesNotExist:   
            return 0
    
    def get(self, request, id_users, format=None):
        id_response = self.get_object(id_users)
        if id_response != 0:
            id_response = CustomUserDetailsSerializer(id_response)
            return Response(self.custom_response("Success", id_response.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", f"User with id: {id_users} not found", status=status.HTTP_400_BAD_REQUEST))
    
class UserDelete(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response
    
    def get_object(self, id_users):
        try:
            return CustomUser.objects.get(pk = id_users)  
        except CustomUser.DoesNotExist:   
            return 0
    
    def delete(self, request, id_users, format=None):
        id_response = self.get_object(id_users)
        if id_response != 0:
            id_response.delete()
            return Response(self.custom_response("Success", f"User with id: {id_users} deleted", status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", f"User with id: {id_users} not found", status=status.HTTP_400_BAD_REQUEST))