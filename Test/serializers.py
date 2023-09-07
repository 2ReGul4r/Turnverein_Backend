from rest_framework import serializers
from .models import *

class StadtSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Stadt
        fields = ['id', 'plz', 'ort']