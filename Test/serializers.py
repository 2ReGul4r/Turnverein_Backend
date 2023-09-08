from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = City
        fields = ['postcode', 'city']
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'birthday', 'street', 'house_number', 'postcode']
        
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'first_name', 'last_name', 'birthday', 'street', 'house_number', 'postcode']
        
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name']
        
class CoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaching
        fields = ['id', 'sport', 'trainer']
