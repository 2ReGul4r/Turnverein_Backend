from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = City
        fields = ['postcode', 'city']
        
class MemberSerializer(serializers.ModelSerializer):
    postcode = CitySerializer(read_only=True)
    postcode_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'birthday', 'street', 'house_number', 'postcode_id', 'postcode']
        extra_kwargs = {'id': {'read_only': True}, 'postcode': {'read_only': True}}
        
class TrainerSerializer(serializers.ModelSerializer):
    postcode = CitySerializer(read_only=True)
    postcode_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Trainer
        fields = ['id', 'first_name', 'last_name', 'birthday', 'street', 'house_number', 'postcode_id', 'postcode', 'username', 'password', 'is_staff', 'last_login']
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True}, 'postcode': {'read_only': True}, 'is_staff': {'read_only': True}, 'last_login': {'read_only': True}}
        
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name']
        extra_kwargs = {'id': {'read_only': True}}

class CoursedateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coursedate
        fields = ['id', 'course_length', 'days', 'hour', 'minute']
        extra_kwargs = {'id': {'read_only': True}}

class ParticipantSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True)
    member_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Participant
        fields = ['id', 'course', 'member', 'course_id', 'member_id']
        extra_kwargs = {'id': {'read_only': True}, 'course': {'read_only': True}, 'member': {'read_only': True}}

class CourseSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    trainer = TrainerSerializer(read_only=True)
    trainer_id = serializers.IntegerField(write_only=True)
    date = CoursedateSerializer()
    class Meta:
        model = Course
        fields = ['id', 'sport', 'trainer_id', 'trainer', 'date', 'hall']
        extra_kwargs = {'id': {'read_only': True}, 'trainer': {'read_only': True}}
    
    def create(self, validated_data):
        sportData = validated_data.pop('sport')
        sport = Sport.objects.get_or_create(name=sportData['name'])
        dateData = validated_data.pop('date')
        date = Coursedate.objects.get_or_create(course_length=dateData['course_length'], days=dateData['days'], hour=dateData['hour'], minute=dateData['minute'])
        return Course.objects.create(sport=sport[0], trainer_id=validated_data['trainer_id'], date=date[0], hall=validated_data['hall'])
    
    def update(self, instance, validated_data):
        if validated_data.get('sport'):
            sportData = validated_data.pop('sport')
            sport = Sport.objects.get_or_create(name=sportData['name'])
            instance.sport = sport[0]
        instance.trainer_id = validated_data.get('trainer_id', instance.trainer_id)
        if validated_data.get('date'):
            dateData = validated_data.pop('date')
            date = Coursedate.objects.get_or_create(course_length=dateData['course_length'], days=dateData['days'], hour=dateData['hour'], minute=dateData['minute'])
            instance.date = date[0]
        instance.hall = validated_data.get('hall', instance.hall)
        instance.save()
        return instance
        
class RegistrationSerializer(serializers.ModelSerializer):
    postcode = CitySerializer(read_only=True)
    postcode_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Trainer
        fields = [
            'id', 
            'username', 
            'first_name', 
            'last_name',
            'birthday',
            'street',
            'house_number',
            'postcode',
            'postcode_id',
            'password', 
            'is_active',
            'is_staff'
        ]
        extra_kwargs = {'id': {'read_only': True}, 'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        birthday = validated_data['birthday']
        street = validated_data['street']
        house_number = validated_data['house_number']
        postcode_id = validated_data['postcode_id']
        password = validated_data['password']

        user = Trainer.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            street=street,
            house_number=house_number,
            postcode_id=postcode_id,
            password=password,
        )
        return user
