from rest_framework import serializers
from .models import NameRemember


class NameRememberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameRemember
        fields = '__all__'