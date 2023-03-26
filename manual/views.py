from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Importaciones de modelos
from manual.models import ManualModel

# Importaciones de serializadores
from manual.serializers import ManualSerializer

# Create your views here.

class ManualView(APIView):
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
        queryset=ManualModel.objects.all()
        serializer=ManualSerializer(queryset,many=True,context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    
    def post(self, request):
        serializer = ManualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))


class ManualDetail(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def get(self, request, pk, format=None):
        queryset=ManualModel.objects.filter(proyecto=pk)
        serializer = ManualSerializer(queryset, many=True, context={'request': request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    
    def patch(self, request, pk, format=None):
        queryset = ManualModel.objects.filter(proyecto=pk)
        instance = queryset.first()
        serializer = ManualSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
