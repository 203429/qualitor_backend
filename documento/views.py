from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

#Importaciones de modelos
from documento.models import DocumentoModel

#Importaciones de serializadores
from documento.serializers import DocumentoSerializer


# Create your views here.
class DocumentoView(APIView):
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
        queryset=DocumentoModel.objects.all()
        serializer=DocumentoSerializer(queryset,many=True,context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    def post(self, request):
        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

class DocumentoDetail(APIView):
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
            return DocumentoModel.objects.get(pk = pk)  
        except DocumentoModel.DoesNotExist:   
            return 0

    def get(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = DocumentoSerializer(id_response)
            return Response(self.custom_response("Success", id_response.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", f"Proceso with id: {pk} not found", status=status.HTTP_400_BAD_REQUEST))