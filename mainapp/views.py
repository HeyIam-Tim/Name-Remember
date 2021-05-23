from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NameRemember
from .serializers import NameRememberSerializer

class IndexAPI(APIView):
    """
    List all nameremembers, or create a new nameremember.
    """
    def get(self, request, format=None):
        name_remembers = NameRemember.objects.all()
        serializer = NameRememberSerializer(name_remembers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NameRememberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class NameRememberDetailAPI(APIView):
    """
        Retrieve, update and delete a namerememberer.
    """

    def get_object(self, pk):
        try:
            return NameRemember.objects.get(id=pk)
        except NameRemember.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        name_remember = self.get_object(pk)
        serializer = NameRememberSerializer(name_remember)
        return Response(serializer.data)
        


    def put(self, request, pk, format=None):
        name_remember = self.get_object(pk)
        serializer = NameRememberSerializer(name_remember, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        name_remember = self.get_object(pk)
        name_remember.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

