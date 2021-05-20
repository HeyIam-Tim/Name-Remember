from django.shortcuts import render
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

    def delete(self, request, pk, format=None):
        name_remember = NameRemember.objects.get(id=pk)
        name_remember.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)