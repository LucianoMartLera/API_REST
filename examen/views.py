from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from examen.models import Proyecto
from examen.serializers import ProyectSerializar

class ProjectViews(APIView):
    def get (self, request):
        proyecto= Proyecto.objects.all()
        serializer = ProyectSerializar(proyecto, many=True)
        return Response(serializer.data)
    
    def post (self, request):
        serialzer=ProyectSerializar(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=201)
        return Response(serialzer.errors, status=400)

class ProjectDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Proyecto, pk=pk)

    def get(self, request, pk):
        proyecto = self.get_object(pk)
        serializer = ProyectSerializar(proyecto)
        return Response(serializer.data)

    def put(self, request, pk):
        proyecto = self.get_object(pk)
        serializer = ProyectSerializar(proyecto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        proyecto = self.get_object(pk)
        serializer = ProyectSerializar(proyecto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        proyecto = self.get_object(pk)
        proyecto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   