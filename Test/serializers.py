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
        fields = ['id', 'first_name', 'last_name', 'birthday', 'street', 'house_number', 'postcode', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name']
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'sport', 'trainer', 'date', 'hall']
        
class CoursedateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coursedate
        fields = ['id', 'course_length', 'days', 'hour', 'minute']
        
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'id_course', 'id_member']