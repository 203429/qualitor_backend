from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .serializers import PhaseCreateUpdateSerializer
from .models import Phase

class PhaseCreateUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = PhaseCreateUpdateSerializer

    http_method_names = ['post','delete','put','patch', 'head']

    queryset = Phase.objects.all()

class CrearPhase(APIView):
    serializer_class = PhaseCreateUpdateSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhaseList(APIView):
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
        queryset=Phase.objects.all()
        serializer = PhaseCreateUpdateSerializer(queryset,many=True,context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    
class PhasePerProject(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def get(self, request, id_proyecto, format=None):
        queryset = Phase.objects.filter(id_proyecto=id_proyecto)
        serializer = PhaseCreateUpdateSerializer(queryset, many=True, context={'request': request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    
class PhaseDetail(APIView):
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
            return Phase.objects.get(pk = pk)  
        except Phase.DoesNotExist:   
            return 0

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = PhaseCreateUpdateSerializer(idResponse)
            return Response(self.custom_response("Success", idResponse.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", "serializer.errors", status=status.HTTP_400_BAD_REQUEST))
    
    def patch(self, request, pk, format = None):
        id_response = self.get_object(pk)
        serializer = PhaseCreateUpdateSerializer(id_response, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)