from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .serializers import ProcesoCreateUpdateSerializer
from .models import Proceso

class ProcesoCreateUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = ProcesoCreateUpdateSerializer

    http_method_names = ['post','delete','put','patch', 'head']

    queryset = Proceso.objects.all()

class ProcesoList(APIView):
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
        queryset=Proceso.objects.all()
        serializer = ProcesoCreateUpdateSerializer(queryset,many=True,context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    
class ProcesoDetail(APIView):
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
            return Proceso.objects.get(pk = pk)  
        except Proceso.DoesNotExist:   
            return 0

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = ProcesoCreateUpdateSerializer(idResponse)
            return Response(self.custom_response("Success", idResponse.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", "serializer.errors", status=status.HTTP_400_BAD_REQUEST))