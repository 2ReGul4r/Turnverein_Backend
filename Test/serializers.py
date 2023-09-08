from rest_framework import serializers
from .models import *

class StadtSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Stadt
        fields = ['plz', 'ort']
        
class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ['id', 'straße', 'hausnummer', 'plz']
        
class MitgliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mitglied
        fields = ['id', 'vorname', 'nachname', 'geburtsdatum', 'adresse']
        
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'vorname', 'nachname', 'geburtsdatum', 'adresse']
        
class SportartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sportart
        fields = ['id', 'name', 'trainer']
        
class TrainiertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainiert
        fields = ['id', 'sportart', 'trainer']
