from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
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